#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from config import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    company = Column(String(100), nullable=True)
