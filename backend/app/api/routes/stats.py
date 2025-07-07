from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.issue import Issue
from sqlalchemy import func

router = APIRouter()

@router.get("/stats/open-by-severity")
def get_open_issue_severity_stats(db: Session = Depends(get_db)):
    result = db.query(Issue.severity, func.count(Issue.id))\
               .filter(Issue.status == "OPEN")\
               .group_by(Issue.severity)\
               .all()
    return {severity: count for severity, count in result}
