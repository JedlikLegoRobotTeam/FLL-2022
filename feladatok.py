from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from fllrobot import *

class Feladat:
    def __init__(self, fllRobot: FllRobot) -> None:
        self.robot = fllRobot

    def firstTask(self):
        self.robot.moveLifter(speed=400, measure=5, wait=True)
        self.robot.aheadCm(distance=70, speed=800, stop=False)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.leftSensor)
        self.robot.leftOneWheel(wheel=Side.right, speed=500)
        self.robot.moveLifter(speed=400, measure=100, wait=False)
        # robot.aheadCm(distance=30, speed=500, stop=False)
        self.robot.aheadCm(speed=700, distance=29, stop=True)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.rightSensor, stop=False)
        self.robot.alignOnWall(seconds=1.1, speed=200)

    def secondTask(self):
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

    def thirdTask(self):
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.aheadCm(distance=4, speed=300, stop=True)
        time.sleep(0.5)
        self.robot.alignOnBlack(speed=100) 
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=10, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.moveLifter(speed=500, measure=Lift.maximum, wait=True)
        self.robot.alignOnWall(seconds=1.5, speed=300)
        self.robot.aheadCm(distance=-6, speed=600, stop=True)
        self.robot.leftTwoWheel(speed=400)
        self.robot.moveLifter(speed=500, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=35, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=-17)
        self.robot.aheadCm(distance=14, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-5, speed=600, stop=True)
        self.robot.moveLifter(speed=500, measure=100, wait=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=400, angle=5)  #TESZT
        self.robot.aheadCm(distance=15, speed=500, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-15, speed=600, stop=True)
        self.robot.moveLifter(speed=500, measure=2, wait=True)
        self.robot.moveGrab(speed=500, measure=Open.halfOpen, wait=True)
        self.robot.aheadCm(distance=9, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-11, speed=500, stop=True)
        self.robot.moveLifter(speed=500, measure=100, wait=True)
        self.robot.aheadCm(distance=15, speed=600, stop=True)
        self.robot.moveGrab(speed=500, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=-5, speed=600, stop=True)

    def fourthTask(self):
        self.robot.leftTwoWheel(speed=300, angle=95)
        self.robot.moveGrab(speed=400, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=12, speed=400, stop=True)
        self.robot.alignOnWhite(speed=300)
        self.robot.aheadCm(distance=3, speed=400, stop=True)
        self.robot.rightTwoWheel(speed=300, angle=95)
        self.robot.moveLifter(speed=300, measure=100, wait=True)
        self.robot.aheadCm(distance=22, speed=400, stop=True)
        self.robot.goUntilWhite(speed=300, szenzor=self.robot.leftSensor, stop=True)
        self.robot.aheadCm(distance=-4.5, speed=400, stop=True)
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

    def fifthTask(self):
        self.robot.aheadCm(distance=-10, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=Lift.maximum, wait=True)
        self.robot.moveGrab(speed=300, measure=Open.maximumOpen, wait=True)
        self.robot.aheadCm(distance=22, speed=500, stop=True)
        self.robot.rightTwoWheel(speed=400) 
        time.sleep(0.3)  #                                          GYORSÍTÁS
        self.robot.aheadCm(distance=-10, speed=500, stop=True)
        self.robot.moveLifter(speed=300, measure=0, wait=True)
        self.robot.aheadCm(distance=4, speed=500, stop=True)
        self.robot.moveGrab(speed=400, measure=Open.closing, wait=True)
        self.robot.aheadCm(distance=-20, speed=400, stop=True)
        self.robot.leftOneWheel(wheel=Side.right, speed=300, angle=-50)
        self.robot.aheadCm(distance=-50, speed=500, stop=True)
