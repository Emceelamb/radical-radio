import os
import subprocess
import time

fox_url="http://tunein.streamguys1.com/secure-foxnews?key=197d25655542f4c4e8d9c1eb15b264b81093805bec3ebed5572706526d919fee"

#os.system('sudo mpg123 -q '+fox_url)
#os.popen('sudo mpg123 ' + fox_url + ' &')
subprocess.Popen(['sudo','mpg123',fox_url])
time.sleep(1)
#time.sleep(10)
serial.write('\x03')



