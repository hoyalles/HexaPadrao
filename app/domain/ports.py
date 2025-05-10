from typing import List, Optional
from .models import User

class UserRepositoryPort:
    def get_all(self) -> List[User]:
        raise NotImplementedError()

    def get_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError()

    def create(self, user: User) -> User:
        raise NotImplementedError()

    def update(self, user_id: int, user: User) -> Optional[User]:
        raise NotImplementedError()

    def delete(self, user_id: int) -> bool:
        raise NotImplementedError()