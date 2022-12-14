import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqlpassword",
        database="library"
    )
except:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqlpassword"
    )
    cursor = database.cursor()
    cursor.execute('CREATE DATABASE library')

    # Create the books table.
    cursor = database.cursor()
    cursor.execute("""
        CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            ISBN VARCHAR(255) NOT NULL,
            copies_purchased INT NOT NULL,
            copies_not_checked_out INT NOT NULL,
            retail_price FLOAT NOT NULL
        )
    """)
    database.commit()

# Adds to the database.
def add(title, author, isbn, copiesP, copiesN, retail):
    cursor = database.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, ISBN, copies_purchased, copies_not_checked_out, retail_price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, author, isbn, copiesP, copiesN, retail))
    database.commit()

# Removes from the database.
def remove(value, varType):
    cursor = database.cursor()
    cursor.execute("""
        DELETE FROM books WHERE %s = %s
    """, (varType, value))
    database.commit()

# Shows all values from the database.
def showAll():
    cursor = database.cursor()
    cursor.execute('SELECT * FROM books')
    mycursor = cursor.fetchall()

    for x in mycursor:
        print(x)

showAll()