from pathlib import Path
import pytest




@pytest.fixture
def source_path(tmp_path):
    src_dir=Path(tmp_path / "src_dir")
    src_dir.mkdir()
    src_file=src_dir / "source.txt"
    src_file.write_text("I am learning pytest when creating a simple cli project")

    return src_file