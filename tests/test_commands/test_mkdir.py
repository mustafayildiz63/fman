import pytest 
from pathlib import Path
from fman.commands import mkdir

def test_mkdir_creates_directory(tmp_path):
    directory=Path(tmp_path / "test_directory")

    mkdir.make_dir(str(directory))

    assert directory.exists()
    assert directory.is_dir() 

