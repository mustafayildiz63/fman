import shutil
from pathlib import Path

def move_path(src:str, dest:str)->None:
    src_path=Path(src)
    dest_path=Path(dest)

    if not src_path.exists():
        raise FileNotFoundError(f"Source path {src} does not exist .")
    if not dest_path.parent.exists():
        raise FileNotFoundError(f"Destination path {dest_path.parent} does not exist .")

    shutil.move(src=src_path,dst=dest_path)
    raise NotImplementedError("move_path() is not yet implemented.")