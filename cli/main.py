import sys
import os
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

# Database setup
engine = create_engine('sqlite:///simple_task_tracker.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import all models here to ensure they are attached to the Base.metadata
    from models.models import User, Category, Task  # Adjust the import path as needed
    Base.metadata.create_all(bind=engine)

# Correctly add the project root to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from models.models import User, Category, Task
# Initialize the database (create tables)
init_db()

@click.group()
def cli():
    """Task Tracker CLI"""
    pass

@cli.command()
@click.argument('username')
def add_user(username):
    """Add a new user"""
    session = db_session()
    user = User(username=username)
    session.add(user)
    try:
        session.commit()
        click.echo(f"User '{username}' added successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Failed to add user '{username}'. Reason: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('name')
def add_category(name):
    """Add a new category"""
    session = db_session()
    category = Category(name=name)
    session.add(category)
    try:
        session.commit()
        click.echo(f"Category '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Failed to add category '{name}'. Reason: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('title')
@click.option('--description', default='')
@click.option('--user_id', type=int)
@click.option('--category_id', type=int)
def add_task(title, description, user_id, category_id):
    """Add a new task"""
    session = db_session()
    task = Task(title=title, description=description, user_id=user_id, category_id=category_id)
    session.add(task)
    try:
        session.commit()
        click.echo(f"Task '{title}' added successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Failed to add task '{title}'. Reason: {e}")
    finally:
        session.close()

@cli.command()
def list_tasks():
    """List all tasks"""
    session = db_session()
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} | Status: {task.status} (Created at: {task.formatted_date})')
    session.close()

@cli.command()
@click.argument('task_id', type=int)
def toggle_task_status(task_id):
    """Toggle the completion status of a task"""
    session = db_session()
    task = session.query(Task).get(task_id)
    if task:
        task.toggle_status()
        session.commit()
        click.echo(f"Task '{task.title}' status toggled to {task.status}.")
    else:
        click.echo('Task not found.')
    session.close()

if __name__ == '__main__':
    cli()

