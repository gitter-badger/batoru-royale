import math
import random

class fighter:

    name = ''

    skill = 60
    strength = 60
    stamina = 60

    offenceReduction = 850
    defenceReduction = 1000
    chanceModifier = 10
    chanceMinimum = 12

    def awardPlayer(self,skillModifier):
        self.skill = int(self.skill) + int(skillModifier)

    def punishPlayer(self,damage,skillModifier):
        self.stamina = int(self.stamina) - int(damage)
        self.skill = int(self.skill) - int(skillModifier)
        if int(self.skill) < 0:
            self.skill = 0

    def isAlive(self):
        if int(self.stamina) > 0:
            return True
        else:
            return False

    def swing(self):

        chance = math.floor(math.fabs(self.skill / self.chanceModifier)) + self.chanceMinimum
        accuracy = random.randint(0,chance)
        return accuracy

    def punch(self):
        offenceModifier = (self.strength * 0.8)/self.offenceReduction
        offence = math.floor(math.fabs(self.skill * offenceModifier))
        if offence < 1:
            offence = 1
        return offence

    def block(self):
        defenceModifier = (self.stamina * 0.8)/self.defenceReduction
        defence = math.floor(math.fabs(self.skill * defenceModifier))
        return defence