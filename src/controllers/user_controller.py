from src.models.user_model import User 
from sqlmodel import Session
 
def create_user(user:User,engine):
    with Session(engine) as session:
        new_user = User(**user.model_dump()) 
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return {"message":"User create succesfully","data":user}