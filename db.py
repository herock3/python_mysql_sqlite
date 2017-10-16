# 导入:
from mysql import connector
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('sqlite:///zyx.db', echo=True)
# engine=create_engine('mysql+mysqlconnector://root:123456@localhost:3306/zyx')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


