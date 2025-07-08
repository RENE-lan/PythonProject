FILEPATH = "todos.txt"

def get_todos():
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):

    """write the to-do items list in the text file."""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello world")
    print("get_todos")