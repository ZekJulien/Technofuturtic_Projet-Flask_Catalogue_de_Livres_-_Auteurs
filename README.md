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

## 🐍 Installation and Usage  

### ℹ️ **Note**  
This project was developed in **Python 3.13**, so it is designed to run on this version.  
It is recommended to use the same version to ensure compatibility and avoid issues related to changes in standard libraries or dependencies.  

### 1️⃣ **Clone the Project**  
Start by retrieving the source code on your machine:  

    git clone https://github.com/ZekJulien/Technofuturtic_Projet-Flask_Catalogue_de_Livres_-_Auteurs

### 2️⃣ **Using a Virtual Environment**
It is recommended to use a virtual environment to isolate project dependencies (run at the root of the cloned repository): 

    py -3 -m venv .venv

### 3️⃣ **Activate the Virtual Environment**
Depending on your OS:
#### Windows  :

    .\.venv\Scripts\activate
#### MacOs/Linux  :

    source .venv/bin/activate


### 4️⃣ **Install Dependencies**
Once the virtual environment is activated, install the required libraries by running:

    pip install -r requirements.txt

### 5️⃣ **Setup your .env**
#### 🔹 Why is this necessary?  
The `.env-example` file contains **template environment variables** that must be copied and configured to ensure the application works correctly.  
This step ensures that Flask and SQLAlchemy have access to the required configurations, like database credentials and secret keys.
#### 📂 Copying the `.env-example` file  
Run the following command in the **root of the project** to create your `.env` file inside `.venv/`:  
#### Windows  :

    copy .env-example .venv\.env

#### MacOs/Linux  :

    cp .env-example .venv/.env

### 🛠️ After copying, open .venv/.env and edit the values ✅


### 6️⃣ **Run the Application** 
After installing dependencies, you can launch the application:

    python run.py



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
📜 README.md                  # Documentation
📜 requirements.txt           # List of dependencies required for the project
📜 exercise.pdf               # Original project instructions and requirements
📜 run.py                     # Script to start the Flask application

