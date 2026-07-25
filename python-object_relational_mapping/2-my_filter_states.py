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
#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed to the script.
"""
import sys
import MySQLdb


def filter_states_by_input():
    """Filters and prints states matching user input from database."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"\
        .format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_input()
#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections.
"""
import sys
import MySQLdb


def safe_filter_states():
    """Filters states safely against SQL Injection."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # استخدام الاستعلام المعلمي (Parameterized Query) لمنع SQL Injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


def list_cities():
    """Lists all cities joined with state names ordered by cities.id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # استخدام JOIN لربط المدن بالولايات في استعلام واحد فقط
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injections.
"""
import sys
import MySQLdb


def filter_cities_by_state():
    """Prints all cities of the specified state separated by commas."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # استخدام JOIN واستعلام آمن لحماية البيانات من الـ SQL Injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    # طباعة أسماء المدن مفصولة بفصلة ونقطة مسافة
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
