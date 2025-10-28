import jwt
from src.lib.configs import env_config
def generate_token(payload:dict):

    return jwt.encode(payload,env_config.JWT_SECRET,env_config.ALGORITHM)