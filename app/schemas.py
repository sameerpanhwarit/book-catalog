from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

current_year = datetime.now().year

class BookBase(BaseModel):
    """Base fields for a book."""
    title: str
    author: str
    published_year: int = Field(..., ge=1500, le=current_year)
    summary: Optional[str] = None

class BookCreate(BookBase):
    """Fields required to create a book."""
    pass

class BookUpdate(BookBase):
    """Fields allowed for updating a book."""
    pass

class BookRead(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }

