
#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_name()+"I heard %s",data.data)
        led.start(1)
        rospy.sleep(0.01)
        for x in range(0,5):
                for pow in range (1, 101, 1):
                        led.ChangeDutyCycle(pow)
                        rospy.sleep(0.015)
                for pow in range (100, 0, -1):
                        led.ChangeDutyCycle(pow)
                        rospy.sleep(0.015)
        led.ChangeDutyCycle(0)
        led.stop()
        GPIO.cleanup()

def listener():
	rospy.init_node('led', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

led=GPIO.PWM(18,50)

if __name__ == '__main__':
	listener()
