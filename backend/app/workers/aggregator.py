from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.db.session import SessionLocal
from app.models.issue import IssueStatus, Issue
from app.models.daily_stats import DailyStats
import logging

logger = logging.getLogger(__name__)

def aggregate_issue_counts():
    db: Session = SessionLocal()
    today = date.today()
    print("🔁 Running issue aggregation...")

    try:
        results = db.query(Issue.status, func.count(Issue.id)).group_by(Issue.status).all()

        for status, count in results:
            stat = DailyStats(date=today, status=status, count=count)
            db.add(stat)

        db.commit()
        print("✅ Aggregation complete")
    except Exception as e:
        print(f"❌ Error aggregating: {e}")
        db.rollback()
    finally:
        db.close()

def start():
    logger.info("Starting APScheduler...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(aggregate_issue_counts, 'interval', minutes=30)
    scheduler.start()
