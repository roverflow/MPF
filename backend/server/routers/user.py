from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from server.serializers.userSerializers import userResponseEntity
from fastapi import APIRouter, Response, status, Depends, HTTPException
from server.serializers.userSerializers import userEntity, userResponseEntity
from datetime import datetime, timedelta
from server.oauth2 import AuthJWT
from server.database import User, MissingPerson
from .. import schemas, oauth2
from ..config import settings
from fastapi import File, UploadFile
from ..oauth2 import require_user
from ..myutils.face_vectors import get_embeddings
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
from typing import Annotated
import numpy as np


router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

@router.post('/register_missing_person', status_code=status.HTTP_201_CREATED)
async def register_missing_person(name: str, contact: str, fir: str, last_seen: str , file : Annotated[UploadFile, File()], Authorize: AuthJWT = Depends()):
    try:
        require_user(Authorize)
    except:
        raise HTTPException(status_code=401, detail="You are not logged in")
    print("here")
    cloudinary.config(
        cloud_name = "demgacv6k",
        api_key = "137451977666999",
        api_secret = "2kIpFYe0d4-ckLuEnBVRrkaPL2o",
        secure = True
    )
    try:
        contents = file.file.read()
        url = upload(contents, folder="missing_persons")
        # embeddings = get_embeddings([np.frombuffer(contents, dtype=np.uint8)])
        # print(embeddings)

        my_dict = {
            "name": name,
            "contact": contact,
            "fir": fir,
            "last_seen": last_seen,
            "image_url" : url['url'],
            "_id": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "secure_url": url["secure_url"],
        }
        MissingPerson.insert_one(my_dict)
        return { "status": "success", "missing_person": my_dict }
    except Exception as e:
        return {"status" : "fail" ,"message": e}
    # finally:
        # file.file.close()

