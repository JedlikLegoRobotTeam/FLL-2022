#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from fllrobot import *
import time

robot = FllRobot()
robot.moveLifter(speed=400, measure=5, wait=True)
robot.aheadCm(distance=70, speed=700, stop=False)
robot.goUntilWhite(speed=300, szenzor=robot.leftSensor)
robot.leftOneWheel(wheel=Side.right,speed=500)
robot.moveLifter(speed=400, measure=100, wait=False)
# robot.aheadCm(distance=30, speed=500, stop=False)
robot.aheadCm(speed=500, distance=29, stop=True)
robot.goUntilWhite(speed=300, szenzor=robot.rightSensor, stop=False)
robot.alignOnWall(seconds=1, speed=200)
robot.aheadCm(distance=-6, speed=400, stop=True)
robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=False)
robot.leftTwoWheel(speed=300, angle=90)
robot.leftOneWheel(wheel=Side.right, speed=400, angle=37)
robot.aheadCm(distance=-12, speed=400, stop=True)
robot.moveLifter(speed=400, measure=5, wait=True)
robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
robot.aheadCm(distance=13, speed=200, stop=True)
robot.moveGrab(speed=300, measure=Open.closing, wait=True)
robot.grabMotor.run(-200)
robot.aheadCm(distance=-4, speed=400, stop=True)
robot.moveLifter(speed=400, measure=80, wait=True)
robot.aheadCm(distance=13, speed=300, stop=True)
time.sleep(0.5)
robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
robot.moveLifter(speed=400, measure=Lift.maximum, wait=True)
robot.aheadCm(distance=-2, speed=600, stop=True)
time.sleep(0.4)
robot.rightTwoWheel(speed=300, angle=130)

# # cuccok bedobasa a konténerbe
robot.moveLifter(speed=300, measure=0, wait=True)
time.sleep(0.5)
robot.alignOnBlack(speed=200) 
robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
robot.aheadCm(distance=10, speed=600, stop=True)
robot.moveGrab(speed=300, measure=Open.closing, wait=True)
robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
robot.alignOnWall(seconds=1.5, speed=300)
robot.aheadCm(distance=-6, speed=600, stop=True)
robot.leftTwoWheel(speed=400)
robot.moveLifter(speed=200, measure=2, wait=True)
robot.moveGrab(speed=300, measure=35, wait=True)
robot.leftOneWheel(wheel=Side.right, speed=400, angle=-15)
robot.aheadCm(distance=14, speed=600, stop=True)
robot.moveGrab(speed=200, measure=Open.closing, wait=True)
robot.aheadCm(distance=-5, speed=400, stop=True) #hatrebb jonni megfogas utan
robot.moveLifter(speed=200, measure=100, wait=True)
robot.leftOneWheel(wheel=Side.right, speed=400, angle=5)
robot.aheadCm(distance=14, speed=400, stop=True)
robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
robot.aheadCm(distance=-15, speed=600, stop=True)
robot.moveLifter(speed=200, measure=2, wait=True)
robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
robot.aheadCm(distance=9, speed=600, stop=True)
robot.moveGrab(speed=300, measure=Open.closing, wait=True)
robot.aheadCm(distance=-11, speed=300, stop=True)
robot.moveLifter(speed=200, measure=100, wait=True)
robot.aheadCm(distance=15, speed=600, stop=True)
robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
robot.aheadCm(distance=-5, speed=200, stop=True)

# # pumpálás
robot.leftTwoWheel(speed=300, angle=95)
robot.moveGrab(speed=400, measure=Open.maximumOpen, wait=True)
robot.aheadCm(distance=12, speed=400, stop=True)
robot.alignOnWhite(speed=300)
robot.aheadCm(distance=3, speed=400, stop=True)
robot.rightTwoWheel(speed=300, angle=91)
robot.moveLifter(speed=300, measure=83, wait=True)
robot.aheadCm(distance=22, speed=400, stop=True)
robot.goUntilWhite(speed=300, szenzor=robot.leftSensor, stop=True)
robot.aheadCm(distance=-4.5, speed=400, stop=True)
robot.moveLifter(speed=300, measure=0, wait=True)
robot.moveGrab(speed=300, measure=18, wait=True)
robot.moveLifter(speed=200, measure=60, wait=True)
robot.moveLifter(speed=200, measure=0, wait=True)
robot.moveLifter(speed=200, measure=60, wait=True)
robot.moveLifter(speed=200, measure=0, wait=True)
robot.moveLifter(speed=200, measure=60, wait=True)
robot.moveLifter(speed=200, measure=0, wait=True)
robot.moveLifter(speed=200, measure=60, wait=True)
robot.moveLifter(speed=200, measure=0, wait=True)

# # tálca kihúzás
robot.aheadCm(distance=-10, speed=500, stop=True)
robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
robot.aheadCm(distance=22, speed=500, stop=True)
robot.rightTwoWheel(speed=400) 
time.sleep(0.3)  #                                          GYORSÍTÁS
robot.aheadCm(distance=-10, speed=500, stop=True)
robot.moveLifter(speed=300, measure=0, wait=True)
robot.aheadCm(distance=4, speed=500, stop=True)
robot.moveGrab(speed=400, measure=Open.closing, wait=True)
robot.aheadCm(distance=-20, speed=400, stop=True)
robot.leftOneWheel(wheel=Side.right, speed=300, angle=-50)
robot.aheadCm(distance=-50, speed=500, stop=True)

sys.exit()
# robot.leftOneWheel(wheel=Side.right, speed=400, angle=50)
# robot.leftOneWheel(wheel=Side.right, speed=400, angle=90)
# robot.aheadCm(distance=55, speed=500, stop=True) 
# Gyurcsótány; Brüsszel; Soros; Biden; Zelenszkij; MZP
# Csak a Ferrari, next year will be our year!44!!!!

                                               # KŐ KALIB BAKKER