from typing import List, Optional
from app.domain.models import User
from app.domain.ports import UserRepositoryPort

class UserService:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def list_users(self) -> List[User]:
        return self.repository.get_all()

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def create_user(self, user: User) -> User:
        return self.repository.create(user)

    def update_user(self, user_id: int, user: User) -> Optional[User]:
        return self.repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)