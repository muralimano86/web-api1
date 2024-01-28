FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and retrun the
    items as list"""
    with open(filepath, 'r') as file_local:
        filecontent = file_local.readlines()
    return filecontent

def write_todos(filecontent, filepath=FILEPATH):
    """ Write the todo items list into a file """
    with open(filepath, "w") as file_local:
        file_local.writelines(filecontent)

if __name__ == "__main__":
    print("Hello")