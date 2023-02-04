from unittest import mock

import pytest

from conftest import my_data
from main import (
    ProductionClass,
    add,
    devide,
    is_not_flat,
    play_random,
    printme,
    sum_list,
)


@pytest.mark.parametrize("input1, input2, expected", [(2, 3, 5), (1, 4, 5)])
def test_add(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected


def test_devide():
    result = devide(8, 2)
    assert result == 4
    with pytest.raises(ZeroDivisionError):
        10 / 0


@mock.patch("main.randint", return_value=7)
def test_play_random(mocked_randint):
    result = play_random()
    assert result == "größer"


def test_produktionclass():
    instanz = ProductionClass()
    instanz.something = mock.MagicMock()
    instanz.method()
    instanz.something.assert_called_once_with(1, 2, 3)


def test_printme(capsys):
    printme()
    captures = capsys.readouterr()
    assert captures.out == "Hallo\n"


def test_is_not_flat(my_data):
    assert is_not_flat(my_data) == False


def test_sum_list(my_data):
    assert sum_list(my_data) == 10


##


# client = TestClient(app)


# def test_root():
#    response = client.get("/")
#   assert response.status_code == 200
#   assert response.json()["message"] == "Hello World"


# def test_say_hello():
#   response = client.get("/hello/User")
#  result = response.json()
# assert response.status_code == 200
# assert result["message"] == "Hello User"
