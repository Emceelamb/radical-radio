import RPi.GPIO as GPIO

import subprocess
import time
import keyboard

# set gpio pin mode
GPIO.setmode(GPIO.BCM)
# set button pins
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# set led pins
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
# set urls
fox_url="http://tunein.streamguys1.com/secure-foxnews?key=197d25655542f4c4e8d9c1eb15b264b81093805bec3ebed5572706526d919fee"
cnn_url="http://tunein.streamguys1.com/cnn?skey=2547892960cb6503cb3adbcaed7ff7a42f7"

while True: 
    # toggle stations
    fox = GPIO.input(18)
    cnn = GPIO.input(15)
    # power light
    GPIO.output(22,GPIO.HIGH) 
    if fox == True:
        # turn blue light off
        GPIO.output(24,GPIO.LOW)
        # turn red light on
        GPIO.output(23,GPIO.HIGH)
        subprocess.Popen(['sudo','mpg123',fox_url])
        print('fox is playing')
        time.sleep(1)
    if cnn == True:
        # turn red light off
        GPIO.output(23,GPIO.LOW)
        # turn blue light ON
        print('cnn play') 
        subprocess.Popen(['sudo','mpg123',cnn_url])
        GPIO.output(24,GPIO.HIGH)
        time.sleep(1)


