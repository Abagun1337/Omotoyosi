from pydantic import BaseModel, Field, conint, constr
from enum import Enum


class RoleEnum(str, Enum):
    student = "student"
    admin = "admin"


class EnrollmentBase(BaseModel):
    user_id: conint(gt=0) = Field(..., example=1,
                                  description="ID of the student")
    course_id: conint(gt=0) = Field(..., example=404,
                                    description="ID of the Course")


class EnrollmentCreate(EnrollmentBase):
    role: constr(min_length=3, max_length=20) = Field(...,
                                                      example="Student", description="Role of the user")


class Enrollment(EnrollmentBase):
    id: conint(gt=0) = Field(..., example=1,
                             description="Unique enrollment_ID")
