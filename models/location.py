from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    city: str = "sonsbeck"
    state: Optional[str] = None
    country = "DE"
