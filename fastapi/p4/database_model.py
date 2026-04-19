from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class product(Base):
    #datbase table name
    __tablename__ = "product"
    id = Column(Integer,primary_key = True, index = True)
    product_name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


