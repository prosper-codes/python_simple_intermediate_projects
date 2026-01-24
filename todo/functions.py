FILEPATH ="todos_list.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todo_list_local = file.readlines()
    return todo_list_local

def write_todos(todos_argu, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_argu)


if __name__ == "__main__":
    print("hello")
    print(get_todos())


