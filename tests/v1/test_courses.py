from app.main import app
from fastapi.testclient import TestClient
from app.schemas.course import RoleEnum

client = TestClient(app)


def test_create_course():
    res = client.post("/courses/", json={
        "title": "Schrödinger equation",
        "code": "PHY404",
        "role": RoleEnum.admin.value
    })
    assert res.status_code == 201


def test_student_cannot_create_courses():
    res = client.post("/courses/", json={
        "title": "Schrödinger equation",
        "code": "PHY404",
        "role": RoleEnum.student.value
    })
    assert res.status_code == 403


def test_course_code_unique():
    res_create = client.post("/courses/", json={
        "title": "Python",
        "code": "PHY401",
        "role": RoleEnum.admin.value
    })
    assert res_create.status_code == 201


def test_get_course_by_id():
    res_create = client.post("/courses/", json={
        "title": "Schrödinger equation",
        "code": "PHY404",
        "role": RoleEnum.admin.value
    })
    assert res_create.status_code == 201
    course_id = res_create.json()["data"]["id"]

    res_get = client.get(f"/courses/{course_id}")
    assert res_get.status_code == 200


def test_course_not_found():
    res = client.get("/courses/9999")
    assert res.status_code == 404


def test_course_update():
    res_create = client.post("/courses/", json={
        "title": "old equation",
        "code": "PHY404",
        "role": RoleEnum.admin.value
    })
    assert res_create.status_code == 201
    course_id = res_create.json()["data"]["id"]

    res_update = client.put(f"/courses/update_course/{course_id}", json={
        "title": "New equation",
        "code": "PHY405",
        "role": RoleEnum.admin.value
    })
    assert res_update.status_code == 200


def test_student_cannot_update_course():
    res_create = client.post("/courses/", json={
        "title": "Old course",
        "code": "PHY406",
        "role": RoleEnum.admin.value
    })
    assert res_create.status_code == 201
    course_id = res_create.json()["data"]["id"]

    res_update = client.put(f"/courses/update_course/{course_id}", json={
        "title": "Newly updated",
        "code": "PHY407",
        "role": RoleEnum.admin.value
    })
    assert res_update.status_code == 200
