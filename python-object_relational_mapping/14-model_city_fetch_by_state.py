#!/usr/bin/python3
"""MODULE NAME"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State
from model_city import City


Base = declarative_base()


if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for s, c in result:
        print(f'{s.name}: ({c.id}) {c.name}')

    session.commit()
    session.close()
