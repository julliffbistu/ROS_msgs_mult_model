# -*- coding:UTF-8 -*-
#!/usr/bin/env python
import rospy
import roslib
#from后边是自己的包.msg，也就是自己包的msg文件夹下，test是我的msg文件名test.msg
from test_mult_msgs.msg import Test
from test_mult_msgs.msg import objs


def callback(data):

    print(data.objects_test[0].name)
    print(data.objects_test[0].vel)
    print(data.objects_test[0].pose.position.x)
    print(data.objects_test[0].pose.position.y)
    print(data.objects_test[0].pose.position.z)
    print(data.objects_test[0].pose.orientation.x)
    print(data.objects_test[0].pose.orientation.y)
    print(data.objects_test[0].pose.orientation.z)
    print(data.objects_test[0].pose.orientation.w)
    #print("-----------",data.name)
    #print("-----------",data.vel)
    #print("-----------",data.pose.position.x)
    #print("-----------",data.pose.position.y)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print("----"*15)

    print(data.objects_test[1].name)
    print(data.objects_test[1].vel)
    print(data.objects_test[1].pose.position.x)
    print(data.objects_test[1].pose.position.y)
    print(data.objects_test[1].pose.position.z)
    print(data.objects_test[1].pose.orientation.x)
    print(data.objects_test[1].pose.orientation.y)
    print(data.objects_test[1].pose.orientation.z)
    print(data.objects_test[1].pose.orientation.w)
    print("----"*15)

def listener():
 
    rospy.init_node('listener', anonymous=True)
 
    rospy.Subscriber("chatter", objs, callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()
