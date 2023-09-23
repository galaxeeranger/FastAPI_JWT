from fastapi import FastAPI, Depends, status, HTTPException, Body
from typing import Annotated
import models
from database import engine, Sessionlocal, Base
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from models import User, Post


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Schema Start
class PostBase(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    is_user: bool
    is_admin: bool

    class Config:
        from_attributes = True

class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True
# Schema end

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


def check_user(data, db: Session):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user and user.password == data.password:
        return True
    return False



@app.post("/usersignup/", status_code=status.HTTP_201_CREATED, tags=["user"])
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...), db: Session = Depends(get_db)):
    if check_user(user, db):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }


@app.get("/users/{user_id}", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["user"])
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    return user

@app.get("/users/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK, tags=["user"])
async def read_user(db: db_dependency):
    user = db.query(models.User).all()
    return user