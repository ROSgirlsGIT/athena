#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_name()+"I heard %s",data.data)
	pwm.start(2.5)
	for x in range(0,5):          
        pwm.ChangeDutyCycle(7.5)
        rospy.sleep(0.2)   
        pwm.ChangeDutyCycle(12.5)
        rospy.sleep(0.6)               
        pwm.ChangeDutyCycle(2.5)
        rospy.sleep(0.2)
        pwm.ChangeDutyCycle(7.5)
        rospy.sleep(0.1)
	pwm.ChangeDutyCycle(0)

def listener():
	rospy.init_node('servo', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)

if __name__ == '__main__':
	listener()
