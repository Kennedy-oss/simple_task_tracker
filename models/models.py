from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    tasks = relationship('Task', back_populates='user')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    tasks = relationship('Task', back_populates='category')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)  # New field to track task completion
    user = relationship('User', back_populates='tasks')
    category = relationship('Category', back_populates='tasks')

    @hybrid_property
    def formatted_date(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @hybrid_property
    def status(self):
        return 'Completed' if self.completed else 'Pending'

    def toggle_status(self):
        self.completed = not self.completed

# Setup database connection and sessionmaker
engine = create_engine('sqlite:///simple_task_tracker.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)


