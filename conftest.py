import pytest


@pytest.fixture  # type: ignore
def my_data():
    return [1, 2, 3, 4]
