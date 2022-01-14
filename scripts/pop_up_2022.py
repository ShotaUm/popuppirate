#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

import random

rospy.init_node('mogura')
pub = rospy.Publisher('mogura_sagasi', Int32, queue_size=1)

num = random.randint(0,9)

i = 0


print("勝負をしよう")
print("私が思い浮かべた数字をひたすら避けるんだ")

while i < 9:

    st = input()

    if num == int(st):
        print("君の負けだ")
        print(("\a"))
        i = 9
    else:
        print("続けよう")
        i = i + 1
