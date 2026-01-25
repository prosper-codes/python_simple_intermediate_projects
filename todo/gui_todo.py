
import FreeSimpleGUI as fsg
import functions
import time
import os

if not os.path.exists("todo_list.txt"):
    with open("todos_list.txt","w") as file:
        pass

fsg.theme("purple")

current_time=fsg.Text(key="clock")
label = fsg.Text("Type in a to do")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")
todos_list_box=fsg.Listbox(values=functions.get_todos(),key='todos',
                           enable_events=True, size=[40,10])
edit_button=fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")


window=fsg.Window("My Simple To-D  no App",
                  layout=[[current_time],[label],
                          [input_box,add_button],
                          [todos_list_box,edit_button,complete_button],
                          [exit_button]
                          ],
                  font =('Sans',20)
                  )

while True:

    event,values=window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))


    match event:

        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']

                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                window["todos"].update(values=todos)
                functions.write_todos(todos)

            except IndexError:
                fsg.popup("PLEASE SELECT AND ITEM FIRST :)" ,font=("Sans",16))
        case "Complete":
            try:
                todo_to_complete=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError:
                fsg.popup("PLEASE SELECT AND ITEM FIRST :)", font=("Sans", 16))


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WINDOW_CLOSED:
            break




window.close()




