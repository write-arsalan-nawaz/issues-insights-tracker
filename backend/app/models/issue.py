from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum

from app.db.base import Base

class IssueStatus(PyEnum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CLOSED = "CLOSED"

class IssueSeverity(PyEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    file_path = Column(String, nullable=True)
    severity = Column(Enum(IssueSeverity), default=IssueSeverity.LOW)
    status = Column(Enum(IssueStatus), default=IssueStatus.OPEN)

    reporter_id = Column(Integer, ForeignKey("users.id"))
    reporter = relationship("User", back_populates="issues")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
