#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from config import Base

class Campus(Base):
    __tablename__ = "campus"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
