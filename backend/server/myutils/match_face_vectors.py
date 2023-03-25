from server.database import MissingPerson, realtimeFaceVectors,foundPerson
import numpy as np
from numpy import asarray
from scipy.spatial.distance import cosine
from server.database import db
import gridfs
import cv2
from bson.objectid import ObjectId



realTimeFaces = realtimeFaceVectors.find({}, {"embeddings":1,'frame':1,"location":1, "_id":0})
real_time_embedds = []
real_time_frames = []
real_time_location = []


missingFaces = MissingPerson.find({},{"embeddings":1, "_id":1})
missing_embedds = []
missing_ids = []
    
for i in missingFaces:
    if i == {}:
         continue
    em  = np.array(i["embeddings"])
    id  = np.array(i["_id"])
    missing_ids.append(id)
    missing_embedds.append(em)


for i in realTimeFaces:
    if i == {}:
        continue
    em  = np.array(i["embeddings"])
    frame = i["frame"]
    location = i['location']
    # fs = gridfs.GridFS(db)
    # file = fs.get(frame)
    # image_bytes = file.read()
    # image = cv2.imdecode(np.frombuffer(image_bytes,np.uint8), cv2.IMREAD_COLOR)
    real_time_frames.append(frame)
    real_time_location.append(location)
    real_time_embedds.append(em)



def  check_similarity_with_database(face_vector, faceid):
      score =  is_match(face_vector, faceid)
      
	
        

def is_match(real_time_embedds, missing_embedds, thresh=0.5):
    score = cosine(real_time_embedds, missing_embedds)
    score = (1-score)*100
    return score

def find_match(real_time_embedds,missing_embedds):
     for index, i in enumerate(real_time_embedds):
        
        for ind, j in enumerate(missing_embedds):
            
            score = is_match(i[0], j[0])
            if score >= 50.0:
                person = foundPerson.find_one({"_id": str(missing_ids[ind])})
               
                if person != None  :
                        if 'found' in person.keys():
                            person['found'].append({'score':score,'real_time_location':real_time_location[index],'real_time_frames':real_time_frames[index]})
                        else:
                            person['found'] = [{'score':score,'real_time_location':real_time_location[index],'real_time_frames':real_time_frames[index]}]
                        result = foundPerson.update_one({"_id": str(missing_ids[ind])}, {"$set":person})                  
                        print(result.raw_result)
                else :
                        print("Hi")
                        person = MissingPerson.find({"_id": str(missing_ids[ind])})
                        for a in person:
                            a['found'] = [{'score':score,'real_time_location':real_time_location[index],'real_time_frames':real_time_frames[index]}]
                            foundPerson.insert_one(a)
total_num = len(real_time_embedds)


if total_num < 10:
    find_match(real_time_embedds[0:total_num],missing_embedds)
else:
    d =int(len(real_time_embedds) / 10)
    r = int(len(real_time_embedds) % 10)
    start= 0
    for i in range(0, d):
         find_match(real_time_embedds[start: start+10],missing_embedds)
         start= start+10
    find_match(real_time_embedds[-r:],missing_embedds)
     