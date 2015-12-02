import unittest
from batoru.ningyo.fighter import Fighter
from batoru.ningyo.attributes import Attributes


class TestFighter(unittest.TestCase):

    def setUp(self):
        attributes = Attributes()
        self.player = Fighter(attributes)
        self.player.name = 'name'

if __name__ == '__main__':
    unittest.main()
