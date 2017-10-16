from SQLAIchemy.db import DBSession, Base, engine
from SQLAIchemy.models import User

session = DBSession()

def init():
    Base.metadata.create_all(engine)

def insert(user):
    session.add(user)
    finalSession()
def update_Id(id,json):
    session.query(User).filter(User.id==id()).update(json)
    finalSession()
    return True
def delete_Id(id):
    session.query(User).filter(User.id==id).delete()
    finalSession()
    return True

def query_all():
    res = session.query(User).all
    return res
def query_id(id):
    res=session.query(User).filter(User.id==id).all()
    return res

def query_name(name):
    ret=session.query(User).filter(User.name==name).all()
    return ret
def finalSession():
    session.commit()
    session.close()

if __name__ == '__main__':
    # rose=User(id=1,name='Rsoe')
    # admin=User(2,'admin')
    #  insert(rose)
    #  init()
    userList=query_id(1)
    for user in userList:
         print(user.id+"-->"+user.name)
    # insert()
    # update()
    # delete_Id(1)
    # userList=query_id(5)
    # # print(user)
    # for user in userList:
    #   print(user.id+"-->"+user.name)