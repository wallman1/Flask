# Templates

### Step 1: Updating `routes.py` to Use Templates

To move onto using templates in Flask, we'll update our `routes.py` to render an HTML page dynamically. Templates allow us to separate the HTML structure from the Python code, making the code cleaner and more manageable.

#### 1.1. Updating `routes.py`

Replace the existing code in `routes.py` with the following:

```python
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return '''
<html>
    <head>
        <title>Home Page - Moose</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
```

### Explanation of the Code

```python
from app import app
```

- This line imports the `app` instance from the `app` package.

```python
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return '''
<html>
    <head>
        <title>Home Page - Moose</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
```

- **`@app.route('/')` and `@app.route('/index')`**:
  - These lines define the routes for the root URL (`'/'`) and the `/index` URL.

- **`def index()`**:
  - This function will be called when either of the defined routes is accessed.

- **`user = {'username': 'Moose'}`**:
  - This creates a dictionary representing a user with the username 'Moose'.

- **`return ''' ... '''`**:
  - This multi-line string returns an HTML document. It includes a simple HTML structure with a title and a greeting that uses the `username` from the `user` dictionary.

### Step 2: Creating a Template Directory and Template File

Using inline HTML within the Python code is not ideal for larger applications. Instead, we'll use templates. Flask uses the Jinja2 templating engine, which allows us to create HTML files with placeholders for dynamic content.

#### 2.1. Create a Templates Directory

1. **Create a folder named `templates` inside the `app` folder**:
   - The `templates` folder will hold all your HTML template files.

2. **Create a file named `index.html` inside the `templates` folder**:
   - This file will be the template for the `index` route.

#### 2.2. Add the Following Content to `index.html`

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home Page - {{ title }}</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>
```

### Explanation of the Template

- **`{{ title }}`** and **`{{ user.username }}`**:
  - These are Jinja2 placeholders that will be replaced with dynamic content from the view function.

### Step 3: Updating `routes.py` to Use the Template

Now, we'll update the `index` function in `routes.py` to render the `index.html` template.

#### 3.1. Update `routes.py` as Follows:

```python
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return render_template('index.html', title='Home', user=user)
```

### Explanation of the Updated Code

```python
from flask import render_template
```

- This line imports the `render_template` function from Flask, which is used to render templates.

```python
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return render_template('index.html', title='Home', user=user)
```

- **`render_template('index.html', title='Home', user=user)`**:
  - This function renders the `index.html` template, passing `title` and `user` as variables to the template.

### Folder Structure Overview

After creating the `templates` directory and updating `routes.py`, your project structure should look like this:

```
your_project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│       ├── index.html
│
├── moose.py
├── .flaskenv
```

### Step 4: Running Your Flask Application with Templates

To see the changes, start your Flask application using the following command in the Visual Studio Code terminal:

```bash
python -m flask run
```

Open your web browser and go to `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/index`. You should see the message `'Hello, Moose!'` displayed using the `index.html` template.


### Step 5: Using Conditional Statements in Templates

In this step, we will introduce conditional statements in our templates using Jinja2 syntax. Conditional statements allow us to control the flow of rendering based on certain conditions.

#### 5.1. Adding Conditional Statements in `index.html`

We'll update the `index.html` template to include a conditional statement that changes the title of the page based on whether a `title` variable is provided.

Replace the content of `index.html` with the following code:

```html
<!DOCTYPE html>
<html>
    <head>
        {% if title %}
        <title>Home Page - {{ title }}</title>
        {% else %}
        <title>Welcome to Moose!</title>
        {% endif %}
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>
```

### Explanation of the Conditional Statement

```html
<!DOCTYPE html>
<html>
    <head>
        {% if title %}
        <title>Home Page - {{ title }}</title>
        {% else %}
        <title>Welcome to Moose!</title>
        {% endif %}
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>
```

- **`{% if title %}`**:
  - This line starts an `if` statement in Jinja2. It checks whether the `title` variable is defined and has a value.

- **`<title>Home Page - {{ title }}</title>`**:
  - If the `title` variable is defined, this line sets the title of the page to "Home Page - " followed by the value of the `title` variable.

- **`{% else %}`**:
  - This line defines the alternative case, which will be executed if the `title` variable is not defined or is empty.

- **`<title>Welcome to Moose!</title>`**:
  - If the `title` variable is not defined, this line sets the title of the page to "Welcome to Moose!".

- **`{% endif %}`**:
  - This line ends the `if` statement.

### Step 6: Testing Conditional Statements

To test the conditional statements, we will modify our `routes.py` to provide different scenarios.

#### 6.1. Updating `routes.py` for Testing

Replace the content of `routes.py` with the following code:

```python
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return render_template('index.html', title='Home', user=user)

@app.route('/no_title')
def no_title():
    user = {'username': 'Moose'}
    return render_template('index.html', user=user)
```

### Explanation of the Code

- **`@app.route('/no_title')`**:
  - This new route `/no_title` renders the `index.html` template without providing a `title` variable.

- **`return render_template('index.html', user=user)`**:
  - This line renders the `index.html` template and passes only the `user` variable, omitting the `title` variable.

### Testing the Application

To see the changes, start your Flask application using the following command in the Visual Studio Code terminal:

```bash
python -m flask run
```

Open your web browser and go to the following URLs to test the conditional statements:

1. **With Title**: Go to `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/index`
   - You should see the page title as "Home Page - Home" and the message "Hello, Moose!".

2. **Without Title**: Go to `http://127.0.0.1:5000/no_title`
   - You should see the page title as "Welcome to Moose!" and the message "Hello, Moose!".

### Summary

1. **Updated `routes.py`** to return a multi-line HTML string.
2. **Created a `templates` directory** and added an `index.html` template file.
3. **Updated `routes.py`** to render the `index.html` template using the `render_template` function.
4. **Added Conditional Statements** in the `index.html` template using Jinja2.
5. **Updated `routes.py`** to include a new route for testing the absence of the `title` variable.
6. **Tested the Application** by accessing different URLs to verify the behavior of conditional statements.

This setup separates the HTML structure from the Python code, making your application more maintainable and scalable.

By using conditional statements in your templates, you can create dynamic and flexible HTML pages that adapt to different conditions and data provided by your Flask application.