from fastapi import APIRouter, Request
from src.models.user_model import  User, UserBase
from src.controllers.auth_controller import register_controller
router = APIRouter()

@router.post("/register")
def register(registerData:UserBase,request:Request):
    engine = request.app.state.engine
    return register_controller(registerData,engine)