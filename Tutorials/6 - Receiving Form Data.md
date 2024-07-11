# Receiving Form Data

### Step 1: Enhancing Login Functionality with Flash Messages

In this step, we'll enhance our login functionality by handling form submissions, adding flash messages for user feedback, and updating templates accordingly.

#### 1.1. Update `routes.py` for Login Functionality

We update the `login()` function in `routes.py` to handle form submissions using `LoginForm` and incorporate flash messages for user feedback.

**`routes.py`**

```python
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
```

### Explanation

- **`flash()`**: Generates a temporary message that can be displayed to the user.
- **`redirect('/index')`**: Redirects the user to the home page (`/index`) upon successful login.

#### 1.2. Update `base.html` Template for Flash Messages

Update the `base.html` template to display flashed messages using Jinja's `get_flashed_messages()` function.

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
        <div>Moose: 
            <a href="/index">Home</a>
            <a href="/login">Login</a>
        </div>
        <hr>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}    
    </body>
</html>
```

### Explanation of `base.html`

- **`get_flashed_messages()`**: Retrieves flashed messages from the session.
- **`{% with messages = get_flashed_messages() %}`**: Temporarily assigns flashed messages to `messages`.
- **`{% if messages %}`**: Checks if there are flashed messages to display.
- **`<ul>` and `<li>`**: Renders flashed messages in a list format.

#### 1.3. Update `login.html` Template for Form Validation Errors

Update the `login.html` template to include form validation errors for username and password fields.

**`login.html`**

```html
{% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}<br>
            {% for error in form.username.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}
```

### Explanation of `login.html`

- **`{% for error in form.username.errors %}`**: Iterates through validation errors for the username field.
- **`<span style="color: red;">[{{ error }}]</span>`**: Displays each validation error message in red.

### Step 2: Improving URL Handling and Redirection

In this step, we'll enhance our application by using `url_for` for URL generation and redirection within Flask. This improves flexibility and maintains URLs dynamically.

#### 2.1. Update `base.html` Links

Update the links in `base.html` to use `url_for` for generating URLs dynamically.

**Updated `base.html`**

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
        <div>Moose: 
            <a href="{{ url_for('index') }}">Home</a>
            <a href="{{ url_for('login') }}">Login</a>
        </div>
        <hr>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}    
    </body>
</html>
```

### Explanation

- **`url_for('index')`**: Generates a URL for the `index` function in `routes.py`.
- **`url_for('login')`**: Generates a URL for the `login` function in `routes.py`.

#### 2.2. Update `routes.py` for Redirection

Update `routes.py` to use `url_for` for redirection instead of hard-coded URLs.

**Updated `routes.py`**

```python
from flask import render_template, flash, redirect, url_for
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
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
```

### Explanation

- **`redirect(url_for('index'))`**: Redirects to the URL generated by `url_for('index')`.
- **Dynamic URL Generation**: Using `url_for` ensures that your application's URLs remain flexible and can adapt to changes in route names or URL structure.

### Summary

In this tutorial, you've:

- Updated `routes.py` to handle form submissions and flash messages.
- Updated `base.html` to display flashed messages.
- Updated `login.html` to include form validation error messages for username and password fields.

 
Next, you can proceed with testing your login functionality and further refining your application.

- Updated `base.html` to use `url_for` for generating dynamic URLs.
- Updated `routes.py` to use `url_for` for redirection instead of hard-coded URLs.

These changes improve the maintainability and flexibility of your Flask application. Next, you can test these changes to ensure they work as expected.