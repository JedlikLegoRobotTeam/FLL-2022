from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from fllrobot import *
from enums import *
import time

class Feladat:
    def __init__(self, fllRobot: FllRobot) -> None:
        self.robot = fllRobot
        
    def FourthLap(self):
        # First Task
        self.robot.moveLifter(speed=400, measure=5, wait=True)
        self.robot.aheadCm(distance=70, speed=800, stop=False)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.leftSensor)
        self.robot.leftOneWheel(wheel=Side.right, speed=500)
        self.robot.moveLifter(speed=400, measure=100, wait=False)
        # robot.aheadCm(distance=30, speed=500, stop=False)
        self.robot.aheadCm(speed=700, distance=29, stop=True)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.rightSensor, stop=False)
        self.robot.alignOnWall(seconds=1.1, speed=200)

        # SecondTask
        self.robot.aheadCm(distance=-6, speed=400, stop=True)
        self.robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=False)
        self.robot.leftTwoWheel(speed=300, angle=90)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=37)
        self.robot.aheadCm(distance=-12, speed=400, stop=True)
        self.robot.moveLifter(speed=400, measure=5, wait=True)
        self.robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=13, speed=200, stop=True)
        self.robot.moveGrab(speed=300, measure=Open.closing, wait=True)
        self.robot.grabMotor.run(-200)
        self.robot.aheadCm(distance=-4, speed=400, stop=True)
        self.robot.moveLifter(speed=400, measure=80, wait=True)
        self.robot.aheadCm(distance=13, speed=300, stop=True)
        time.sleep(0.5)
        self.robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
        self.robot.moveLifter(speed=400, measure=Lift.maximum, wait=True)
        self.robot.aheadCm(distance=-2, speed=600, stop=True)
        time.sleep(0.4)
        self.robot.rightTwoWheel(speed=300, angle=125)

        # Third Task
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.aheadCm(distance=4, speed=300, stop=True)
        time.sleep(0.5)
        self.robot.alignOnBlack(speed=100) 
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=10, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
        self.robot.alignOnWall(seconds=1.5, speed=300)
        self.robot.aheadCm(distance=-6, speed=600, stop=True)
        self.robot.leftTwoWheel(speed=400)
        self.robot.moveLifter(speed=300, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=35, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=-17)
        self.robot.aheadCm(distance=14, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-5, speed=600, stop=True)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=8)  #TESZT
        self.robot.aheadCm(distance=15, speed=500, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-15, speed=600, stop=True)
        self.robot.moveLifter(speed=300, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=9, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-11, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.aheadCm(distance=15, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-5, speed=600, stop=True)

        # Fourth Task
        self.robot.leftTwoWheel(speed=300, angle=95)
        self.robot.moveGrab(speed=400, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=12, speed=400, stop=True)
        self.robot.alignOnWhite(speed=300)
        self.robot.aheadCm(distance=3, speed=400, stop=True)
        self.robot.rightTwoWheel(speed=300, angle=92)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.aheadCm(distance=22, speed=400, stop=True)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.leftSensor, stop=True)
        self.robot.aheadCm(distance=-5, speed=400, stop=True)
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.moveGrab(speed=300, measure=18, wait=True)
        self.robot.moveLifter(speed=200, measure=60, wait=True)
        self.robot.moveLifter(speed=200, measure=0, wait=True)
        self.robot.moveLifter(speed=200, measure=60, wait=True)
        self.robot.moveLifter(speed=200, measure=0, wait=True)
        self.robot.moveLifter(speed=200, measure=60, wait=True)
        self.robot.moveLifter(speed=200, measure=0, wait=True)
        self.robot.moveLifter(speed=200, measure=60, wait=True)
        self.robot.moveLifter(speed=200, measure=0, wait=True)

        # Fifth Task
        self.robot.aheadCm(distance=-10, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
        self.robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=21, speed=500, stop=True)
        self.robot.rightTwoWheel(speed=400) 
        time.sleep(0.3)  #                                          GYORSÍTÁS
        self.robot.aheadCm(distance=-10, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.aheadCm(distance=4, speed=500, stop=True)
        self.robot.moveGrab(speed=400, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-20, speed=400, stop=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=300, angle=-50)
        self.robot.aheadCm(distance=-50, speed=500, stop=True)
    
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
