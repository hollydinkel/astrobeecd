#! /usr/bin/env python

import numpy as np
from pyquaternion import Quaternion
import os
import argparse
from vedo import *

# ROS libraries
import rosbag

def main():
    """Extract a folder of images from a rosbag.
    """ 

    parser = argparse.ArgumentParser(description="Plot trajectories")
    parser.add_argument("survey", help="Indicate survey number")
    parser.add_argument("date", help="Dataset date.")
    parser.add_argument("robot", help="Robot name")

    args = parser.parse_args()

    bag_dir = f"./data/{args.date}/{args.robot}/bags/survey{args.survey}"
    output_dir = f"./data/{args.date}/{args.robot}/plot"

    # # nav_cam_tf = transform(vec3(0.1157+0.002, -0.0422, -0.0826), quat4(-0.46938154, -0.52978318, -0.5317378, -0.46504373))
    
    body_to_cam_trans = np.array([0.1157+0.002, -0.0422, -0.0826])
    body_to_cam_quat_xyzw = np.array([0.500, 0.500, 0.500, 0.500])
    body_to_cam_quat_wxyz = Quaternion(w=body_to_cam_quat_xyzw[3],x=body_to_cam_quat_xyzw[0],y=body_to_cam_quat_xyzw[1],z=body_to_cam_quat_xyzw[2])
    body_to_cam_transf = body_to_cam_quat_wxyz.transformation_matrix
    body_to_cam_transf[0:3,3] = body_to_cam_trans.T

    if args.robot=="sim":
        jpm_to_world = np.zeros((4,4))
        # note: rpy in ROS is ZYX Euler angles representation
        # jpm_to_world_rpy = np.array([3.1415, 0, -1.570796])
        jpm_to_world[0:3, 3] = np.array([10.9358938, -2.3364698, 4.8505872])
        jpm_to_world[0:3, 0:3] = np.array([[0,-1,0],[-1,0,0],[0, 0,-1]])
        jpm_to_world[3,3] = 1
        view = "+x"
        model = "./data/models/sim/model.obj"
    elif args.robot=="bsharp":
        jpm_to_world = np.identity(4)
        model = "./data/models/granite/model.obj"
        view = "-z"
    elif args.robot=="bumble" or args.robot=="queen":
        jpm_to_world = np.identity(4)
        view = "+z"
        model = "./data/models/sim/model.obj"

    data = {'pose': [],
            'pose_time': [],
            'image_time': [],
            'x': [],
            'y': [],
            'z': []}

    for bag_file in sorted(os.listdir(bag_dir)):
        bag = rosbag.Bag(os.path.join(bag_dir,bag_file),"r")

        for (topic, msg, t) in bag.read_messages(topics=['/gnc/ekf']):
            
            if topic == '/gnc/ekf':
                pose = msg.pose
                trans = np.array([pose.position.x, pose.position.y, pose.position.z])
                quat_xyzw = [pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w]
                quat_wxyz = Quaternion(w=quat_xyzw[3],x=quat_xyzw[0],y=quat_xyzw[1],z=quat_xyzw[2])
                transf = quat_wxyz.transformation_matrix
                transf[0:3,3] = trans.T
                transform = np.linalg.inv(jpm_to_world)@transf@body_to_cam_transf
                data['pose'].append(transform)
                data['pose_time'].append(t)
                data['x'].append(transform[0,3])
                data['y'].append(transform[1,3])
                data['z'].append(transform[2,3])
    
    granite = Mesh(model)
    granite.c('white').lighting('glossy')
    trajectory=Line([data['x'],data['y'],data['z']], c=(255, 0, 0), lw=3)
    plotter = Plotter()
    plotter.show(granite,trajectory, viewup=view,axes=False, roll=180, azimuth=180)
    print(output_dir+f'/survey{args.survey}.png')
    plotter.screenshot(filename=output_dir+f'/survey{args.survey}.png', scale=1)

if __name__ == "__main__":
    main()