from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.hashing import verify_password
from auth.jwt_handler import create_access_token
from crud.user_crud import get_user_by_email, create_user
from schemas import user_schema
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/signup", response_model=user_schema.UserOut)
def signup(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    new_user = create_user(db, user)
    return user_schema.UserOut(
        message="success",
        data=user_schema.UserData(
            id=new_user.id,
            email=new_user.email,
            username=new_user.username
        )
    )

@router.post("/login", response_model=user_schema.Token)
def login(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials."
        )
    token = create_access_token(data={"sub": db_user.email})
    return {'message': 'success', 'access_token': token, 'token_type': 'bearer'}
