import shutil
from pathlib import Path



def copy_path(src:str,dest:str)->None:

    src_path=Path(src)
    dest_path=Path(dest)


    if not src_path.exists():
        raise FileNotFoundError(f"There is no directory {src}")
    if not dest_path.parent.exists():
            raise FileNotFoundError(f"There is no directory {dest_path.parent}")

    if src_path.is_file():
        shutil.copy2(src=src_path,dst=dest_path)
    elif src_path.is_dir():
        shutil.copytree(src=src_path,dst=dest_path)
    else:
         raise ValueError(f"Source path {src} is neither a file nor a directory.")

    raise NotImplementedError("copy_path() is not yet implemented.")
