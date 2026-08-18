from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schema.user import UserCreate
from app.service.auth_service import register_user


def register_user_controller(user: UserCreate, db: Session):
    try:
        return register_user(db=db, user=user)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
