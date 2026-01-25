
import FreeSimpleGUI as fsg

import functions


label = fsg.Text("Type in a to do")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")
todos_list_box=fsg.Listbox(values=functions.get_todos(),key='todos',
                           enable_events=True, size=[40,10])
edit_button=fsg.Button("Edit")

window=fsg.Window("My Simple To-D  no App",
                  layout=[[label],[input_box,add_button],[todos_list_box,edit_button]],
                  font =('Sans',20)
                  )

while True:

    event,values=window.read()
    print(event)
    print(values)

    match event:

        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']

            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            window["todos"].update(values=todos)
            functions.write_todos(todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WINDOW_CLOSED:
            break




window.close()




