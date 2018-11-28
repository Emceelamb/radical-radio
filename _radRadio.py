import subprocess
import time
import keyboard

fox_url="http://tunein.streamguys1.com/secure-foxnews?key=197d25655542f4c4e8d9c1eb15b264b81093805bec3ebed5572706526d919fee"
cnn_url="http://tunein.streamguys1.com/cnn?skey=2547892960cb6503cb3adbcaed7ff7a42f7"

while True: 
    # try:
    if keyboard.is_pressed('f'):
        subprocess.Popen(['sudo','mpg123',fox_url])
        time.sleep(1)
        print('fox is playing')
    if keyboard.is_pressed('c'):
        subprocess.Popen(['sudo','mpg123',cnn_url])
        time.sleep(1)
    # except:
    #     break


