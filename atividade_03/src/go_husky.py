#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker

marker = Marker()

marker.header.frame_id = "base_link";
# marker.header.stamp = rospy.Time.now()
marker.ns = "my_namespace";
marker.id = 0;
marker.action = marker.ADD
marker.type = marker.ARROW
marker.pose.position.x = 1
marker.pose.position.y = 1
marker.pose.position.z = 1
marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 1.0
marker.scale.x = 1
marker.scale.y = 0.1
marker.scale.z = 0.1
marker.color.a = 1.0
marker.color.r = 0.0
marker.color.g = 1.0
marker.color.b = 0.0


dist = float('inf')
past_dist = float('inf')

def talker():
    vel_msg = Twist()
    
    kp = 0.5
    epsilon = 0.2

    while not rospy.is_shutdown():
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.init_node('husky_vel', anonymous=True)
        rospy.Subscriber("scan",LaserScan,callback)
        pub2 = rospy.Publisher('/marker',Marker,queue_size=10)
        
        rate = rospy.Rate(10) # 10hz
        marker.header.frame_id = "base_link";
        # marker.header.stamp = rospy.Time.now()
        marker.ns = "my_namespace";
        marker.id = 0;
        marker.action = marker.ADD
        marker.type = marker.CYLINDER
        marker.pose.position.x = 9.17
        marker.pose.position.y = 0
        marker.pose.position.z = 0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 1
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        
        while dist > epsilon:
            print(dist)
            vel_msg.linear.x = dist*kp
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            # rospy.loginfo(vel_msg)
            # pub.publish(vel_msg)
            pub2.publish(marker)
        rate.sleep()

def callback(msg):
    global dist
    dist = min(msg.ranges)

    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass