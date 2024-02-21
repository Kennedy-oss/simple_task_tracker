import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Import the Base class and your models
from models.models import Base, Task

# Setup database connection and sessionmaker
engine = create_engine('sqlite:///simple_task_tracker.db', echo=True)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Simple Task Tracker CLI."""
    pass

@cli.command()
def list_tasks():
    """Lists all tasks."""
    session = Session()
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.title} | Status: {task.status} (Created at: {task.formatted_date})')

@cli.command()
@click.argument('title')
@click.option('--description', default='', help='Description of the task')
def add_task(title, description):
    """Adds a new task with the given TITLE and optional DESCRIPTION."""
    session = Session()
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    click.echo(f'Task "{title}" added successfully.')

@cli.command()
@click.argument('task_id', type=int)
def toggle_task_status(task_id):
    """Toggles the completion status of a task."""
    session = Session()
    task = session.query(Task).get(task_id)
    if task:
        task.toggle_status()
        session.commit()
        click.echo(f'Task "{task.title}" status toggled to {task.status}.')
    else:
        click.echo('Task not found.')


