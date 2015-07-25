import math
import random
from stats import combatStats

class fighter:

    name = ''
    type = 'D'
    typeStat = 1

    skill = 1
    fightSkill = 1
    strength = 1
    stamina = 1

    hitPointsBase = 100

    hitPoints = 0

    strengthMultiplier = 10
    staminaMultiplier = 100
    chanceMultiplier = 1

    offenceReduction = 100
    defenceReduction = 100

    def calculateStats(self):
        self.hitPoints = self.hitPointsBase * self.stamina
        self.fightSkill = self.skill

        primaryStat = self.skill
        secondaryStat = (self.strength + self.stamina)
        primaryType = 'A'
        secondaryType = 'D'

        if self.strength > primaryStat:
            primaryStat = self.strength
            secondaryStat = (self.skill + self.stamina)
            primaryType = 'B'
            secondaryType = 'E'

        if self.stamina > primaryStat:
            primaryStat = self.stamina
            secondaryStat = (self.strength + self.skill)
            primaryType = 'C'
            secondaryType = 'F'

        self.type = primaryType
        self.typeStat = primaryStat
        self.fightSkill = primaryStat

        if secondaryStat > primaryStat:
            self.typeStat = secondaryStat
            self.type = secondaryType

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
        chance = math.floor(self.typeStat + self.fightSkill)
        accuracy = random.randint(0,chance) * self.chanceMultiplier
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