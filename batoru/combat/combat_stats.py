class CombatStats:

    def __init__(self):
        self.wins = {}

    def register_win(self, player):
        if player.name not in self.wins:
            self.wins[player.name] = {}

        player_wins = self.wins[player.name]

        if player.type not in player_wins:
            player_wins[player.type] = 0
            self.wins[player.name] = player_wins

        self.wins[player.name][player.type] += 1

    def get_stats(self):
        return self.wins
