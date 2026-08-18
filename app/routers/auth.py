from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controller.auth_controller import register_user_controller
from app.database import get_db
from app.schema.user import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user_controller(user=user, db=db)
