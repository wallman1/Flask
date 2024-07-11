# SQL Queries Explained

### Introduction to SQL

**SQL (Structured Query Language)** is a standardized language used to manage and manipulate relational databases. SQL allows you to create, read, update, and delete (CRUD) data within a database. It is a powerful tool for querying and managing data.

### Key SQL Commands

Here's a table of the main SQL commands with their purposes and examples:

| **Command** | **Description** | **Example** |
|-------------|------------------|-------------|
| **SELECT** | Retrieve data from a database | `SELECT * FROM users;` |
| **INSERT** | Add new rows of data to a table | `INSERT INTO users (username, email) VALUES ('john', 'john@example.com');` |
| **UPDATE** | Modify existing data in a table | `UPDATE users SET email='john.doe@example.com' WHERE username='john';` |
| **DELETE** | Remove data from a table | `DELETE FROM users WHERE username='john';` |
| **CREATE TABLE** | Create a new table in the database | `CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR(64), email VARCHAR(120));` |
| **ALTER TABLE** | Modify an existing table | `ALTER TABLE users ADD COLUMN password VARCHAR(128);` |
| **DROP TABLE** | Delete a table from the database | `DROP TABLE users;` |
| **JOIN** | Combine rows from two or more tables based on a related column | `SELECT users.username, posts.body FROM users JOIN posts ON users.id = posts.user_id;` |
| **WHERE** | Filter records that meet certain conditions | `SELECT * FROM users WHERE username='john';` |
| **GROUP BY** | Group rows that have the same values in specified columns into summary rows | `SELECT COUNT(*), country FROM users GROUP BY country;` |
| **HAVING** | Filter records after `GROUP BY` | `SELECT COUNT(*), country FROM users GROUP BY country HAVING COUNT(*) > 1;` |
| **ORDER BY** | Sort records in ascending or descending order | `SELECT * FROM users ORDER BY username ASC;` |
| **LIMIT** | Specify the number of records to return | `SELECT * FROM users LIMIT 10;` |
| **DISTINCT** | Return unique records | `SELECT DISTINCT country FROM users;` |
| **INNER JOIN** | Return records with matching values in both tables | `SELECT * FROM users INNER JOIN posts ON users.id = posts.user_id;` |
| **LEFT JOIN** | Return all records from the left table, and matched records from the right table | `SELECT * FROM users LEFT JOIN posts ON users.id = posts.user_id;` |
| **RIGHT JOIN** | Return all records from the right table, and matched records from the left table | `SELECT * FROM users RIGHT JOIN posts ON users.id = posts.user_id;` |
| **FULL JOIN** | Return all records when there is a match in either left or right table | `SELECT * FROM users FULL JOIN posts ON users.id = posts.user_id;` |

### Key SQL Concepts and Queries

#### 1. Selecting Fields
The `SELECT` statement is used to retrieve data from a database. You can specify the columns you want to retrieve.

```sql
SELECT username, email FROM users;
```

#### 2. Filtering Records
The `WHERE` clause is used to filter records that meet certain conditions.

```sql
SELECT * FROM users WHERE username = 'john';
```

#### 3. Sorting Records
The `ORDER BY` clause is used to sort records in ascending or descending order.

```sql
SELECT * FROM users ORDER BY username ASC;
```

#### 4. Grouping Records
The `GROUP BY` clause is used to group rows that have the same values in specified columns into summary rows.

```sql
SELECT country, COUNT(*) FROM users GROUP BY country;
```

#### 5. Filtering Grouped Records
The `HAVING` clause is used to filter records after they have been grouped.

```sql
SELECT country, COUNT(*) FROM users GROUP BY country HAVING COUNT(*) > 1;
```

#### 6. Combining Tables
Joins are used to combine rows from two or more tables based on a related column.

- **INNER JOIN:** Returns records with matching values in both tables.

```sql
SELECT users.username, posts.body FROM users INNER JOIN posts ON users.id = posts.user_id;
```

- **LEFT JOIN:** Returns all records from the left table and the matched records from the right table.

```sql
SELECT users.username, posts.body FROM users LEFT JOIN posts ON users.id = posts.user_id;
```

- **RIGHT JOIN:** Returns all records from the right table and the matched records from the left table.

```sql
SELECT users.username, posts.body FROM users RIGHT JOIN posts ON users.id = posts.user_id;
```

- **FULL JOIN:** Returns all records when there is a match in either the left or right table.

```sql
SELECT users.username, posts.body FROM users FULL JOIN posts ON users.id = posts.user_id;
```

### Additional SQL Concepts

1. **Constraints Using WHERE Keyword:**
   The `WHERE` clause can include various conditions to filter the data.

   ```sql
   SELECT * FROM users WHERE username = 'john' AND email LIKE '%@example.com';
   ```

2. **Table Joins:**
   Joins are used to retrieve data from multiple tables based on a related column between them.

   - **Self Join:** Joining a table with itself.
     ```sql
     SELECT a.username, b.username
     FROM users a, users b
     WHERE a.referrer_id = b.id;
     ```

   - **Cross Join:** Returns the Cartesian product of the sets of rows from the joined tables.
     ```sql
     SELECT * FROM users CROSS JOIN posts;
     ```

3. **Common SQL Queries:**
   Some commonly used SQL queries include:

   - **Finding the highest value:**
     ```sql
     SELECT MAX(salary) FROM employees;
     ```

   - **Finding the lowest value:**
     ```sql
     SELECT MIN(salary) FROM employees;
     ```

   - **Calculating the average:**
     ```sql
     SELECT AVG(salary) FROM employees;
     ```

   - **Counting rows:**
     ```sql
     SELECT COUNT(*) FROM users;
     ```

4. **Selecting Fields:**
   Specifying which fields (columns) to retrieve in a query.
   
   ```sql
   SELECT username, email FROM users;
   ```

### Summary

SQL is a powerful language used to interact with relational databases. Key commands include `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and various types of `JOINs`. Understanding how to filter, sort, and group data, as well as how to combine data from multiple tables, is crucial for effective database management and data retrieval.