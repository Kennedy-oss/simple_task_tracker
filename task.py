from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    due_date = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)

engine = create_engine('sqlite:///simple_task_tracker.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

