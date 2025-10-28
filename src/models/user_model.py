from sqlmodel import SQLModel,Field
from pydantic import field_validator,BaseModel,Field as F,EmailStr

class UserBase(BaseModel):
    email:EmailStr
    password:str = F(min_length=8)
    # @field_validator('email', mode='after')
    # @classmethod
    # def validate_email_domain(cls, v: str):
    #     # We can also use PydanticCustomError for more control,
    #     # but a simple ValueError will do for this case.
    #     if not v.endswith('@example.com'):
    #         raise ValueError('Email address must end with @example.com')
    #     return v
class User(SQLModel,table = True):
    id:int|None = Field(default=None,primary_key=True)
    email:str = Field(unique=True)
    password:str
    