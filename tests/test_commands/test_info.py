import pytest
from fman.commands import info
from conftest import source_path

def test_path_info_func(source_path):


    result=info.path_info(str(source_path))

    

    assert result["name"] == "source.txt"
    assert result["type"] == "file"
    assert result["exists"] == source_path.exists()
    assert result["absolute_path"] == str(source_path.absolute())
    

    