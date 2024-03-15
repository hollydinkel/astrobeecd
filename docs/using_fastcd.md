# Using FastCD with Prepared Data

First, [create a ROS workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). Next, `cd YOUR_ROS_WORKSPACE/src`. Clone this repository into this workspace and build the package:

```bash
git clone https://github.com/hollydinkel/astrobee_change_detection --recurse-submodules
catkin deps fetch
catkin build
```

Remember, `catkin build` is required after modifying any C++ files. Next, download our example dataset into your fastcd folder.

```bash
cd ~/YOUR_ROS_WORKSPACE/src/fast_change_detection
mkdir data/ && cd data/
wget https://bit.ly/astrobee_fastcd_data
cd .. && ./bin/fastcd_example DATASET_PATH
```