import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.models.user import Base, User, UserRole
from app.core.security import get_password_hash

DATABASE_URL = "postgresql+asyncpg://dev@localhost/issues_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        for email, role in [
            ("admin@example.com", UserRole.ADMIN),
            ("maintainer@example.com", UserRole.MAINTAINER),
            ("reporter@example.com", UserRole.REPORTER),
        ]:
            session.add(User(
                email=email,
                hashed_password=get_password_hash("password123"),
                full_name=role.capitalize(),
                role=role
            ))
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed())
