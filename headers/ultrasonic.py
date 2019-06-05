import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setmode(GPIO.BCM) #referring to pins by Boardcom SOC channel (i.e. not physical pin numbers)
GPIO.setwarnings(False)

class ultrasonic():
    def __init__(self,trig,echo):
        self.trig = trig
        self.echo = echo
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        
    def get_dist(self):
        GPIO.output(self.trig,False)
        time.sleep(0.00005)
    
##      sends out 10us signal     
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo)==0: #at first the ECHO pin in low
            pulse_start=time.time() #clock when the ECHO pin is high (pulse sent out)

        while GPIO.input(self.echo)==1:
            pulse_end=time.time() #clock when the ECHO pin drops low again (pulse recieved)

        pulse_duration = pulse_end - pulse_start #overall pulse duration

        distance = pulse_duration*17150
        distance=round(distance,2) #round for neatness
    
        return distance
    
    def measure(self):
        distance = []
        for i in range(20):
            distance.append(ultrasonic.get_dist(self))
        
        mean_dist = round(np.mean(distance),1)
        return mean_dist


##ultra = ultrasonic(5,16)
##dist = ultra.measure()
##print(dist)
##GPIO.cleanup()