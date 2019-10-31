#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String& msg)
{
    ROS_INFO("I heard: [%s]", msg.data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "husky_listener");
    ros::NodeHandle nodeHandle("~");
    std::string topic;
    int size;
    nodeHandle.getParam("scan/queue_size", size);
    nodeHandle.getParam("scan/name", topic);
    ros::Subscriber subscriber = nodeHandle.subscribe("scan", 10, chatterCallback);
    ros::spin();
    return 0;
}