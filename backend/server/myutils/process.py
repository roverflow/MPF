import time
import subprocess
while True:
    subprocess.call(["python", "server/myutils/match_face_vectors.py"])
    time.sleep(10)