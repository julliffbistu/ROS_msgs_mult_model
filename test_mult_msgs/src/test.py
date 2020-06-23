# -*- coding:UTF-8 -*-
#!/usr/bin/env python
import rospy
import roslib
#from后边是自己的包.msg，也就是自己包的msg文件夹下，test是我的msg文件名test.msg
from test_mult_msgs.msg import Test
from test_mult_msgs.msg import objs

B = objs()

def talker():
    pub = rospy.Publisher('chatter', objs, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        beef=Test()
        beef.vel = 20.0
        beef.name = "beef"
        beef.data = [10.0]
        beef.pose.position.x = 1
        beef.pose.position.y = 2
        beef.pose.position.z = 3

        beef.pose.orientation.x = 0.1
        beef.pose.orientation.y = 0.2
        beef.pose.orientation.z = 0.3
        beef.pose.orientation.w = 0.4

        #这里test就像构造函数般使用，若有多个msg，那么写成test(a,b,c,d...)
        #rospy.loginfo(Test.name=temp)
        print(beef)
        print("---------------------------------------------")

        plate=Test()
        plate.vel = 22.0
        plate.name = "plate"
        plate.data = [11.0]
        plate.pose.position.x = 11
        plate.pose.position.y = 22
        plate.pose.position.z = 33

        plate.pose.orientation.x = 0.11
        plate.pose.orientation.y = 0.22
        plate.pose.orientation.z = 0.33
        plate.pose.orientation.w = 0.44
        print(plate)
        print("---------------------------------------------")

        B.objects_test.append(beef)
        B.objects_test.append(plate)
        pub.publish(B)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass