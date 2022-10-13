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
        self.robot.log('Starting 1st lap')
        self.robot.aheadCm(-35, 600, False)
        self.robot.aheadCm(-5, 250, True)
        self.robot.moveLifter(100, Lift.maximum, False)
        self.robot.moveGrab(300, 80, True)
        self.robot.rightOneWheel(Side.left, 800, 135)
        self.robot.aheadCm(9.5, 800, False)
        self.robot.rightOneWheel(Side.left, 800, 95)
        self.robot.aheadCm(5, 800, False)
        self.robot.aheadCm(2.75, 300, True)
        self.robot.ev3.speaker.beep()
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(6, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(7.5, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-7, 400, True)
        self.robot.aheadCm(7.5, 400, True)
        time.sleep(0.5)
        self.robot.aheadCm(-15, 800, True)
        self.robot.moveLifter(100, Lift.carLift, False)
        self.robot.moveGrab(200, Open.carGrab - 5, False)
        self.robot.leftTwoWheel(800, 90)
        self.robot.aheadCm(14, 600, True)
        self.robot.grabMotor.run(-200)
        time.sleep(1)
        self.robot.moveLifter(200, Lift.carLift + 10, True)
        self.robot.aheadCm(-10, 800, True)
        self.robot.rightTwoWheel(800, 250)
        # self.robot.aheadCm(15, 800, False)
        # self.robot.rightOneWheel(Side.right, 800, 25)
        self.robot.aheadCm(80, 800, True)

        
    
    def secondLap(self):
        self.robot.log('Starting 2nd lap')
        self.robot.grabMotor.run(200)
        time.sleep(0.5)
        self.robot.grabMotor.stop()
        self.robot.ev3.speaker.beep()
        time.sleep(3.5)
        self.robot.grabMotor.run(-200)
        time.sleep(1)
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
        self.robot.log('Starting 3rd lap')
        self.robot.moveLifter(800, Lift.maximum, True)
        self.robot.aheadCm(75, 800, False)
        self.robot.goUntilBlack(800, self.robot.rightSensor, False)
        self.robot.aheadCm(6, 800, True)
        self.robot.leftTwoWheel(800) 
        self.robot.alignOnBlack(-400)
        self.robot.aheadCm(-13, 800, True)
        self.robot.moveLifter(200, Lift.carLift, True) 
        self.robot.aheadCm(-4, 600, True)
        self.robot.moveLifter(200, 5, True)
        self.robot.moveGrab(200, 45, True)
        self.robot.aheadCm(5, 800, True)
        self.robot.grabMotor.run(-200)
        time.sleep(0.5)
        self.robot.aheadCm(-5, 800, True)
        self.robot.rightTwoWheel(800)
        self.robot.aheadCm(-8, 800, True)
        self.robot.leftTwoWheel(800)
        self.robot.moveLifter(200, Lift.carLift, True)
        self.robot.aheadCm(6, 800, True)
        # self.robot.rightOneWheel(Side.left, 800, 15)
        # self.robot.moveLifter(200, Lift.maximum, True)
        self.robot.liftingMotor.run(200)
        time.sleep(1)
        self.robot.liftingMotor.stop(Stop.HOLD)
        self.robot.moveLifter(200, Lift.carLift, True)
        # self.robot.aheadCm(-1, 800, True)
        self.robot.rightTwoWheel(800,125)
        self.robot.aheadCm(-30, 800, False)
        self.robot.leftOneWheel(Side.left, 800, 45)
        self.robot.aheadCm(-70, 800, False)

    def startProgramOnPress(self, nextProgramNumber):
        while True:
            if self.robot.button.pressed():
                break
        if nextProgramNumber == 0:
            self.firstLap()
        elif nextProgramNumber == 1:
            self.secondLap()
        elif nextProgramNumber == 2:
            self.thirdLap
    # def dinoToTheOtherSide(self)



    def menu(self):
        program = 0
        self.robot.ev3.screen.print(Programs.programs[program])
        while True:
            if Button.DOWN in self.robot.ev3.buttons.pressed():
                program = 0 if program >= 2 else program + 1
                self.robot.ev3.screen.clear()
                self.robot.ev3.screen.print(Programs.programs[program])
                time.sleep(0.5)
            elif Button.UP in self.robot.ev3.buttons.pressed():
                program = 0 if program >= 2 else program - 1
                self.robot.ev3.screen.clear()
                self.robot.ev3.screen.print(Programs.programs[program])
                time.sleep(0.5)
            if Button.CENTER in self.robot.ev3.buttons.pressed():
                return program