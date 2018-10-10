#!/usr/bin/env python 

import rospy
import sys
import math
from crazyflie_driver.msg import FullState
from crazyflie_driver.msg import Hover

if __name__ == '__main__':

    pub = rospy.Publisher('/cf1/cmd_hover',Hover,queue_size=5)
    rospy.init_node('rviz')
    rate = rospy.Rate(10)
    msg = Hover()
    i = 0
    while i < 60:
    	print i
    	msg.zDistance = 40
    	pub.publish(msg)
    	rate.sleep()
    	i=i+2



