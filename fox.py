import os
import subprocess
import time

fox_url="http://tunein.streamguys1.com/secure-foxnews?key=30c6a0f4051091d05642a8178d21f17151b61e9cb6503cb3adbcaed7ff7a42f7"

#os.system('sudo mpg123 -q '+fox_url)
#os.popen('sudo mpg123 ' + fox_url + ' &')
subprocess.Popen(['sudo','mpg123',fox_url])
time.sleep(1)
#time.sleep(10)
serial.write('\x03')



