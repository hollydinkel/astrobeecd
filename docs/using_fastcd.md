# Using FastCD with Prepared Data

First, [create a ROS workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). Next, `cd YOUR_ROS_WORKSPACE/src`. Next, read the [fastcd installation instructions](https://github.com/PRBonn/fast_change_detection) to ensure all required dependencies are installed. Clone this repository into this workspace and build the package:

```bash
git clone https://github.com/hollydinkel/astrobee_change_detection --recurse-submodules
catkin deps fetch
catkin build
```

Remember, `catkin build` is required after modifying any C++ files. Next, download our example dataset into your fastcd folder.

```bash
cd ~/YOUR_ROS_WORKSPACE/src/fast_change_detection
mkdir data/ && cd data/
gdown https://drive.google.com/uc?id=1qNCRl9XceINrHLFUp4pBti9I4oJO2zf1
unzip *.zip
rm *.zip
cd .. && ./bin/fastcd_example DATASET_PATH
```