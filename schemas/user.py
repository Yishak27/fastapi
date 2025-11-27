from pydantic import BaseModel, EmailStr

class userRegister(BaseModel):
    name: str
    fullName:str
    role:enumerate("admin","user")
    email: EmailStr
    password: str

class userResponse(BaseModel):
    name: str
    email: EmailStr

class config:
    orm_mode = True