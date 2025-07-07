from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime
from app.models.issue import IssueSeverity, IssueStatus

class IssueStatus(str, Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CLOSED = "CLOSED"

class IssueSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class IssueBase(BaseModel):
    title: str
    description: Optional[str] = None
    severity: IssueSeverity = IssueSeverity.LOW

class IssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: IssueSeverity

class IssueRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    severity: IssueSeverity
    status: IssueStatus
    reporter_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class IssueUpdate(BaseModel):
    status: IssueStatus

class IssueOut(IssueBase):
    id: int
    status: IssueStatus
    reporter_id: int

    class Config:
        orm_mode = True
