#!/bin/bash
export HOME=/home/hdinkel
export ASTROBEE_WS=$HOME/astrobee/src/
export ASTROBEE_DEVEL=$HOME/astrobee/devel
export ASTROBEE_CHANGE_DETECTION=$HOME/astrobee_change_detection
export DATA=$ASTROBEE_CHANGE_DETECTION/data
export DATE=20230419
export ROBOT=bsharp
source $ASTROBEE_DEVEL/setup.bash

# Install dependencies
apt-get update
apt-get install -y python3-pip
pip install numpy --upgrade
pip install gdown pyquaternion pandas

# Download data
cd $DATA && gdown https://drive.google.com/uc?id=1qNCRl9XceINrHLFUp4pBti9I4oJO2zf1
unzip data.zip
rm data.zip

for SURVEY_NUMBER in 1 2 3 4
do
    export SURVEY=$SURVEY_NUMBER
    cd $DATA && python3 $ASTROBEE_CHANGE_DETECTION/astrobee_data_processing_scripts/poses_to_file.py $SURVEY $DATE $ROBOT
    rosrun sparse_mapping process_sequential_images.py $DATA/data/$DATE/$ROBOT/bayer/survey$SURVEY $ASTROBEE_WS/src/astrobee/config
    cd $DATA && python3 $ASTROBEE_CHANGE_DETECTION/astrobee_data_processing_scripts/process_sequential_poses.py $SURVEY $DATE $ROBOT
    cd $DATA/data/$DATE/$ROBOT/bayer/survey$SURVEY
    # ls -v | nl -v 0 | while read n f; do mv -n "$f" "Image$n.JPG"; done
done