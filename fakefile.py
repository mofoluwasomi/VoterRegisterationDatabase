"""
This Python script generates fake data. This fake data is stored in an SQLite database
Each voter is assigned  a unique Voter id and its hash function equivalent
"""


import sqlite3
import uuid
import hashlib
from faker import Faker
import random


def hash_function(key):
    # Convert the string key to bytes  and generate the SHA-256 hash
    return hashlib.sha256(key.encode('utf-8')).hexdigest()


# Create an instance of the Faker class
fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('voters.db')
cursor = conn.cursor()

# Create a table for the voters
cursor.execute('''
    CREATE TABLE IF NOT EXISTS voters (
        id TEXT PRIMARY KEY,
        name TEXT,
        address TEXT,
        email TEXT,
        phone TEXT,
        polling_unit_id INTEGER,
        last_participation_date TEXT,
        date_of_birth TEXT,
        hash_id TEXT,
        FOREIGN KEY (polling_unit_id) REFERENCES polling_units(id)
    )
''')

for i in range(100000):
    # Generate fake voter data
    voter_name = fake.name()
    voter_address = fake.address()
    voter_email = fake.email()
    voter_phone = fake.phone_number()

    # Generate a unique ID for the voter record and its respective hash function
    voter_id = uuid.uuid4().hex
    hash_id = hash_function(voter_id)

    # Generate a random polling unit ID between 1 and 100
    polling_unit_id = random.randint(1, 100)

    # Generate a random date for the last participation
    last_participation_date = fake.date_between(start_date='-20y', end_date='today').year

    # Generate a random date of birth
    date_of_birth = fake.date_of_birth().strftime('%Y-%m-%d')

    # Insert the new voter record with the polling unit ID as a foreign key
    cursor.execute('''
        INSERT INTO voters (id, name, address, email, phone, polling_unit_id, last_participation_date, date_of_birth, hash_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (voter_id, voter_name, voter_address, voter_email, voter_phone, polling_unit_id, last_participation_date, date_of_birth, hash_function(voter_id)))

# Commit changes and close the connection
conn.commit()
conn.close()
