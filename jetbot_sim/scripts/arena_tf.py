#! /usr/bin/env python
import rospy
import tf2_ros
from geometry_msgs.msg import PoseStamped


rospy.init_node('arena_tf_publisher') 

tf_broadcaster = tf2_ros.TransformBroadcaster()
parent_frame_id = 'ground_plane' 
child_frame_id = 'arena'

rate = rospy.Rate(100)
while not rospy.is_shutdown(): 


    transform_msg = PoseStamped()
    transform_msg.header.stamp = rospy.Time.now()
    transform_msg.header.frame_id = parent_frame_id


    transform_msg.pose.position.x = 0
    transform_msg.pose.position.y = 0
    transform_msg.pose.position.z = 0
    transform_msg.pose.orientation.x = 0
    transform_msg.pose.orientation.y = 0
    transform_msg.pose.orientation.z = 0
    transform_msg.pose.orientation.w = 1

    transform_stamped = tf2_ros.TransformStamped()
    transform_stamped.header.stamp = rospy.Time.now()
    transform_stamped.header.frame_id = parent_frame_id
    transform_stamped.child_frame_id = child_frame_id
    transform_stamped.transform.translation = transform_msg.pose.position
    transform_stamped.transform.rotation = transform_msg.pose.orientation
    tf_broadcaster.sendTransform(transform_stamped)



    # rospy.loginfo(result) # Print the result type CoolServiceResponse
    
    rate.sleep()



    
    