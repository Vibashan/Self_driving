#!/usr/bin/env python

import rospy
import math
import threading
from geometry_msgs.msg import Twist,Pose2D
from nav_msgs.msg import Odometry
from std_msgs.msg import String

class coord(object):
    def __init__(self):
        self._event = threading.Event()
        self.x = None
        self.y = None
        self.theta = None

    def __call__(self, msg):
        self.x = msg.x*1000
        self.y = -msg.y*1000
        self.theta = -math.degrees(msg.theta)
        if self.theta >= 0:
          self.theta = self.theta
        else:
          self.theta = 360 + self.theta          
        self._event.set()

    def get_msg(self, timeout=None):
        self._event.wait(timeout)
        return self.x,self.y,self.theta

class speed(object):
    def __init__(self):
        self._event = threading.Event()
        self.vx = None
        self.wt = None

    def __call__(self, msg):
        self.vx = msg.twist.twist.linear.x
        self.wt = msg.twist.twist.angular.z
        self._event.set()

    def get_msg(self, timeout=None):
        self._event.wait(timeout)
        return self.vx,self.wt

def go_to_goal(x_1,y_1,x_error1):
    Kp_x = 0.9
    Kd_x = 0.5
    
    x_error2 = x_t-x_1
    x_d_err = x_error1 - x_error2
    if abs(x_error2) < 100:
        x_i_err = 0 
    x_pid = (Kp_x*x_error2 + Kd_x*x_d_err )/(Kp_x*4000+Kd_x*4000)
    x_error1 = x_error2

    if abs(x_pid) > 0.15:
        if x_pid < 0:
            x_pid = -0.15
        elif x_pid > 0:
            x_pid = 0.15
    if abs(x_pid) < 0.04:
        if x_pid < 0:
            x_pid = -0.04
        elif x_pid > 0:
            x_pid = 0.04
    
    x_dot = x_pid
    print('x_dot-',x_dot)

    return x_dot,y_dot,x_error1
    

if __name__ == '__main__':

    x_dot = 0
    y_dot = 0
    x_error1 = 0
    wt_1 = 0

    rospy.init_node('pose_action', anonymous=True)
    rate = rospy.Rate(100)

    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    twist = Twist()

    x_t = 1000

    while not rospy.is_shutdown():
        while(1):

            twist.linear.x = 1
            twist.linear.y = 0
            twist.angular.z = 0
            pub.publish(twist)
