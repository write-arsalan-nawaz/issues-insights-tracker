from logging.config import fileConfig
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import os
import sys
from sqlalchemy.engine import engine_from_config
from sqlalchemy import pool
from app.models.user import Base as UserBase
from app.models.issue import Base as IssueBase

# Add app to sys path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from app.models.user import Base  # import all models here

# Alembic Config
config = context.config
fileConfig(config.config_file_name)

# Target metadata
target_metadata = UserBase.metadata
target_metadata = IssueBase.metadata

DATABASE_URL = "postgresql+asyncpg://dev@localhost/issues_db"
engine = create_async_engine(DATABASE_URL, echo=True)

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

def main():
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()

main()
