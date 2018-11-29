from madlib import *
import pytest


def test_print_intro_exists():
    """Test that print_intro exists"""
    assert print_intro


def test_get_template_text_open_file_success():
    """Test that get_template_text doesn't raise FileNotFound exception."""
    filename = 'template.txt'
    try:
        get_template_text(filename)
    except FileNotFoundError:
        pytest.fail('File not found error in get_template_text')

def test_get_template_text_open_file_returns_string():
    """Test that return value returned is a string."""
    filename = 'template.txt'
    assert type(get_template_text(filename)) == str


def test_parse_template_text():
    """Test that return value for the given sample text matches the expected."""
    sample_text = 'Here {is} some {sample} text'
    expected = ('Here {} some {} text', ['is', 'sample'])
    assert parse_template_text(sample_text) == expected
