#!/usr/bin/env python
import pyglet
song = pyglet.media.load('/home/pi/sounds/serdce.mp3')
song.play()
pyglet.app.run()
