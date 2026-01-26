import streamlit as sl
import functions


import streamlit as sl
import  functions


def add_todo():
    todo = sl.session_state["new_todo"].strip() + "\n"  # remove extra spaces/newlines
    if todo:  # only add if not empty
        todos_list.append(todo)
        functions.write_todos(todos_list)
    sl.session_state["new_todo"] = ""  # clear the input field

todos_list= functions.get_todos()

sl.title("📝 Prosper Todo App 📝")
sl.subheader("Stay productive")
sl.write("This app helps you manage your tasks efficiently.")


for index,todo in enumerate(todos_list):
    checkbox = sl.checkbox(todo, key=f"{index}_{todo}")
    if checkbox:
        todos_list.pop(index)
        functions.write_todos(todos_list)
        del sl.session_state[f"{index}_{todo}"]
        sl.rerun()

sl.text_input(label="Enter a todo here", placeholder="Add a new todo ...:)",
              on_change=add_todo,key="new_todo")





