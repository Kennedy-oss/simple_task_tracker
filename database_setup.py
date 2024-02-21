from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database URL
DATABASE_URL = "sqlite:///simple_task_tracker.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Base class for declarative models
Base = declarative_base()

# Session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import all your models here
from models.task import Task

def create_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()

