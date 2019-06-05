import RPi.GPIO as GPIO
from time import sleep
import ultrasonic as US
import numpy as np

# setup ultrasonics
uL = US.ultrasonic(8,7)
uR = US.ultrasonic(6,5)
uB = US.ultrasonic(27,22)

# initialize variables
max_dist=0
min_dist=100
tot_dist=0

for i in range(20):
    dist = uL.measure()
    max_dist = max(max_dist,dist)
    min_dist = min(min_dist,dist)
    tot_dist += dist

mean_dist = tot_dist/20
print("mean: "+str(mean_dist))
print("range: "+str((max_dist-min_dist)/2))