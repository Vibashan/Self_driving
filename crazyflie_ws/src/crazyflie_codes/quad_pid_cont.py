#!/usr/bin/env python

import rospy
import threading
import tf
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Pose2D
from std_msgs.msg import String

class coord(object):
    def __init__(self):
        self._event = threading.Event()
        self.x = None
        self.z = None

    def __call__(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.z = msg.pose.pose.position.z
        quaternion = (msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]
        self.theta = yaw
        self._event.set()

    def get_msg(self, timeout=None):
        self._event.wait(timeout)
        return self.x,self.y,self.z,self.theta

def go_to_goal(z_1,z_t,z_err1,z_i_err):
    Kp_z = 0.7
    Kd_z = 0.8
    Ki_z = 0.02

    z_err2 = z_t-z_1
    z_d_err = z_err2 - z_err1
    if abs(z_err2) < 0.15:
        z_i_err = 0 
    z_i_err = z_i_err + z_err2
    vz_1 = (Kp_z*z_err2 + Kd_z*z_d_err + Ki_z*z_i_err)
    z_err1 = z_err2
    return vz_1,z_err1,z_i_err

if __name__ == '__main__':
    
    z_t = 2
    z_old_err = 0
    z_int_err = 0
    rospy.init_node('robot_state_publisher', anonymous=True)
    r = rospy.Rate(100)

    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=2)
    twist = Twist()

    while(1):
        pose = coord()
        rospy.Subscriber("/ground_truth/state",Odometry,pose,queue_size=1)
        x_1,y_1,z_1,theta_1 = pose.get_msg()

        vz_1,z_old_err,z_int_err = go_to_goal(z_1,z_t,z_old_err,z_int_err)
        print 'x_1-',x_1,'y_1-',y_1,'z_1-',z_1,'vz_1-',vz_1
        twist.linear.z = vz_1
        pub.publish(twist)

  
    