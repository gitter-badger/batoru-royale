# import math and random number functions
import random
import math
import time
from fighter import fighter
from combatLogs import combatLogs
from combatStats import combatStats

class battle:

    levelCap = 1

    def __init__(self,**levelCap):
        self.levelCap = 10
        self.main()

    def main(self):
        stats = combatStats()

        self.tournament(self.levelCap)

        tournamentStats = stats.getStats()

        for player in tournamentStats:
            for type in tournamentStats[player]:
                print(str(player) + " - Type " + str(type) + ": " + str(tournamentStats[player][type]))


    def tournament(self,rounds):
        fight = combatLogs()
        fight.logLevel = 1

        playerOne = fighter()
        playerTwo = fighter()

        fight.logEvent("\n******************************************",0)
        playerOne.create('Ishino',1,0,0,0)
        fight.logEvent("------------------------------------------",0)

        # for i in range(int(rounds)):
        while (playerOne.level < rounds):
            eventText = "At level " + str(playerOne.level) + " " + playerOne.name + " has < " + str(playerOne.skill) + " ap | " + str(playerOne.strength) + " str | " + str(playerOne.stamina) + " sta | " + str(playerOne.hitPoints) + " hp | " + str(playerOne.experience) + " XP | needed: " + str(playerOne.calculateExperienceNeed()) + " >"
            fight.logEvent(eventText,0)
            lowerOpponentLevel = playerOne.level - 1
            if lowerOpponentLevel < 1:
                lowerOpponentLevel = 1
            upperOpponentLevel = playerOne.level + 2
            playerTwoLevel = random.randint(lowerOpponentLevel, upperOpponentLevel)
            playerTwo.create('Ogre',playerTwoLevel,0,0,0)
            eventText = "At level " + str(playerTwo.level) + " " + playerTwo.name + " has < " + str(playerTwo.skill) + " ap | " + str(playerTwo.strength) + " str | " + str(playerTwo.stamina) + " sta | " + str(playerTwo.hitPoints) + " hp >"
            fight.logEvent(eventText,0)
            self.compete(playerOne,playerTwo)


    def fightRound(self,playerOnePunch, playerTwoPunch):

        if not playerOnePunch == playerTwoPunch:
            if playerOnePunch > playerTwoPunch:
                return 1
            else:
                return 2
        else:
            return 0


    def calcModifier(self,valueOne, valueTwo, multiplier):
        difference = int(valueOne) - int(valueTwo)
        modifier = math.floor(math.fabs(difference) * multiplier)
        if modifier == 0:
            modifier = 1
        return int(modifier)


    def compete(self,playerOne,playerTwo):

        fight = combatLogs()
        fight.enabledScroll = False
        fight.logLevel = 1

        stats = combatStats()

        swing = 1

        while True:
           strengthModifier = self.calcModifier(playerOne.strength,playerTwo.strength,1)
           skillModifier = self.calcModifier(playerOne.typeStat,playerTwo.typeStat,0.2)

           result = self.fightRound(int(playerOne.swing()),int(playerTwo.swing()))
           if result == 1:

               damage = playerOne.punch() - playerTwo.block()
               if(damage < 1):
                    damage = 0

               playerOne.awardPlayer(skillModifier)
               playerTwo.punishPlayer(damage,skillModifier)

               fight.scroll(playerOne, playerTwo, damage, skillModifier)

           elif result == 2:

               damage = playerTwo.punch() - playerOne.block()
               if(damage < 1):
                   damage = 0

               playerTwo.awardPlayer(skillModifier)
               playerOne.punishPlayer(damage,skillModifier)

               fight.scroll(playerTwo, playerOne, damage, skillModifier)

           else:
               fight.scroll(playerTwo, playerOne, 0, 0)

           if not playerOne.isAlive():
               eventText = "After " + str(swing) + " swings, " + playerTwo.name + " won!"
               fight.logEvent(eventText + "\n",0)
               fight.logEvent("******************************************",0)
               stats.registerWin(playerTwo)
               playerOne.calculateStats()
               playerTwo.calculateStats()
               return 2
           elif not playerTwo.isAlive():
               eventText = "After " + str(swing) + " swings, " + playerOne.name + " won!"
               fight.logEvent(eventText,0)
               fight.logEvent("******************************************",0)
               stats.registerWin(playerOne)
               playerOne.levelUp(playerTwo.level)
               playerOne.calculateStats()
               playerTwo.calculateStats()
               return 1
           swing = swing+1

battle = battle()