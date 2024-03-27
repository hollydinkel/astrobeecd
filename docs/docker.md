## Astrobee Fast Change Detection with Docker

This repository can be tested inside of a [Docker](https://www.docker.com/) container to isolate all software and dependency changes from the host system. This document describes how to create and run a Docker image that contains a complete catkin workspace and system environment for this repository.

The current configuration was tested on an x86 host computer running Ubuntu 20.04 with Docker 25.0.2.

### Steps

1. **Download AstrobeeCD**
   ```bash
   git clone --recurse-submodules https://github.com/RMDLO/astrobeecd.git astrobeecd
   ```

2. **Build the Docker Image**
   ```bash
   cd astrobeecd/docker
   docker build -t astrobeecd:noetic -f Dockerfile.noetic ..
   ```

This will take several minutes and require connection to the internet. This command will install all dependencies and build the catkin workspace within the image.

3. **Run the Container**
   ```
   ./run_docker.sh [name] [host dir] [container dir]
   ```
   Optional Parameters:
   - `name` specifies the name of the image. By default, it is `astrobeecd`. Multiple containers can be created from the same image by changing this parameter.
   - `host dir` and `container dir` map a directory on the host machine to a location inside the container. This enables sharing code and data between the two systems. By default, the `run_docker.sh` bash script maps the directory containing `astrobeecd` to `/root/fastcd_ws/src/astrobeecd` in the container.

    Only the first call of this script with a given name will create a container. Subsequent executions will attach to the running container to enable running multiple terminal sessions in a single container.

   *Note:* Since the Docker container binds directly to the host's network, it will see `roscore` even if running outside the docker container.

For more information about using ROS with docker, see the ![ROS tutorial](http://wiki.ros.org/docker/Tutorials/Docker).