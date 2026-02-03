Personal Blog Website using Flask

A full-stack personal blog web application built using Flask, featuring user authentication, blog post management, and a commenting system.
This project demonstrates core Flask concepts such as Blueprints, Flask-Login, Flask-WTF, SQLAlchemy, and Flask-Migrate.

🚀 Features

👤 User Registration & Login

🔐 Secure authentication with Flask-Login

✍️ Create, read, and view blog posts

💬 Comment system on posts

🧱 Modular structure using Blueprints

🎨 Responsive UI using Bootstrap

🗄️ SQLite database with SQLAlchemy ORM

🔄 Database migrations using Flask-Migrate

❌ Custom 404 error page

🛠️ Tech Stack

Backend: Flask (Python)

Frontend: HTML, Jinja2, Bootstrap

Database: SQLite

ORM: SQLAlchemy

Forms: Flask-WTF

Authentication: Flask-Login

Migrations: Flask-Migrate

📁 Project Structure
personal_blog/
│── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── comments/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   └── templates/
│       ├── base.html
│       ├── main/
│       ├── auth/
│       ├── posts/
│       └── errors/
│
│── migrations/
│── config.py
│── run.py
│── requirements.txt
│── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-url>
cd personal_blog

2️⃣ Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux / macOS

3️⃣ Install dependencies
pip install -r requirements.txt

🗄️ Database Setup
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

▶️ Run the Application
python run.py


Open in browser:

http://127.0.0.1:5000
