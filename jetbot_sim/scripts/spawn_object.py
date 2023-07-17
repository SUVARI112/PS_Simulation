#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest
from geometry_msgs.msg import Pose

color = "red"
urdf = """
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

def spawn_cube():
    rospy.wait_for_service('/gazebo/spawn_urdf_model')

    colors = ["Blue", "Red", "Red", "Red", "Blue", "Blue"]
    # poses = [(1.14,0.35),(0.635, 0.427),(0.43,0.67),(0.7,0.87),(1.15,1.17),(0.36,1.08)]
    poses = [(1.14,0.35),(0.7,0.87),(1.15,1.17),(0.36,1.08)]
    try:
        spawn_client = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)     

        for i in range(0,6):

        
            model = SpawnModelRequest()
            model.model_name = "cube%s" % str(i)
            model.model_xml = urdf % colors[i]

            model.initial_pose.position.x = poses[i][0]
            model.initial_pose.position.y = poses[i][1]
            model.initial_pose.position.z = 0.1
        
            spawn_client(model)
            rospy.sleep(0.2)



    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    rospy.init_node('spawn_cube_node')
    spawn_cube()
    