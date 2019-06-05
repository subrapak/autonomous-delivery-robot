
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class motor():
    def __init__(self,enable,pin1,pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable = enable
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(enable, GPIO.OUT)
        self.pwm=GPIO.PWM(enable,100)
        self.dir = 2 #means nothing
        
    def rotate(self,dir,speed=25):
        self.dir = dir
        self.pwm.start(0)
        if dir == 1:
            GPIO.output(self.enable,True)
            GPIO.output(self.pin1, True)
            GPIO.output(self.pin2, False)
        elif dir == -1:
            GPIO.output(self.enable,True)
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, True)
        else:
            self.pwm.ChangeDutyCycle(0)
            GPIO.output(self.enable,False)
            
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.enable, True)
##        self.pwm.stop()    
       
def forward(mL,mR,speed=25):
    mL.rotate(1,speed)
    mR.rotate(1,speed)
    return 1,1 #directions for encoder L and R

def backward(mL,mR,speed=25):
    mL.rotate(-1,speed)
    mR.rotate(-1,speed)
    return -1,-1 #directions for encoder L and R
    
def right(mL,mR,speed=25):
    mL.rotate(1,speed)
    mR.rotate(-1,speed)
    return 1,-1

def left(mL,mR,speed=25):
    mL.rotate(-1,speed)
    mR.rotate(1,speed)
    return -1,1
    
def stop(mL,mR):
    mL.rotate(-1,0)
    mR.rotate(-1,0)
    return 0,0
##
##mL = motor(17,4,3)
##mR = motor(18,14,23)
##mR.rotate(1,25)
##sleep(2)
##mR.rotate(1,0)
