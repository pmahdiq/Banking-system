from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float,  DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker   

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    number = Column(String)
    email = Column(String)
    username = Column(String)
    age = Column(Integer)


class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True)
    name = Column(String)
    remaining = Column(Float)
    user_id = Column(String, ForeignKey("users.id"))


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    type = Column(String)
    amount = Column(float)
    created_at = Column(DateTime)
    account_id = Column(String, ForeignKey("accounts.id"))

engine = create_engine("sqlite:///banking.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()






