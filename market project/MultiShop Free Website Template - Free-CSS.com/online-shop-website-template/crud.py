from sqlalchemy.orm import Session

from models import User, UserInfo
from schemas import UserInfoSchema

def db_register_user(db: Session, name, password, client_id, client_secret):
    db_item = User(name=name, password=password, client_id=client_id, client_secret=client_secret)
    db_item2 = UserInfo(userid=name, password=password,name=client_secret, membertype=client_id)
    db.add(db_item)
    db.add(db_item2)
    db.commit()
    db.refresh(db_item)
    db.refresh(db_item2)
    return db_item

def db_get_users(db: Session, user: User):
    return db.query(UserInfo).all()

def db_del_user(db: Session, user: UserInfoSchema):
    print(user.id)
    db.query(UserInfo) \
           .filter(UserInfo.id == user.id) \
           .delete()
    db.commit()
    print(UserInfo.id)
    return True