# Repository for Processing Astrobee `.bag` Data

## Usage

Install the ![Astrobee flight software](https://github.com/nasa/astrobee). Additional instructions for using the Astrobee flight software with Docker are ![here](https://docs.google.com/document/d/1Wx54si5_24rz0kJie31X54PIk_k_owT6qzlziGnAWYc/edit?usp=sharing) Clone this data processing repository into the astrobee flight software repository:

```bash
git clone https://github.com/hollydinkel/astrobee_data_processing
```

The steps for creating a dataset to use with Fast Change Detection are included below. The raw data used to create the dataset are ![here](https://drive.google.com/drive/folders/1mBr_7hCGb8cP5V2ny_jZI7lhxymfJc7W?usp=sharing). Note that the survey number (e.g., 1, 2, 3), the date (e.g., 20230419), and the robot name (e.g., bsharp) must be specified in each step.

1. Perform initial extraction of images and poses from bag data to folder:
```bash
export ASTROBEE_WS=$HOME/astrobee
export DATA=$ASTROBEE_WS/src/astrobee_data_processing
cd $DATA & python3 poses_to_file.py [survey] [date] [robot]
```

2. Process sequential images to remove images where frames did not move much between images:

```bash
cd $ASTROBEE_WS && source devel/setup.bash
rosrun sparse_mapping process_sequential_images.py $DATA/data/[date]/[robot]/bayer/[survey] $ASTROBEE_WS/src/astrobee/config
```

3. Process sequential poses so that final poses are close in time (timestamps are close) to the image timestamps:

```bash
cd $DATA
python3 process_sequential_poses.py [survey] [date] [robot]
```

4. Rename all images in each folder to match what FastCD expects:
```bash
cd $DATA/data/[date]/[robot]/bayer/survey[survey]
ls -v | nl -v 0 | while read n f; do mv -n "$f" "Image$n.JPG"; done
```

5. Create `cameras.xml` file used in FastCD:

```bash
cd $DATA
python3 create_cameras_xml.py [survey] [date] [robot]
```

## **References**
<a id="1">[1]</a> 
NASA, "Astrobee Robot Software," (2023). [[code]](https://github.com/nasa/astrobee)

<a id="2">[2]</a> 
NASA, "ISAAC (Integrated System for Autonomous and Adaptive Caretaking)," (2023). [[code]](https://github.com/nasa/isaac)

<a id="3">[3]</a> 
E. Palazzolo and C. Stachniss, "Fast Image-Based Geometric Change Detection Given a 3D Model," in IEEE Int. Conf. Robot. Autom. (ICRA), 2018, pp. 6308–6315. doi: 10.1109/ICRA.2018.
8461019 [[paper]](https://ieeexplore.ieee.org/document/8461019) [[code]](https://github.com/PRBonn/fast_change_detection)