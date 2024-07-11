# Database Migrations

### Step 1: Creating the Migration Repository

#### 1.1 Create the Repository

Open the terminal in VS Code and type the following command:

```bash
python -m flask db init
```

##### Explanation

- **Command**: `python -m flask db init`
- **Purpose**: This command initializes a new migration repository.
- **What it does**:
  - **Initializes the Repository**: It sets up the `migrations` directory in your project. This directory will hold all migration scripts, which are files that describe changes to the database schema.
  - **Creates Configuration Files**: The command generates configuration files that Alembic (the underlying tool used by Flask-Migrate) uses to manage migrations. These files include details about the database connection and the migration environment.
  - **Sets Up Version Control for Schema Changes**: This repository acts like version control for your database schema, allowing you to apply, track, and revert changes systematically.

### Step 2: Running the First Database Migration

#### 2.1 Generate Migration Script

Next, generate the initial migration script by typing the following command in the terminal:

```bash
python -m flask db migrate -m "users table"
```

##### Explanation

- **Command**: `python -m flask db migrate -m "users table"`
- **Purpose**: This command generates a new migration script based on the current state of your models and the database schema.
- **What it does**:
  - **Compares Models to Schema**: It scans the models defined in your application (like the `User` model) and compares them to the existing database schema.
  - **Creates Migration Script**: Based on the differences, it creates a new migration script in the `migrations/versions` directory. This script includes SQL commands needed to bring the database schema in sync with the models.
  - **Adds Descriptive Message**: The `-m "users table"` part adds a descriptive message to the migration script, making it easier to identify the purpose of this migration.

### Step 3: Applying the Migration to the Database

#### 3.1 Apply Changes

Finally, apply the changes to the database by typing the following command in the terminal:

```bash
python -m flask db upgrade
```

##### Explanation

- **Command**: `python -m flask db upgrade`
- **Purpose**: This command applies the generated migration scripts to the database.
- **What it does**:
  - **Executes Migration Scripts**: It runs the migration script generated in the previous step, which includes the SQL commands needed to modify the database schema.
  - **Updates the Database**: This process updates the actual database schema to reflect the current state of your models. For example, it will create the `users` table as defined in the `User` model.
  - **Tracks Migration History**: Alembic keeps a record of applied migrations in a special table in the database. This helps in tracking what migrations have been applied and managing future migrations.

### Additional Information: Downgrading Migrations

#### Explanation

- **Command**: `python -m flask db downgrade`
- **Purpose**: This command is used to revert the database schema to a previous state.
- **What it does**:
  - **Reverts Applied Migrations**: It undoes the changes made by the last applied migration. This is useful if you need to roll back to a previous schema version due to errors or changes in requirements.
  - **Manages Database Versions**: By keeping track of migration history, Alembic allows you to move forward and backward through different versions of the database schema, providing flexibility in managing database changes.

### Summary

1. **Step 1**: Created the migration repository using `python -m flask db init`, which sets up the directory and configuration files needed for managing database migrations.
2. **Step 2**: Generated the initial migration script with `python -m flask db migrate -m "users table"`, which created a script to add the `users` table to the database by comparing the models with the current database schema.
3. **Step 3**: Applied the migration to the database using `python -m flask db upgrade`, which executed the migration script and updated the database schema to include the `users` table.

Additionally, `python -m flask db downgrade` would revert the last migration, allowing you to undo changes to the database schema if needed.