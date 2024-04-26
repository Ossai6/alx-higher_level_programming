#!/usr/bin/python3
"""  script that lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, username=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], charset="utf-8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    [print(state) for state in states]
    cursor.close()
    db.close()
