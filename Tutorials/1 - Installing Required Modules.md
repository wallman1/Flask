# Installing Required Modules

Before you start building your Flask application, you need to install several essential modules, including Flask extensions for web forms, SQL support, and database migrations.

#### 1.1. Installing Flask

To install Flask, open your terminal or command prompt and run the following command:

```bash
pip install flask
```

#### 1.2. Installing python-dotenv

Similarly, to install python-dotenv for managing environment variables, run:

```bash
pip install python-dotenv
```

#### 1.3. Installing Flask-WTF

For Flask forms support, install `flask-wtf`:

```bash
pip install flask-wtf
```

#### 1.4. Installing Flask-SQLAlchemy

For SQLAlchemy support within Flask, install `flask-sqlalchemy`:

```bash
pip install flask-sqlalchemy
```

#### 1.5. Installing Flask-Migrate

To handle database migrations with Flask and SQLAlchemy, install `flask-migrate`:

```bash
pip install flask-migrate
```

### Why These Modules?

- **Flask**: A lightweight and flexible web framework for Python.
- **python-dotenv**: Manages environment variables from a `.env` file securely.
- **Flask-WTF**: Provides simple integration with WTForms, a flexible forms validation and rendering library for Flask applications.
- **Flask-SQLAlchemy**: Integrates SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library, into Flask applications.
- **Flask-Migrate**: Provides database migration support for Flask applications using SQLAlchemy.

### Example Output

After running the commands, you should see something like this in your terminal:

```plaintext
Collecting flask
  Downloading Flask-2.0.2-py3-none-any.whl (95 kB)
     |████████████████████████████████| 95 kB 3.3 MB/s 
Collecting python-dotenv
  Downloading python_dotenv-0.19.2-py2.py3-none-any.whl (18 kB)
Collecting flask-wtf
  Downloading Flask_WTF-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting flask-sqlalchemy
  Downloading Flask_SQLAlchemy-2.5.2-py2.py3-none-any.whl (17 kB)
Collecting flask-migrate
  Downloading Flask_Migrate-3.2.1-py2.py3-none-any.whl (14 kB)
Installing collected packages: flask, python-dotenv, flask-wtf, flask-sqlalchemy, flask-migrate
Successfully installed flask-2.0.2 flask-migrate-3.2.1 flask-sqlalchemy-2.5.2 flask-wtf-1.0.0 python-dotenv-0.19.2
```

Now that you have Flask, python-dotenv, Flask-WTF, Flask-SQLAlchemy, and Flask-Migrate installed, you're ready to proceed with building and managing your Flask application with forms and database support.