import sqlite3

# Connect to sqlite
connection = sqlite3.connect('student.db')

# Create cursor (This can insert, retrieve data or create table)
cursor = connection.cursor()

# Create Table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INTEGER
);
"""

cursor.execute(table_info)

# Insert more records
students_data = [
    ('Sruti', 'Data Science', 'A', 90),
    ('Rohit', 'Data Science', 'B', 100),
    ('Aashrith', 'Data Science', 'A', 70),
    ('Ishan', 'DEVOPS', 'B', 95),
    ('Dev', 'DEVOPS', 'A', 80),
    ('Arjun', 'Data Science', 'A', 85),
    ('Meera', 'AI and ML', 'A', 88),
    ('John', 'AI and ML', 'B', 92),
    ('Sara', 'DEVOPS', 'A', 75),
    ('Nina', 'Data Science', 'B', 65),
    ('Ravi', 'AI and ML', 'A', 78),
    ('Priya', 'Data Science', 'A', 93),
    ('Vijay', 'DEVOPS', 'B', 82),
    ('Anika', 'AI and ML', 'B', 87),
    ('Karan', 'Data Science', 'B', 76),
    ('Vishal', 'AI and ML', 'A', 89),
    ('Neha', 'DEVOPS', 'A', 74),
    ('Amit', 'Data Science', 'A', 91),
    ('Suman', 'AI and ML', 'B', 83),
    ('Manish', 'DEVOPS', 'B', 77),
    ('Rakesh', 'Data Science', 'B', 88),
    ('Pooja', 'AI and ML', 'A', 95),
    ('Rahul', 'DEVOPS', 'A', 79),
    ('Sneha', 'Data Science', 'A', 86),
    ('Anil', 'DEVOPS', 'B', 84)
]

cursor.executemany('''INSERT INTO STUDENT VALUES (?, ?, ?, ?)''', students_data)

# Display inserted records
print("Inserted records are: ")

data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
