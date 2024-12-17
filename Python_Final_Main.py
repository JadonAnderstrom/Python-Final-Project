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

# Step 9: Define the edit_record function  
def edit_record(database_connection):  
    cursor = database_connection.cursor()  
    record_id = input("Enter record ID to edit: ")  
    
    # Check if the record exists  
    cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (record_id,))  
    record = cursor.fetchone()  
    
    if record:  
        new_first_name = input(f"Enter new first name (current: {record[1]}): ")  
        new_last_name = input(f"Enter new last name (current: {record[2]}): ")  
        new_username = input(f"Enter new username (current: {record[3]}): ")  
        new_birthdate = input(f"Enter new birthdate (current: {record[4]}): ")  
        new_age = input(f"Enter new age (current: {record[5]}): ")  
        new_city = input(f"Enter new city (current: {record[6]}): ")  

        update_query = f"""  
        UPDATE {table_name}  
        SET first_name = COALESCE(NULLIF(?, ''), first_name),  
            last_name = COALESCE(NULLIF(?, ''), last_name),  
            username = COALESCE(NULLIF(?, ''), username),  
            birthdate = COALESCE(NULLIF(?, ''), birthdate),  
            age = COALESCE(NULLIF(?, ''), age),  
            city = COALESCE(NULLIF(?, ''), city)  
        WHERE id = ?;  
        """  
        cursor.execute(update_query, (  
            new_first_name, new_last_name, new_username,  
            new_birthdate, new_age, new_city, record_id  
        ))  
        database_connection.commit()  
        print("Record Updated.")  
    else:  
        print("Record not found.")  

# Step 10: Call the edit_record function to allow user to edit records  
edit_record(conn)  

# Step 11: Display queried student data  
cursor.execute(f"SELECT * FROM {table_name}")  
student_records = cursor.fetchall()  
for record in student_records:  
    print(record)  

# Step 12: Close the database connection  
conn.close()  
