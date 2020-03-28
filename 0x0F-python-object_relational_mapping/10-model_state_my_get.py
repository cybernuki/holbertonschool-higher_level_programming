#!/usr/bin/python3
# This script find states that contains a using sqlalchem
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    usr_name, usr_pass, db_name, search = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            usr_name,
            usr_pass,
            db_name),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id)
        idx = states.index(search)
        print("{}".format(states[idx].id))
    except ValueError:
        print("Not found")
