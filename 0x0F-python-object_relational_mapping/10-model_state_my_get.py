#!/usr/bin/python3
""" This script prints the State objects from
the database hbtn_0e_6_usa"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    query = db_session.query(State.id).filter(State.name == sys.argv[4]).first()
    if query is None:
        print('Not found')
    else:
        print(query[0])
