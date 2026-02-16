from app.main import app
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../app')))


client = TestClient(app)


def test_create_user():
    res = client.post("/users/", json={
        "name": "Abagun Omotoyosi",
        "email": "Abaguntoyosi002@icloud.com",
        "role": "student"
    })
    assert res.status_code == 201


# def test_create_user_invalid_role():
#     res = client.post("/users/", json={
#         "name": "Abagun Omotoyosi",
#         "email": "Abaguntoyosi002@icloud.com",
#         "role": "teacher"
#     })
#     assert res.status_code == 422


def test_get_users():
    res = client.get("/users")
    assert res.status_code == 200


def test_get_user_not_found():
    res = client.get("/users/9999")
    assert res.status_code == 404


def test_get_user_by_id():
    res_create = client.post("/users/", json={
        "name": "Abagun Omotoyosi",
        "email": "Abaguntoyosi002@icloud.com",
        "role": "student"
    })
    assert res_create.status_code == 201
    user_id = res_create.json()["data"]["id"]
    res_get = client.get(f"/users/{user_id}")
    assert res_get.status_code == 200


def test_create_user_invalid_email():
    res = client.post("/users/", json={
        "name": "Abagun Omotoyosi",
        "email": "Invalid-email",
        "role": "student"
    })
    assert res.status_code == 422


def test_user_empty_name():
    res = client.post("/users/", json={
        "name": "",
        "email": "Abaguntoyosi002@icloud.com",
        "role": "student"
    })
    assert res.status_code == 422
