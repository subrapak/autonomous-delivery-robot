import RPi.GPIO as GPIO
from time import sleep
import motorcontrol as MC
import encoders as EC
from functools import partial

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #referring to pins by Boardcom SOC channel (i.e. not physical pin numbers)

# setup motors
mL = MC.motor(23,18,14)
mR = MC.motor(4,17,3)

# setup encoders
eL = EC.encoder(24,25)
eL.dir = 1
eR = EC.encoder(9,11)
eR.dir = 1

test = "R"

# interrupt function for left encoder
def pulse_countL(eC,channel):
    global distanceL
    eC.pulsecount += eC.dir
    
# interrupt function for right encoder    
def pulse_countR(eC,channel):
    global distanceR
    eC.pulsecount += eC.dir
        
mycall_L = partial(pulse_countL,eL)
mycall_R = partial(pulse_countR,eR)

GPIO.add_event_detect(eL.pinA,GPIO.RISING,callback=mycall_L)
GPIO.add_event_detect(eR.pinA,GPIO.RISING,callback=mycall_R)

if (test == "L"):
    mL.rotate(1,speed=25)
    sleep(3.55)  # change this number to the time it takes for 1 revolution
    mL.rotate(1,speed=0)
    print("L_unitrev: "+str(eL.pulsecount))
elif (test == "R"):
    mR.rotate(1,speed=25)
    sleep(2.3)  # change this number to the time it takes for 1 revolution
    mR.rotate(1,speed=0)
    print("R_unitrev: "+str(eR.pulsecount))
else:
    print("Set test to L or R")


""" Encoder Accuracy Test
eL.dir,eR.dir = MC.forward(mL,mR,25)
sleep(30)
eL.dir,eR.dir = MC.backward(mL,mR,25)
sleep(30)
MC.stop(mL,mR)

print('L %02d cm' %distanceL)
print('R %02d cm' %distanceR)
print('%02d cm mean' %np.mean([distanceL,distanceR])) 
"""

