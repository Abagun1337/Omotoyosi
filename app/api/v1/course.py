from fastapi import APIRouter, HTTPException, status, Body
from app.schemas.course import CourseCreate, CourseUpdate
from app.services.courses import CourseService
from app.schemas.course import RoleEnum

course_router = APIRouter(tags=["Course Route"])


@course_router.post("/", status_code=status.HTTP_201_CREATED)
def Create_course(course_in: CourseCreate):
    if course_in.role != RoleEnum.admin:
        raise HTTPException(
            status_code=403, detail="Only admin can create courses")
    new_course = CourseService.create_course(course_in)
    return {"message": "Course created sucessfully", "data": new_course}


@course_router.get("/", status_code=200)
def list_course():
    new_course = CourseService.get_all_courses()
    return {"message": "Course Created Successfully", "data": new_course}


@course_router.get("/{course_id}", status_code=status.HTTP_200_OK)
def get_course(course_id: int):
    course = CourseService.get_course_by_id(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not Found")
    return {"message": "Course retrieved successfully", "data": course}


@course_router.put("/update_course/{course_id}", status_code=status.HTTP_200_OK)
def course_update(course_id: int, course_in: CourseUpdate):
    if course_in.role != RoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied")
    update_course = CourseService.course_update(course_id, course_in)
    return {"message": "Course Updated Successfully", "data": update_course}


@course_router.delete("/{course_id}", status_code=status.HTTP_200_OK)
def delete_course(course_id: int, role: RoleEnum = Body(..., embed=True)):
    if role != RoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access Denied")
    delete_course = CourseService.delete_course_by_id(course_id)
    return {"message": "Course Deleted Sucessfully", "data": delete_course}
