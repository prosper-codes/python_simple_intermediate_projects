while True:
    user_action=input("Type add, view, edit, complete, stop to cancel: ").strip()

    match user_action:

        case 'add':
            todo=input("Enter a todo: ")+"\n"

            with open('todos_list.txt','r') as file:
                todo_list=file.readlines()

            todo_list.append(todo)

            with open('todos_list.txt','w') as file:
                file.writelines(todo_list)


        case 'view':
            
            with open("todos_list.txt", 'r') as file:
                todo_list = file.readlines()

            for index,task in enumerate(todo_list):
                 task = task.strip('\n')
                 index=index+1
                 print(f"{index}-{task}")

        case 'edit':
             num = int(input("enter number to edit: "))-1

             with open("todos_list.txt", 'r') as file:
                 todo_list = file.readlines()

             new_todo =input("Enter your new todo: ")
             todo_list[num]=new_todo + '\n'

             with open("todos_list.txt", 'w') as file:
                 file.writelines(todo_list)




        case 'complete':

            num = int(input("enter the number of the to do you completed"))

            with open("todos_list.txt",'r') as file:
                todo_list = file.readlines()
            todo_completed = todo_list[num-1].strip('\n')
            todo_list.pop(num-1)

            with open("todos_list.txt", 'w') as file:
                file.writelines(todo_list)

            print( f"Todo {todo_completed} was successfully completed and removed from the list")

        case 'stop':
            break


        case whatever:
            print("you entered an invalid option")

