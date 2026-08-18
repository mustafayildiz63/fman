import shutil
from pathlib import Path 

def removePath(path:str,force:bool=False)->None:
    p=Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Path {path} does not exist .")

    if not force:
        yes_or_no=input(f"Are you sure you want to delete {path}? (y/n):")
        if yes_or_no.lower() !="y":

            print("Delete operation cancelled.")
            return
        
        if yes_or_no.lower() == "y":

            if p.is_file():
                p.unlink()
            elif p.is_dir():
                shutil.rmtree(p)
