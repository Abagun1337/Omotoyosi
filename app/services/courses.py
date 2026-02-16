from app.schemas.course import CourseCreate, Course, CourseUpdate
from app.core.db import Courses
from typing import Optional


class CourseService:
    @staticmethod
    def create_course(course_in: CourseCreate):
        course_id = len(Courses) + 1
        new_course = Course(
            id=course_id,
            **course_in.model_dump()
        )
        Courses[course_id] = new_course
        return new_course

    @staticmethod
    def get_all_courses():
        return list(Courses.values())

    @staticmethod
    def get_course_by_id(course_id: int) -> Course | None:
        return Courses.get(course_id)

    @staticmethod
    def course_update(course_id: int, course_in: CourseUpdate):
        course = Courses.get(course_id)
        if not course:
            return None

        if course_in.title is not None:
            course.title = course_in.title
        if course_in.code is not None:
            course.code = course_in.code

    @staticmethod
    def delete_course_by_id(course_id: int) -> Optional[Course]:
        if course_id not in Courses:
            return None
        deleted_course = Courses.pop(course_id)
        return deleted_course
