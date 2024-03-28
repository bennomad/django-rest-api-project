# Django REST API Project

Simple Django REST API for an `Item` model, demonstrating basic CRUD operations.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django
- Django Rest Framework

### Installation

1. Clone the repository:
   - Run: `git clone https://github.com/bennomad/django-rest-api-project.git`
   - Then cd into the directory: `cd django-rest-api-project`

2. Set up and activate a virtual environment:
- Windows: `python -m venv venv && venv\Scripts\activate`
- Unix/MacOS: `python3 -m venv venv && source venv/bin/activate`

3. Install dependencies:
`pip install django djangorestframework`
4. Apply migrations:
`python3 manage.py migrate`
5. Run the server:
`python3 manage.py runserver`

Access the application at `http://127.0.0.1:8000/api/items/`.

## API Endpoints

- **List all items**: `GET /api/items/`
- **Retrieve a specific item**: `GET /api/items/<id>/`
- **Filter items by name**: `GET /api/items/?name=<name>`

