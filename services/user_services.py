from typing import List

from models.user import User
from repository.user_repository import UserRepository


class UserServices:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, user: User) -> User:
        if not user.email.endswith("@monadical.com"):
            raise ValueError("Invalid email")

        return self.user_repository.create_user(user=user)

    async def get_users(self) -> List[User]:
        return self.user_repository.get_users()

    async def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email=email)

    async def update_user(self, new_user: User) -> User:
        return self.user_repository.update_user(new_user=new_user)

    async def delete_user(self, email: str) -> bool:
        user_to_delete = self.user_repository.get_user_by_email(email=email)
        return self.user_repository.delete_user(user_to_delete=user_to_delete)
