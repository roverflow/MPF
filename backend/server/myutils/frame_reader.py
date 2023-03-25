
from vidgear.gears import CamGear
import cv2
import time 
from face_vectors import get_embeddings
from datetime import datetime 
from server.database import realtimeFaceVectors, streamLinks
from multiprocessing import Process

def read_frame(path, location):
    print("Process with stream link :", path , "Started")
    embeddings = []
    while True:
        stream = CamGear(source=path, stream_mode = True, logging=True).start()
        frame = stream.read()
        print(frame.shape)
        if frame is None:
            break
       
        embeddings = get_embeddings([frame])
        print(embeddings)
        if embeddings != [[]]:
            embeddings = embeddings.tolist()
            my_dict = {
                "_id": str(datetime.now().strftime('%s'))+"location",
                "embeddings": embeddings,
                'location':location
            }
            realtimeFaceVectors.insert_one(my_dict)
            print( { "status": "success", "missing_person": my_dict } )
        time.sleep(5)
    stream.stop()


if __name__ == '__main__':
    streamlinks = streamLinks.find({})
    print("Stream link is ", streamLinks)
    for data in streamlinks:
        p = Process(target=read_frame, args=(data['stream'], data['location']))
        p.start()
    

