#!/usr/bin/env python3

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


# class to store user information
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)


class ContactUs(Base):
    __tablename__ = 'contact_us'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    message = Column(String(250), nullable=False)


engine = create_engine('sqlite:///almozaini_website.db')
Base.metadata.create_all(engine)
print("database created!")
