import time
import subprocess
while True:
    subprocess.call(["python", "frame_reader.py"])
    time.sleep(10)