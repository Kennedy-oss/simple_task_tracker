from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configure the database engine
# Note: Replace 'sqlite:///simple_task_tracker.db' with your database URI if different
engine = create_engine('sqlite:///simple_task_tracker.db', convert_unicode=True, echo=False)

# Create a session factory bound to this engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Use scoped_session to ensure thread safety
Session = scoped_session(SessionLocal)

# Base class for declarative models
Base = declarative_base()
Base.query = Session.query_property()

def init_db():
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    from models.models import User, Category, Task  # Adjust the import path as needed
    Base.metadata.create_all(bind=engine)

