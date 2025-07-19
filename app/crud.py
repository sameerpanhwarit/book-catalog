from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session):
    """Return all books in the database."""
    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):
    """Return a single book by ID, or None if not found."""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    """Create a new book."""
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    """Update an existing book. Returns the updated book or None if not found."""
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    """Delete a book by ID. Returns the deleted book or None if not found."""
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
