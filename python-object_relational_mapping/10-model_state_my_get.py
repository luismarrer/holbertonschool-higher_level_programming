#!/usr/bin/python3

"""
This script fetches a specific state from the database
based on the provided state name and prints its ID.
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state_name = session.query(State).filter(State.name == sys.argv[4]).first()

    if state_name:
        print(state_name.id)
    else:
        print("Not found")

    session.close()
