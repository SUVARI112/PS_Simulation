#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest
from geometry_msgs.msg import Pose

color = "red"
cube_urdf = """
<robot name="cube">
    <link name="link">

      <inertial>
        <origin xyz="0 0 0" rpy="0 0 0"/>
        <mass value="0.050" />
        <inertia ixx="2.3541666666666672e-05" ixy="0.0" ixz="0.0" iyy="2.3541666666666672e-05" iyz="0.0" izz="2.3541666666666672e-05"/>
      </inertial>

      <collision>
        <origin xyz="0 0 0" rpy="0 0 0"/>
        <geometry>
            <box size="0.03 0.03 0.03"/>
        </geometry>
      </collision>

      <visual>
        <geometry>
          <box size="0.03 0.03 0.03"/>
        </geometry>
      </visual>

    </link>

    <gazebo reference="link">
      <material>Gazebo/%s</material>
    </gazebo>
</robot>
""" 

ball_urdf = """
<robot name="wooden_ball">
  <link name="ball_link">
    <visual>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="wooden_material">
        <color rgba="0.5 0.3 0.1 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
    </collision>
  </link>

  <gazebo reference="ball_link">
    <material>Gazebo/Wood</material>
  </gazebo>
</robot>
"""



def spawn_cube():
    rospy.wait_for_service('/gazebo/spawn_urdf_model')

    colors = ["Blue", "Red", "Orange", "Yellow", "Purple", "Green", "ball", "ball"]
    poses = [(0.635, 0.427),(0.43,0.67),(0.7,0.87),(1.15,1.17),(0.30,1.08),(1.14,0.35)]
    try:
        spawn_client = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)     

        for i in range(len(poses)):

            model = SpawnModelRequest()
            model.model_name = "Cube%s" % str(i)
            model.model_xml = cube_urdf % colors[i]

            model.initial_pose.position.x = poses[i][0]
            model.initial_pose.position.y = poses[i][1]
            model.initial_pose.position.z = 0.1
        
            spawn_client(model)
            rospy.sleep(0.1)

        # for i in range(6,8):
        #     rospy.loginfo("Im here")
        #     model = SpawnModelRequest()
        #     model.model_name = "Ball%s" % str(i)
        #     model.model_xml = ball_urdf 

        #     model.initial_pose.position.x = poses[i][0]
        #     model.initial_pose.position.y = poses[i][1]
        #     model.initial_pose.position.z = 0.1
        
        #     spawn_client(model)
        #     rospy.loginfo("Im there")
        #     rospy.sleep(0.1)




    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    rospy.init_node('spawn_cube_node')
    spawn_cube()