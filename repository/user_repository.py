from typing import List, Union

from models.user import User


class UserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, *, user: User) -> User:
        self.users.append(user)
        return user

    def get_users(self) -> List[User]:
        return self.users

    def get_user_by_email(self, email: str) -> Union[User, None]:
        for user in self.users:
            if user.email == email:
                return user
        raise ValueError("User not found")

    def update_user(self, new_user: User) -> User:
        user_found = self.get_user_by_email(new_user.email)
        user_found.name = new_user.name
        user_found.bio = new_user.bio
        user_found.avatar = new_user.avatar
        return user_found

    def delete_user(self, user_to_delete: User) -> bool:
        for index, user in enumerate(self.users):
            if user.email == user_to_delete.email:
                del self.users[index]
                return True
        raise ValueError("User not found")
