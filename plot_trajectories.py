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

    args = parser.parse_args()

    bag_dir = f"./data/{args.date}/bags/survey{args.survey}"
    model = f"./data/{args.date}/model.obj"
    output_dir = f"./data/{args.date}/plot/survey{args.survey}"
    try: os.mkdir(output_dir)
    except FileExistsError:
        print(f"{output_dir} already exists!")

    # # nav_cam_tf = transform(vec3(0.1157+0.002, -0.0422, -0.0826), quat4(-0.46938154, -0.52978318, -0.5317378, -0.46504373))
    
    body_to_cam_trans = np.array([0.1157+0.002, -0.0422, -0.0826])
    body_to_cam_quat_xyzw = np.array([-0.46938154, -0.52978318, -0.5317378, -0.46504373])
    body_to_cam_quat_wxyz = Quaternion(w=body_to_cam_quat_xyzw[3],x=body_to_cam_quat_xyzw[0],y=body_to_cam_quat_xyzw[1],z=body_to_cam_quat_xyzw[2])
    body_to_cam_transf = body_to_cam_quat_wxyz.transformation_matrix
    body_to_cam_transf[0:3,3] = body_to_cam_trans.T

    for bag_file in os.listdir(bag_dir):
        bag = rosbag.Bag(os.path.join(bag_dir,bag_file),"r")

        data = {'pose': [],
                'pose_time': [],
                'image_time': [],
                'x': [],
                'y': [],
                'z': []}
        for (topic, msg, t) in bag.read_messages(topics=['/gnc/ekf']):
            
            if topic == '/gnc/ekf':
                pose = msg.pose
                trans = np.array([pose.position.x, pose.position.y, pose.position.z])
                quat_xyzw = [pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w]
                quat_wxyz = Quaternion(w=quat_xyzw[3],x=quat_xyzw[0],y=quat_xyzw[1],z=quat_xyzw[2])
                transf = quat_wxyz.transformation_matrix
                transf[0:3,3] = trans.T
                data['pose'].append(transf)
                data['pose_time'].append(t)
                data['x'].append(pose.position.x)
                data['y'].append(pose.position.y)
                data['z'].append(pose.position.z)

        bag.close()
    
    granite = Mesh(model)
    granite.c('white').lighting('glossy')
    trajectory=Line([data['x'],data['y'],data['z']], c=(255, 0, 0), lw=3)
    plotter = Plotter()
    plotter.show(granite,trajectory, viewup="+z",axes=False)
    plotter.interactive().close()

if __name__ == "__main__":
    main()