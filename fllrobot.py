from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time, sys, os
from enums import *

class FllRobot:
    def __init__(self, setAccelertion = True):
        self.ready = False
        self.ev3 = EV3Brick()
        try:
            self.rightMotor = Motor(Port.C, Direction.CLOCKWISE)
        except:
            self.startError('Jobb (C) motor')
            return

        try:
            self.leftMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        except:
            self.startError('Bal (B) motor')
            return
        
        try:
            self.liftingMotor = Motor(Port.D, Direction.CLOCKWISE)
        except:
            self.startError('Emelo (D) motor')
            return

        try:
            self.grabMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        except:
            self.startError('Megfogo (A) motor')
            return

        if setAccelertion:
            self.rightMotor.control.limits(speed=1000, acceleration=1500, actuation=100)
            self.leftMotor.control.limits(speed=1000, acceleration=1500, actuation=100)

        try:
            self.rightSensor = ColorSensor(Port.S3)
        except:
            self.startError('Jobb LE (3) szenzor')
            return

        try: 
            self.leftSensor = ColorSensor(Port.S2)
        except:
            self.startError('Bal LE (2) szenzor')
            return
        
        try:
            self.gyroSensor = GyroSensor(Port.S1)
            self.gyroSensor.reset_angle(0)
            # r,g,b,w = self.balOldalSzenzor.rgbw()
        except:
            self.startError('GYRO (1) szenzor')
            return
        
        self.stopWatch = StopWatch()
        self.startLog()        
        self.ready = True
    
    def startError(self, errorText):
        self.ev3.screen.print(errorText)
        self.ev3.speaker.beep(duration=500)
        while (not Button.CENTER in self.ev3.buttons.pressed()):
            pass

    def starting(self):  #gomb lenyomásra indul a robot                      
        self.ev3.speaker.beep()
        time.sleep(0.2)
        self.ev3.speaker.beep()
        self.ev3.screen.print("AMD READY!")
        self.ev3.screen.print(self.ev3.battery.voltage() / 1000, "V")
        while (not Button.CENTER in self.ev3.buttons.pressed()):
            pass
            
    def stop(self, mode = Stop.HOLD):
        self.leftMotor.stop(mode)
        self.rightMotor.stop(mode)

    def aheadCm(self, distance, speed, stop:bool):
        # Egy fordulat 18.5 centi
        angle = 20*distance
        if stop:
            self.leftMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=False)
            self.rightMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=True)
            # print(self.balMotor.angle(), self.jobbMotor.angle())
        else:    
            start_angle = self.leftMotor.angle() 
            if angle > 0: 
                self.leftMotor.run(speed=speed)
                self.rightMotor.run(speed=speed)
                while self.leftMotor.angle() < start_angle + angle:
                    pass
            else:
                self.leftMotor.run(speed=-speed)
                self.rightMotor.run(speed=-speed)
                while self.leftMotor.angle() > start_angle + angle:
                    pass

    def rightTwoWheel(self, speed, angle=90):
        angle = 3.35*angle
        self.leftMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=False)
        self.rightMotor.run_angle(speed=-speed, rotation_angle=angle, then=Stop.HOLD, wait=True)
    
    def leftTwoWheel(self, speed, angle=90):
        angle = 3.35*angle
        # print(angle)
        self.leftMotor.run_angle(speed=-speed, rotation_angle=angle, then=Stop.HOLD, wait=False)
        self.rightMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=True)

    def leftOneWheel(self, wheel, speed, angle=90):
        angle = 6.6666*angle
        if wheel == Side.left:
            angle += (abs(self.rightMotor.speed()) / 50)
            self.rightMotor.stop(Stop.HOLD)
            self.leftMotor.run_angle(speed=-speed, rotation_angle=angle, then=Stop.HOLD, wait=True)
        else:
            angle += (abs(self.leftMotor.speed()) / 50)
            self.leftMotor.stop(Stop.HOLD)
            self.rightMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=True)

    def rightOneWheel(self, wheel, speed, angle=90):
        angle = 6.6666*angle
        if wheel == Side.left:
            angle += (abs(self.rightMotor.speed()) / 50)
            self.rightMotor.stop(Stop.HOLD)
            self.leftMotor.run_angle(speed=speed, rotation_angle=angle, then=Stop.HOLD, wait=True)
        else:
            angle += (abs(self.leftMotor.speed()) / 50)
            self.leftMotor.stop(Stop.HOLD)
            self.rightMotor.run_angle(speed=-speed, rotation_angle=angle, then=Stop.HOLD, wait=True)

    def goUntilBlack(self, speed, szenzor:ColorSensor, stop = True):
        self.leftMotor.run(speed=speed)
        self.rightMotor.run(speed=speed)
        red, green, blue = (255,255,255)
        while red + green + blue > 50:
            red, green, blue = szenzor.rgb()
        if stop:
            self.leftMotor.stop(Stop.HOLD)
            self.rightMotor.stop(Stop.HOLD)

    def goUntilWhite(self, speed, szenzor:ColorSensor, stop = True):
        self.leftMotor.run(speed=speed)
        self.rightMotor.run(speed=speed)
        red, green, blue = (0,0,0)
        while red + green + blue < 165:
            red, green, blue = szenzor.rgb()
            print(red + green + blue)
        if stop:
            self.leftMotor.stop(Stop.HOLD)
            self.rightMotor.stop(Stop.HOLD)

    def alignOnWhite(self, speed):
        self.leftMotor.run(speed=speed)
        self.rightMotor.run(speed=speed)
        time.sleep(0.2)
        jred, jgreen, jblue = (0,0,0)
        bred, bgreen, bblue = (0,0,0)
        while abs(self.rightMotor.speed()) > 0 or abs(self.leftMotor.speed()) > 0:
            jred, jgreen, jblue = self.rightSensor.rgb()
            bred, bgreen, bblue = self.leftSensor.rgb()
            if jred + jgreen + jblue > 165:
                self.rightMotor.stop(Stop.HOLD)
            if bred + bgreen + bblue > 165:
                self.leftMotor.stop(Stop.HOLD)

    def alignOnBlack(self, speed):
        self.leftMotor.run(speed=speed)
        self.rightMotor.run(speed=speed)
        time.sleep(0.2)
        jred, jgreen, jblue = (255,255,255)
        bred, bgreen, bblue = (255,255,255)
        while abs(self.rightMotor.speed()) > 0 or abs(self.leftMotor.speed()) > 0:
            jred, jgreen, jblue = self.rightSensor.rgb()
            bred, bgreen, bblue = self.leftSensor.rgb()
            if jred + jgreen + jblue < 50:
                self.rightMotor.stop(Stop.HOLD)
            if bred + bgreen + bblue < 50:
                self.leftMotor.stop(Stop.HOLD)
        # time.sleep(0.2)

    def moveGrab(self, speed, measure, wait=True):
        print(self.grabMotor.angle())
        self.grabMotor.stop()
        self.grabMotor.run_target(speed=speed, target_angle=measure, then=Stop.HOLD, wait=wait)

    def moveLifter(self, speed, measure, wait=True):
        self.liftingMotor.run_target(speed = speed, target_angle = measure, wait = wait)
    
    def alignOnWall(self, seconds, speed=-300):
        self.leftMotor.run_time(speed=speed, time=seconds*1000, then=Stop.HOLD, wait=False)
        self.rightMotor.run_time(speed=speed, time=seconds*1000, then=Stop.HOLD, wait=True)
        while self.leftMotor.speed() != 0 and self.rightMotor.speed() != 0:
            pass
        time.sleep(0.2)
        
    def startLog(self):
        try:
            os.mkdir('./log')
        except:
            pass
        
        logFiles = os.listdir('./log')
        i = 1
        if (len(logFiles) > 0):
            logFiles.sort()
            i = int(logFiles[-1][4:7]) + 1

        self.logFileName = './log/log_{0:03d}.txt'.format(i)
        self.displayedEvents = []
        with open(self.logFileName, 'w+') as f:
            pass
        print('Log file created: {0}'.format(self.logFileName))

    def log(self, text, logtext = ''):
        with open(self.logFileName, 'a') as f:
            if logtext == '':
                f.write('{0:06d} - {1}\n'.format(self.stopWatch.time(), text))
                print('Log ({0}): {1}'.format(self.stopWatch.time(), text))
            else:
                f.write('{0:06d} - {1}\n'.format(self.stopWatch.time(), logtext))
                print('Log ({0}): {1}'.format(self.stopWatch.time(), logtext))

        if len(self.displayedEvents) == 4:
            self.displayedEvents.pop(0)

        self.displayedEvents.append(text)
        self.ev3.screen.clear()
        for i, event in enumerate(self.displayedEvents):
            self.ev3.screen.draw_text(0, i * 30, event)

    def forwardWithGyro(self, speed, distance, stop = True):
        self.gyroSensor.reset_angle(0)
        time.sleep(0.2)
        self.leftMotor.reset_angle(0)
        self.rightMotor.reset_angle(0)
        self.leftMotor.run(speed=speed)
        self.rightMotor.run(speed=speed)
        time.sleep(0.2)
        while True:
            gyroValue = self.gyroSensor.angle()
            leftStopped, rightStopped = False, False
            if gyroValue > 0:
                self.leftMotor.run(speed-100)
                self.rightMotor.run(speed)
            elif gyroValue < 0:
                self.rightMotor.run(speed-100)
                self.leftMotor.run(speed)
            else:
                self.leftMotor.run(speed=speed) if not leftStopped else None
                self.rightMotor.run(speed=speed) if not rightStopped else None
            if self.leftMotor.angle() > distance * Conversion.cmToRotation and stop:
                self.leftMotor.stop()
                leftStopped = True
            if self.rightMotor.angle() > distance * Conversion.cmToRotation and stop:
                self.rightMotor.stop()
                rightStopped = True
            if (self.rightMotor.speed() == 0 or ( not stop and self.rightMotor.angle() > distance * Conversion.cmToRotation)) and (self.leftMotor.speed() == 0 or ( not stop and self.leftMotor.angle() > distance * Conversion.cmToRotation)):
                break
        self.rightMotor.stop() if stop else None
        self.leftMotor.stop() if stop else None

    def oneWheelLeftWithGyro(self, speed, wheel, rotation = 90):
        self.gyroSensor.reset_angle(0)
        time.sleep(0.2)
        rotation *= -1
        if wheel == Side.left:
            self.rightMotor.stop() if self.rightMotor.speed() > 0 else None
            self.leftMotor.run(-speed)
            time.sleep(0.2)
            while True:
                gyrovalue = self.gyroSensor.angle()
                if gyrovalue <= rotation:
                    self.leftMotor.stop()
                    break
        else:
            self.leftMotor.stop() if self.leftMotor.speed() > 0 else None
            self.rightMotor.run(speed)
            time.sleep(0.2)
            while True:
                gyrovalue = self.gyroSensor.angle()
                if gyrovalue <= rotation:
                    self.rightMotor.stop()
                    break
    
    def oneWheelRightWithGyro(self, speed, wheel, rotation = 90):
        self.gyroSensor.reset_angle(0)
        time.sleep(0.2)
        if wheel == Side.left:
            self.leftMotor.run(speed)
            time.sleep(0.2)
            while True:
                gyrovalue = self.gyroSensor.angle()
                if gyrovalue >= rotation:
                    self.leftMotor.stop()
                    break
        else:
            self.rightMotor.run(-speed)
            time.sleep(0.2)
            while True:
                gyrovalue = self.gyroSensor.angle()
                if gyrovalue >= rotation:
                    self.rightMotor.stop()
                    break

    def twoWheelRightWithGyro(self, speed, rotation = 90):
        self.gyroSensor.reset_angle(0)
        time.sleep(0.2)
        self.rightMotor.run(-speed)
        self.leftMotor.run(speed)
        while True:
            if self.gyroSensor.angle() + (speed / 100) > rotation:
                self.rightMotor.stop()
                self.leftMotor.stop()
                break

    def twoWheelLeftWithGyro(self, speed, rotation = 90):
        self.gyroSensor.reset_angle(0)
        time.sleep(0.2)
        self.rightMotor.run(-speed)
        self.leftMotor.run(speed)
        while True:
            if self.gyroSensor.angle() - (speed / 100) < rotation:
                self.rightMotor.stop()
                self.leftMotor.stop()
                break