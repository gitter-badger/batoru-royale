import math
import random

class fighter:

    name = ''

    skill = 60
    fightSkill = 60
    strength = 60
    stamina = 60

    hitPointsBase = 100

    hitPoints = 0

    strengthMultiplier = 10
    staminaMultiplier = 1

    offenceReduction = 85
    defenceReduction = 100

    chanceModifier = 10
    chanceMinimum = 12

    wins = 0

    def win(self):
        self.wins = self.wins + 1

    def calculateSecondaryStats(self):
        self.hitPoints = self.hitPointsBase * self.stamina
        self.fightSkill = self.skill

    def awardPlayer(self,skillModifier):
        self.fightSkill = int(self.fightSkill) + int(skillModifier)

    def punishPlayer(self,damage,skillModifier):
        self.hitPoints = int(self.hitPoints) - int(damage)
        self.fightSkill = int(self.fightSkill) - int(skillModifier)
        if int(self.fightSkill) < 0:
            self.fightSkill = 0

    def isAlive(self):
        if int(self.hitPoints) > 0:
            return True
        else:
            return False

    def swing(self):
        chance = math.floor(math.fabs((self.skill + self.strength + self.stamina) / self.chanceModifier)) + self.chanceMinimum
        accuracy = random.randint(0,chance)
        return accuracy

    def punch(self):
        offenceModifier = (self.strength * self.strengthMultiplier)/self.offenceReduction
        offence = math.floor(math.fabs(self.fightSkill * offenceModifier))
        if offence < 1:
            offence = 1
        return offence

    def block(self):
        defenceModifier = (self.stamina * self.staminaMultiplier)/self.defenceReduction
        defence = math.floor(math.fabs(self.fightSkill * defenceModifier))
        return defence