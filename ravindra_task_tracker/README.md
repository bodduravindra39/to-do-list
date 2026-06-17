# Ravindra Boddu - Console To-Do List Application

## Project Overview

This project is a console-based To-Do List Application built in Python using
Object-Oriented Programming. It was created as an internship-style submission by
Ravindra Boddu.

The application allows users to add tasks, view tasks, mark tasks as completed,
delete tasks, search tasks, and view task statistics. Tasks are stored in a JSON
file, so the data remains available after the program is closed.

## Project Structure

```text
ravindra_task_tracker/
|
|-- app_runner.py
|-- ravindra_task.py
|-- boddu_task_manager.py
|-- ravindra_tasks.json
|-- README.md
```

## Features

- Add Task
- View Tasks
- Mark Task as Completed
- Delete Task
- Search Task
- Show Task Statistics
- Exit Program
- Automatic JSON file loading
- Automatic JSON file saving
- Input validation for menu choices and task numbers
- Graceful handling of invalid task IDs

## Technologies Used

- Python 3
- Object-Oriented Programming
- JSON file handling
- Console-based user interface
- PEP-8 coding style

## How to Run the Project

1. Open the project folder.
2. Run the application:

```bash
python app_runner.py
```

## File Explanation

### app_runner.py

This file starts the application and controls the menu shown to the user.

- `from boddu_task_manager import BodduTaskManager`
  imports the manager class so the menu can perform task actions.
- `show_main_menu()`
  prints all menu options.
- `ask_for_task_number()`
  asks the user for a task number and validates that the input is numeric.
- `run_application()`
  creates the task manager and keeps the program running until the user exits.
- `if __name__ == "__main__":`
  makes sure the application starts only when this file is run directly.

### ravindra_task.py

This file contains the `RavindraTask` class. One object of this class represents
one task.

- `from datetime import datetime`
  imports Python's date and time tool.
- `class RavindraTask`
  defines the blueprint for a task.
- `__init__()`
  stores task number, title, status, and created date.
- `get_current_date()`
  creates a readable date and time for new tasks.
- `mark_completed()`
  changes the task status to completed.
- `get_status_text()`
  returns `Completed` or `Pending`.
- `to_dictionary()`
  converts the object into dictionary format for JSON saving.
- `from_dictionary()`
  rebuilds a task object from JSON data.

### boddu_task_manager.py

This file contains the `BodduTaskManager` class. It manages the complete task
list.

- `import json`
  imports Python's JSON module for file storage.
- `from pathlib import Path`
  helps create a safe file path for the JSON file.
- `from ravindra_task import RavindraTask`
  imports the task class.
- `class BodduTaskManager`
  defines the manager that controls all tasks.
- `__init__()`
  prepares the JSON file path and loads saved tasks.
- `load_tasks()`
  reads tasks from `ravindra_tasks.json`.
- `save_tasks()`
  writes all tasks into `ravindra_tasks.json`.
- `get_next_task_number()`
  creates the next available task ID.
- `find_task_by_number()`
  searches for a task using its number.
- `add_task()`
  validates and adds a new task.
- `view_tasks()`
  displays all tasks.
- `mark_task_completed()`
  marks an existing task as completed.
- `delete_task()`
  removes an existing task.
- `search_task()`
  finds tasks by title text.
- `show_task_statistics()`
  displays total, completed, and pending task counts.

### ravindra_tasks.json

This file stores the task data permanently. It starts with an empty list:

```json
[]
```

When tasks are added, the file stores details like this:

```json
[
    {
        "task_number": 1,
        "task_title": "Complete Python assignment",
        "completion_status": false,
        "created_date": "17-06-2026 10:30 AM"
    }
]
```

## Sample Output

```text
=============================================
RAVINDRA BODDU - TO-DO LIST APPLICATION
=============================================
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Search Task
6. Show Task Statistics
7. Exit Program
=============================================
Choose an option from 1 to 7: 1
Enter task title: Complete Python internship task
Task added successfully with ID 1.

Choose an option from 1 to 7: 2

Your Tasks
----------------------------------------------------------------------
Task Number : 1
Title       : Complete Python internship task
Status      : Pending
Created On  : 17-06-2026 10:30 AM
----------------------------------------------------------------------

Choose an option from 1 to 7: 3
Enter task number: 1
Task marked as completed successfully.

Choose an option from 1 to 7: 6

Task Statistics
------------------------------
Total Tasks     : 1
Completed Tasks : 1
Pending Tasks   : 0
```

## GitHub Repository Description

Console-based To-Do List Application built with Python OOP by Ravindra Boddu.
Includes task creation, completion tracking, deletion, search, statistics, input
validation, and JSON file storage.

## LinkedIn Post Content

I am happy to share my Python internship project: a console-based To-Do List
Application built using Object-Oriented Programming.

In this project, I created a `RavindraTask` class to represent each task and a
`BodduTaskManager` class to manage task operations. The application supports
adding tasks, viewing tasks, marking tasks as completed, deleting tasks,
searching tasks, and showing task statistics.

I also implemented JSON file storage so tasks are automatically loaded when the
application starts and saved whenever changes occur. This project helped me
practice Python classes, file handling, input validation, and clean project
structure.

Skills used:
- Python
- OOP
- JSON file handling
- Console application development
- Beginner-friendly software design

## Additional Features to Make This Project Stand Out

1. Add due dates for tasks.
2. Add task priority levels such as High, Medium, and Low.
3. Add edit/update task title feature.
4. Add categories such as Study, Work, Personal, and Internship.
5. Add export option to save completed tasks in a separate report file.
