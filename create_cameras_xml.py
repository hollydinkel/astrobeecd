# Creating XML Document in Python
# from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
import argparse
from numpy import loadtxt

parser = argparse.ArgumentParser(description="Process sequential poses.")
parser.add_argument("survey", help="Indicate survey number")
parser.add_argument("date", help="Dataset date.")

args = parser.parse_args()

poses_dir = f'./data/{args.date}/pose/survey{args.survey}'
poses = os.listdir(poses_dir)
fastcd_data_dir = f'/home/hdinkel/change_ws/src/fast_change_detection/example/dataset/granite_groundtruth_survey{args.survey}'
try: os.mkdir(fastcd_data_dir)
except FileExistsError:
    print(f"{fastcd_data_dir} already exists!")

tree = ET.parse('./cameras.xml')
root = tree.getroot()
separator = " "

for i,pose in enumerate(poses):
    with open(f"{poses_dir}/{pose}",'r') as f:
        content = f.readlines()
        l = []
        for line in content:
            row = line.split()
            val = [str(a) for a in row]
            l.append(val)
        listed = [item for val in l for item in val]

    root[0][1][i].set('id',f'{i}')
    root[0][1][i].set('label',f'Image{i}.JPG')
    root[0][1][i].set('sensor_id','0')
    root[0][1][i].set('enabled','true')
    root[0][1][i][0].text = separator.join(listed)

tree.write(os.path.join(fastcd_data_dir,'cameras.xml'))    