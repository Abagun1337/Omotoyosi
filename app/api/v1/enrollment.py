from fastapi import APIRouter, HTTPException, status, Body, Path, Query
from app.schemas.enrollment import EnrollmentCreate
from app.services.enrollments import EnrollmentService
from app.schemas.course import RoleEnum


enrollment_router = APIRouter(tags=["Enrollment Route"])


@enrollment_router.post("/", status_code=status.HTTP_201_CREATED)
def enroll_student(enrollment_in: EnrollmentCreate):
    if enrollment_in.role != RoleEnum.student:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only a Student can enroll"
        )

    new_enrollment = EnrollmentService.enroll_student(enrollment_in)
    return {"message": "Student enrolled", "data": new_enrollment}


@enrollment_router.get("/{enrollment_id}", status_code=status.HTTP_200_OK)
def get_enrollment(enrollment_id: int = Path(..., description="ID of the enrollment")):
    enrollment = EnrollmentService.get_enrollment(enrollment_id)
    return {"message": "Enrollment retrieved successfully", "data": enrollment}


@enrollment_router.get("/", status_code=status.HTTP_200_OK)
def list_enrollment(role: RoleEnum = Query(..., description="Role for request")):
    if role != RoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin can list enrollment"
        )

    enrollments = EnrollmentService.get_all_enrollment()
    return {"message": "Enrollments retrieved successfully", "data": enrollments}


@enrollment_router.delete("/deregister", status_code=status.HTTP_200_OK)
def deregister_student(user_id: int, course_id: int, role: RoleEnum = Query()):
    if role != RoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin can deregister students"
        )

    result = EnrollmentService.deregister_student(
        course_id=course_id, user_id=user_id, role=role)
    return result
