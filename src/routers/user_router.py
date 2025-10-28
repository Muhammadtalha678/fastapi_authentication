from fastapi import APIRouter, Request

from src.models.user_model import User
from src.controllers.user_controller import create_user
router = APIRouter()

@router.get('/users')
def all_users():
    return [{"name":"talha"}]

@router.post('/users')
def add_user(user:User,request:Request):
    engine = request.app.state.engine
    return create_user(user,engine)