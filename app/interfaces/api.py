from fastapi import APIRouter, HTTPException
from typing import List
from app.domain.models import User, UserCreate
from app.application.services import UserService

def get_user_router(service: UserService) -> APIRouter:
    router = APIRouter()

    @router.get("/users", response_model=List[User])
    def list_users():
        return service.list_users()

    @router.get("/users/{user_id}", response_model=User)
    def get_user(user_id: int):
        user = service.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @router.post("/users", response_model=User)
    def create_user(user: UserCreate):
        return service.create_user(user)

    @router.put("/users/{user_id}", response_model=User)
    def update_user(user_id: int, user: UserCreate):
        updated = service.update_user(user_id, user)
        if not updated:
            raise HTTPException(status_code=404, detail="User not found")
        return updated

    @router.delete("/users/{user_id}")
    def delete_user(user_id: int):
        if not service.delete_user(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}

    return router
