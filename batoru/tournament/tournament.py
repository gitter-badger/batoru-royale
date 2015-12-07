from ningyo.fighter import Fighter
from ningyo.modifiers import Accuracy, Power
from ningyo.attributes import Attributes
from ningyo.experience import Experience


class Tournament:

    def __init__(self):
        self.load_player()

    def load_player(self, name):

        # load player

        # create player
        player = Fighter(Attributes())
        player.set_experience_calculator(Experience())
        player.set_accuarcy_calculator(Accuracy())
        player.set_power_calculator(Power())

        player.create('Ishino', 1, 0, 0, 0)

        # persist player

        return player
