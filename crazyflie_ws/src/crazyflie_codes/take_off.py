#!/usr/bin/env python 

import rospy
import sys
import math
from crazyflie_driver.msg import Hover

def takeOff(zDistance):
    time_range = zDistance
    while not rospy.is_shutdown():
        for y in range(zDistance):
            msg.vx = 0.0
            msg.vy = 0.0
            msg.yawrate = 0.0
            msg.zDistance = y 
            msg.header.seq += 1
            msg.header.stamp = rospy.Time.now()
            pub.publish(msg)
            rate.sleep()
        for y in range(20):
            msg.vx = 0.0
            msg.vy = 0.0
            msg.yawrate = 0.0
            msg.zDistance = zDistance
            msg.header.seq += 1
            msg.header.stamp = rospy.Time.now()
            pub.publish(msg)
            rate.sleep()
        break

def land(zDistance):
    print 'oky'
    while not rospy.is_shutdown():
        while zDistance > 0:
            msg.vx = 0.0
            msg.vy = 0.0
            msg.yawrate = 0.0
            msg.zDistance = zDistance 
            msg.header.seq += 1
            msg.header.stamp = rospy.Time.now()
            pub.publish(msg)
            zDistance -= 2
            #print zDistance
            rate.sleep()
        break

if __name__ == '__main__':

    pub = rospy.Publisher('/cf1/cmd_hover',Hover,queue_size=1)
    rospy.init_node('rviz')
    rate = rospy.Rate(10)
    msg = Hover()
    takeOff(50)
    land(50)



