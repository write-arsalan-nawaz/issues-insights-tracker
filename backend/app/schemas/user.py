from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MAINTAINER = "MAINTAINER"
    REPORTER = "REPORTER"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None
    role: UserRole

    class Config:
        orm_mode = True
