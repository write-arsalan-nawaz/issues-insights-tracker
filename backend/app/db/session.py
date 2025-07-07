from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://dev@localhost/issues_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
