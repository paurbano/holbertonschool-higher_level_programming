#!/usr/bin/python3
''' Use of SQlALchemy
    contains the class definition of a State and
    an instance Base = declarative_base()
'''

import sys
import os
from sqlalchemy import Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declare a Mapping: create the base class using the declarative_base()
Base = declarative_base()


# Mapping table states
class State(Base):
    ''' Table states'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
