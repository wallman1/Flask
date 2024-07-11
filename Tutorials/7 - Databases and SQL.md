# Databases and SQL
### Step 1: Updating `config.py`

In this step, we're configuring the application's settings related to the database using a `Config` class in `config.py`.

#### Code Explanation:

```python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'walkies'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

- **`SECRET_KEY`**: 
  - This is a critical configuration for Flask applications. It's used for cryptographic operations like generating session cookies, signing tokens, etc. It's recommended to set this as an environment variable (`SECRET_KEY`) for security reasons.
  - If not provided via environment variables, it defaults to `'walkies'`.

- **`SQLALCHEMY_DATABASE_URI`**:
  - This specifies the URI for the database that SQLAlchemy will use.
  - `os.environ.get('DATABASE_URL')` checks if there's a `DATABASE_URL` environment variable set (commonly used in deployment environments like Heroku). If set, it uses that URI.
  - If `DATABASE_URL` is not set, it defaults to using a SQLite database (`sqlite:///`) located at `os.path.join(basedir, 'app.db')`. `basedir` is the absolute path to the directory where `config.py` resides.

- **`SQLALCHEMY_TRACK_MODIFICATIONS`**:
  - SQLAlchemy's modification tracking system can be resource-intensive if left enabled unnecessarily. Setting this to `False` disables it, which is typically recommended unless you explicitly need it.

### Step 2: Updating `__init__.py`

Here, we initialize the Flask application (`app`) with the configurations set in `Config`, and set up SQLAlchemy (`db`) and Flask-Migrate (`migrate`) extensions.

#### Code Explanation:

```python
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
```

- **`Flask`**:
  - Creates an instance of the Flask application (`app`).

- **`Config`**:
  - Imports the `Config` class we defined in `config.py`, which contains all the configuration variables we set earlier.

- **`SQLAlchemy`** (`db`):
  - Initializes the SQLAlchemy extension with our Flask application (`app`). This allows us to interact with the database using SQLAlchemy's ORM (Object-Relational Mapping) features.

- **`Flask-Migrate`** (`migrate`):
  - Sets up Flask-Migrate to handle database migrations (`app` and `db`). Migrations are scripts that manage changes to the database schema over time, ensuring that the database evolves along with the application's codebase.

- **`from app import routes, models`**:
  - Imports the `routes` module and `models` module from the `app` package. This assumes you have separate files (`routes.py` for handling routes and `models.py` for defining database models) within your `app` package.

Certainly! Let's consolidate everything into Step 3 and provide a clear overview without requiring the user to create a separate data dictionary. Here's how we can structure it:

### Step 3: Creating User Model and Explanation

#### 3.1 Define User Model

Here is the structure of the `User` model, which represents users in the database:

| Field          | Type         | Description                      |
|----------------|--------------|----------------------------------|
| id             | Integer      | Primary key                      |
| username       | VARCHAR(64)  | Username, indexed and unique     |
| email          | VARCHAR(120) | Email address, indexed and unique|
| password_hash  | VARCHAR(128) | Hashed password                  |

#### Explanation of Primary Key

The `id` field serves as the primary key for the `User` model. A primary key uniquely identifies each record in a database table. Its main purposes are:
- **Uniqueness**: Ensures each record in the table is distinct.
- **Efficiency**: Enables quick retrieval and referencing of specific records.
- **Relationships**: Facilitates establishing relationships (e.g., foreign keys) with other tables.

#### VARCHAR
The VARCHAR file type is similar to a string, but is a variable-length character type. This means that we can specify the number of characters in the string. It is commonly used in databases to help limit the amount of required data in each record.


#### Implementing `models.py`

In your Flask application, create a file named `models.py` within the `app` folder and define the `User` class using SQLAlchemy:

Certainly! Let's integrate the `User` model creation into the tutorial format, starting from Step 3 and providing a summary at the end.

#### 3.2 Define User Model

In `models.py`, create the `User` model using SQLAlchemy:

```python
# models.py
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
```

#### 3.3 Explanation

- **Imports**: 
  - `sqlalchemy as sa`: Alias for the SQLAlchemy library.
  - `sqlalchemy.orm as so`: Alias for SQLAlchemy's ORM features.
  - `from app import db`: Imports the SQLAlchemy `db` instance from the `app` package.

- **User Class**:
  - **Attributes**:
    - `id`: Primary key of type integer (`so.Mapped[int]`), marked as `primary_key=True`.
    - `username`: Username field of type string (`sa.String(64)`), indexed and unique.
    - `email`: Email field of type string (`sa.String(120)`), indexed and unique.
    - `password_hash`: Password hash field of type optional string (`Optional[str]`).

  - **Methods**:
    - `__repr__()`: Returns a string representation of the `User` object, primarily for debugging and logging.


### Summary

1. **Configuring `config.py`**:
   - We defined the `Config` class to store essential configuration variables such as `SECRET_KEY` for security and `SQLALCHEMY_DATABASE_URI` for specifying the database URI (SQLite in this case).

2. **Initializing in `__init__.py`**:
   - We set up the Flask application (`app`), configured it with our `Config` class, and initialized SQLAlchemy (`db`) and Flask-Migrate (`migrate`). SQLAlchemy allows us to work with databases using Python objects, and Flask-Migrate helps manage database migrations.

3. **Creating user model in `models.py`**
    - Created a `User` model in `models.py` using SQLAlchemy, defining fields for `id`, `username`, `email`, and `password_hash`, with `id` serving as the primary key.

This setup prepares your Flask application to interact with an SQLite database, enabling you to define models, create tables, and manage schema changes seamlessly. It also ensures your Flask application is equipped with a structured database model (`User`) and lays the foundation for integrating SQLAlchemy seamlessly. 

