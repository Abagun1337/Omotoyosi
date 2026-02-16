from app.main import app
from fastapi.testclient import TestClient
from app.schemas.enrollment import RoleEnum
from app.core.db import Users, Courses


client = TestClient(app)

Users[1] = {"id": 1, "role": "student", "name": "Alice"}

Courses[1] = {"id": 1, "name": "PHY404"}


def test_create_enrollment():
    res_create = client.post("/enrollments/", json={
        "user_id": 1,
        "course_id": 1,
        "role": RoleEnum.student.value
    })
    assert res_create.status_code == 201


def test_admin_force_deregister():
    res_create = client.post("/enrollments/", json={
        "user_id": 1,
        "course_id": 1,
        "role": "student"
    })
    assert res_create.status_code == 201

    res = client.delete("/enrollments/deregister", params={
        "user_id": 1,
        "course_id": 1,
        "role": "admin"
    })
    assert res.status_code == 200
    assert res.json()["message"] == "Student deregistered successfully"


def admin_list_enrollments():
    res_create = client.post("/enrollments/", json={
        "user_id": 1,
        "course_id": 1,
        "role": RoleEnum.student.value
    })

    res_create_2 = client.post("/enrollments/", json={
        "user_id": 2,
        "course_id": 1,
        "role": RoleEnum.student.value
    })
    assert res_create.status_code == 201
    assert res_create_2.status_code == 201
    res_list = client.get(
        "/enrollments", params={"role": RoleEnum.admin.value})
    assert len(res_list.json()["data"]) == 2
