# src/myapp/api/v1/routes/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from myapp.db.session import get_db
from myapp.schemas.user import UserCreate, UserOut
from myapp.crud.user import create_user

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_new_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return user