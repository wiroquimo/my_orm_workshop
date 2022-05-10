#!/usr/bin/env python3
from sqlalchemy.orm import sessionmaker

from config import Base, engine
from models.user import User
from models.campus import Campus
from models.cohort import Cohort
from models.eventType import EventType
from models.event import Event

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # QUERY
    # users = session.query(User)
    # LIST
    users = session.query(User).all()

    session.close()
