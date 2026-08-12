"""
commands.py — the actual file-manipulation logic.
 
Fill these in one at a time. Use pathlib.Path, not raw string paths.
Each function should raise a clear exception on failure — let cli.py
decide how to display errors to the user.
"""

from importlib.resources import path
from pathlib import Path
import shutil

def list_dir(path:str)->None:
     """
    List the contents of `path`.
 
    TODO:
    - Convert `path` to a Path object.
    - Check it exists and is a directory (raise if not).
    - Iterate over entries with .iterdir().
    - Print name, type (file/dir), and size for each entry.
    Hint: Path.stat().st_size gives size in bytes.
    """    



    # - Convert `path` to a Path object.
     p= Path(path)
     # - Check it exists and is a directory (raise if not).
     if not p.exists():
         raise FileNotFoundError(f"Path {path} does not exist.")
     if not p.is_dir():
         raise NotADirectoryError(f"Path {path} is not a directory.")
     #- Iterate over entries with .iterdir().
     for entry in p.iterdir():
         entry_type = "Directory" if entry.is_dir() else "File"

         #Path.stat().st_size gives size in bytes.
         entry_size = entry.stat().st_size
         print(f"{entry.name} - {entry_type} - {entry_size} bytes")
     raise NotImplementedError("list_dir() is not yet implemented.")

def copy_path(src:str, dest:str)->None:
  """
    Copy `source` to `dest`. Should work for both files and directories.
 
    TODO:
    - Use shutil.copy2() for files (preserves metadata).
    - Use shutil.copytree() for directories.
    - Decide: what happens if dest already exists?
    """

  src_path=Path(src)
  dest_path=Path(dest)

  if not src_path.exists():
      raise FileNotFoundError(f"Source path {src} does not exist.")
  if not dest_path.parent.exists():
      raise FileNotFoundError(f"Destination directory {dest_path.parent} does not exist.")

  if src_path.is_file():
      shutil.copy2(src_path, dest_path)
  elif src_path.is_dir():
      shutil.copytree(src_path, dest_path)
  else:
      raise ValueError(f"Source path {src} is neither a file nor a directory.")

  raise NotImplementedError("copy_path() is not yet implemented.")

def move_path(src:str, dest:str)->None:

    src_path=Path(src)
    dest_path=Path(dest)

    if not src_path.exists():
        raise FileNotFoundError(f"Source path {src} does not exist.")
    if not dest_path.parent.exists():
        raise FileNotFoundError(f"Destination directory {dest_path.parent} does not exist.")

    
    shutil.move(src=src_path,dest=dest_path)


    raise NotImplementedError("move_path() is not yet implemented.")

def delete_path(path:str,force:bool=False)->None:
    delete_path=Path(path)
    if not delete_path.exists():
        raise FileNotFoundError(f"Path {path} does not exist.")
    if not force:
        yes_no=input(f"Are you sure you want to delete {path}? (y/n): ")
        if yes_no.lower() != "y":
            print("Delete operation cancelled.")
            return
        else:
            if delete_path.is_file():
                Path.unlink()
            if delete_path.is_dir():
                shutil.rmtree()

def rename_path(path:str,new_name:str)->None:

    rename_path=Path(path)

    if not rename_path.exists():
        raise FileNotFoundError(f"Source directory {path} does not exist ." )


    Path.rename(rename_path,rename_path.parent/new_name)

    raise NotImplementedError("rename_path() is not yet implemented.")

def create_dir(path:str)->None:

    new_path=Path(path)

    if  new_path.exists():
        raise shutil.Error(f"Directory {path} already exists.")
    
    new_path.mkdir(parents=True, exist_ok=False)

    raise NotImplementedError("create_dir is not implemented yet ")


def create_file(path:str)->None:
    """Create a new empty file at `path` (like the Unix `touch` command)
    #TODO:
        - Convert `path` to a Path object.
        - Check if the parent directory exists; if not, create it.
        - Check if the file already exists; if so, raise an exception.
        - Use Path.touch() to create the file.

    """

    new_path=Path(path)
    parent_path=new_path.parent
    if not parent_path.exists():
        print(f"Parent directory {parent_path} does not exist . Creating it ..." )
        parent_path.mkdir(parents=True,exist_ok=True)

    if new_path.exists():
        raise shutil.Error(f"File {path} is already exist.")

    Path.touch(exist_ok=False)
    print(f"✅ Success: File created at '{new_path}'")

    raise NotImplementedError("create_file is not implemented yet ")       