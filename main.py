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
robot.rightOneWheel(wheel=Side.left,speed=400,angle=50)
robot.leftOneWheel(wheel=Side.left,speed=400,angle=50)
sys.exit()

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
robot.aheadCm(distance=70, speed=700, stop=False)
robot.goUntilWhite(speed=300, szenzor=robot.leftSensor)
robot.leftOneWheel(wheel=Side.right,speed=500)
robot.moveLifter(speed=400, measure=90, wait=False)
# robot.aheadCm(distance=30, speed=500, stop=False)
robot.forwardWithGyro(speed=500, distance=29, stop=True)
robot.goUntilWhite(speed=300, szenzor=robot.rightSensor, stop=False)
robot.aheadCm(distance=13, speed=400, stop=True)
robot.alignOnWhite(speed=-300)
robot.alignOnBlack(speed=-300)
robot.aheadCm(distance=-8, speed=400, stop=True)
robot.rightOneWheel(wheel=Side.right, speed=400, angle=32)
robot.moveLifter(speed=400, measure=0, wait=False)
robot.aheadCm(distance=29, speed=500, stop=True) # Gyurcsótány; Brüsszel; Soros; Biden; Zelenszkij; MZP

print()
time.sleep(0.2)









time.sleep(1)