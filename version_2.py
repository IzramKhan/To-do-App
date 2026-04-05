# Note: This is version 2.0 of to-do app added after months of original upload
import time

class Messages:
    
    # Success messages
    TASK_ADDED = '\n✅ Task added successfully!'
    TASK_DELETED = '\n✅ Task deleted successfully!'
    TASK_CHECKED = '\n✅ Task marked as completed!'
    TASKS_SAVED = '\n✅ All tasks saved successfully!'
    DATA_RESET = '\n✅ All data cleared successfully!'
    
    # Error messages
    INVALID_CHOICE = '\n❌ Invalid choice. Please enter a valid choice!'
    ALREADY_EXISTS = '\n❌ Task already exists. Please enter a different task.'
    DOESNOT_EXIST = '\n❌ Task does not exist. Please enter a valid task.'
    EMPTY_INPUT = '\n❌ Input cannot be empty. Please enter a valid input!'
    LENGHT_EXCEEDED = '\n❌ Task name cannot exceed 24 characters. Please enter a shorter task name.'

    
tasks = []
completed_tasks = []
remaining_tasks = []
no_of_tasks = 0


def view_all_tasks():
    
    headers = f'{'Tasks':<26} {'Completed'}'
    
    print('-' * 50)
    print(headers)
    print('-' * 50)
    for task in tasks:
        completed = '✅' if task in completed_tasks else '❌'
        print(f'{task.title():<26} {completed}')
    print('-' * 50)
    print(f'Total tasks: {len(tasks)}')
    print(f'Completed: {len(completed_tasks)}')
    print(f'Remaining: {len(remaining_tasks)}')
    print('-' * 50)

def add_task():
    task = input('\nEnter the task you want to add: ').lower().strip(' ')

    if not task:
        print(Messages.EMPTY_INPUT)
    elif task in tasks:
        print(Messages.ALREADY_EXISTS)
    elif len(task) > 24:
        print(Messages.LENGHT_EXCEEDED)
    else:
        tasks.append(task)
        remaining_tasks.append(task)
        print(Messages.TASK_ADDED)

def delete_task():
    task = input('\nEnter the task you want to delete: ').lower().strip(' ')

    if task not in tasks:
        print(Messages.DOESNOT_EXIST)
        return
    tasks.remove(task)
    remaining_tasks.remove(task)
    if task in completed_tasks:
        completed_tasks.remove(task)
    print(Messages.TASK_DELETED)

def check_task():
    
    task = input('\nEnter the task to check: ').lower().strip(' ')

    if task not in tasks:
        print(Messages.DOESNOT_EXIST)
        return 
    completed_tasks.append(task)
    remaining_tasks.remove(task)
    print(Messages.TASK_CHECKED)

def reset_data():
    global tasks, completed_tasks, remaining_tasks, no_of_tasks
    tasks = []
    completed_tasks = []
    remaining_tasks = []
    no_of_tasks = 0
    print(Messages.DATA_RESET)

def save_all_tasks():

    headers = f'{'Tasks':<26} {'Completed'}'
    
    with open('tasks.txt', 'w') as file:
        file.write('-' * 50 + '\n')
        file.write(headers + '\n')
        file.write('-' * 50 + '\n')
        for task in tasks:
            completed = '✅' if task in completed_tasks else '❌'
            file.write(f'{task.title():<26} {completed}\n')
        file.write('-' * 50 + '\n')
        file.write(f'Total tasks: {len(tasks)}\n')
        file.write(f'Completed: {len(completed_tasks)}\n')
        file.write(f'Remaining: {len(remaining_tasks)}\n')
        file.write('-' * 50 + '\n')
    print(Messages.TASKS_SAVED)

def guide():
    print('''
          
----------------------------------------------------------------
       Welcome to the quick guide of the To-Do Manager!

1. Add task            -> Add a new task     
2. Check task          -> Mark a task as completed
3. Delete task         -> Remove a task from the list
4. View all tasks      -> Display all tasks
5. Save all tasks      -> Save all active tasks into a .txt file
6. Clear all tasks     -> Clear all data and start fresh
0. Exit                -> Exit the To-Do Manager

----------------------------------------------------------------
Created by: Izram Khan
Version: 2.0
----------------------------------------------------------------
''')

def animation(test, delay=0.03):
    print('\n')
    for char in test:
        print(char, end='', flush=True)
        time.sleep(delay)
    time.sleep(0.7)   
    
def intro():
    animation(f'||| *** || ** | *  WELCOME TO THE TO-DO MANAGER! * | ** ||| *** |||')

def outro():
    animation(f'||| *** || ** | *  THANK YOU FOR USING THE TO-DO MANAGER! * | ** ||| *** |||')

def main():
    intro()
    guide()
    all_methods = [add_task, check_task, delete_task, view_all_tasks, save_all_tasks, reset_data]

    while True:
        try:
            user_choice = int(input('\nEnter your choice (1 - 6) or 0 to exit: '))
            
            if user_choice == 0:
                outro()
                break
            
            all_methods[user_choice - 1]()
        
        except (IndexError, ValueError):
                print(Messages.INVALID_CHOICE)

if __name__ == '__main__':
    main()

# ______________________________THE-END____________________________________
# Completed on: 30th March 2026
