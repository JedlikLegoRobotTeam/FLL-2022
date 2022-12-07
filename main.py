#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from fllrobot import *
from feladatok import *
import time

robot = FllRobot()
feladatok = Feladat(robot)

feladatok.firstTask()
feladatok.secondTask()
feladatok.thirdTask()
feladatok.fourthTask()
feladatok.fifthTask()

sys.exit()
# robot.leftOneWheel(wheel=Side.right, speed=400, angle=50)
# robot.leftOneWheel(wheel=Side.right, speed=400, angle=90)
# robot.aheadCm(distance=55, speed=500, stop=True) 
# Gyurcsótány; Brüsszel; Soros; Biden; Zelenszkij; MZP
# Csak a Ferrari, next year will be our year!44!!!!

                                               # KŐ KALIB BAKKER