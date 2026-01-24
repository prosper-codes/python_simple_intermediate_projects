import time

from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is",now)

while True:
    user_action = input("Type add, view, edit, complete, stop to cancel: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()
        todo_list = get_todos()
        todo_list.append(todo + '\n')
        write_todos(todo_list)

    elif user_action == 'view':
        todo_list = get_todos()
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}-{task.strip()}")

    elif user_action.startswith('edit'):
        try:
            parts = user_action.split()
            if len(parts) == 2 and parts[1].isdigit():
                num = int(parts[1]) - 1
            else:
                num = int(input("Enter number to edit: ")) - 1

            todo_list = get_todos()
            new_todo = input("Enter your new todo: ")
            todo_list[num] = new_todo + '\n'
            write_todos(todo_list)
        except ValueError:
            print("your command is invalid")
            continue

    elif user_action.startswith('complete'):
        parts = user_action.split()
        if len(parts) == 2 and parts[1].isdigit():
            num = int(parts[1]) - 1
        else:
            num = int(input("Enter the number of the todo you completed: ")) - 1

        todo_list = get_todos()
        todo_completed = todo_list.pop(num)
        write_todos(todo_list)

        print(f"Todo '{todo_completed.strip()}' was successfully completed and removed from the list")

    elif user_action == 'stop':
        break

    else:
        print("You entered an invalid option")
