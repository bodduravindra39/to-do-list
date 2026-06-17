import json
from pathlib import Path

from ravindra_task import RavindraTask


class BodduTaskManager:
    def __init__(self, file_name="ravindra_tasks.json"):
        self.file_path = Path(__file__).parent / file_name
        self.ravindra_tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not self.file_path.exists():
            self.save_tasks()
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as task_file:
                saved_tasks = json.load(task_file)

            self.ravindra_tasks = [
                RavindraTask.from_dictionary(task_data)
                for task_data in saved_tasks
            ]

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Could not read saved tasks. Starting with an empty list.")
            self.ravindra_tasks = []

    def save_tasks(self):
        task_dictionary_list = [
            task.to_dictionary()
            for task in self.ravindra_tasks
        ]

        with self.file_path.open("w", encoding="utf-8") as task_file:
            json.dump(task_dictionary_list, task_file, indent=4)

    def get_next_task_number(self):
        if not self.ravindra_tasks:
            return 1

        highest_task_number = max(
            task.task_number
            for task in self.ravindra_tasks
        )
        return highest_task_number + 1

    def find_task_by_number(self, task_number):
        for task in self.ravindra_tasks:
            if task.task_number == task_number:
                return task

        return None

    def add_task(self, task_title):
        
        if not task_title:
            print("Task title cannot be empty. Please try again.")
            return

        new_task = RavindraTask(
            task_number=self.get_next_task_number(),
            task_title=task_title,
        )
        self.ravindra_tasks.append(new_task)
        self.save_tasks()

        print(f"Task added successfully with ID {new_task.task_number}.")

    def view_tasks(self):
        if not self.ravindra_tasks:
            print("No tasks available. Please add a task first.")
            return

        print("\nYour Tasks")
        print("-" * 70)

        for task in self.ravindra_tasks:
            print(f"Task Number : {task.task_number}")
            print(f"Title       : {task.task_title}")
            print(f"Status      : {task.get_status_text()}")
            print(f"Created On  : {task.created_date}")
            print("-" * 70)

    def mark_task_completed(self, task_number):
        
        selected_task = self.find_task_by_number(task_number)

        if selected_task is None:
            print("Task ID not found. Please enter an existing task number.")
            return

        if selected_task.completion_status:
            print("This task is already marked as completed.")
            return

        selected_task.mark_completed()
        self.save_tasks()
        print("Task marked as completed successfully.")

    def delete_task(self, task_number):
        selected_task = self.find_task_by_number(task_number)

        if selected_task is None:
            print("Task ID not found. Nothing was deleted.")
            return

        self.ravindra_tasks.remove(selected_task)
        self.save_tasks()
        print("Task deleted successfully.")

    def search_task(self, search_word):
        if not search_word:
            print("Search word cannot be empty. Please try again.")
            return

        matching_tasks = [
            task for task in self.ravindra_tasks
            if search_word.lower() in task.task_title.lower()
        ]

        if not matching_tasks:
            print("No matching tasks found.")
            return

        print("\nSearch Results")
        print("-" * 70)

        for task in matching_tasks:
            print(
                f"{task.task_number}. {task.task_title} "
                f"({task.get_status_text()})"
            )

    def show_task_statistics(self):
        total_tasks = len(self.ravindra_tasks)
        completed_tasks = sum(
            task.completion_status
            for task in self.ravindra_tasks
        )
        pending_tasks = total_tasks - completed_tasks

        print("\nTask Statistics")
        print("-" * 30)
        print(f"Total Tasks     : {total_tasks}")
        print(f"Completed Tasks : {completed_tasks}")
        print(f"Pending Tasks   : {pending_tasks}")
