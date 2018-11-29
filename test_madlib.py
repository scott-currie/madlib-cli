from madlib import *
import pytest

# print_intro


def test_print_intro_exists():
    """Test that print_intro exists"""
    assert print_intro

# get_template_text


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

# parse_template_text


def test_parse_template_text():
    """Test that return value for the given sample text matches the expected."""
    sample_text = 'Here {is} some {sample} text'
    expected = ('Here {} some {} text', ['is', 'sample'])
    assert parse_template_text(sample_text) == expected

# get_user_responses


def test_get_user_responses_exists():
    """Test that function get_user_responses exists."""
    assert get_user_responses

# format_template_text


def test_format_template_text_exists():
    """Test that function format_template_text exists."""
    assert format_template_text


def test_format_template_text_():
    """Test that function format_template_text returns correctly formatted text."""
    text = 'Here {} some {} to {}.'
    subs = ['is', 'text', 'format']
    expected = 'Here is some text to format.'
    assert format_template_text(text, subs) == expected

# print_formatted_text


def test_print_formatted_text_exists():
    """Test that function print_formatted_text exists."""
    assert print_formatted_text


def test_print_formatted_text_no_exceptions():
    """Call print_formatted_text and fail if any exceptions are thrown."""
    test_string = 'Here is some sample text to print.'
    try:
        print_formatted_text(test_string)
    except:
        pytest.fail('Exception occurred in print_formatted_text')

# write_to_file


def test_write_to_file_no_io_error():
    test_filename = 'test.txt'
    test_string = 'Here is some text to write.'
    try:
        write_to_file(test_filename, test_string)
    except IOError:
        pytest.fail('IOError was thrown in write_to_file.')
