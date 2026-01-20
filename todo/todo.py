while True:
    user_action = input("Type add, view, edit, complete, stop to cancel: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        with open('todos_list.txt', 'r') as file:
            todo_list = file.readlines()

        todo_list.append(todo + '\n')

        with open('todos_list.txt', 'w') as file:
            file.writelines(todo_list)

    elif user_action == 'view':
        with open("todos_list.txt", 'r') as file:
            todo_list = file.readlines()

        for index, task in enumerate(todo_list):
            print(f"{index + 1}-{task.strip()}")

    elif user_action.startswith('edit'):
        # Try to get the number directly from the input
        parts = user_action.split()
        if len(parts) == 2 and parts[1].isdigit():
            num = int(parts[1]) - 1
        else:
            num = int(input("Enter number to edit: ")) - 1

        with open("todos_list.txt", 'r') as file:
            todo_list = file.readlines()

        new_todo = input("Enter your new todo: ")
        todo_list[num] = new_todo + '\n'

        with open("todos_list.txt", 'w') as file:
            file.writelines(todo_list)

    elif user_action.startswith('complete'):
        parts = user_action.split()
        if len(parts) == 2 and parts[1].isdigit():
            num = int(parts[1])
        else:
            num = int(input("Enter the number of the todo you completed: "))

        with open("todos_list.txt", 'r') as file:
            todo_list = file.readlines()

        todo_completed = todo_list[num - 1].strip()
        todo_list.pop(num - 1)

        with open("todos_list.txt", 'w') as file:
            file.writelines(todo_list)

        print(f"Todo '{todo_completed}' was successfully completed and removed from the list")

    elif user_action == 'stop':
        break

    else:
        print("You entered an invalid option")
