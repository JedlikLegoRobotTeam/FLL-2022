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
    
    def firstLap(self):
        self.robot.aheadCm(-35, 600, False)
        self.robot.aheadCm(-5, 250, True)
        self.robot.moveLifter(100, Lift.maximum, False)
        self.robot.moveGrab(300, 80, True)
        self.robot.rightOneWheel(Side.left, 800, 135)
        self.robot.aheadCm(9.5, 800, False)
        self.robot.rightOneWheel(Side.left, 800, 100)
        self.robot.aheadCm(5, 800, False)
        self.robot.aheadCm(7, 300, True)
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
        self.robot.moveLifter(100, 40, False)
        self.robot.moveGrab(200, Open.carGrab, False)
        self.robot.leftTwoWheel(800, 100)
        self.robot.aheadCm(7.5, 600, True)
        self.robot.grabMotor.run(-200)
        time.sleep(1)
        self.robot.aheadCm(-25, 800, False)
        self.robot.rightOneWheel(Side.right, 800, 35)
        self.robot.aheadCm(-50, 800, False)
        
    
    def secondLap(self):
        self.robot.log('Starting 2nd lap')
        self.robot.grabMotor.run(200)
        time.sleep(0.5)
        self.robot.grabMotor.stop()
        self.robot.changeProgram()
        self.robot.ev3.speaker.beep()
        self.robot.grabMotor.run(-200)
        time.sleep(3.5)
        self.robot.moveLifter(200, Lift.maximum, False)
        self.robot.aheadCm(54, 800, False)
        self.robot.leftOneWheel(Side.right, 800, 90)
        self.robot.aheadCm(8.5, 800, False)
        self.robot.leftOneWheel(Side.right, 800, 47)
        self.robot.aheadCm(3, 800, True)
        self.robot.grabMotor.stop()
        self.robot.moveGrab(200, 81, True)
        self.robot.aheadCm(-17.5, 800, True)
        self.robot.moveLifter(200, 0, True)
        self.robot.aheadCm(8, 800, True)
        self.robot.grabMotor.run(-200)
        time.sleep(1)
        # self.robot.aheadCm(-10, 800, False)
        self.robot.rightOneWheel(Side.right, 800, 125)
        self.robot.aheadCm(-100, 800, False)
    
    def thirdLap(self):
        self.robot.moveLifter(800, Lift.maximum, True)
        self.robot.aheadCm(75, 800, False)
        self.robot.goUntilBlack(800, self.robot.rightSensor, False)
        self.robot.aheadCm(6, 800, True)
        self.robot.leftTwoWheel(800) 
        self.robot.alignOnBlack(-400)
        self.robot.aheadCm(-12, 800, True)
        self.robot.moveLifter(200, Lift.carLift, True)   
        # Még meg kell nyomni a másikat
        # self.robot.rightOneWheel(Side.left, 800, 30) # Valamiért még szar
        # self.robot.aheadCm(, 800, False)
        # self.robot.leftOneWheel(Side.right, 800, 30)
        # self.robot.aheadCm(10, 800, False)
        # self.robot.alignOnBlack(400)
        # self.robot.aheadCm(6, 800, True)
        # Még ninc teljesen befejezve.