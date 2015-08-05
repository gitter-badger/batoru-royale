import unittest
from batoru.fighter import Fighter


class TestCombatCalculations(unittest.TestCase):

    def setUp(self):
        self.player = Fighter()
        self.player.name = 'name'

    def test_calculate_experience_need(self):
        result = 1001
        self.assertEqual(self.player.calculate_experience_need(), result)

        self.player.level = 2
        result = 8016
        self.assertEqual(self.player.calculate_experience_need(), result)

    def test_calculate_experience_gain(self):
        self.player.level = 1
        self.assertEqual(self.player.calculate_experience_gain(1), 1)
        self.assertEqual(self.player.calculate_experience_gain(2), 7)
        self.assertEqual(self.player.calculate_experience_gain(3), 17)

        self.player.level = 2
        self.assertEqual(self.player.calculate_experience_gain(1), 0)
        self.assertEqual(self.player.calculate_experience_gain(2), 4)
        self.assertEqual(self.player.calculate_experience_gain(3), 14)

        self.player.level = 3
        self.assertEqual(self.player.calculate_experience_gain(1), 0)
        self.assertEqual(self.player.calculate_experience_gain(2), 0)
        self.assertEqual(self.player.calculate_experience_gain(3), 9)

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

    def test_is_alive(self):
        self.player.hitPoints = 1
        self.assertTrue(self.player.is_alive())

        self.player.hitPoints = 0
        self.assertFalse(self.player.is_alive())

        self.player.hitPoints = -1
        self.assertFalse(self.player.is_alive())

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
