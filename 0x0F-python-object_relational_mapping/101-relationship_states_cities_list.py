#!/usr/bin/python3
""" ASDHIJAI SFADISJF ADSIFJAIDFJADF """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import State
from relationship_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for estado in session.query(State).order_by(State.id):
        print(estado.id, end="")
        print(":", estado.name)
        for city in estado.cities:
            print("\t", end="")
            print(city.id, end="")
            print(":", city.name)
