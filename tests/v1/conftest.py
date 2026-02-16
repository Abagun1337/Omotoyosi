import pytest
from app.core.db import Users, Courses, Enrollments
from app.schemas.user import User, EmailStr
from app.schemas.course import Course, RoleEnum


@pytest.fixture(autouse=True)
def setup_test_data():
    Enrollments.clear()

    Users.clear()
    Users[1] = User(
        id=1,
        name="Abagun Omotoyosi",
        email="Abaguntoyosi002@icloud.com",
        role=RoleEnum.student.value  # now "student", lowercase
    )

    Users[2] = User(id=2, name="Ola", email="Ola@gmail.com",
                    role=RoleEnum.admin.value)

    Courses.clear()
    Courses[1] = Course(id=1, title="Newton law", code="401")
    Courses[2] = Course(id=2, title="Schrödinger equation", code="PHY404")
