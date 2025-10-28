from fastapi import FastAPI, Request,status
from contextlib import asynccontextmanager

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.lib.configs import env_config
from src.routers.auth_router import router as AuthRouter
from src.lib.db.connect_db import ConnectDB
from src.models.user_model import User
@asynccontextmanager
async def lifespan(app:FastAPI):
    db = ConnectDB(env_config.DATABASE_URL)
    db.connection()
    db.create_tables()
    app.state.engine = db.engine
    yield 
    db.close_connection()
    print("close")
app = FastAPI(lifespan=lifespan)

@app.get("/")
def index():
    return {"message":"Welcome to api"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    formatted_errors = []
    for err in errors:
        # Join the 'loc' tuple/list into a string for better readability
        loc_path = ".".join(str(l) for l in err['loc'])
        formatted_errors.append({"loc": loc_path, "msg": err['msg']})
        
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "statusCode": 422,
            "error": True,
            "errors": formatted_errors,
            "data": None
        }
    )

app.include_router(AuthRouter)