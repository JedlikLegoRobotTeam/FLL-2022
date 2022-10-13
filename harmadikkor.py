#!/usr/bin/env pybricks-micropython

from fllrobot import *
from feladatok import *

robot = FllRobot()
feladatok = Feladat(robot)
robot.ev3.speaker.beep()

feladatok.startProgramOnPress(feladatok.thirdLap)
