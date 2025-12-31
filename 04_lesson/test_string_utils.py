import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    (" python", "python"),
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ])
def test_trim_negative(input_str, expected):
        assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol", [
    ("SkyPro", "S"),
    ("hello world", "o"),
    ("python", "n"),
])
def test_contains_positive(input_str, input_symbol):
    assert string_utils.contains (input_str, input_symbol) == True

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("SkyPro", "u"),
    ("123", "u"),
    ("", "n"),
])
def test_contains_negative(input_str, input_symbol):
    assert string_utils.contains (input_str, input_symbol) == False

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("hello world", "o", "hell wrld"),
    ("python", "n", "pytho"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("SkyPro", "u", "SkyPro"),
    ("hello world", "u", "hello world"),
    ("", "n", ""),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected