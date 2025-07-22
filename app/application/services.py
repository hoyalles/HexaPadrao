from typing import List, Optional
from app.domain.models import User, UserCreate
from app.domain.ports import UserRepositoryPort

class UserService:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def list_users(self) -> List[User]:
        return self.repository.get_all()

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def create_user(self, user_create: UserCreate) -> User:
        new_id = self._generate_id()
        user = User(id=new_id, name=user_create.name, email=user_create.email)
        return self.repository.create(user)

    def update_user(self, user_id: int, user_update: UserCreate) -> Optional[User]:
        # Verifica se existe antes de atualizar
        existing_user = self.repository.get_by_id(user_id)
        if not existing_user:
            return None

        updated_user = User(id=user_id, name=user_update.name, email=user_update.email)
        return self.repository.update(user_id, updated_user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)

    def _generate_id(self) -> int:
        users = self.repository.get_all()
        if not users:
            return 1
        return max(user.id for user in users) + 1
