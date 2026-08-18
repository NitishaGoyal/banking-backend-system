from sqlalchemy.orm import Session

from app.dao.user_dao import create_user, get_user_by_email
from app.schema.user import UserCreate
from app.settings.security import hash_password


def register_user(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db=db, email=user.email)
    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = hash_password(user.password)
    create_user(
        db=db,
        full_name=user.full_name,
        email=str(user.email),
        password_hash=hashed_password,
    )

    return {"message": "User registered successfully"}
