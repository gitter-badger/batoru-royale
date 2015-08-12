import unittest
from batoru.combat.combat_stats import CombatStats
from batoru.ningyo.fighter import Fighter


class TestCombatStats(unittest.TestCase):

    def setUp(self):
        self.player = Fighter()
        self.player.name = 'name'

    def test_register_win(self):
        result = {'name': {'D': 1}}

        register_win_stats = CombatStats()

        register_win_stats.register_win(self.player)
        self.assertEqual(register_win_stats.wins, result)

    def test_get_stats(self):
        result = {'name': {'D': 1}}

        get_stats_stats = CombatStats()

        get_stats_stats.register_win(self.player)
        self.assertEqual(get_stats_stats.get_stats(), result)

if __name__ == '__main__':
    unittest.main()
