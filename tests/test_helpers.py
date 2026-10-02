# Practice tests for daily exercises
import sys
sys.path.insert(0, '..')

import pytest
from utils.helpers import print_header, print_exercise, get_input, confirm


def test_print_header(capsys):
    print_header("Test")
    captured = capsys.readouterr()
    assert "Test" in captured.out
    assert "=" in captured.out


def test_print_exercise(capsys):
    print_exercise(1, "Variables")
    captured = capsys.readouterr()
    assert "Exercise 1" in captured.out
    assert "Variables" in captured.out


def test_get_input_str(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert get_input("Prompt: ") == "hello"


def test_get_input_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "42")
    assert get_input("Prompt: ", int) == 42


def test_get_input_default(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert get_input("Prompt: ", default="default") == "default"


def test_confirm_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert confirm("Continue?") is True


def test_confirm_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert confirm("Continue?") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])