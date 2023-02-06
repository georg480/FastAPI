from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    """erstellt eine Lokation

    Parameters
    ----------
    msg : str
        TEST Ausgabe
    code : :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg : str
        Human Test
    code : int
        Numeric error code.

    """
    city: str = "sonsbeck"
    state: Optional[str] = None
    country = "DE"
