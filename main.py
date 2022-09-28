#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from enums import *
from fllrobot import *
from feladatok import *
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
robot = FllRobot()
robot.aheadCm(distance=70, speed=500, stop=False)
robot.goUntilWhite(speed=300, szenzor=robot.leftSensor)
robot.leftOneWheel (wheel=Side.right,speed=500)
robot.moveGrab(speed=500, measure=45, wait=False)
robot.aheadCm(distance=30, speed=500, stop=False)
robot.goUntilWhite(speed=300, szenzor=robot.rightSensor)









time.sleep(1)