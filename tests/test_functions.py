from github_actions_python import example
import pytest




def test_my_add_function():
    result = example.my_add_function(5, 10)
    assert result == 15


def test_my_throw_function_not_throw():
    result = example.my_throw_function(5)
    assert result == 10


def test_my_throw_function_throw():
    with pytest.raises(ValueError):
        example.my_throw_function(15)
