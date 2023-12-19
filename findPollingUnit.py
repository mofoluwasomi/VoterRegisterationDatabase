import sqlite3
import hashlib
from flask import Flask, render_template, request
from datetime import datetime
import threading

# Define a local object to store the connection for each thread
local = threading.local()



# Create a Flask application object and connect to the SQLite database
conn = sqlite3.connect('voters.db')
cursor = conn.cursor()
app = Flask(__name__)
# Function to get the connection for the current thread
def get_conn():
    if not hasattr(local, 'conn'):
        local.conn = sqlite3.connect('voters.db')
    return local.conn

# route where voter can input their information
@app.route('/')
def home():
    #return 'Flask is working'
    return render_template('findingPollingUnit.html')
# take in voters id
@app.route('/search', methods=['POST','GET'])
def search():
    conn = get_conn()
    cursor = conn.cursor()
    if 'id' not in request.form:
        return render_template('errror.html')
    vid = request.form['id']
    name = request.form['name']
    dob = request.form['date_of_birth']
    dob = datetime.strptime(dob, '%m/%d/%Y').strftime('%Y-%m-%d')

    # find the hash function associated with the voter id
    voter_hash = hashlib.sha256(vid.encode('utf-8')).hexdigest()

    # use query to find polling unit(s) associated with given as function
    cursor.execute('Select id, name, date_of_birth, polling_unit_id FROM voters WHERE hash_id = ?', (voter_hash,))
    result = cursor.fetchone()
    polling_unit_name, polling_unit_address, polling_unit_city = None, None, None
    if result is None:
        # Handles if the voter id was not found in the database
        pollID = None
    else:
        pollID = None
        # Handles a case where there is at least one voter id associated with the hash function.
        poll_units = [result[3]]  # fetches all polling units associated with specified hash function
        for poll in  poll_units:
            # use query to find all voters' id, name , date of birth associated with each polling unit
            cursor.execute('SELECT id, name, date_of_birth FROM voters WHERE polling_unit_id = ? AND hash_id = ?', (poll, voter_hash))
            voters = cursor.fetchall()
            for v in voters:
                # Voter ID was found in this collision
                if v[0] == vid and v[1] == name and v[2] == dob:
                    # Voter ID, name, and date of birth match
                    pollID = poll
                    break
        if pollID is not None:
            cursor.execute('SELECT name, address, city FROM polling_units WHERE id = ?', (pollID,))
            unit = cursor.fetchone()
            polling_unit_name, polling_unit_address, polling_unit_city = unit

        else:
            # Handle the case where the voter ID was not found
            polling_unit_name, polling_unit_address, polling_unit_city = None, None, None
    conn.close()
    if polling_unit_name is not None:
        return render_template('result.html', name=name, dob=dob, polling_unit_name=polling_unit_name,
                               polling_unit_address=polling_unit_address, polling_unit_city=polling_unit_city)
    else:
        return render_template('errror.html')


if __name__ == '__main__':
    app.run(debug=True)

