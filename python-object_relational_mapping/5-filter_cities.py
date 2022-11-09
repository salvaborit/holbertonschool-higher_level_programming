#!/usr/bin/python3
"""task 2"""


import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT c.name FROM cities c \
        LEFT JOIN states s ON c.state_id = s.id \
        WHERE s.name = %s \
        ORDER BY c.id", (sys.argv[4], ))
    result = cursor.fetchall()
    for i, record in enumerate(result):
        if i > 0:
            print(', ', end='')
        print(str(record[0]), end='')
    print()
    cursor.close()
    db.close()
