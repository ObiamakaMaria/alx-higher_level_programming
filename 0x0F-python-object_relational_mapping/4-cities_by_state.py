#!/usr/bin/python3
"""This script lists all cities  from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
            FROM `cities` INNER JOIN `states` ON\
            `cities`.`state_id` = `states`.`id`\
            ORDER BY `cities`.`id` ASC")
    for c in curs.fetchall():
        print(c)

    curs.close()
    db.close()
