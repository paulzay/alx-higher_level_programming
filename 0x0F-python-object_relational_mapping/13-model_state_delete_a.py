#!/usr/bin/python3

"""comment"""
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
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.close()


if __name__ == '__main__':
    main()
