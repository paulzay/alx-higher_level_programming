#!/usr/bin/python3

"""commment"""
import sys
from sqlalchemy import engine
from model_state import Base, State
from sqlalchemy.orm import Session


def main():
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print("{}".format(state.id))


if __name__ == '__main__':
    main()
