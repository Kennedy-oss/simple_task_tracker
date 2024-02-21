import click
from datetime import datetime
from sqlalchemy.orm import Session
from database_setup import SessionLocal, engine
from models.task import Task
from database_setup import Base


# Bind the engine with the base metadata
Base.metadata.bind = engine

# Add task command
@click.command('add-task')
@click.argument('name')
@click.option('--due-date', default=None, help='Due date of the task in YYYY-MM-DD format.')
def add_task(name, due_date):
    if due_date:
        try:
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            click.echo("Invalid date format. Please use YYYY-MM-DD.")
            return
    else:
        due_date_obj = None
    
# Continue with adding the task to the database

# Update task command
@click.command('update-task')
@click.argument('task_id', type=int)
@click.option('--name', default=None, help='New name of the task.')
@click.option('--due-date', default=None, help='New due date of the task in YYYY-MM-DD format.')
@click.option('--completed', is_flag=True, help='Mark the task as completed.')
def update_task(task_id, name, due_date, completed):
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            click.echo("Task not found.")
            return
        
        if due_date:
            try:
                task.due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            except ValueError:
                click.echo("Invalid date format. Please use YYYY-MM-DD.")
                return

        if name:
            task.name = name
        if completed:
            task.completed = True
        
        session.commit()
        click.echo(f"Task updated: {task.name}")

# List tasks command
@click.command('list-tasks')
@click.option('--completed', is_flag=True, help='List only completed tasks.')
@click.option('--pending', is_flag=True, help='List only pending tasks.')
def list_tasks(completed, pending):
    """List tasks."""
    with SessionLocal() as session:
        query = session.query(Task)
        if completed:
            query = query.filter(Task.completed == True)
        elif pending:
            query = query.filter(Task.completed == False)
        tasks = query.all()
        for task in tasks:
            click.echo(f"{task.id}: {task.name} - {'Completed' if task.completed else 'Pending'}")

# Complete task command 
@click.command('complete-task')
@click.argument('task_id', type=int)
def complete_task(task_id):
    """Mark a task as completed."""
    with SessionLocal() as session:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            task.completed = True
            session.commit()
            click.echo(f"Task completed: {task.name}")
        else:
            click.echo("Task not found.")

# Combine Commands into CLI Group
@click.group()
def cli():
    """Simple Task Tracker CLI"""
    pass

# Add commands to the CLI group
cli.add_command(add_task)
cli.add_command(update_task)
cli.add_command(list_tasks)
cli.add_command(complete_task)

if __name__ == '__main__':
    cli()

