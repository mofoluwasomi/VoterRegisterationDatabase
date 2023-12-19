
import sqlite3
import pandas as pd


# Connect to the database
conn = sqlite3.connect('voters.db')

# Load data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM voters", conn)

# Export DataFrame to a CSV file
df.to_csv("voters.csv", index=False)

# Close the connection
conn.close()
