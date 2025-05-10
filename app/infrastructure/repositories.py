from typing import List, Optional
from app.domain.models import User
from app.domain.ports import UserRepositoryPort

class InMemoryUserRepository(UserRepositoryPort):
    def __init__(self):
        self.users = []
        self.counter = 1

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self.users if u.id == user_id), None)

    def create(self, user: User) -> User:
        user.id = self.counter
        self.counter += 1
        self.users.append(user)
        return user

    def update(self, user_id: int, user: User) -> Optional[User]:
        existing = self.get_by_id(user_id)
        if existing:
            existing.name = user.name
            existing.email = user.email
            return existing
        return None

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False