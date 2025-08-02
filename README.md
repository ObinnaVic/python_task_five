# FastAPI Applications Collection

This repository contains 5 simple FastAPI applications demonstrating different concepts and functionalities.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

Install dependencies:
```bash
pip install fastapi uvicorn
```

## Applications Overview

### 1. Student Scores Manager
**File:** `student_scores_api.py`

Manages student scores and automatically calculates grades.

**Features:**
- Student class with name, subject_scores, average, and grade
- Automatic grade calculation (A: 90+, B: 80+, C: 70+, D: 60+, F: <60)
- JSON file persistence

**Endpoints:**
- `POST /students/` - Create a new student
- `GET /students/{name}` - Get student by name
- `GET /students/` - Get all students

---

### 2. Product Cart API
**Files:** `main.py`, `cart.py`

E-commerce API for browsing products and managing shopping cart.

**Features:**
- Product catalog with ID, name, and price
- Shopping cart with quantity management
- Cart persistence in JSON file
- Math module for price rounding

**Endpoints:**
- `GET /products/` - Browse all products
- `POST /cart/add?product_id=1&qty=2` - Add items to cart
- `GET /cart/checkout` - View cart and total

---

### 3. Job Applications Manager
**Files:** `main.py`, `file_handler.py`

Manages job applications with search functionality.

**Features:**
- JobApplication class with name, company, position, status
- Search by application status
- File handling module for JSON persistence
- Error handling with try-except blocks

**Endpoints:**
- `POST /applications/` - Create new application
- `GET /applications/` - Get all applications
- `GET /applications/search?status=pending` - Search by status

---

### 4. Notes App API
**File:** `notes_api.py`

File system-based notes management where each note is saved as a .txt file.

**Features:**
- Each note saved as individual .txt file
- CRUD operations for notes
- OS module for file operations
- Safe filename generation

**Endpoints:**
- `POST /notes/` - Create new note
- `GET /notes/{title}` - Read note by title
- `POST /notes/{title}` - Update existing note
- `DELETE /notes/{title}` - Delete note

---

### 5. Simple Contact API
**File:** `contact_api.py`

Contact management system demonstrating path and query parameters.

**Features:**
- Contact model with name, phone, email
- In-memory dictionary storage
- Path parameters for specific operations
- Query parameters for searching
- Graceful error handling

**Endpoints:**
- `POST /contacts/` - Create new contact
- `GET /contacts/?name=John` - Get contacts (all or search by name)
- `POST /contacts/{name}` - Update contact by name
- `DELETE /contacts/{name}` - Delete contact by name

## Running the Applications

1. Choose an application
2. Save the required files in a directory
3. Navigate to the directory
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Access the API at `http://localhost:8000`
6. View interactive documentation at `http://localhost:8000/docs`
