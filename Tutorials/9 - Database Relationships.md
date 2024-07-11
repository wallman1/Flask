# Database Relationships

### Step 1: Adding a 'posts' Table

To turn our SQLite database into a relational database, we need to add a `posts` table. This will allow users to write blog posts.

#### Data Dictionary for the `posts` Table

| Column     | Type      | Description                                          |
|------------|-----------|------------------------------------------------------|
| id         | INTEGER   | Primary key, unique identifier for each post         |
| body       | VARCHAR(140) | The content of the post                            |
| timestamp  | DATETIME  | The time when the post was created                   |
| user_id    | INTEGER   | Foreign key, links to the `id` field in the `user` table |

##### Explanation

- **id**: This is the primary key for the `posts` table, which uniquely identifies each post. It is an integer and automatically increments for each new post.
- **body**: This field contains the text of the blog post. It is a string with a maximum length of 140 characters.
- **timestamp**: This field records the date and time when the post was created. It uses the `DATETIME` type.
- **user_id**: This is a foreign key that references the `id` field in the `user` table. It establishes a relationship between the `posts` table and the `user` table.

#### Foreign Keys and Relationships

- **Foreign Keys**: A foreign key is a field (or collection of fields) in one table that uniquely identifies a row in another table. In this case, `user_id` in the `posts` table is a foreign key that references `id` in the `user` table.
- **Relationships**: Relationships define how tables are related to each other. Here, each post is associated with a user, meaning a user can have many posts (one-to-many relationship).

### Step 2: Updating the Models

We need to update `models.py` to include the `Post` model and establish the relationship between `User` and `Post`.

```python
from datetime import datetime, timezone
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
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(
        back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)

    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
```

##### Explanation

- **User Model**:
  - Added `posts` attribute: `so.relationship` establishes a one-to-many relationship with the `Post` model. `back_populates='author'` indicates that the `Post` model will have a corresponding relationship attribute named `author`.

- **Post Model**:
  - `id`: Primary key for the `posts` table.
  - `body`: Contains the text of the post.
  - `timestamp`: Automatically set to the current UTC time when a post is created.
  - `user_id`: Foreign key that links to the `id` field in the `User` model.
  - `author`: `so.relationship` establishes the inverse relationship to the `User` model. `back_populates='posts'` indicates that the `User` model has a `posts` attribute representing all posts by that user.

### Step 3: Creating a New Migration

To generate a migration script that includes the changes for the `posts` table, open the terminal and type:

```bash
python -m flask db migrate -m "posts table"
```

##### Explanation

- **Command**: `python -m flask db migrate -m "posts table"`
- **Purpose**: Generates a new migration script based on the current state of the models.
- **What it does**:
  - **Scans Models**: Scans the updated `models.py` file to detect changes.
  - **Creates Script**: Generates a new migration script that includes SQL commands to create the `posts` table and establish the relationship with the `users` table.

### Step 4: Applying the Migration

To apply the generated migration script to the database, type:

```bash
python -m flask db upgrade
```

##### Explanation

- **Command**: `python -m flask db upgrade`
- **Purpose**: Applies the migration script to the actual database.
- **What it does**:
  - **Executes Script**: Runs the SQL commands in the migration script, creating the `posts` table and updating the database schema.
  - **Updates Database**: Modifies the database to match the current state of the models.

### Additional Information: Downgrading Migrations

- **Command**: `python -m flask db downgrade`
- **Purpose**: Reverts the last applied migration.
- **What it does**:
  - **Rolls Back Changes**: Reverts the database schema to the state before the last migration was applied. This can be useful if you need to undo changes due to errors or changes in requirements.

### Summary

1. **Created the `posts` table** with fields: `id`, `body`, `timestamp`, and `user_id`, and explained foreign keys and relationships.
2. **Updated `models.py`** to include the `Post` model and established a relationship between `User` and `Post`.
3. **Generated a migration script** with `python -m flask db migrate -m "posts table"` to include the new table and relationships.
4. **Applied the migration** to the database using `python -m flask db upgrade`, updating the schema to include the `posts` table.