from asyncio import current_task
from decouple import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import declarative_base, sessionmaker

MYSQL_URL = config("MYSQL_URL")


engine = create_async_engine(MYSQL_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session = async_scoped_session(async_session, scopefunc=current_task)

Base = declarative_base()
