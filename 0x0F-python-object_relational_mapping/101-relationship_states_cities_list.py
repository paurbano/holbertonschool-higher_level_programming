#!/usr/bin/python3
''' lists all State objects, and corresponding City objects '''

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    # Query States and its cities
    query = session.query(State).join(City).\
        filter(State.id == City.state_id).order_by(State.id, City.id)

    # Now print it
    # every state has a list with its cities
    for state in query:
        print("{}: {}".format(str(state.id), state.name))
        for city in state.cities:
            print("     {}: {}".format(str(city.id), city.name))

    session.close()
