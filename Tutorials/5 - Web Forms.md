# Web Forms

### Step 1: Setting Up Configuration and Initialization

In this step, we'll set up configuration for your Flask application using a `config.py` file and update `__init__.py` to include the configuration.

#### 1.1. Create `config.py` for Application Configuration

Create a new file named `config.py` in your project directory (`app` folder) with the following content:

**`config.py`**

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'walkies'
```

### Explanation of `config.py`

- **`SECRET_KEY`**:
  - This configuration variable is essential for securely signing session cookies and other security-related functionality in Flask.
  - It retrieves the secret key from an environment variable named `SECRET_KEY`. If not found, it defaults to `'walkies'`.

#### 1.2. Update `__init__.py` to Include Configuration

Update your `__init__.py` file inside the `app` folder to import and configure your Flask application using the `Config` class defined in `config.py`.

**`__init__.py`**

```python
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
```

### Explanation of `__init__.py`

- **`app.config.from_object(Config)`**:
  - This line tells Flask to use the `Config` class defined in `config.py` for configuration settings.
  - It sets up your Flask application with the `SECRET_KEY` configuration and any other configurations you may add to the `Config` class later.

### Why Use Configuration?

- **Centralized Settings**: By storing configuration settings in a separate `Config` class, you can easily manage and modify settings for different environments (development, testing, production).
- **Security**: Keeping sensitive information like the secret key (`SECRET_KEY`) outside of your main application code enhances security.

### Example Output

Ensure your project structure looks like this after adding `config.py` and updating `__init__.py`:

```
your_project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── config.py
│   └── ... (other files and folders)
│
├── .env
└── moose.py
```

### Step 2: Creating a Login Form and Template

In this step, we'll create a login form using WTForms and integrate it into our Flask application.

#### 2.1. Create `forms.py` for Login Form

Create a new file named `forms.py` in your `app` folder. This file will define the `LoginForm` using WTForms.

**`forms.py`**

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
```

### Explanation of `forms.py`

- **`LoginForm`**: Inherits from `FlaskForm` and defines fields for username, password, a checkbox for remembering the user, and a submit button.
- **Validators**: `DataRequired()` ensures that the fields are not submitted empty.

#### 2.2. Create `login.html` Template

Create a new template file named `login.html` in your `templates` folder. This template will render the login form.

**`login.html`**

```html
{% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}
```

### Explanation of `login.html`

- **`{% extends "base.html" %}`**: Inherits the structure from `base.html`.
- **`{% block content %}`**: Defines a block where content specific to this template will be inserted.
- **`{{ form.hidden_tag() }}`**: Renders hidden fields for CSRF protection.
- **Form Fields**: Renders fields for username, password, remember me checkbox, and submit button.

#### 2.3. Update `base.html` for Login Link

Update your `base.html` template to include a link to the login page.

**`base.html`**

```html
<!doctype html>
<html>
    <head>
        {% if title %}
        <title>Home Page - {{ title }}</title>
        {% else %}
        <title>Welcome to Moose</title>
        {% endif %}
    </head>
    <body>
        <div>Moose: <a href="/index">Home</a> | <a href="/login">Login</a></div>
        <hr>
        {% block content %}{% endblock %}
    </body>
</html>
```

### Explanation of `base.html`

- **Login Link**: Added `<a href="/login">Login</a>` to the navigation bar.
  - This link directs users to the `/login` route where the login form will be rendered.

#### 2.4. Update `routes.py` to Handle Login Route

Update your `routes.py` file to include a route for handling the login page and rendering the `LoginForm`.

**`routes.py`**

```python
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    posts = [
        {
            'author': {'username': 'Reggie'},
            'body': 'Ruff, ruff!'
        },
        {
            'author': {'username': 'Fallon'},
            'body': 'Awooooooooo!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/no_title')
def no_title():
    user = {'username': 'Moose'}
    return render_template('index.html', user=user)
```

### Explanation of `routes.py`

- **`@app.route('/login', methods=['GET', 'POST'])`**:
  - Defines a route for `/login` that handles both `GET` (initial page load) and `POST` (form submission) requests.
  - Initializes an instance of `LoginForm` (`form = LoginForm()`) to be passed to the `login.html` template.

### Summary

In this tutorial, you have: 

- Created a `config.py` file to define application configurations such as `SECRET_KEY`.
- Updated `__init__.py` to load configuration settings using `Config` class from `config.py`.
- Created a `LoginForm` using WTForms in `forms.py`.
- Created a `login.html` template to render the login form.
- Updated `base.html` to include a login link.
- Updated `routes.py` to handle the `/login` route and render the `LoginForm`.
