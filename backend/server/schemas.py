from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    email: str
    role: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass 


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class MissingPerson(BaseModel):
    name: str
    image_url: str
    fir_num: int
    contact_number: int

    class Config:
        orm_mode = True