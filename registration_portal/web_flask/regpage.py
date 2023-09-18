from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Replace these values with your database connection details
host = "localhost"
user = "mufatech"
password = "mukarram"
database = "myregistration"

@app.route('/')
def display_table():
    # Connect to the database
    connection = mysql.connector.connect(
        host=localhost,
        user=mufatech,
        password=mukarram,
        database=myregistration
    )

    cursor = connection.cursor()

    # Query the database (replace 'your_table' with your actual table name)
    query = "SELECT * FROM regpage"
    cursor.execute(query)

    # Fetch all rows
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Render an HTML template and pass the data
    return render_template('regpage.html', data=data)

if _name_ == '__main__':
    app.run(debug=True)