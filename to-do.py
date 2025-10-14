
# A class for all the important things
class mini:
    tasks = []
    completed_task = []
    remaining_task = []
    deleted_task = []
    no_of_tasks = 0
    no_of_completed_tasks = 0
    no_of_remaining_tasks = 0

class To_do:

    # 1. Function for viewing all task
    @staticmethod
    def view_all_tasks():
        # Printing all available tasks
        print('\nALL TASKS:')
        if not mini.tasks:
            print('\nNo tasks available')
        else:
            for i, j in enumerate(mini.tasks, start=1):
                print(f'{i}. {j}')

        # Printing all the completed tasks
        print('\nCOMPLETED TASKS:')
        if len(mini.completed_task) > 0:
            for i, j in enumerate(mini.completed_task, start=1):
                print(f'{i}. {j}')
        else:
            print('\nNo task is completed yet.')

        # Printing all the remaining tasks
        print('\nREMAINING TASKS: ')
        if len(mini.remaining_task) > 0:
            for i, j in enumerate(mini.remaining_task, start=1):
                print(f'{i}. {j}')
        else:
            print('\nNo task remaining.')

    # 2. Function for adding a task
    @staticmethod
    def add_task():
        while True:
            new_task = input('\nEnter the task you want to add: ').lower()

            if new_task in mini.tasks:
                print(f'\nTask: [{new_task}] already exists!')

            elif new_task == '0':
                print('\nStopped adding tasks.')
                break

            else:
                mini.tasks.append(new_task)  # Adding the task to task list
                mini.remaining_task.append(new_task) # Also adding the task to remaining list
                # When task will be completed it will be removed from this list. Present in line 104.
                mini.no_of_tasks += 1
                print(f'\nTask: [{new_task}] added successfully.')

    # 3. Function for deleting a task
    @staticmethod
    def delete_task():
        while True:
            task_to_delete = input('\nEnter the task you want to delete: ').lower()

            if task_to_delete not in mini.tasks:

                if task_to_delete == '0':
                    print('\nStopped deleting tasks.')
                    break
                else:
                    print(f'\nTask [{task_to_delete}] does not exist.')

            else:
                mini.tasks.remove(task_to_delete)
                mini.remaining_task.remove(task_to_delete)
                mini.deleted_task.append(task_to_delete)
                mini.no_of_tasks -= 1
                print(f'\nDeleted task: [{task_to_delete}]')

    # 4. Function for viewing deleted task
    @staticmethod
    def view_deleted_task():
        print('\nDELETED TASKS:')
        for i, j in enumerate(mini.deleted_task, start=1):
            print(f'{i}: {j}')

    # 5. Function for checking tasks
    @staticmethod
    def check_task():
        while True:
            task_to_check = input('\nEnter the task you have completed: ').lower()

            if task_to_check not in mini.tasks:

                if task_to_check == '0':
                    print('\nStopped checking tasks.')
                    break
                else:
                    print(f'\nTask: [{task_to_check}] does not exist.')

            else:
                mini.completed_task.append(task_to_check)
                mini.remaining_task.remove(task_to_check)
                mini.no_of_completed_tasks += 1
                print(f'\nTask: [{task_to_check}] is completed!')

    # 6. Function for viewing checked tasks
    @staticmethod
    def view_checked_task():
        print('\nCHECKED TASKS:')
        for i, j in enumerate(mini.completed_task, start=1):
            print(f'{i}: {j}')

    # 7. Function for viewing remaining tasks
    @staticmethod
    def view_remaining_task():
        print('\nREMAINING TASKS:')
        while mini.tasks:
            if mini.tasks not in mini.completed_task:
                for i, j in enumerate(mini.tasks, start=1):
                    print(f'{i}: {j}')

    # 8. Function for clearing all tasks
    @staticmethod
    def clear_all_tasks():
        mini.tasks = []
        mini.completed_task = []
        mini.remaining_task = []
        mini.deleted_task = []
        mini.no_of_tasks = 0
        mini.no_of_completed_tasks = 0
        mini.no_of_remaining_tasks = 0
        print('\nAll tasks cleared successfully.')

    # 9. Function for saving all the tasks in a .txt file
    @staticmethod
    def save_all_tasks():
        print('\nYour all tasks are saved in a task.txt file.')
        with open('task.txt', 'w') as f:
            f.write("ALL TASKS:\n")

            if not mini.tasks:
                f.write("No tasks available\n")
            else:
                for i, task in enumerate(mini.tasks, start=1):
                    f.write(f"{i}. {task}\n")

            f.write("\nCOMPLETED TASKS:\n")
            if len(mini.completed_task) > 0:
                for i, task in enumerate(mini.completed_task, start=1):
                    f.write(f"{i}. {task}\n")
            else:
                f.write("No task is completed yet.\n")

            f.write("\nREMAINING TASKS:\n")
            if len(mini.remaining_task) > 0:
                for i, task in enumerate(mini.remaining_task, start=1):
                    f.write(f"{i}. {task}\n")
            else:
                f.write("No task remaining.\n")

def help():
        print("""
──────────────────────────── HELP ────────────────────────────
Here is a quick overview of all available options:

1. View all tasks       → Show all tasks (completed, pending, remaining)
2. Add task             → Add a new task to your list
3. Check task           → Mark a task as completed
4. Delete task          → Remove a task from the list
5. View completed task  → View all completed tasks
6. View remaining task  → View tasks still pending
7. View deleted task    → View all deleted tasks
8. Save all tasks       → Save all active tasks into a .txt file
9. Clear all task       → Clear all active tasks
──────────────────────────────────────────────────────────────
Tip: You can type 0 anytime to stop an action.
──────────────────────────────────────────────────────────────
""")

def intro():
        print("""
───────────────────────────────────────────────────────────────
              ✅ WELCOME TO THE TO-DO MANAGER ✅
───────────────────────────────────────────────────────────────
Your personal mini task tracker that is built purely in Python.
  Add tasks, check them off, delete, and save them to a file.
           Simple, clean, and completely offline.

This project may not change the world...
but hey, at least it changes your schedule. 😎

───────────────────────────────────────────────────────────────
Created by: Izram Khan
Version: 1.0
───────────────────────────────────────────────────────────────
""")

# Loop to run the whole code
intro()

while True:
    print('\n1. Start')
    print('2. Help')
    print('3. Exit')

    user_choice = input('\nEnter your choice (1/2/3): ')

    if user_choice == '1':
        print('\nFunctions are following:')
        print('1. View all tasks')
        print('2. Add task')
        print('3. Check task')
        print('4. Delete task')
        print('5. View completed task')
        print('6. View remaining task')
        print('7. View deleted task')
        print('8. Save all tasks')
        print('9. Clear all task')
        print('10. Exit')

        while True:
            user_choice = input('\nEnter your choice (1-10): ')

            if user_choice == '1':
                To_do.view_all_tasks()

            elif user_choice == '2':
                To_do.add_task()

            elif user_choice == '3':
                To_do.check_task()

            elif user_choice == '4':
                To_do.delete_task()

            elif user_choice == '5':
                To_do.view_checked_task()

            elif user_choice == '6':
                To_do.view_remaining_task()

            elif user_choice == '7':
                To_do.view_deleted_task()

            elif user_choice == '8':
                To_do.save_all_tasks()

            elif user_choice == '9':
                To_do.clear_all_tasks()

            elif user_choice == '10':
                print('\nExiting...')
                break

            else:
                print('\nInvalid choice. Please enter a valid choice.')

    elif user_choice == '2':
        help()

    elif user_choice == '3':
        print('\nExiting...')
        break

    else:
        print('\nInvalid choice. Please enter a valid choice.')

# ____________________________________THE-END____________________________________