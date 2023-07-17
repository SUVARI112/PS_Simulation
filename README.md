## Project Seminar ris | Technical University of Darmstadt | Gruppe 8


### Before you get started with the simulation
- Install 
  - **Ubuntu 18.04** (Dual boot is recommended)
  - Drivers for your GPU (will be important to ensure a smooth simulation)
  - `ROS Melodic`
- run 
```bash 
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
### To start the simulation
- run `roscore`
- Create the following file structure:
```
  |-- catkin_ws
  |   |-- src

```
- In **src** folder clone the project repository:
```bash 
https://github.com/SUVARI112/PS_Simulation.git
```
- run ``` catkin build ```
- run  ``` source  {the_absolute_path_to_catkin_workspace}/catkin_ws/devel/setup.bash" >> ~/.bashrc ```
- in another Terminal run the command:
```bash 
export GAZEBO_MODEL_PATH={the_absolute_path_to_catkin_workspace}/catkin_ws/src/jetbot_sim/models:$GAZEBO_MODEL_PATH
```

- run ``` roslaunch jetbot_with_arena_and_apriltag_tf.launch ```

the simulator (Gazebo) and Rviz should appear as follows:

![gazebo](https://github.com/dansge7/Ps-Robotik/assets/131165247/1c2a0052-a90d-4c46-9941-bd3c330d4831)
![rviz](https://github.com/dansge7/Ps-Robotik/assets/131165247/f13a7529-7403-4bee-bfed-17755196cdbe)

- To control the robot with keyboard run ```rosrun jetbot_sim teleop_keyboard.py``` on another terminal.

### Important things to take into account:
- It's highly recommended to **place all nodes of the tasks (task 1,2 and 3) in a seperate ros package** because that would make the moving to work on the the real robot much easier.
- please note that the **topics names, camera specs and tf names** of the simulation will/may be different from the real robot, for example:
  - topic name of the velocity in simulation is ```/jetbot_velocity_controller/cmd_vel``` , but in the real robot is ```cmd_vel```
so changing them when running nodes on the real robot will be nessesarry later on.
