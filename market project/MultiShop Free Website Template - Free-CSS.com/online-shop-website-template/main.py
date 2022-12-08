from pydantic import BaseModel

from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session


from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from fastapi.staticfiles import StaticFiles

from models import Base, User
from crud import db_register_user
from database import SessionLocal, engine

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
            return db.query(User).filter(User.name == username).first()
    return db.query(User).filter(User.name == username).first()



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

    user = db_register_user(db, username, password)
    if user:
        access_token = manager.create_access_token(
            data={'sub': username}
        )
        manager.set_cookie(response, access_token)
        return "User created"
    else:
        return "Failed"
    

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
