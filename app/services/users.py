
from app.schemas.user import UserCreate, User
from app.core.db import Users


class UserService:
    @staticmethod
    def create_user(user_in: UserCreate) -> User:
        user_id = len(Users) + 1
        new_user = User(
            id=user_id,
            **user_in.model_dump()
        )
        Users[user_id] = new_user
        return new_user

    @staticmethod
    def get_all_users():
        return list(Users.values())

    @staticmethod
    def get_user_by_id(user_id: int) -> User | None:
        return Users.get(user_id)

    @staticmethod
    def delete_user_by_id(user_id: int) -> User | None:
        if user_id not in Users:
            return None
        deleted_user = Users.pop(user_id)
        return deleted_user
