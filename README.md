# Repository for Processing Astrobee `.bag` Data

## Usage

Install the ![Astrobee flight software](https://github.com/nasa/astrobee). Additional instructions for using the Astrobee flight software with Docker are ![here](https://docs.google.com/document/d/1Wx54si5_24rz0kJie31X54PIk_k_owT6qzlziGnAWYc/edit?usp=sharing). Clone this data processing repository into the astrobee flight software repository:

```bash
export ASTROBEE_LOCAL_WS=$HOME/astrobee
cd $ASTROBEE_WS && git clone https://github.com/hollydinkel/astrobee_data_processing
```

The steps for creating a dataset to use with Fast Change Detection are included below. Download a dated raw dataset from ![here](https://drive.google.com/drive/folders/1mCxaicloRZOwuGWVxp52GwxBaCMDVEri?usp=sharing). Unzip the dataset into  Note that the survey number (e.g., 1, 2, 3), the date (e.g., 20230419), and the robot name (e.g., bsharp) must be specified in each step. The first four steps can be performed in a docker container where the running container is mounted to a local directory. The provided `process.sh` script runs these four steps. The last step should be performed locally if the FastCD workspace is built outside of the container.

1. The first step of data processing is extraction of images and poses from bag data to folder, processing of sequential images to remove images where frames did not move much between images, and processing of sequential poses so that final poses are close in time (timestamps are close) to the image timestamps. First, start a running Astrobee docker container with

```bash
cd $ASTROBEE_LOCAL_WS && sudo ./scripts/docker/run.sh -m bash
```

Inside the docker container, run

```bash
export DATA=/src/astrobee/src/astrobee_data_processing
cd $DATA && ./run.sh
```
After processing the data in the the docker container, return to a local terminal to create a `cameras.xml` file for the dataset to use in FastCD. Make sure to change the `fastcd_data_directory` variable in line 21 of `scripts/create_cameras_xml.py` before running this. Also make sure the `DATE` and `ROBOT` arguments match those used in `run.sh`.

```bash
export SURVEY=1
export DATE=20230419
export ROBOT=bsharp
cd $HOME/astrobee/astrobee_data_processing
python3 scripts/create_cameras_xml.py $SURVEY $DATE $ROBOT
```

## **References**
<a id="1">[1]</a> 
NASA, "Astrobee Robot Software," (2023). [[code]](https://github.com/nasa/astrobee)

<a id="2">[2]</a> 
NASA, "ISAAC (Integrated System for Autonomous and Adaptive Caretaking)," (2023). [[code]](https://github.com/nasa/isaac)

<a id="3">[3]</a> 
E. Palazzolo and C. Stachniss, "Fast Image-Based Geometric Change Detection Given a 3D Model," in IEEE Int. Conf. Robot. Autom. (ICRA), 2018, pp. 6308–6315. doi: 10.1109/ICRA.2018.
8461019 [[paper]](https://ieeexplore.ieee.org/document/8461019) [[code]](https://github.com/PRBonn/fast_change_detection)