import click
from models.models import User, Category, Task
from sqlalchemy.orm import sessionmaker
from database import Session  # Import the sessionmaker instance
# Initialize the database (create tables)
init_db()

# Create a new database session for operations
session = Session()

@click.group()
def cli():
    """Task Tracker CLI"""
    pass

@cli.command()
@click.argument('username')
def add_user(username):
    """Add a new user"""
    session = Session()
    user = User(username=username)
    session.add(user)
    try:
        session.commit()
        click.echo(f"User '{username}' added successfully.")
    except:
        session.rollback()
        click.echo(f"Failed to add user '{username}'.")
    finally:
        session.close()

@cli.command()
@click.argument('name')
def add_category(name):
    """Add a new category"""
    session = Session()
    category = Category(name=name)
    session.add(category)
    try:
        session.commit()
        click.echo(f"Category '{name}' added successfully.")
    except:
        session.rollback()
        click.echo(f"Failed to add category '{name}'.")
    finally:
        session.close()

@cli.command()
@click.argument('title')
@click.option('--description', default='')
@click.option('--user_id', type=int)
@click.option('--category_id', type=int)
def add_task(title, description, user_id, category_id):
    """Add a new task"""
    session = Session()
    task = Task(title=title, description=description, user_id=user_id, category_id=category_id)
    session.add(task)
    try:
        session.commit()
        click.echo(f"Task '{title}' added successfully.")
    except:
        session.rollback()
        click.echo(f"Failed to add task '{title}'.")
    finally:
        session.close()

@cli.command()
def list_tasks():
    """List all tasks"""
    session = Session()
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} | Status: {task.status} (Created at: {task.formatted_date})')
    session.close()

@cli.command()
@click.argument('task_id', type=int)
def toggle_task_status(task_id):
    """Toggle the completion status of a task"""
    session = Session()
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



