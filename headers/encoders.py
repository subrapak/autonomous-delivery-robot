

import RPi.GPIO as GPIO
from time import sleep
import numpy as np
GPIO.setwarnings(False)


class encoder():
    
    def __init__(self,pinA,pinB):
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(pinA, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(pinB, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
        self.pulsecount = 0   
        self.dir = 0
        
    def get_state(self):    
        if GPIO.input(self.pinA) == 0:
            self.state = GPIO.input(self.pinB)+1
        elif GPIO.input(self.pinA) == 1:
            self.state = 4-GPIO.input(self.pinB)     
        return self.state
    
    def pulse_count(self,channel):
        self.pulsecount += 1
        return self.pulsecount
#i = 0

##    global i
##    i+=1
##    print(i)
       
#GPIO.add_event_detect(self.pinA,GPIO.RISING,callback = pulse_interrupt)
           
        
        



