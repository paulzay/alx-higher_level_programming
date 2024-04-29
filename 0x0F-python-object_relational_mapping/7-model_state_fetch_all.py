#!/usr/bin/python3

from sqlalchemy import engine
import sys
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def main():
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[0], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    main()
