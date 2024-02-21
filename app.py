import click
from database_setup import SessionLocal, engine, Base
from models.task import Task
# Import your CLI commands
from cli import add_task, update_task, list_tasks, complete_task

# Initialize the database connection and create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Main CLI group
@click.group()
def cli():
    """Simple Task Tracker CLI"""
    pass

# Register CLI commands
cli.add_command(add_task)
cli.add_command(update_task)
cli.add_command(list_tasks)
cli.add_command(complete_task)

if __name__ == '__main__':
    cli()

