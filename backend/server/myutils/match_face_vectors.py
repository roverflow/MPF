from server.database import MissingPerson, realtimeFaceVectors
import numpy as np
from numpy import asarray
from scipy.spatial.distance import cosine
from server.database import db
import gridfs
import cv2
import base64

realTimeFaces = realtimeFaceVectors.find({}, {"embeddings":1,'frame':1,"location":1, "_id":0})
real_time_embedds = []
real_time_frames = []
real_time_location = []


missingFaces = MissingPerson.find()
missing_embedds = []


for i in realTimeFaces:
    if i == {}:
        continue
    em  = np.array(i["embeddings"])
    frame = i["frame"]
    location = i['location']
    fs = gridfs.GridFS(db)
    file = fs.get(frame)
    image_bytes = file.read()
    image = cv2.imdecode(np.frombuffer(image_bytes,np.uint8), cv2.IMREAD_COLOR)
    real_time_frames.append(image)
    real_time_location.append(location)
    real_time_embedds.append(em)
print(missingFaces)
for i in missingFaces:
    print(i)
    if i == {}:
         continue
    em  = np.array(i["embeddings"])
    missing_embedds.append(em)

d = len(real_time_embedds) / 5
r = len(real_time_embedds) % 5

def  check_similarity_with_database(face_vector, faceid):
      score =  is_match(face_vector, faceid)
      
	
        

def is_match(real_time_embedds, missing_embedds, thresh=0.5):
    score = cosine(real_time_embedds, missing_embedds)
    score = (1-score)*100
    return score

print(len(real_time_embedds), len(missing_embedds))
for index, i in enumerate(real_time_embedds):
     for j in missing_embedds:
          score = is_match(i[0], j[0])
          if score >= 50.0:
               print(score,real_time_location[index] )
