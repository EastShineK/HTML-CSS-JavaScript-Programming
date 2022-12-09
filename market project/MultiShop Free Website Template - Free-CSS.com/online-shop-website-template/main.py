from pydantic import BaseModel
from typing import List

from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session


from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from fastapi.staticfiles import StaticFiles

from models import Base, User, UserInfo
from crud import db_register_user, db_get_users, db_del_user, db_modify_users, db_get_membertype, db_register_product, db_get_products, db_del_product, db_modify_products, db_buy_products
from database import SessionLocal, engine
from schemas import UserInfoSchema, ProductSchema

import shutil
from fastapi import APIRouter, File, UploadFile




Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


app.mount("/css", StaticFiles(directory="css"))
app.mount("/lib", StaticFiles(directory="lib"))
app.mount("/img", StaticFiles(directory="img"))
app.mount("/scss", StaticFiles(directory="scss"))
app.mount("/mail", StaticFiles(directory="mail"))
app.mount("/js", StaticFiles(directory="js"))

class NotAuthenticatedException(Exception):
    pass

SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/login', use_cookie=True,
                       custom_exception=NotAuthenticatedException
)
@app.exception_handler(NotAuthenticatedException)
def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    """
    Redirect the user to the login page if not logged in
    """
    return RedirectResponse(url='/login')



@manager.user_loader
def get_user(username: str, db: Session = None):
    if not db:
        with SessionLocal() as db:
            return db.query(UserInfo).filter(UserInfo.userid == username).first()
    return db.query(UserInfo).filter(UserInfo.userid == username).first()
    

@app.post('/token')
def login(response: Response, data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = get_user(username)
    if not user:
        raise InvalidCredentialsException
    if user.password != password:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data={'sub': username}
    )
    manager.set_cookie(response, access_token)
    return {'access_token': access_token}

@app.post('/register')
def register_user(response: Response,
                  data: OAuth2PasswordRequestForm = Depends(),
                  db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    client_id = data.client_id
    client_secret = data.client_secret

    user = db_register_user(db, username, password, client_id, client_secret)
    print(client_id)
    if user:
        access_token = manager.create_access_token(
            data={'sub': username}
        )
        manager.set_cookie(response, access_token)
        return "User created"
    else:
        return "Failed"
    

@app.get("/user", response_model=List[UserInfoSchema])    
def get_todo(db: Session = Depends(get_db),
             user=Depends(manager)):
    return db_get_users(db, user)

@app.delete("/user", response_model=List[UserInfoSchema])    
def del_todo(user: UserInfoSchema,
             db: Session = Depends(get_db)
             ):
    result = db_del_user(db, user)
    # print(result.content)
    # if not result:
    #     return None
    return db_get_users(db, user)

@app.post("/user", response_model=List[UserInfoSchema])    
def add_todo(user: UserInfoSchema,
             db: Session = Depends(get_db)):
    print(user)
    result = db_modify_users(db, user)
    if not result:
        return None
    return db_get_users(db, user)

@app.get("/")
def get_root(user=Depends(manager)):
    return FileResponse("index1.html")

@app.get("/login")
def get_login():
    return FileResponse("index.html")

@app.get("/logout")
def logout(response : Response):
  response = RedirectResponse("/login", status_code= 302)
  response.delete_cookie(key ="access-token")
  return response

@app.get("/gologin")
def go_loginpage():
    return FileResponse("signin.html")

@app.get("/gosignup")
def go_signuppage():
    return FileResponse("signup.html")

@app.get("/gomanage")
def go_manage():
    return FileResponse("manage.html")

@app.get("/goselllist")
def go_manage():
    return FileResponse("sellerList.html")

@app.get("/godetail")
def go_manage():
    return FileResponse("detail.html")

@app.get("/goshop")
def go_manage():
    return FileResponse("shop.html")

@app.get("/gomypage")
def go_mypage(db: Session = Depends(get_db), user=Depends(manager)):
    x = db_get_membertype(db, user)
    print(x)
    if x == 1:
        return FileResponse("manage.html")
    elif x == 2:
        return FileResponse("sellpage.html")
    else:
        return FileResponse("contact.html")
    
@app.post("/product", response_model=List[ProductSchema])    
def add_product(product: ProductSchema,
             db: Session = Depends(get_db)):
    print(product)
    name =product.name
    price = product.price
    place =product.place
    phonenum =product.phonenum
    auction =product.auction
    purchased =product.purchased
    progress =product.progress
    imgpath = product.imgpath
    result = db_register_product(db, name, price, place, phonenum, auction, purchased, progress, imgpath)
    if not result:
        return None
    return db_get_products(db, product)

@app.get("/products", response_model=List[ProductSchema])    
def get_product(db: Session = Depends(get_db),
             user=Depends(manager)):
    return db_get_products(db, user)

@app.delete("/products", response_model=List[ProductSchema])    
def del_product(user: ProductSchema,
             db: Session = Depends(get_db)
             ):
    result = db_del_product(db, user)
    # print(result.content)
    # if not result:
    #     return None
    return db_get_products(db, user)

@app.post("/products", response_model=List[ProductSchema])    
def modify_product(user: ProductSchema,
             db: Session = Depends(get_db)):
    print(user)
    result = db_modify_products(db, user)
    if not result:
        return None
    return db_get_products(db, user)

@app.post("/products2", response_model=List[ProductSchema])    
def modify_product(user: ProductSchema,
             db: Session = Depends(get_db)):
    print(user)
    result = db_buy_products(db, user)
    if not result:
        return None
    return db_get_products(db, user)