#!/usr/bin/env python3
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/db', echo = True)
Base = declarative_base()

event_campus = Table('event_campus', Base.metadata,
                     Column('event_id', Integer, ForeignKey('event.id'), primary_key=True),
                     Column('campus_id', Integer, ForeignKey('campus.id'), primary_key=True)
                    )

event_cohort = Table('event_cohort', Base.metadata,
                     Column('event_id', Integer, ForeignKey('event.id'), primary_key=True),
                     Column('cohort_id', Integer, ForeignKey('cohort.id'), primary_key=True)
                    )
