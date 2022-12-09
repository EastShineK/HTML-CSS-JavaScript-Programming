from sqlalchemy.orm import Session

from models import User, UserInfo, Product
from schemas import UserInfoSchema, ProductSchema

def db_register_user(db: Session, name, password, client_id, client_secret):
    db_item = User(name=name, password=password, client_id=client_id, client_secret=client_secret)
    db_item2 = UserInfo(userid=name, password=password,membertype=client_id,name=client_secret)
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

def db_modify_users(db: Session, user: UserInfoSchema):
    row = db.query(UserInfo).filter(UserInfo.id == user.id)
    
    print(user.name)
    print(row)
    row.update({"name" : user.name, "userid" : user.userid})
    db.commit()
    
    return True

def db_get_membertype(db: Session, user: User):
    row = db.query(UserInfo).filter(UserInfo.id == user.id)
    print(row.value(UserInfo.membertype))
    print('whi')
    print(row.value(UserInfo.membertype))
    if row.value(UserInfo.membertype) == '3':
        return 1
    elif row.value(UserInfo.membertype) == '2':
        return 2
    else:
        return 3
    
    
def db_register_product(db: Session, name, price, place, phonenum, auction, purchased, progress, imgpath, sellername, numofwish):
    db_item = Product(name=name, price=price, place=place, phonenum=phonenum, auction=auction, purchased=purchased, progress=progress, imgpath=imgpath, sellername=sellername, numofwish=numofwish)
    print(db_item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def db_get_products(db: Session, product: Product):
    return db.query(Product).all()

def db_del_product(db: Session, user: ProductSchema):
    print(user.id)
    db.query(Product) \
           .filter(Product.id == user.id) \
           .delete()
    db.commit()
    return True

def db_modify_products(db: Session, user: ProductSchema):
    row = db.query(Product).filter(Product.id == user.id)
    
    print(user.price)
    print(row)
    row.update({"price" : user.price, "place" : user.place})
    db.commit()
    
    return True

def db_buy_products(db: Session, user: ProductSchema):
    row = db.query(Product).filter(Product.id == user.id)
    
    row.update({"purchased" : "Yes", "progress" : "No"})
    db.commit()
    
    return True

def db_wish_products(db: Session, user: ProductSchema):
    row = db.query(Product).filter(Product.id == user.id)
    
    row.update({"numofwish" : user.numofwish})
    db.commit()
    
    return True