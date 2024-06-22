#!/usr/bin/python3
"""
This module defines the City class, which represents a city in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
	"""
	City class represents a city in the database.

	Attributes:
		id (int): The unique identifier for the city.
		name (str): The name of the city.
		state_id (int): The foreign key referencing the associated state.

	"""
	__tablename__ = 'cities'
	id = Column(Integer, unique=True, primary_key=True,
				autoincrement=True, nullable=False)
	name = Column(String(128), nullable=False)
	state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
