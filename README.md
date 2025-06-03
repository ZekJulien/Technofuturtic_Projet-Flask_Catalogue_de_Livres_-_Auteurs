# [Technofuturtic] Project – Book & Author Catalog

## 📌 Project Objective
This project aims to develop a web application using Flask based on the **Model-View-Template (MVT)** architecture. The application will manage a catalog of books, their authors, and categories. The key objectives include:
- Handling relationships between database entities.
- Dynamically displaying data with Jinja2.
- Styling the UI using DaisyUI.
- **No authentication is required**.

## ⚙️ Technologies Used
- **Flask**
- **SQLAlchemy** for database management
- **Jinja2** for templating
- **Flask-WTF** for form handling (protected by CSRF)
- **DaisyUI** for styling

## 🛠️ Features & Requirements
Each entity must have complete CRUD functionality:
- **Create**
- **Read**
- **Update**
- **Delete**

### 🧭 Routes Implementation:
The Flask application should support navigation through:
- 📚 **Book List** (includes author and categories)
- 📖 **Book Details**
- 🖊️ **Author List** (shows the number of books written)
- 🏷️ **Category List** (shows books associated with each category)

## 🎨 Frontend Requirements:
- HTML pages must be dynamically structured using **Jinja2 templates**.
- Form inputs should use **Flask-WTF** and be protected by **CSRF**.
- The design should be **clean & structured**, using **DaisyUI** for styling.

## 🌟 Bonus Features (Optional)
To enhance usability, you may implement:
- 🔍 **Search bar** for books (by title or genre).
- 🏷️ **Category filter**.
- 📄 **Pagination** for book lists.
- 📊 **Statistics** (e.g., number of books per author, average books per genre).
- 🖼️ **Book cover image** (static visual representation).

## 📁 Project Structure
```bash
📦 app
 ┃ 📂 database/               # Manages connection and session
 ┃ ┗ 📜 database.py
 ┣ 📂 static                  # CSS, JS, images
 ┣ 📂 templates               # HTML templates (Jinja2)
 ┣ 📂 models                  # SQLAlchemy models (Entities)
 ┃ ┣ 📜 name.py               # name entity
 ┣ 📂 repositories            # Database access layer
 ┃ ┗ 📜 name_repository.py    # CRUD operations via SQLAlchemy
 ┣ 📂 services                # Business logic
 ┃ ┗ 📜 name_service.py       # Handles book-related operations
 ┣ 📂 forms                   # Flask-WTF forms for handling user input
 ┣ 📂 routes                  # Flask routes (Controllers)
 ┃ ┗ 📜 routes.py             # Application routes
 ┣ 📜 app.py                  # Main application entry point
 ┣ 📜 config.py               # Global settings (Database, environment variables)
📜 README.md                  # Documentation
📜 requirements.txt           # List of dependencies required for the project
📜 exercise.pdf               # Original project instructions and requirements
📜 run.py                     # Script to start the Flask application