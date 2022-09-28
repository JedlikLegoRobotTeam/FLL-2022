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
import time

class Feladat:
    def __init__(self, fllRobot: FllRobot) -> None:
        self.robot = fllRobot
    
    def elsoKor(self):
        self.robot.aheadCm(-35, 600, False)
        self.robot.aheadCm(-5, 250, True)
        self.robot.moveLifter(100, Lift.maximum, False)
        # Ki kell nyitni
        self.robot.moveGrab(300, 80, True)
        self.robot.rightOneWheel(Side.left, 800, 135)
        self.robot.aheadCm(9.5, 800, False)
        self.robot.rightOneWheel(Side.left, 800, 100)
        self.robot.aheadCm(5, 800, False)
        self.robot.aheadCm(9, 300, True)
        self.robot.ev3.speaker.beep()
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(9, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(9, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(9, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-15, 800, True)
        self.robot.moveLifter(100, 45, False)
        self.robot.leftTwoWheel(800, 105)
        self.robot.moveGrab(200, 35, False)
        self.robot.aheadCm(9, 600, True)
        self.robot.grabMotor.run(-200)
        time.sleep(1)
        self.robot.aheadCm(-20, 800, True)
        self.robot.moveLifter(200, 25, True)
        self.robot.leftTwoWheel(500, 180)
        
        self.robot.aheadCm(80, 800, False)