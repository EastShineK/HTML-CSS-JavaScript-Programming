from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    password: str
    client_id: str
    client_secret: str

    class Config:
        orm_mode = True

class UserInfoSchema(BaseModel):
    id: Optional[int]
    userid: Optional[str]
    password: Optional[str]
    name: Optional[str]
    membertype: Optional[str]
    class Config:
        orm_mode = True
        
class ProductSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[int]
    place: Optional[str]
    phonenum: Optional[str]
    auction: Optional[str]
    purchased: Optional[str]
    progress: Optional[str]
    imgpath: Optional[str]
    class Config:
        orm_mode = True