
import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coins(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    fiat = Column(String(25))
    ask = Column(Float)
    totalAsk = Column(Float)
    bid = Column(Float)
    totalBid = Column(Float)
    time = Column(DateTime)
    # fecha y hora de ultima actualización
    updated = Column(DateTime)

    def __init__(self, name, ask, totalAsk, bid, totalBid, time):
        self.name = name
        self.ask = ask
        self.totalAsk = totalAsk
        self.bid = bid
        self.totalBid = totalBid
        self.time = datetime.datetime.fromtimestamp(time)
        self.updated = datetime.date.today()
