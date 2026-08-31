import sys
import pytest

def test_cli_cat_command_prints_file_contents(monkeypatch, tmp_path, capsys):
    file_path = tmp_path / "example.txt"
    file_path.write_text("hello from cat\n", encoding="utf-8")

    monkeypatch.setattr(sys, "argv", ["prog", "--cat", str(file_path)])

    from fman import cli

    cli.main()

    captured = capsys.readouterr()
    assert "hello from cat" in captured.out
