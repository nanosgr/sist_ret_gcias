from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a FastAPI app
app = FastAPI()

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Pydantic model for the users table
class User(BaseModel):
    uid: str
    first_name: str
    last_name: str
    lastlogin: str
    is_active: int
    email: str
    hashed_password: str

# Define the SQLAlchemy model for the users table
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String(20), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    lastlogin = Column(DateTime)
    is_active = Column(Integer, default=1)
    email = Column(String(40), nullable=True)
    hashed_password = Column(String(90), nullable=True)

# Create the table in the database
Base.metadata.create_all(bind=engine)

# API endpoint to create a new user
@app.post("/users/")
async def create_user(user: User):
    db = SessionLocal()
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
