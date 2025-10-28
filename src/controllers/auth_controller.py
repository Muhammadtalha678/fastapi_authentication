from sqlmodel import Session, select, text
from src.models.user_model import  User, UserBase
from pwdlib import PasswordHash
def register_controller(registerData:UserBase,engine):
    password_hash_helper = PasswordHash.recommended()
    try:
        data = registerData.model_dump()
        with Session(engine) as session:
            # check user already register or not
            exisiting_user = session.exec(select(User).where(User.email == data['email'])).first()
            # print(isinstance(data,dict))
            # print(exisiting_user)
            if exisiting_user:
                return {
                    "statusCode" : 409,
                    "error":True,
                    "errors": {
                        "general":"User already register"
                    },
                    "data":None
                }
            password_hash = password_hash_helper.hash(password=data['password'])
            print("password_hash",password_hash)

            new_user = User(email=data['email'],password=password_hash)
            # session.exec(text("TRUNCATE TABLE user"))
            # session.commit()
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return {
                    "statusCode" : 200,
                    "error":False,
                    "errors": None,
                    "data":{
                        "message":"User register successfully","data":new_user
                    }
                }
    except Exception as e:
        return {
                    "statusCode" : 500,
                    "error":True,
                    "errors": {
                        "general":f"Some thing went wrong {e}"
                    },
                    "data":None
                }