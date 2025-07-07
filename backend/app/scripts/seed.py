from app.db.session import SessionLocal
from app.models.user import User, UserRole
from app.models.issue import Issue, IssueStatus, IssueSeverity
from app.core.security import get_password_hash

db = SessionLocal()

db.query(Issue).delete()
db.query(User).delete()
db.commit()

users = [
    User(
        email="admin@example.com",
        hashed_password=get_password_hash("password"),
        full_name="Admin User",
        role=UserRole.ADMIN,
    ),
    User(
        email="maintainer@example.com",
        hashed_password=get_password_hash("password"),
        full_name="Maintainer User",
        role=UserRole.MAINTAINER,
    ),
    User(
        email="reporter@example.com",
        hashed_password=get_password_hash("password"),
        full_name="Reporter User",
        role=UserRole.REPORTER,
    ),
]

for user in users:
    db.add(user)
db.commit()

reporter = db.query(User).filter(User.role == UserRole.REPORTER).first()

issues = [
    Issue(title="Bug in dashboard", description="Chart not loading", status=IssueStatus.OPEN, severity=IssueSeverity.HIGH, reporter_id=reporter.id),
    Issue(title="Login fails", description="403 after login", status=IssueStatus.OPEN, severity=IssueSeverity.CRITICAL, reporter_id=reporter.id),
    Issue(title="Text overflow", description="Bad UI on mobile", status=IssueStatus.CLOSED, severity=IssueSeverity.LOW, reporter_id=reporter.id),
]

for issue in issues:
    db.add(issue)

db.commit()
db.close()

print("✅ Seeded test data.")
