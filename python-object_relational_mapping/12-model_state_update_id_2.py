#!/usr/bin/python3
"""MODULE NAME"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State


Base = declarative_base()


if __name__ == '__main__':

    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
