#!/bin/bash
export HOME=/home/hdinkel
export CATKIN_WS=$HOME/test_ws/src
export ASTROBEE=$HOME/astrobee
export ASTROBEE_CHANGE_DETECTION=$CATKIN_WS/astrobee_change_detection
export DATA=$ASTROBEE_CHANGE_DETECTION/data
export FASTCD=$ASTROBEE_CHANGE_DETECTION/fast_change_detection
export DATE=20230419
export ROBOT=bsharp
source $ASTROBEE/devel/setup.bash

# mkdir $DATA

# # Install dependencies
# apt-get update
# apt-get install -y python3-pip
# pip install numpy --upgrade
# pip install gdown pyquaternion pandas

# # Download data
# cd $DATA && gdown https://drive.google.com/uc?id=1qNCRl9XceINrHLFUp4pBti9I4oJO2zf1
# unzip data.zip
# cp data/ ../
# rm -rf data/
# rm $DATA/data.zip

for SURVEY_NUMBER in 2 3 4
do
    export SURVEY=$SURVEY_NUMBER
    cd $DATA && python3 $ASTROBEE_CHANGE_DETECTION/astrobee_data_processing_scripts/poses_to_file.py $SURVEY $DATE $ROBOT
    rosrun sparse_mapping process_sequential_images.py $DATA/$DATE/$ROBOT/bayer/survey$SURVEY $ASTROBEE/src/astrobee
    mv $DATA/$DATE/$ROBOT/bayer/survey$SURVEY/0/* $DATA/$DATE/$ROBOT/bayer/survey$SURVEY/
    rm -rf $DATA/$DATE/$ROBOT/bayer/survey$SURVEY/0 $DATA/$DATE/$ROBOT/bayer/survey$SURVEY/invalid $DATA/$DATE/$ROBOT/bayer/survey$SURVEY/rotation
    cd $DATA && python3 $ASTROBEE_CHANGE_DETECTION/astrobee_data_processing_scripts/process_sequential_poses.py $SURVEY $DATE $ROBOT && rm *.txt
    cd $DATA/$DATE/$ROBOT/bayer/survey$SURVEY && ls -v | nl -v 0 | while read n f; do mv -n "$f" "Image$n.JPG"; done
    cp -r $DATA/$DATE/$ROBOT/bayer/survey$SURVEY $FASTCD/
    cd $ASTROBEE_CHANGE_DETECTION && python3 astrobee_data_processing_scripts/create_cameras_xml.py $SURVEY $DATE $ROBOT
done