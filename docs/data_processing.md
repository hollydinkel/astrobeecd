# Instructions Processing Astrobee `.bag` Data

The steps for creating a dataset to use with Fast Change Detection are included below. Download a dated raw dataset from [here](https://docs.google.com/document/d/1Wx54si5_24rz0kJie31X54PIk_k_owT6qzlziGnAWYc/edit?usp=sharing). Unzip the dataset into a `astrobee_change_detection/data` directory (**HD 20231113: This is not the correct link, and the data on GDrive is no longer in the format to support this step anyway. Needs re-testing**). Note that the survey number (e.g., 1, 2, 3), the date (e.g., 20230419), and the robot name (e.g., bsharp) must be specified in each step. The first four steps can be performed in a docker container where the running container is mounted to a local directory. The provided `run.sh` script runs these four steps. The last step should be performed locally if the FastCD workspace is built outside of the container.

1. The first step of data processing is extraction of images and poses from bag data to folder, processing of sequential images to remove images where frames did not move much between images, and processing of sequential poses so that final poses are close in time (timestamps are close) to the image timestamps. First, start a running Astrobee docker container with

```bash
cd $ASTROBEE_LOCAL_WS && sudo ./scripts/docker/run.sh -m bash
```

Inside the docker container, run

```bash
export DATA=/src/astrobee/src/astrobee_change_detection
cd $DATA && ./run.sh
```
After processing the data in the the docker container, return to a local terminal to create a `cameras.xml` file for the dataset to use in FastCD. Make sure to change the `fastcd_data_directory` variable in line 21 of `scripts/create_cameras_xml.py` before running this. Also make sure the `DATE` and `ROBOT` arguments match those used in `run.sh`.

```bash
export SURVEY=1
export DATE=20230419
export ROBOT=bsharp
cd $HOME/astrobee/astrobee_change_detection
python3 scripts/create_cameras_xml.py $SURVEY $DATE $ROBOT
```

Example processed data is provided [here](https://drive.google.com/file/d/1G3sMFmZ3kstxJwPudJo4NLC4ZkHNYkZt/view?usp=drive_link).