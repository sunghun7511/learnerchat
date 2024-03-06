from sqlalchemy import Column, BigInteger, String

from database import Base


class UserDAO(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(128), nullable=False)
    nickname = Column(String(128), nullable=False)
