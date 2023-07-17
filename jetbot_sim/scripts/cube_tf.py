#! /usr/bin/env python
import rospy
from gazebo_msgs.srv import GetModelState, GetModelStateRequest 
from geometry_msgs.msg import Pose

import tf2_ros
from geometry_msgs.msg import PoseStamped


rospy.init_node('robot_tf_publisher') 
rospy.wait_for_service('/gazebo/get_model_state') 
jetbot_state_service_client = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState) 
request_object = GetModelStateRequest() 
request_object.model_name = 'cube'
request_object.relative_entity_name = 'ground_plane'



tf_broadcaster = tf2_ros.TransformBroadcaster()
parent_frame_id = 'map' 
child_frame_id = 'obstacle'

rate = rospy.Rate(200)
while not rospy.is_shutdown(): 


    transform_msg = PoseStamped()
    transform_msg.header.stamp = rospy.Time.now()
    transform_msg.header.frame_id = parent_frame_id

    result = jetbot_state_service_client(request_object)
    pose = result.pose

    transform_msg.pose.position.x = pose.position.x
    transform_msg.pose.position.y = pose.position.y
    transform_msg.pose.position.z = pose.position.z
    transform_msg.pose.orientation.x = pose.orientation.x
    transform_msg.pose.orientation.y = pose.orientation.y
    transform_msg.pose.orientation.z = pose.orientation.z
    transform_msg.pose.orientation.w = pose.orientation.w

    transform_stamped = tf2_ros.TransformStamped()
    transform_stamped.header.stamp = rospy.Time.now()
    transform_stamped.header.frame_id = parent_frame_id
    transform_stamped.child_frame_id = child_frame_id
    transform_stamped.transform.translation = transform_msg.pose.position
    transform_stamped.transform.rotation = transform_msg.pose.orientation
    tf_broadcaster.sendTransform(transform_stamped)



    # rospy.loginfo(result) # Print the result type CoolServiceResponse
    
    rate.sleep()



    
    