#!/usr/bin/python3
"""This script lists all the cities from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT `cities`.`name` FROM `cities` INNER JOIN `states` ON\
            `cities`.`state_id` = `states`.`id` WHERE `states`.`name` LIKE %s\
            ORDER BY `cities`.`id` ASC", (sys.argv[4],))
    print(", ".join(city[0] for city in curs.fetchall()))
    curs.close()
    db.close()
