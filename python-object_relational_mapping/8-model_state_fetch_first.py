#!/usr/bin/python3
"""
This script fetches all the states from
the database and prints their IDs and names.
"""

from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    if session.query(State).first() is None:
        print("Nothing")
    state_id = session.query(State).first().id
    state_name = session.query(State).first().name

    # HERE: no SQL query, only objects!
    print("{}: {}".format(state_id, state_name))
    session.close()
