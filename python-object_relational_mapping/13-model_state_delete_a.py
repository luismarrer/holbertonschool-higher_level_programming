#!/usr/bin/python3

"""
This script changes the name of a State
object from the database hbtn_0e_6_usa
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

    del_state = session.query(State).filter(State.name.like('%a%')).all()

    for states in del_state:
        session.delete(states)

    session.commit()
    session.close()
