"""
Purpose of cat command is to display the contents of a file in the terminal. It can be used to quickly view the contents of text files without opening them in a text editor. The command can also be used to concatenate multiple files and display their combined contents.
"""
from pathlib import Path

def cat_file(file_path:Path):
    """
    Display the contents of a file in the terminal.

    Args:
        file_path (Path): The path to the file to be displayed.
    """
    filePath = file_path.resolve()
    if not filePath.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return

    if not filePath.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return

    try:
        with open(filePath, 'r', encoding="utf-8") as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")