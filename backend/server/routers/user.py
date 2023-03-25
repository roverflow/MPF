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
import json
from ..serializers.helpers import users_serializer
import cv2
from io import BytesIO
from PIL import Image

router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

@router.post('/register_missing_person', status_code=status.HTTP_201_CREATED)
async def register_missing_person(name: str, contact: str, fir: str, last_seen: str , file : Annotated[UploadFile, File()]):
    cloudinary.config(
        cloud_name = "demgacv6k",
        api_key = "137451977666999",
        api_secret = "2kIpFYe0d4-ckLuEnBVRrkaPL2o",
        secure = True
    )
    try:
        contents = file.file.read()
        url = upload(contents, folder="missing_persons")
        pil_image = Image.open(BytesIO(contents))
        numpy_array = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGBA2BGR)
        embeddings = get_embeddings([numpy_array])
        my_dict = {
            "name": name,
            "contact_number": contact,
            "fir": fir,
            "last_seen": last_seen,
            "image_url" : url['url'],
            "_id": datetime.now().strftime('%s'),
            "secure_url": url["secure_url"],
            "embeddings": embeddings.tolist()
        }
        MissingPerson.insert_one(my_dict)
        return { "status": "success", "missing_person": my_dict }
    except Exception as e:
        return {"status" : "fail" ,"message": e}
    finally:
        file.file.close()

@router.get('/get_missing_persons')
def get_missing_persons():
    missing_persons =  users_serializer(MissingPerson.find())
    return {"status": "success", "missing_persons": missing_persons}
