#!/usr/bin/python3
""" ASDHIJAI SFADISJF ADSIFJAIDFJADF """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    new_id = 0
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    element = session.query(State).filter(State.id == 2).first()
    element.name = "New Mexico"
    session.commit()
