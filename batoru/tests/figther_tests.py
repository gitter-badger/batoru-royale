import unittest
from batoru.ningyo.fighter import Fighter
from batoru.ningyo.attributes import Attributes


class TestFighter(unittest.TestCase):

    def setUp(self):
        attributes = Attributes()
        self.player = Fighter(attributes)
        self.player.name = 'name'

    def test_award_player(self):
        self.player.fightSkill = 1
        self.player.award_player(1)
        self.assertEqual(self.player.fightSkill, 2)

    def test_punish_player(self):
        self.player.fightSkill = 2
        self.player.hitPoints = 2

        self.player.punish_player(1, 1)
        self.assertEqual(self.player.fightSkill, 1)
        self.assertEqual(self.player.hitPoints, 1)

        self.player.punish_player(1, 1)
        self.assertEqual(self.player.fightSkill, 0)
        self.assertEqual(self.player.hitPoints, 0)

        self.player.punish_player(1, 1)
        self.assertEqual(self.player.fightSkill, 0)
        self.assertEqual(self.player.hitPoints, -1)

    def test_is_dead(self):
        self.player.hitPoints = 1
        self.assertFalse(self.player.is_dead())

        self.player.hitPoints = 0
        self.assertTrue(self.player.is_dead())

        self.player.hitPoints = -1
        self.assertTrue(self.player.is_dead())

    def test_punch(self):

        self.player.strength = 1
        self.player.strengthMultiplier = 1
        self.player.offenceReduction = 1
        self.player.fightSkill = 1
        self.assertEqual(self.player.punch(), 1)

    def test_block(self):

        self.player.stamina = 1
        self.player.staminaMultiplier = 1
        self.player.defenceReduction = 1
        self.player.fightSkill = 1
        self.assertEqual(self.player.block(), 1)

if __name__ == '__main__':
    unittest.main()
