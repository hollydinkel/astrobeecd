export ASTROBEE_WS=/src/astrobee/src
export DATA=$ASTROBEE_WS/astrobee_data_processing
export SURVEY=1
export DATE=20230419
export ROBOT=bsharp

# Install dependencies
apt-get install -y python3-pip
pip install gdown pyquaternion

# Download data
cd $DATA && gdown https://drive.google.com/uc?id=1qNCRl9XceINrHLFUp4pBti9I4oJO2zf1
unzip data.zip
rm data.zip

for SURVEY_NUMBER in 1 2 3 4
do
    export SURVEY=$SURVEY_NUMBER
    cd $DATA && python3 scripts/poses_to_file.py $SURVEY $DATE $ROBOT
    cd $ASTROBEE_WS && source ../devel/setup.bash
    rosrun sparse_mapping process_sequential_images.py $DATA/data/$DATE/$ROBOT/bayer/survey$SURVEY $ASTROBEE_WS/src/astrobee/config
    cd $DATA && python3 scripts/process_sequential_poses.py $SURVEY $DATE $ROBOT
    cd $DATA/data/$DATE/$ROBOT/bayer/survey$SURVEY
    ls -v | nl -v 0 | while read n f; do mv -n "$f" "Image$n.JPG"; done