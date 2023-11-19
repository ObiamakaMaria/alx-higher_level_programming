#!/usr/bin/python3
""" This script adds the State object “Louisiana” to the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    state = State(name='Louisiana')
    db_session.add(state)
    db_session.commit()
    print(state.id)
