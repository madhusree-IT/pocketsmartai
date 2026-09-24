# 💰 PocketSmart AI

PocketSmart AI is a smart budget and recommendation assistant that helps users record expenses, monitor spending, and receive personalized budget recommendations.

## 🚀 Features

- Add daily expenses
- View recorded expenses
- Calculate total spending
- Get budget recommendations
- REST API using FastAPI
- SQLite database
- Interactive API documentation with Swagger
- Simple web interface

## 🛠️ Technologies

- Python
- FastAPI
- Pydantic
- SQLite
- AioSQLite
- HTML
- CSS
- JavaScript
- uv

## 📁 Project Structure

```text
pocketsmartai/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── expense.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── frontend/
│   └── index.html
│
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md