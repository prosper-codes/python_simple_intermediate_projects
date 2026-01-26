
import streamlit as sl
import  functions


def add_todo():
    todo = sl.session_state["new_todo"] +"\n"
    todos_list.append(todo)
    functions.write_todos(todos_list)

todos_list= functions.get_todos()

sl.title("My Todo App")
sl.subheader("This is my Todo App")
sl.write("This app increases your productivity")

for todo in todos_list:
    sl.checkbox(todo)


sl.text_input(label="Enter a todo here", placeholder="Add a new tod0 ...:)",
              on_change=add_todo,key="new_todo")


sl.session_state