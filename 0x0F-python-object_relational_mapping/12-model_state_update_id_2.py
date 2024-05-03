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
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
