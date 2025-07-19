"""
Main application entry point for the Book Catalog API.
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Catalog API")

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/", response_model=List[schemas.BookRead])
def list_books(db: Session = Depends(get_db)):
    """Retrieve all books from the catalog."""
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Retrieve a single book by its ID."""
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/", response_model=schemas.BookRead, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the catalog."""
    return crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book's details."""
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}", response_model=schemas.BookRead)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Remove a book from the catalog."""
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted
