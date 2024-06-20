#!/usr/bin/python3
"""
This script connects to a MySQL database and
retrieves all rows from the 'states' table
that match a given name.
The name is passed as a command-line argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM states
                WHERE name='{sys.argv[4]}' ORDER BY id ASC""")
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
