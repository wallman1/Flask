# Database Queries

### Step-by-Step Guide: Working with the Database Using SQLAlchemy Queries

In this step, we'll interact with our database directly using SQLAlchemy queries in a Python shell. We'll perform basic operations like creating users, adding blog posts, and querying data.

#### Step 1: Opening the Python Shell
1. Open a new terminal in your development environment.
2. Enter the Python interactive shell by typing:
    ```bash
    python
    ```

#### Step 2: Setting Up the Application Context
Before interacting with the database, we need to set up the application context:
```python
>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa
>>> app.app_context().push()
```

#### Step 3: Creating Users
To create new users and add them to the database:
```python
>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()

>>> u = User(username='susan', email='susan@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```

#### Step 4: Retrieving All Users
To retrieve and display all users:
```python
>>> query = sa.select(User)
>>> users = db.session.scalars(query).all()
>>> users
```

#### Step 5: Iterating Over Users
To iterate over and print user details:
```python
>>> users = db.session.scalars(query)
>>> for u in users:
...     print(u.id, u.username)
```
(Note: The `id` fields automatically increment starting from 1)

#### Step 6: Fetching a User by ID
To fetch a user by their ID:
```python
>>> u = db.session.get(User, 1)
>>> u
```

#### Step 7: Adding a Blog Post
To add a new blog post for a user:
```python
>>> u = db.session.get(User, 1)
>>> p = Post(body='my first post!', author=u)
>>> db.session.add(p)
>>> db.session.commit()
```

#### Step 8: Retrieving Posts by User
To get all posts written by a specific user:
```python
>>> u = db.session.get(User, 1)
>>> query = u.posts.select()
>>> posts = db.session.scalars(query).all()
>>> posts
```

To check for a user with no posts:
```python
>>> u = db.session.get(User, 2)
>>> query = u.posts.select()
>>> posts = db.session.scalars(query).all()
>>> posts
```

#### Step 9: Printing Post Details
To print the author and body of all posts:
```python
>>> query = sa.select(Post)
>>> posts = db.session.scalars(query)
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
```

#### Step 10: Advanced Queries
To get all users in reverse alphabetical order:
```python
>>> query = sa.select(User).order_by(User.username.desc())
>>> db.session.scalars(query).all()
```

To get all users with usernames starting with "s":
```python
>>> query = sa.select(User).where(User.username.like('s%'))
>>> db.session.scalars(query).all()
```

#### Step 11: Removing Test Data
To remove all test data and reset the database:
1. Close the Python shell.
2. Open a terminal and type the following commands:
    ```bash
    python -m flask db downgrade base
    python -m flask db upgrade
    ```

#### Detailed Explanations:

1. **Creating Users:**
   - We create new user instances and add them to the database session with `db.session.add(u)`.
   - Committing the session with `db.session.commit()` saves these changes to the database.

2. **Retrieving Users:**
   - We use `sa.select(User)` to create a query that selects all users.
   - `db.session.scalars(query).all()` executes the query and returns all results as a list.

3. **Iterating Over Users:**
   - We can iterate over the results of a query to print each user's ID and username.

4. **Fetching a User by ID:**
   - Using `db.session.get(User, 1)`, we retrieve a user with a specific ID.

5. **Adding a Blog Post:**
   - We create a new post instance and associate it with a user using the `author` attribute.
   - Adding and committing the post to the session saves it to the database.

6. **Retrieving Posts by User:**
   - By using the `posts` relationship, we can query all posts associated with a user.

7. **Advanced Queries:**
   - We use SQLAlchemy's query construction to filter and order users based on specific criteria.

8. **Removing Test Data:**
   - `flask db downgrade base` rolls back all migrations to the initial state.
   - `flask db upgrade` re-applies the migrations, effectively resetting the database.

#### Summary:
- **Open Python Shell**: Set up the application context.
- **Create Users**: Add new users to the database.
- **Retrieve Users**: Fetch and display all users.
- **Fetch User by ID**: Retrieve a user by their ID.
- **Add Blog Post**: Add a new post for a user.
- **Retrieve Posts**: Query and display posts for users.
- **Advanced Queries**: Perform complex queries like ordering and filtering users.
- **Reset Database**: Remove test data and reset the database.

By following these steps, you will interact directly with your SQLite database using SQLAlchemy queries, gaining hands-on experience with database operations in Flask.