# simple_task_tracker
Task Tracker CLI is a simple, command-line interface application for managing tasks. Built with Python and SQLAlchemy, it allows users to add, list, and toggle the status of tasks, along with managing users and categories for better organization.

#Features
1. User Management: Add new users to the task tracker system.
2. Category Management: Create categories to organize tasks.
3. Task Management: Add new tasks, list all tasks, and toggle the completion status of tasks.

#Getting Started
#Prerequisites
Before you begin, ensure you have met the following requirements:
Python 3.8 or later

SQLAlchemy
You can install SQLAlchemy using pip:
pip install SQLAlchemy

#Installation
Clone the project repository to your local machine:
git clone https://yourrepositoryurl.git
cd task-tracker-cli

#Setting Up the Database
Before running the application, initialize the database:
python cli/main.py init_db
This command sets up the SQLite database and prepares the necessary tables.

#Usage
The Task Tracker CLI provides several commands to manage tasks, users, and categories:

#Add a User:
python cli/main.py add_user <username>

#Add a Category:
python cli/main.py add_category <name>

#Add a Task:
python cli/main.py add_task <title> --description <description> --user_id <user_id> --category_id <category_id>

#List All Tasks:
python cli/main.py list_tasks

#Toggle Task Status:
python cli/main.py toggle_task_status <task_id>

