#!/usr/bin/python3

"""comment"""
from sqlalchemy import engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys


def main():
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()


if __name__ == '__main__':
    main()
