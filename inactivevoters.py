"""
This python script connects to the voter database and identifies voters who have been inactive for the last two elections.
The cutoff ate is defined as 8 years prior to the current year
"""

import sqlite3
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('voters.db')

# Create an index on the 'last_participation_date' column
conn.execute('CREATE INDEX IF NOT EXISTS last_participation_idx ON voters (last_participation_date)')


currentYear = datetime.today().year
# Define the cutoff date for inactive voters (voters who have been inactive for at least 8 years )
cutoff = datetime(currentYear,1,1) - timedelta(days=365*8)
# Find voters who have not voted in the last two elections and have been inactive for over 8 years
inactive_voters = conn.execute('''
       SELECT * FROM voters WHERE last_participation_date < ? 
           AND id NOT IN (
               SELECT id FROM voters WHERE last_participation_date >= ? 
           )
   ''', (cutoff, cutoff - timedelta(days=365 * 2)))

# Delete the inactive voters from the database
for voter in inactive_voters:
    conn.execute('DELETE FROM voters WHERE id = ?', (voter[0],))

# Commit the changes and close the connection
conn.commit()
conn.close()
