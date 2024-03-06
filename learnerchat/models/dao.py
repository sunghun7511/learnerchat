from sqlalchemy import Column, BigInteger, String

from learnerchat.database import Base


class UserDAO(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(128), nullable=False)
    nickname = Column(String(128), nullable=False)


class CharacterDAO(Base):
    __tablename__ = 'character'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_email = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    profile_image = Column(String(1024), nullable=False)
    prompt = Column(String(1024), nullable=False)

    tags = Column(String(1024), nullable=False)


class CharacterChatDAO(Base):
    __tablename__ = 'character_chat'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    character_id = Column(BigInteger, nullable=False)
    chat = Column(String(1024), nullable=False)
