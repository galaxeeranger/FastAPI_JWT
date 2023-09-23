
from sqlalchemy import Boolean, Column, Integer, String, MetaData
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(50))
    is_user = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)


