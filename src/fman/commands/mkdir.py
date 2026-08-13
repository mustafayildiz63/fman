import shutil
from pathlib import Path


def make_dir(path:str)->None:
    p=Path(path)

    if p.exists():
        raise ValueError(f"{path} already exist")

    p.mkdir(parents=True,exist_ok=False)
    raise NotImplementedError("create_dir is not implemented yet ")