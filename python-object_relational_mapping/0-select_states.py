#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Ensure correct number of arguments are passed
    if len(sys.argv) < 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}", file=sys.stderr)
        sys.exit(1)