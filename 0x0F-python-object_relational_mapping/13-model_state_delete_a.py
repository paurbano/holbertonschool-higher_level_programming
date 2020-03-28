#!/usr/bin/python3
''' deletes all State objects with a name containing the letter a
from database hbtn_0e_6_usa '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # create states object
    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        states.delete(state)

    # commit and close session
    session.commit()
    session.close()
