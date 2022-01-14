# popuppirate

# 概要
黒ひげ危機一髪風の簡単なゲームができるパッケージ

# 動作環境
OS:Ubuntu 20.04
          
# 実行方法

  コマンドを入力  
  ```
  $cd ~/catkin_ws/src  
  $git clone -b master https://github.com/ShotaUm/popuppirate.git  
  $catkin_make  

  $roscore  

  $rosrun popuppirate pop_up_2022.py  
  ```
  0~9までランダムな数字を聞かれます。  
  乱数で選ばれたある一つの数字を当ててしまったら終了です。  
``````
  例)  
  勝負をしよう  
  私が思い浮かべた数字をひたすら避けるんだ  
  1  
  続けよう  
  2  
  続けよう  
  3  
  続けよう  
  4  
  君の負けだ  

# 参考動画  
https://youtu.be/ebRE607LCJQ  

# 引用  
pop_up_2022.py  
"#!/usr/bin/env python3  
import rospy  
from std_msgs.msg import Int32  

import random  
  
rospy.init_node('mogura')  
pub = rospy.Publisher('mogura_sagasi', Int32, queue_size=1)  
  
num = random.randint(0,9) "  
(Ryuichi Ueda)  
