#!/usr/bin/python3

"""comment"""
from sqlalchemy import engine
import sys
from model_state import Base, State


def main():
    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).order_by(State.id).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
    session.close()


if __name__ == '__main__':
    main()
