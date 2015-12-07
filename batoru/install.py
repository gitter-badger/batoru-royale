from interfaces.db import Engine
from install.models.base import Base

# although we don't use them directly in the code, also import the models for which we create tables.
from install.models.ningyo import Player

db_engine = Engine()
Base.metadata.create_all(db_engine.get_engine())
