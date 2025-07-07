from sqlalchemy import Column, Integer, String, Boolean, Enum as SqlEnum
from sqlalchemy.orm import relationship
import enum

from app.db.base import Base

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    MAINTAINER = "MAINTAINER"
    REPORTER = "REPORTER"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(SqlEnum(UserRole), default=UserRole.REPORTER)

    issues = relationship("Issue", back_populates="reporter")
