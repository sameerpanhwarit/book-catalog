from app import crud, models, schemas
from app.database import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)
db = SessionLocal()

def test_create_and_get_book():
    """Test creating a book and retrieving it from the database."""
    book = schemas.BookCreate(title="Sample", author="Author", published_year=2000)
    created = crud.create_book(db, book)
    fetched = crud.get_book(db, created.id)
    assert fetched.id == created.id
    assert fetched.title == "Sample"
    assert fetched.author == "Author"
    assert fetched.published_year == 2000
