#!/usr/bin/env python3
from email.policy import default
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from config import Base

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    attendees = Column(Integer, nullable=False, default=0)

    created_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    type = Column(Integer, ForeignKey('event_type.id'), nullable=False)
