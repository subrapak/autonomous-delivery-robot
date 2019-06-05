import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BOARD)

# change for each pin
test_pin = 40

GPIO.setup(test_pin,GPIO.OUT)

print("LED on")
GPIO.output(test_pin,True)
sleep(1)
print("LED off")
GPIO.output(test_pin,False)

print("now testing pwm...")
pwm = GPIO.PWM(test_pin,100)
pwm.start(0)

for i in range(0,100,20):
    pwm.ChangeDutyCycle(i)
    sleep(0.5)
    print("pwm "+str(i))

pwm.stop()
GPIO.output(test_pin,False)

print("test over.")