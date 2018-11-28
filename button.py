import RPi.GPIO as GPIO

import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
while True:
    fox = GPIO.input(18)
    cnn = GPIO.input(15)
    # power light
    GPIO.output(22,GPIO.HIGH) 
    if fox == True:
	# turn blue light off
	GPIO.output(24,GPIO.LOW)
	# turn red light on
	GPIO.output(23,GPIO.HIGH)
        print('fox Button Pressed')
        time.sleep(0.2)
    if cnn == True:
	# turn red light off
	GPIO.output(23,GPIO.LOW)
	# turn blue light ON
	GPIO.output(24,GPIO.HIGH)
	print('cnn play') 
	time.sleep(0.2)

