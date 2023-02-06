import pytest


@pytest.fixture  # type: ignore
def my_data():
    """Daten für pytest speichern

    Returns: Liste mit festen werten
    """
    return [1, 2, 3, 4]
