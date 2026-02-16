## Course Enrollment Management API

A RESTful API built with **FastAPI** to manage users,courses and enrollment with **role-based behaviour**

```
uvicorn app.main:app -- reload
```

### Entity

- Public access to informtion
- User roles: **student** and **admin**
- Role-based restictions on operation
- student enrollment and deregistration
- Admin enro
  llment oversight
- In-memory storage
- Full test coverage Pytest

### Tech stack

- **Python 3.10**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **HTTPX**
- **email-validator**

### Project Structure

```
karatu25 project
|────app/
|    |────main.py
     └── api/
│    |   └── v1/
│           ├── __init__.py
│    |        ├── users.py
│    |        ├── courses.py
│    |        └── enrollments.py

|
│    ├── core/
│    │   ├── __init__.py
│    │   └── db.py
│    │
│    ├── schemas/
│    │   ├── __init__.py
│    │   ├── user.py
│    │   ├── course.py
│    │   └── enrollment.py
│    ├── services/
│    │   ├── __init__.py
│    │   ├── users.py
│    │   ├── courses.py
│    │   └── enrollments.py
│    │
├── tests/
│   └── v1/
│   |   ├── test_users.py
│   |   ├── test_courses.py
|   |   |── test_enrollment.py
|
├── README.md
├── requirement.txt

```
