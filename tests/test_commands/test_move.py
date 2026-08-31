import pytest
from pathlib import Path
from fman.commands import move
from conftest import source_path



def test_move_path_func(source_path,tmp_path):

    
    dest_dir=Path(tmp_path/"dest")    
    dest_dir.mkdir()


    dest_file=dest_dir/"example.txt"
    
    
    move.move_path(src=str(source_path),dest=str(dest_file))

    assert not source_path.exists()

    assert dest_file.exists()

    assert dest_file.read_text() == "I am learning pytest when creating a simple cli project"


  





