# Book Catalog API

A simple, well-structured RESTful API for managing a catalog of books, built with FastAPI, SQLAlchemy, and SQLite.

## Features
- Add, update, delete, and list books
- Retrieve details for a single book
- Data validation with Pydantic
- Simple SQLite database (easy to swap for PostgreSQL, etc.)
- Well-tested with pytest

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd book-catalog
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install fastapi sqlalchemy uvicorn pydantic pytest
   ```

## Usage
1. **Start the API server:**
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Access the interactive API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## API Endpoints
- `GET /books/` — List all books
- `GET /books/{book_id}` — Get details for a specific book
- `POST /books/` — Add a new book
- `PUT /books/{book_id}` — Update an existing book
- `DELETE /books/{book_id}` — Delete a book

## Running Tests
Run all tests with:
```bash
pytest
```

