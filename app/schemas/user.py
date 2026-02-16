from pydantic import BaseModel, EmailStr, Field, constr, conint
from typing import Literal


class UserBase(BaseModel):
    name: constr(min_length=3, max_length=50) = Field(...,
                                                      example="Abagun Omotoyosi", description="Fullname of the user ")
    email: EmailStr = Field(..., example="Abaguntoyosi002@icloud.com",
                            description="Valid email address")
    role: Literal['student',
                  'admin', 'teacher'] = Field(..., example="student", description="Role of the user")


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: conint(gt=0) = Field(..., example="1,", description="Unique user ID")
