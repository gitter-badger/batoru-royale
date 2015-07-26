class combatStats:
    wins = {}

    def registerWin(self,player):
        if player.name not in self.wins:
            self.wins[player.name] = {}

        playerWins = self.wins[player.name]

        if player.type not in playerWins:
            playerWins[player.type] = 0
            self.wins[player.name] = playerWins

        self.wins[player.name][player.type] = self.wins[player.name][player.type] + 1

    def getStats(self):
        return self.wins