import pytest
from pathlib import Path
import fman.commands.ls as ls

def test_list_dir(tmp_path):


    directory=Path(tmp_path/"example_dir")

    directory.mkdir()

    file1=Path(tmp_path/"file1.txt")
    file1.write_text("Hello")

    result=ls.list_dir(str(tmp_path))

    assert len(result) == 2
    assert result[0]["name"] == "example_dir"
    assert result[0]["type"] == "Dir"
    assert result[1]["name"] == "file1.txt"
    assert result[1]["size"] == 5


     
















"""import pytest
from pathlib import Path
@pytest.mark.parametrize(

    "filename , content",
    [
        ("file1.txt","Hello from 1"),
        ("file2.txt","Hello from 2"),
        ("file3.txt","Hello from 3")
    ]
)

def test_for_learning(tmp_path,filename,content):
    file=Path(tmp_path / filename)
    file.write_text(content)

    assert file.exists()
    assert file.read_text() == content"""

