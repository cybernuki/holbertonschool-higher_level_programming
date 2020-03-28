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

    found = False
    for state in session.query(State):
        if state.name == search:
            print("{}".format(state.id))
            found = True
            break
    if not found:
        print("Not found")