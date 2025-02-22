# Books API 

## Overview
This Django REST Framework (DRF) API allows users to manage a list of books. The API includes CRUD operations with validation for unique ISBN and past publication dates.
## Features
- **Book Model:** Stores books with title, author, publication date, ISBN, and summary.
- **API Endpoints:**
  - `GET /api/books/` - Retrieve all books.
  - `POST /api/books/` - Create a new book.
  - `GET /api/books/{id}/` - Retrieve a book by ID.
  - `PUT /api/books/{id}/` - Update a book by ID.
  - `DELETE /api/books/{id}/` - Delete a book by ID.
- **Validation:**
  - ISBN must be unique and either 10 or 13 digits.
  - Publication date must be in the past.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Ericmuturimwangi/Book_manager.git
   cd interview

