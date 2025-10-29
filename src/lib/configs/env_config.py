from dotenv import load_dotenv
import os

from sqlalchemy import URL

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")
DATABASE_URL = os.getenv("DATABASE_URL")

drivername=os.getenv("drivername")
username=os.getenv("db_username")
password=os.getenv("password")
host=os.getenv("host")
database=os.getenv("database")
query={
        "driver":os.getenv("driver")
        }
url_object = URL.create(
    drivername=drivername,
    username=username,
    password=password,
    host=host,
    database=database,
    query=query
)

