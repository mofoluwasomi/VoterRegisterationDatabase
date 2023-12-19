import sqlite3

from faker import Faker


# Create an instance of the Faker class
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('voters.db')
cursor = conn.cursor()

# Create a table for the polling units
cursor.execute('''
    CREATE TABLE IF NOT EXISTS polling_units (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        city TEXT

    )
''')


# Generate fake data and add it to the database
for i in range(1, 101):
    # Generate fake polling unit data
    polling_unit_name = fake.company()
    polling_unit_address = fake.address()
    polling_unit_city = fake.city()

    # Insert the new polling unit record
    cursor.execute('''
        INSERT INTO polling_units (id, name, address, city)
        VALUES (?, ?, ?, ?)
    ''', (i, polling_unit_name, polling_unit_address, polling_unit_city))


# close the connection
conn.commit()
conn.close()
