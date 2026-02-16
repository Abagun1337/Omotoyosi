from pydantic import BaseModel, Field, constr, conint
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"


class CourseBase(BaseModel):
    title: constr(min_length=3, max_length=100) = Field(...,
                                                        example="Schrödinger equation", description="The title of the course")
    code: constr(min_length=3, max_length=10) = Field(...,
                                                      example="PHY402", description="The unique course code")


class CourseCreate(CourseBase):
    role: RoleEnum = Field(..., example="Admin",
                           description="Role of the creator(must be Admin)")


class Course(CourseBase):
    id: conint(gt=0) = Field(..., example=1, description="Unique course")


class CourseUpdate(BaseModel):
    title: Optional[constr(min_length=3, max_length=100)] = Field(
        None, example="Law of Newton", description="Updated title")
    code: Optional[constr(min_length=3, max_length=10)] = Field(
        None, example="PHY403", description=" course update")
    role: RoleEnum = Field(..., example="Admin",
                           description="Role must be Admin")
