from sqlalchemy import Column, Integer, String
from poie.model.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age