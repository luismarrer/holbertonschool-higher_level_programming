#!/usr/bin/python3

"""
This script fetches all the states from the database
and prints their IDs and names.
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = State(name='Louisiana')
    session.add(state_obj)
    session.commit()
    states = session.query(State).distinct().count()
    print(states)
    session.close()
