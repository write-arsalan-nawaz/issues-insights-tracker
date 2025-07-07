from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.models.user import User, UserRole
from app.core.security import get_password_hash
from app.db.session import get_db
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        full_name=user.full_name,
        role=UserRole.REPORTER
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(400, detail="Incorrect email or password")

    token = create_access_token({"sub": user.email, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
