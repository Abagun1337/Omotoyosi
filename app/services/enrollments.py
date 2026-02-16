from app.schemas.enrollment import EnrollmentCreate, Enrollment
from app.core.db import Users, Courses, Enrollments
from fastapi import HTTPException, status
from app.schemas.course import RoleEnum


class EnrollmentService:
    @staticmethod
    def enroll_student(enrollment_in: EnrollmentCreate):
        user_id = enrollment_in.user_id
        course_id = enrollment_in.course_id

        if user_id not in Users:
            raise HTTPException(status_code=404, detail="User not found")
        user = Users[user_id]

        if user.role.lower() != "student":
            raise HTTPException(
                status_code=403, detail="Only students can enroll")

        if course_id not in Courses:
            raise HTTPException(status_code=404, detail="Course not found")

        if any(e.user_id == user_id and e.course_id == course_id for e in Enrollments.values()):
            raise HTTPException(
                status_code=400, detail="Student already enrolled")

        enrollment_id = len(Enrollments) + 1
        new_enrollment = Enrollment(
            id=enrollment_id, user_id=user_id, course_id=course_id)
        Enrollments[enrollment_id] = new_enrollment
        return new_enrollment

    @staticmethod
    def deregister_student(user_id: int, course_id: int, role: RoleEnum):
        if role != RoleEnum.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
        if user_id not in Users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
        if course_id not in Courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="course not found")

        enrollment_to_remove = None
        for e_id, e in Enrollments.items():
            if e.user_id == user_id and e.course_id == course_id:
                enrollment_to_remove = e_id
                break
        if enrollment_to_remove is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
        removed_enrollment = Enrollments.pop(enrollment_to_remove)
        return {"message": "Student deregistered successfully", "data": removed_enrollment}

    @staticmethod
    def get_all_enrollment():
        return list(Enrollments.values())

    @staticmethod
    def get_enrollment(enrollment_in: int):
        if enrollment_in not in Enrollments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found")
