from sqlalchemy import Column, String

# 定义User对象:
from SQLAIchemy.db import Base


class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))