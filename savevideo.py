import os
import subprocess
import time
for i in range(1,144):
	time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
	cmd =  "raspivid -t 600000 -w 320 -h 240 -fps 20 -o "+time_stamp+".h264"
	subprocess.call(cmd,shell=True)
	time.sleep(1)

