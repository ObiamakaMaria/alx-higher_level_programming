#!/usr/bin/python3
""" This script lists all states from the
database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `states`")
        for state in cursor.fetchall():
            print(state)
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
