import time
import subprocess
while True:
    subprocess.call(["python","server/myutils/frame_reader.py"])
    time.sleep(10)