
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import motorcontrol as MC
from RPLCD import CharLCD
import ultrasonic as US
import encoders as EC
from functools import partial
import numpy as np

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #referring to pins by Boardcom SOC channel (i.e. not physical pin numbers)

# setup LCD
lcd = CharLCD(numbering_mode = GPIO.BCM, pin_rs=26, pin_e=19, pins_data=[21,20,16,12], cols=16, rows=2)
lcd.clear()

# setup ultrasonics
uL = US.ultrasonic(trig=8,echo=7) 
uR = US.ultrasonic(trig=6,echo=5)
uB = US.ultrasonic(trig=27,echo=22)

# setup motors
mL = MC.motor(23,18,14) # enable, pin1, pin2
mR = MC.motor(4,17,3) # enable, pin1, pin2

# setup encoders
eL = EC.encoder(24,25) #outA, out B
eR = EC.encoder(9,11)
radius = 5   #in cm
distanceL = 0	# initialize distance travelled by left wheel
distanceR = 0	# initialize distance travelled by right wheel

#setup pulsecounts
L_unitrev = 600	# left encoder pulse count
R_unitrev = 1200 # right encoder pulse count

#setup camera
camera = PiCamera()
camera.resolution = (720,480)

"""========== Encoder Interrupts =========="""

def pulse_mainL(eC,channel):
    global distanceL
    
    eC.pulsecount += eC.dir
    distanceL = (int((eC.pulsecount*radius*6.283185)/L_unitrev))
    #lcd.clear()
    if eC.pulsecount%50 == 0:
        lcd.cursor_pos = (0,0)
        lcd.write_string('L %02d cm' %distanceL)
#        print("L"+str(eC.pulsecount))
    
    
def pulse_mainR(eC,channel):
    global distanceR
  
    eC.pulsecount += eC.dir
    distanceR = (int((eC.pulsecount*radius*6.283185)/R_unitrev))
    #lcd.clear()
    if eC.pulsecount%50 == 0:
        lcd.cursor_pos = (1,0)
        lcd.write_string('R %02d cm' %distanceR)
#        print("R"+str(eC.pulsecount))
    
def ultra_check(uS):
    tot_dist=0
    max_dist=0
    min_dist=100
    
    for i in range(5):
        dist1 = uS.measure()
        max_dist = max(max_dist,dist)
        min_dist = min(min_dist,dist)
        tot_dist += dist
    mean_dist = tot_dist/20
    return mean_dist
    
    
    
mycall_L = partial(pulse_mainL,eL)
mycall_R = partial(pulse_mainR,eR)

GPIO.add_event_detect(eL.pinA,GPIO.RISING,callback=mycall_L)
GPIO.add_event_detect(eR.pinA,GPIO.RISING,callback=mycall_R)


""" ==========Begin Routine========== """

#camera.start_preview()
camera.start_recording('/home/pi/Videos/latest.mp4')

# moving forwards
for i in range(10):
    distL = ultra_check(uL)
    distR = ultra_check(uR)
    
    if min(distL,distR) > 5:
        eL.dir,eR.dir = MC.forward(mL,mR,25)
        sleep(3)
    else:
        lcd.clear()
        lcd.cursor_pos = (0,0)
        lcd.write("L %02d" %distL)
        lcd.cursor_pos = (1,0)
        lcd.write("R %02d" %distL)

#moving backwards
for i in range(10):
    distB = ultra_check(uB)
    
    if min(distL,distR) > 5:
        eL.dir,eR.dir = MC.backward(mL,mR,25)
        sleep(3)
    else:
        lcd.clear()
        lcd.cursor_pos = (0,0)
        lcd.write("B %02d" %distB)
        lcd.cursor_pos = (1,0)

MC.stop(mL,mR)

camera.stop_recording()

"""========== End Routine =========="""
