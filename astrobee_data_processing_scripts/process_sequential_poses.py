#! /usr/bin/env python3

import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description="Process sequential poses.")
parser.add_argument("survey", help="Indicate survey number")
parser.add_argument("date", help="Dataset date.")
parser.add_argument("robot", help="Robot name")

args = parser.parse_args()

img_dir = f"./data/{args.date}/{args.robot}/bayer/survey{args.survey}"
pose_dir = f"./data/{args.date}/{args.robot}/pose/survey{args.survey}"

pose_list = sorted([int(os.path.splitext(file)[0]) for file in os.listdir(pose_dir)])
img_list = sorted([int(os.path.splitext(file)[0]) for file in os.listdir(img_dir)])

save = []
for img in img_list:
    diff = []
    for pose in pose_list:
        diff.append(abs(pose-img))
    i = np.argmin(diff)
    save.append(f'{pose_list[i]}.txt')

remove = sorted(list(set(os.listdir(pose_dir)).difference(save)))

for file in remove:
    os.remove(os.path.join(pose_dir,file))