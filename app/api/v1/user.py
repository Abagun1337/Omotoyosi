from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate
from app.services.users import UserService


user_router = APIRouter(tags=["User Route"])


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate):
    if user_in.role not in ("student", "admin"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Role must be student or admin")
    new_user = UserService.create_user(user_in)
    return {"message": "successfull", "data": new_user}


@user_router.get("/", status_code=200)
def list_users():
    new_user = UserService.get_all_users()
    return {
        "message": "Users retrieved sucessfully", "data": new_user
    }


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    return {"message": "User retrieved sucessfully", "data": user}


@user_router.delete('/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    deleted_user = UserService.delete_user_by_id(user_id)
    return {"message": "User deleted sucessfully", "data": deleted_user}
