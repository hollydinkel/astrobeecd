# Creating XML Document in Python

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import shutil
import argparse
from numpy import loadtxt
from decimal import Decimal

parser = argparse.ArgumentParser(description="Process sequential poses.")
parser.add_argument("survey", help="Indicate survey number")
parser.add_argument("date", help="Dataset date.")
parser.add_argument("robot", help="Robot name")

args = parser.parse_args()

images_dir = f'./data/{args.date}/{args.robot}/bayer/survey{args.survey}'
poses_dir = f'./data/{args.date}/{args.robot}/pose/survey{args.survey}'
poses = os.listdir(poses_dir)
fastcd_data_dir = f'/home/hollydinkel/change_ws/src/fast_change_detection/example/dataset/{args.date}_survey{args.survey}'

try: os.mkdir(fastcd_data_dir)
except FileExistsError:
    print(f"{fastcd_data_dir} already exists!")
try: shutil.copytree(images_dir, fastcd_data_dir+'/images')
except:
    pass

shutil.copy("cameras_template.xml","cameras.xml")

# camera configs
# bsharp2
if args.robot=='bsharp':
    distortion_coeff = 1.0092039
    fx = '621.04422'
    cx = '580.56427'
    fy = '621.04422'
    cy = '495.51236'
    gain = 100
    exposure = 150
elif args.robot=='bumble':
    distortion_coeff = 0.998693,
    fx = '608.8073'
    cx = '632.53684'
    fy = '607.61439'
    cy = '549.08386'
    gain=50
    exposure=175
elif args.robot=='queen':
    distortion_coeff = 1.00201
    fx = '604.19903'
    cx = '588.79562'
    fy = '602.67924'
    cy = '509.73835'
    gain=50
    exposure=175

tree = ET.parse('./cameras.xml')
root = tree.getroot()
separator = " "

root[0][0][0].set('label',f'{args.robot}_navcam')
fx_element = ET.Element("fx")
fx_element.text = fx
root[0][0][0][5].append(fx_element)
fy_element = ET.Element("fy")
fy_element.text = fy
root[0][0][0][5].append(fy_element)
cx_element = ET.Element("cx")
cx_element.text = cx
root[0][0][0][5].append(cx_element)
cy_element = ET.Element("cy")
cy_element.text = cy
root[0][0][0][5].append(cy_element)

for i,pose in enumerate(poses):
    with open(f"{poses_dir}/{pose}",'r') as f:
        content = f.readlines()
        l = []
        for line in content:
            row = line.split()
            val = [str(a) for a in row]
            l.append(val)
        listed = [item for val in l for item in val]
        
        child_camera = ET.Element("camera")
        child_transform = ET.Element("transform")
        child_camera.append(child_transform)
        root[0][1].append(child_camera)

    root[0][1][i].set('id',f'{i}')
    root[0][1][i].set('label',f'Image{i}.JPG')
    root[0][1][i].set('sensor_id','0')
    root[0][1][i].set('enabled','true')
    root[0][1][i][0].text = separator.join(listed)

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

with open("cameras.xml", "w") as f:
    f.write(xmlstr)
with open("cameras.xml", "r") as f:
    lines = [line for line in f if line.strip() != ""]
with open("cameras.xml", "w") as f:
    f.writelines(lines)

shutil.move("cameras.xml",os.path.join(fastcd_data_dir,'cameras.xml'))
try: shutil.copytree(images_dir,f'{fastcd_data_dir}/images/')
except: pass
