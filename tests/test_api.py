from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book_api():
    """Test creating a new book via the API."""
    response = client.post("/books/", json={
        "title": "Test Book",
        "author": "Tester",
        "published_year": 2020
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Tester"
    assert data["published_year"] == 2020

def test_get_books_api():
    """Test retrieving the list of books via the API."""
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
