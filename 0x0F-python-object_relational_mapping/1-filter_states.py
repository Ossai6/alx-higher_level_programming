#!/usr/bin/python3
"""  script that lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, username=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE `name` LIKE
                   'N%' ORDER BY `id`")

    [print(state_with_n) for state_with_n in cur.fetchall()]
    cursor.close()
    db.close()
