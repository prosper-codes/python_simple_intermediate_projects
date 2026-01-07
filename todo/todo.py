
todo_list=[]


while True:
    user_action=input("Type add, view, edit, complete, stop type stop to cancel: ").strip()

    match user_action:

        case 'add':
            todo=input("Enter a todo: ")
            todo_list.append(todo)

        case 'view':

            for index,task in enumerate(todo_list):
                index=index+1
                print(f"{index}-{task}")

        case 'edit':

            num = int(input("enter number to edit: "))-1
            new_todo=input("enter new todo: ")
            todo_list[num]=new_todo
        case 'complete':
            num = int(input("enter the number of the to do you completed"))
            todo_list.pop(num-1)

        case 'stop':
            break


        case whatever:
            print("you entered an invalid option")

