import pytest
from fman.commands import find

@pytest.mark.parametrize(
        "name,type,content",
        [
            ("file1.txt","file","Hello"),
            ("file2.txt","file","I am learning how to test my code. "),
            ("file3.txt","file","Hello"),
           ("Example_dir","directory",None)
        ]

)

def test_find_path_func(tmp_path,name,type,content):

    if type == "directory":
        exaple_dir=tmp_path/name
        exaple_dir.mkdir()
    elif type == "file":
        exaple_file=tmp_path/name
        exaple_file.write_text(content)

    result=find.find_path(start_path=str(tmp_path),name_pattern=name)

    assert len(result) == 1 
    assert result[0]["name"] == name
    assert result[0]["type"] == type


 
    