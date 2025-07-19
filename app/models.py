from sqlalchemy import Column, Integer, String
from .database import Base

class Book(Base):
    """SQLAlchemy model for a book in the catalog."""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
    summary = Column(String, nullable=True)
