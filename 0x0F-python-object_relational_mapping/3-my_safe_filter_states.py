#!/usr/bin/python3
"""Thus script takes in arguments and displays all values
in the states f hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    value = sys.argv[4]
    curs.execute("SELECT * FROM `states` WHERE name\
            LIKE %s ORDER BY `id` ASC", (value,))
    for b in curs.fetchall():

        print(b)
    curs.close()
    db.close()
