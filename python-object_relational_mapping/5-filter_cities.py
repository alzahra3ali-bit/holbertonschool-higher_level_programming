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