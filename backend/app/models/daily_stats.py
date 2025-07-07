from sqlalchemy import Column, Integer, Date, Enum
from app.db.base import Base
from enum import Enum as PyEnum
from app.models.issue import IssueStatus

class DailyStats(Base):
    __tablename__ = "daily_stats"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False)
    count = Column(Integer, nullable=False)
