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

def go_to_goal(x_1,x_t,x_err1,x_i_err,y_1,y_t,y_err1,y_i_err,z_1,z_t,z_err1,z_i_err):
    Kp_x = 0.1
    Kd_x = 0.4
    Ki_x = 0.001

    x_err2 = x_t-x_1
    x_d_err = x_err2 - x_err1
    if abs(x_err2) < 0.15:
        x_i_err = 0 
    x_i_err = x_i_err + x_err2
    vx_1 = (Kp_x*x_err2 + Kd_x*x_d_err + Ki_x*x_i_err)
    x_err1 = x_err2

    Kp_y = 0.1
    Kd_y = 0.4
    Ki_y = 0.001

    y_err2 = y_t-y_1
    y_d_err = y_err2 - y_err1
    if abs(y_err2) < 0.15:
        y_i_err = 0 
    y_i_err = y_i_err + y_err2
    vy_1 = (Kp_y*y_err2 + Kd_y*y_d_err + Ki_y*y_i_err)
    y_err1 = y_err2

    Kp_z = 0.1
    Kd_z = 0.4
    Ki_z = 0.001

    z_err2 = z_t-z_1
    z_d_err = z_err2 - z_err1
    if abs(z_err2) < 0.15:
        z_i_err = 0 
    z_i_err = z_i_err + z_err2
    vz_1 = (Kp_z*z_err2 + Kd_z*z_d_err + Ki_z*z_i_err)
    z_err1 = z_err2
    return vx_1,x_err1,x_i_err,vy_1,y_err1,y_i_err,vz_1,z_err1,z_i_err

if __name__ == '__main__':
    
    x_t,y_t,z_t = 3,3,2
    x_old_err,x_int_err = 0,0
    y_old_err,y_int_err = 0,0
    z_old_err,z_int_err = 0,0

    rospy.init_node('robot_state_publisher', anonymous=True)
    r = rospy.Rate(100)

    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    twist = Twist()

    while(1):
        pose = coord()
        rospy.Subscriber("/ground_truth/state",Odometry,pose,queue_size=1)
        x_1,y_1,z_1,theta_1 = pose.get_msg()

        vx_1,x_old_err,x_int_err,vy_1,y_old_err,y_int_err,vz_1,z_old_err,z_int_err = go_to_goal(x_1,x_t,x_old_err,x_int_err,y_1,y_t,y_old_err,y_int_err,z_1,z_t,z_old_err,z_int_err)
        print 'x_1-',x_1,'y_1-',y_1,'z_1-',z_1,'vx_1-',vx_1,'vy_1-',vy_1,'vz_1-',vz_1
        
        twist.linear.x = vx_1
        twist.linear.y = vy_1
        twist.linear.z = vz_1
        pub.publish(twist)

  
    