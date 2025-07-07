from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.issue import Issue, IssueStatus, IssueSeverity
from app.schemas.issue import IssueCreate, IssueOut, IssueUpdate
from app.db.session import get_db
from app.core.deps import get_current_user, get_current_user_role
from app.models.user import User, UserRole
from app.models.issue import Issue, IssueStatus
from app.schemas.issue import IssueCreate, IssueRead

router = APIRouter()

@router.post("/", response_model=IssueRead)
def create_issue(
    issue: IssueCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.REPORTER:
        raise HTTPException(status_code=403, detail="Only REPORTERS can create issues.")

    new_issue = Issue(
        title=issue.title,
        description=issue.description,
        severity=issue.severity,
        status=IssueStatus.OPEN,
        reporter_id=current_user.id
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

@router.get("/", response_model=List[IssueOut])
def list_issues(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if user.role == UserRole.REPORTER:
        return db.query(Issue).filter(Issue.reporter_id == user.id).all()
    return db.query(Issue).all()

@router.patch("/{issue_id}", response_model=IssueOut)
def update_issue(
    issue_id: int,
    update: IssueUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(404, detail="Issue not found")

    if user.role == UserRole.REPORTER:
        if issue.reporter_id != user.id:
            raise HTTPException(403, detail="Not allowed to edit others' issues")

    elif user.role == UserRole.MAINTAINER:
        if update.status is None:
            raise HTTPException(403, detail="Maintainers can only update status")
        issue.status = update.status

    elif user.role == UserRole.ADMIN:
        for field, value in update.dict(exclude_unset=True).items():
            setattr(issue, field, value)
    else:
        raise HTTPException(403, detail="Invalid role")

    db.commit()
    db.refresh(issue)
    return issue
