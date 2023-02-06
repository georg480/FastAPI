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
    """für pytest feste Werte zum Testen
    Return: Richtig/ Falsch
    -------
    """
    result = add(input1, input2)
    assert result == expected


def test_devide():
    """für pytest teilen

    Return: Richtig / Falsch
    -------
    """
    result = devide(8, 2)
    assert result == 4
    with pytest.raises(ZeroDivisionError):
        10 / 0


@mock.patch("main.randint", return_value=7)
def test_play_random(mocked_randint):
    """für pytest play Random

    Return: Richtig/ Falsch
    -------
    object
    """
    result = play_random()
    assert result == "größer"


def test_produktionclass():
    """für pytest pacht eine Methode

    Return: Richtig/ Falsch
    -------
    object
    """
    instanz = ProductionClass()
    instanz.something = mock.MagicMock()
    instanz.method()
    instanz.something.assert_called_once_with(1, 2, 3)


def test_printme(capsys):
    """für pytest wird das print Ergenis ausgewertet

    Return: Richtig / Falsch
    -------
    object
    """
    printme()
    captures = capsys.readouterr()
    assert captures.out == "Hallo\n"


def test_is_not_flat(my_data):
    """prüft die Testdaten aus der my_Data Klasse
    Return Richtig/ Falsch
    -------
    object
    """
    assert is_not_flat(my_data) == False


def test_sum_list(my_data):
    """Berechntet die Summe der My Data kllasee und vergliecht das Ergebnis
    Returns Richtig / Falsch
    -------
    object
    """
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
