"""Slide 17 — pytest tests."""
import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

_path = Path(__file__).parent / "17_unit_testing.py"
_spec = importlib.util.spec_from_file_location("unit_testing", _path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

add = _mod.add
double = _mod.double


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_double():
    assert double(10) == 20


@patch("builtins.print")
def test_mock_print(mock_print):
    print("hello")
    mock_print.assert_called_once_with("hello")
