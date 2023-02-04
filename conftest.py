import pytest


@pytest.fixtures()
def my_data():
    return [1, 2, 3, 4]
