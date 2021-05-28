from sqlalchemy import Column, Integer, String
from poie.model.base import Base


class Results(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __init__(self, name=None, age=None):
        self.name = name