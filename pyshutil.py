from os import system


def move(file_path_and_name: str, destiny: str, newfilename: str):
    """
    Move a file from a path to another path with a filename.
    """
    def show_secret():
        """
        Shows a secret from the current function.
        """
        secret = "This function actually reads the file, deletes the file, and puts it right into the destiny directory with the set filename."
        print(f"This is the secret: {secret} Pretty cool, right?")
    with open(file_path_and_name, "r") as file:
        content = file.read()
    system(f"del {file_path_and_name}")
    filename = destiny.join("/").join(newfilename)
    with open(filename, "w") as movedfile:
        movedfile.write(content)


def copy(file_path_and_name: str, destiny: str, newfilename: str):
    """
    Copy a file from a path to another path with a filename.
    """
    def show_secret():
        """
        Shows a secret from the current function.
        """
        secret = "This function actually reads the file, and puts it right into the destiny directory with the set filename."
        print(f"This is the secret: {secret} Pretty cool, right?")
    with open(file_path_and_name, "r") as file:
        content = file.read()
    filename = destiny.join("/").join(newfilename)
    with open(filename, "w") as copiedfile:
        copiedfile.write(content)


print("PyShutil 1.0.0\nHello! This is PyShutil 1.0.0. More updates are coming soon. Let's start!")
