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

router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

@router.post('/register_missing_person', status_code=status.HTTP_201_CREATED)
async def register_missing_person(payload: schemas.MissingPerson, response: Response, Authorize: AuthJWT = Depends()):
    
    try:
        Authorize.jwt_refresh_token_required()

        user_id = Authorize.get_jwt_subject()
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not refresh access token')
        user = userEntity(User.find_one({'_id': ObjectId(str(user_id))}))
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='The user belonging to this token no logger exist')
        access_token = Authorize.create_access_token(
            subject=str(user["id"]), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))
    except Exception as e:
        error = e.__class__.__name__
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='Please provide refresh token')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)
        #Check if user already exist
    print(user["id"])
    result = MissingPerson.insert_one(payload.dict())
    return {"status": "success"}