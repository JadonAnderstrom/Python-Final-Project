# Step 1: Import SQLite
import sqlite3

# Step 2: Define the database file path
database_file = "students.db"

# Step 3: Manually define student data
student_data = [
    {"id": 100029, "first_name": "Donal", "last_name": "Salvatore", "username": "d.salvatore", "birthdate": "3/28/2004", "age": 19, "city": "Elk River"},
    {"id": 100069, "first_name": "Jo-anne", "last_name": "Misson", "username": "j.misson", "birthdate": "10/27/2004", "age": 18, "city": "Stillwater"},
    {"id": 100076, "first_name": "Rafe", "last_name": "Ilewicz", "username": "r.ilewicz", "birthdate": "4/20/2004", "age": 19, "city": "Aitkin"},
    {"id": 100127, "first_name": "Bobbie", "last_name": "Thewlis", "username": "b.thewlis", "birthdate": "6/1/2002", "age": 21, "city": "Becker"},
    {"id": 100312, "first_name": "Larine", "last_name": "Gooden", "username": "l.gooden", "birthdate": "3/1/2002", "age": 21, "city": "Brooklyn Park"}
]

# Step 4: Define the database structure
table_name = "students"
fields = [
    "id INTEGER PRIMARY KEY",  # Unique identifier for each student
    "first_name TEXT",
    "last_name TEXT",
    "username TEXT",
    "birthdate TEXT",
    "age INTEGER",
    "city TEXT"
]

# Step 5: Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Step 6: Create the table if it doesn't exist
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    {', '.join(fields)}
);
"""
cursor.execute(create_table_query)

# Step 7: Insert student data into the table
insert_query = f"""
INSERT INTO {table_name} (id, first_name, last_name, username, birthdate, age, city)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""
for student in student_data:
    cursor.execute(insert_query, (
        student["id"], student["first_name"], student["last_name"],
        student["username"], student["birthdate"], student["age"], student["city"]
    ))

# Step 8: Commit changes
conn.commit()
