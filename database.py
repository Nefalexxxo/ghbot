from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Complex(Base):
    tablename = 'complexes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    apartments = relationship("Apartment", back_populates="complex")

class Apartment(Base):
    tablename = 'apartments'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    area = Column(Float)
    price = Column(Float)
    complex_id = Column(Integer, ForeignKey('complexes.id'))
    complex = relationship("Complex", back_populates="apartments")

# Создание базы данных
engine = create_engine('sqlite:///bot_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()