#!/usr/bin/env python
import rospy
import pyglet

def callback(data):
    song = pyglet.media.load('/home/pi/sounds/serdce.mp3')
    song.play()
    pyglet.app.run()

def listener():
	rospy.init_node('sound', anonymous=True)
	rospy.Subscriber("chatter", String, callback)

if __name__ == '__main__':
    listener()

