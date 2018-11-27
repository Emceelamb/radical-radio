import subprocess
import time
import keyboard

fox_url="http://tunein.streamguys1.com/secure-foxnews?key=30c6a0f4051091d05642a8178d21f17151b61e9cb6503cb3adbcaed7ff7a42f7"
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


