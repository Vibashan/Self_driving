#!/usr/bin/env python

import rospy
import threading
import tf
from nav_msgs.msg import Odometry

class coord(object):
    def __init__(self):
        self._event = threading.Event()
        self.x = None
        self.y = None

    def __call__(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        quaternion = (msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]
        self.theta = yaw
        self._event.set()

    def get_msg(self, timeout=None):

        self._event.wait(timeout)
        return self.x,self.y,self.theta

if __name__ == '__main__':
    rospy.init_node('robot_state_publisher', anonymous=True)
    r = rospy.Rate(100)
    while(1):
        pose = coord()
        rospy.Subscriber("/ground_truth/state",Odometry,pose)
        x_1,y_1,theta_1 = pose.get_msg()
        r.sleep()
        print x_1, y_1,theta_1
  
    