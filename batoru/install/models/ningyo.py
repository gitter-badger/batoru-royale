from sqlalchemy import Column, Integer, String
from install.models.base import Base


class Fighter(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    level = Column(String)
    skill = Column(Integer)
    strength = Column(Integer)
    stamina = Column(Integer)
    hitpoints = Column(Integer)
    experience = Column(Integer)
