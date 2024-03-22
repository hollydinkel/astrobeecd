# Processing Astrobee `.bag` Data

The files documents the steps for creating a dataset to use with Fast Change Detection. 

First, install the [Astrobee flight software](https://github.com/nasa/astrobee) in the '$HOME' directory. Additional instructions for using the Astrobee flight software with Docker are [here](https://docs.google.com/document/d/1Wx54si5_24rz0kJie31X54PIk_k_owT6qzlziGnAWYc/edit?usp=sharing). Next, clone this repository:

```bash
cd $HOME && git clone https://github.com/hollydinkel/astrobee_change_detection --recurse-submodules
```

Follow the steps in the provided `process_data.sh` file to download raw `.bag` data and process it into a change detection-compatible dataset. Note that the home directory, the change detection catkin workspac, the survey number (e.g., 1, 2, 3), the date (e.g., 20230419), and the robot name (e.g., bsharp) must be specified in the `process_data.sh` script. If the `astrobee` catkin workspace does not build locally, it is possible to do these steps in a docker container where the running container is mounted to a local directory. The provided `process_data.sh` script runs these four steps.

1. The first step of data processing is extraction of images and poses from bag data to folder, processing of sequential images to remove images where frames did not move much between images, and processing of sequential poses so that pose timestamps are close in time to image timestamps. First, start a running Astrobee docker container with

```bash
export ASTROBEE_WS=$HOME/astrobee
cd $ASTROBEE_WS && sudo ./scripts/docker/run.sh -m bash
```

Inside the docker container, run

```bash
cd $DATA && ./process_data.sh
```

After processing the data in the the docker container, return to a local terminal to create a `cameras.xml` file for the dataset to use in FastCD. Make sure to change the `fastcd_data_directory` variable in line 21 of `scripts/create_cameras_xml.py` before running this. Also make sure the `DATE` and `ROBOT` arguments match those used in `run.sh`.

```bash
export SURVEY=1
export DATE=20230419
export ROBOT=bsharp
cd $HOME/astrobee_change_detection
python3 scripts/create_cameras_xml.py $SURVEY $DATE $ROBOT
```

Example processed data are provided [here](https://drive.google.com/file/d/1G3sMFmZ3kstxJwPudJo4NLC4ZkHNYkZt/view?usp=drive_link).