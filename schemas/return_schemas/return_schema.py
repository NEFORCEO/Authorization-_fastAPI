from pydantic import BaseModel


class RegLogSchema(BaseModel):
    id: int
    name: str
    password: int

    model_config = {"from_attributes": True}

class GetResponse(BaseModel):
    status: int
    result: list[RegLogSchema]

class Error(BaseModel):
    message: str 
    
class Register(BaseModel):
    id: int 
    name: str 
    password: int 
    
class Login(BaseModel):
    password: int 
    result: bool 