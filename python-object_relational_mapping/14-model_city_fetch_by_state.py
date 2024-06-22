#!/usr/bin/python3
"""
This script fetches all cities and their corresponding
states from a database using SQLAlchemy.

Usage: python3 14-model_city_fetch_by_state.py
<username> <password> <database_name>
"""

from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State).join(State).order_by(City.id).all():
        # HERE: no SQL query, only objects!
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
