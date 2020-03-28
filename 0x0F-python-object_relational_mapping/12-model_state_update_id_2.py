#!/usr/bin/python3
''' changes the name of a State object from database hbtn_0e_6_usa '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import update

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # create and query state object
    state = session.query(State).filter_by(id=2)
    # state = State.update().where(State.name == 'New Mexico').values(id=2)
    state.name = 'New Mexico'
    # commit and close session
    session.commit()
    session.commit()
    session.close()
