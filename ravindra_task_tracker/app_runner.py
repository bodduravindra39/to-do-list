
from boddu_task_manager import BodduTaskManager


def show_main_menu():
    print("\n" + "=" * 45)
    print("RAVINDRA BODDU - TO-DO LIST APPLICATION")
    print("=" * 45)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Show Task Statistics")
    print("7. Exit Program")
    print("=" * 45)


def ask_for_task_number():
    
    task_number_text = input("Enter task number: ").strip()

    if not task_number_text.isdigit():
        print("Please enter a valid numeric task number.")
        return None

    return int(task_number_text)


def run_application():
    task_manager = BodduTaskManager()

    while True:
        show_main_menu()
        user_choice = input("Choose an option from 1 to 7: ").strip()

        if user_choice == "1":
            task_title = input("Enter task title: ").strip()
            task_manager.add_task(task_title)

        elif user_choice == "2":
            task_manager.view_tasks()

        elif user_choice == "3":
            task_number = ask_for_task_number()

            if task_number is not None:
                task_manager.mark_task_completed(task_number)

        elif user_choice == "4":
            task_number = ask_for_task_number()

            if task_number is not None:
                task_manager.delete_task(task_number)

        elif user_choice == "5":
            search_word = input("Enter word to search: ").strip()
            task_manager.search_task(search_word)

        elif user_choice == "6":
            task_manager.show_task_statistics()

        elif user_choice == "7":
            print("Thank you for using Ravindra's To-Do List Application.")
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    run_application()
