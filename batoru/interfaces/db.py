from sqlalchemy import create_engine


class Engine:

    def __init__(self):
        self.engine = create_engine('sqlite:///sqlalchemy_example.db')

    def get_engine(self):
        return self.engine
