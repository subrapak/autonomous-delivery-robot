from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin1, GPIO.OUT, initial=0)


lcd = CharLCD(numbering_mode = GPIO.BCM, pin_rs=26, pin_e=19, pins_data=[21,20,16,12], cols=16, rows=2)
lcd.cursor_pos = (1,0)
lcd.write_string(str("wys"))
time.sleep(2)
#lcd.clear()
#lcd.cursor_mode = CursorMode.blink, .line, .hide
#\n newline \r reset to line start
