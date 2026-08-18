from pathlib import Path


def make_dir(path: str) -> None:
    dir_path=Path(path).resolve()
    if dir_path.exists():
        raise ValueError(f"{path} already exists")

    dir_path.mkdir(parents=True, exist_ok=False)
    