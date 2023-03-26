import time
import subprocess
while True:
    subprocess.call(["python", "frame_reader.py"])
    subprocess.call(["python", "match_face_vectors.py"])
    time.sleep(10)