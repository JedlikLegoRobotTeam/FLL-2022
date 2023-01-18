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

    def firstLap(self):
        # watcherThread = threading.Thread(target=self.buttonWatcher)
        # watcherThread.start()
        self.robot.log('Starting 1st lap')
        self.robot.aheadCm(-35, 900, False)
        self.robot.aheadCm(-5, 250, True)
        self.robot.moveLifter(100, Lift.maximum, False)
        self.robot.moveGrab(400, 80, True)
        self.robot.rightOneWheel(Side.left, 900, 135)
        self.robot.aheadCm(9.5, 900, False)
        self.robot.rightOneWheel(Side.left, 900, 95)
        self.robot.aheadCm(5, 900, False)
        self.robot.aheadForXSec(0.75, 900)
        # self.robot.aheadCm(3, 300, True)
        self.robot.ev3.speaker.beep()
        time.sleep(0.2)
        self.robot.aheadCm(-7, 900, True)
        self.robot.aheadForXSec(0.75, 900)
        # self.robot.aheadCm(7, 900, True)
        time.sleep(0.2)
        self.robot.aheadCm(-7, 900, True)
        self.robot.aheadForXSec(0.75, 900)
        # self.robot.aheadCm(8, 900, True)
        time.sleep(0.2)
        self.robot.aheadCm(-7, 900, True)
        # self.robot.aheadCm(8, 900, True)
        self.robot.aheadForXSec(0.75, 900)
        time.sleep(0.2)
        self.robot.aheadCm(-15, 900, True)
        self.robot.leftTwoWheel(900, 100)
        # self.robot.aheadCm(8, 900, True)
        self.robot.aheadForXSec(0.5, 900)
        self.robot.moveLifter(150, Lift.carLift - 10, True)
        self.robot.moveGrab(400, Open.carGrab, False)
        self.robot.grabMotor.run(-400)
        time.sleep(0.75)
        self.robot.aheadCm(-10, 900, True)
        self.robot.moveLifter(100, Lift.maximum, True)
        self.robot.rightTwoWheel(900, 190)
        # self.robot.aheadCm(15, 900, False)
        # self.robot.rightOneWheel(Side.right, 900, 25)
        self.robot.aheadCm(30, 900, False)
        self.robot.goUntilWhite(900, self.robot.rightSensor, False)
        self.robot.aheadCm(30, 900, True)
        
    
    def secondLap(self):
        self.robot.log('Starting 2nd lap')
        self.robot.log(self.robot.liftingMotor.angle())
        self.robot.grabMotor.run(200)
        time.sleep(0.5)
        self.robot.grabMotor.stop()
        self.robot.ev3.speaker.beep()
        while not self.robot.button.pressed():
            pass
        self.robot.grabMotor.run(-400)
        time.sleep(0.5)
        self.robot.moveLifter(200, Lift.maximum, False)
        self.robot.aheadCm(53, 900, False)
        self.robot.leftOneWheel(Side.right, 900, 110)
        self.robot.aheadCm(5, 900, False)
        self.robot.leftOneWheel(Side.right, 900, 15)
        self.robot.aheadCm(5.5, 900, True)
        self.robot.grabMotor.stop()
        self.robot.moveGrab(200, 81, True)
        self.robot.aheadCm(-17.5, 900, True)
        self.robot.moveLifter(200, 30, True)
        self.robot.aheadCm(8, 900, True)
        self.robot.grabMotor.run(-500)
        time.sleep(0.5)
        # self.robot.aheadCm(-10, 900, False)
        self.robot.rightOneWheel(Side.right, 900, 100)
        self.robot.aheadCm(-30, 900, False)
        self.robot.goUntilWhite(-900, self.robot.leftSensor, False)
        self.robot.aheadCm(-35, 900, True)

        
    def thirdLap(self):
        self.robot.log('Starting 3rd lap')
        self.robot.moveLifter(900, Lift.maximum, True)
        self.robot.aheadCm(75, 900, False)
        self.robot.goUntilBlack(900, self.robot.rightSensor, False)
        self.robot.aheadCm(6, 900, True)
        self.robot.leftTwoWheel(900) 
        self.robot.alignOnBlack(-400)
        self.robot.aheadCm(-11.5, 900, True)
        self.robot.moveLifter(200, Lift.carLift, True) 
        self.robot.aheadCm(-4, 800, True)
        self.robot.moveLifter(200, 5, True)
        self.robot.moveGrab(400, 55, True)
        self.robot.aheadCm(5, 900, True)
        self.robot.grabMotor.run(-400)
        time.sleep(0.5)
        self.robot.aheadCm(-5, 900, True)
        self.robot.rightTwoWheel(900)
        self.robot.aheadCm(-8, 900, True)
        self.robot.leftTwoWheel(900)
        self.robot.moveLifter(200, Lift.carLift, True)
        self.robot.aheadCm(6, 900, True)
        # self.robot.rightOneWheel(Side.left, 900, 15)
        # self.robot.moveLifter(200, Lift.maximum, True)
        self.robot.liftingMotor.run(200)
        time.sleep(0.5)
        self.robot.liftingMotor.stop(Stop.HOLD)
        self.robot.moveLifter(600, 100, True)
        # self.robot.aheadCm(-1, 900, True)
        self.robot.rightTwoWheel(900,125)
        self.robot.aheadCm(-55, 900, False)
        # self.robot.leftOneWheel(Side.left, 900, 10)
        # self.robot.aheadCm(-25, 900, False)
        self.robot.goUntilWhite(-900, self.robot.rightSensor, False)
        self.robot.aheadCm(-30, 900, True)
        self.robot.alignOnBlack(-200)

    def FourthLap(self):
        # First Task
        self.robot.moveLifter(speed=400, measure=5, wait=True)
        self.robot.aheadCm(distance=70, speed=900, stop=False)
        self.robot.goUntilWhite(speed=900, szenzor=self.robot.leftSensor)
        self.robot.leftOneWheel(wheel=Side.right, speed=600)
        self.robot.moveLifter(speed=400, measure=100, wait=False)
        # robot.aheadCm(distance=30, speed=500, stop=False)
        self.robot.aheadCm(speed=900, distance=29, stop=False)
        self.robot.ev3.speaker.beep()
        self.robot.alignOnWhite(300)
        self.robot.aheadForXSec(time_=0.35, speed=800)

        # SecondTask
        self.robot.aheadCm(distance=-4, speed=400, stop=True)
        self.robot.moveGrab(speed=800, measure=Open.maximumOpen, wait=False)
        self.robot.leftTwoWheel(speed=900, angle=90)
        self.robot.leftOneWheel(wheel=Side.right, speed=900, angle=37)
        self.robot.aheadCm(distance=-12, speed=900, stop=True)
        self.robot.moveLifter(speed=900, measure=5, wait=True)
        self.robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=11.5, speed=900, stop=True)
        self.robot.grabMotor.run(-200)
        time.sleep(0.5)
        self.robot.aheadCm(distance=-4, speed=900, stop=True)
        self.robot.moveLifter(speed=900, measure=80, wait=True)
        self.robot.aheadCm(distance=13, speed=900, stop=True)
        time.sleep(0.5)
        self.robot.moveGrab(speed=300, measure=Open.halfOpen, wait=True)
        self.robot.moveLifter(speed=400, measure=Lift.maximum, wait=True)
        self.robot.aheadCm(distance=-2, speed=900, stop=True)
        time.sleep(0.4)
        self.robot.rightTwoWheel(speed=900, angle=125)

        # Third Task
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.aheadCm(distance=4, speed=900, stop=False)
        # self.robot.alignOnBlack(speed=900) 
        self.robot.moveGrab(speed=500, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=10, speed=900, stop=True)
        self.robot.grabMotor.run(-400)
        time.sleep(0.5)
        self.robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
        self.robot.alignOnWall(seconds=1.5, speed=500)
        self.robot.aheadCm(distance=-6, speed=600, stop=True)
        self.robot.leftTwoWheel(speed=400)
        self.robot.moveLifter(speed=300, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=35, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=-17)
        self.robot.aheadCm(distance=11, speed=600, stop=True)
        self.robot.grabMotor.run(-400)
        time.sleep(0.5)
        self.robot.aheadCm(distance=-2, speed=600, stop=True)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=8)  #TESZT
        self.robot.aheadCm(distance=15, speed=500, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-15, speed=600, stop=True)
        self.robot.moveLifter(speed=300, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=9, speed=600, stop=True)
        self.robot.grabMotor.run(-400)
        time.sleep(0.5)
        # self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-11, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.aheadCm(distance=15, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-5, speed=600, stop=True)

        # Fourth Task
        self.robot.leftTwoWheel(speed=300, angle=95)
        self.robot.moveGrab(speed=400, measure=Open.maximumOpen, wait=True)
        self.robot.alignOnWall(1, -800)
        # self.robot.aheadCm(distance=10, speed=400, stop=True)
        # self.robot.alignOnWhite(speed=150)
        # self.robot.aheadCm(distance=3, speed=400, stop=True)
        self.robot.aheadCm(distance=15, speed=900, stop=True)
        self.robot.rightTwoWheel(speed=300, angle=92)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.aheadCm(distance=22, speed=400, stop=True)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.leftSensor, stop=True)
        self.robot.aheadCm(distance=-4, speed=400, stop=True)
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
        self.robot.aheadCm(distance=19, speed=700, stop=True)
        self.robot.rightTwoWheel(speed=400) 
        time.sleep(0.3)  #                                          GYORSÍTÁS
        self.robot.aheadCm(distance=-10, speed=700, stop=True)
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        # self.robot.aheadCm(distance=2, speed=700, stop=True)
        self.robot.grabMotor.run(-200)
        time.sleep(0.5)
        self.robot.aheadCm(distance=-20, speed=700, stop=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=500, angle=-50)
        self.robot.aheadCm(distance=-50, speed=700, stop=True)

    def startProgramOnPress(self, nextProgramNumber):
        while True:
            if self.robot.button.pressed():
                break
        if nextProgramNumber == 0:
            self.firstLap()
        elif nextProgramNumber == 1:
            self.secondLap()
        elif nextProgramNumber == 2:
            self.thirdLap()
        elif nextProgramNumber == 3:
            self.FourthLap()
        elif nextProgramNumber == 4:
            self.dinoToTheOtherSide()

        self.robot.log('{0}. kör készen!'.format(nextProgramNumber + 1))

    def dinoToTheOtherSide(self):
        self.robot.aheadCm(160, 900, False)
        self.robot.goUntilWhite(900, self.robot.rightSensor, False)
        self.robot.aheadCm(20, 900, True)


    def menu(self):
        self.robot.ev3.screen.clear()
        program = 0
        self.robot.ev3.screen.print(Programs.programs[program])
        while True:
            if Button.DOWN in self.robot.ev3.buttons.pressed():
                program = 4 if program == 0 else program - 1
                self.robot.ev3.screen.clear()
                self.robot.ev3.screen.print(Programs.programs[program])
                time.sleep(0.5)
            elif Button.UP in self.robot.ev3.buttons.pressed():
                program = 0 if program == 4 else program + 1
                self.robot.ev3.screen.clear()
                self.robot.ev3.screen.print(Programs.programs[program])
                time.sleep(0.5)
            elif Button.LEFT in self.robot.ev3.buttons.pressed():
                self.robot.liftingMotor.stop()
                self.robot.grabMotor.stop()
                self.robot.liftingMotor.run(-200)
                self.robot.grabMotor.run(-200)
                time.sleep(1)
                self.robot.grabMotor.reset_angle(0)
                self.robot.liftingMotor.reset_angle(-20)
                self.robot.grabMotor.stop()
                self.robot.liftingMotor.stop()
                # self.robot.ev3.screen.clear()
                # self.robot.ev3.screen.print("Kalib kész")
            if Button.CENTER in self.robot.ev3.buttons.pressed():
                return program
