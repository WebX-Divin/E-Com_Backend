from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.hashing import verify_password
from auth.jwt_handler import create_access_token
from crud.user_crud import get_user_by_email, create_user
from schemas.user_schema import UserCreate, UserOut, Token
from database import get_db



router = APIRouter()



@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    new_user = create_user(db, user.username, user.email, user.password)
    return new_user



@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
