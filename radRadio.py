import RPi.GPIO as GPIO

import subprocess
import os
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
fox_url="http://tunein.streamguys1.com/cnn?aw_0_1st.playerid=RadioTime&aw_0_1st.skey=1543500464"
cnn_url="http://tunein.streamguys1.com/cnn?key=1543500309"

cnnIsPlaying=False
foxIsPlaying=False

while True: 
    # toggle stations
    fox = GPIO.input(18)
    cnn = GPIO.input(15)
    # power light
    GPIO.output(22,GPIO.HIGH) 
    if fox == True:
        if(cnnIsPlaying==True):
            os.system('sudo killall mpg123')
        # turn blue light off
        GPIO.output(23,GPIO.LOW)
        # turn red light on
        GPIO.output(24,GPIO.HIGH)
        if(foxIsPlaying==False):
	    cnnIsPlaying=False
            foxIsPlaying=True
	    
            subprocess.Popen(['sudo','mpg123',fox_url])
            print('fox is playing')
        time.sleep(1)
    if cnn == True:
        if(foxIsPlaying==True):
            os.system('sudo killall mpg123')
        # turn red light off
        GPIO.output(24,GPIO.LOW)
        # turn blue light ON
        GPIO.output(23,GPIO.HIGH)
        if(cnnIsPlaying==False):
	    foxIsPlaying=False
            cnnIsPlaying=True
            subprocess.Popen(['sudo','mpg123',cnn_url])
            print('cnn play') 
        time.sleep(1)


