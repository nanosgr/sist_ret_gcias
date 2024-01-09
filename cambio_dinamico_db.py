from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request

app = FastAPI()

# Define the base database connection string
DATABASE_URL_TEMPLATE = "mysql+pymysql://user:password@localhost/{db_name}"

# Create a declarative base class
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)

# Define the Pydantic model for user requests
class UserCreate(BaseModel):
    username: str
    email: str

# Dependency to dynamically get the database session
def get_db(request: Request):
    db_name = request.headers.get('X-Database-Name')
    if not db_name:
        raise HTTPException(status_code=400, detail="X-Database-Name header missing")

    database_url = DATABASE_URL_TEMPLATE.format(db_name=db_name)
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Now use the get_db dependency in your endpoints
@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    # Your existing create_user logic here
    pass

# Repeat the use of Depends(get_db) for other endpoints
# In this example, the get_db dependency function reads the X-Database-Name header from the incoming request. 
# It uses this header to format the DATABASE_URL_TEMPLATE with the correct database name, creates a new SQLAlchemy engine and session for that database, 
# and then yields the session for use in the endpoint.

# When making requests to the FastAPI application, the client should include the X-Database-Name header with the name of the target database:

# POST /users/ HTTP/1.1
# Host: localhost:8000
# Content-Type: application/json
# X-Database-Name: dynamic_db_name

# {
#     "username": "john_doe",
#     "email": "john@example.com"
# }

# HTTP

# Please note that this approach creates a new SQLAlchemy engine for each request, which can be resource-intensive. In a production environment, 
# you would want to optimize this by reusing engine instances for the same database or implementing a connection pool.

# Additionally, be cautious with this approach as it can expose your application to security risks if not properly handled. 
# Ensure that the databases are properly isolated and that access is controlled to prevent unauthorized database switching.