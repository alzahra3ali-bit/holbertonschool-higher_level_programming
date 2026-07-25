#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute SQL query sorted in ascending order by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all records
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Clean up cursor and database connection
    cursor.close()
    db.close()