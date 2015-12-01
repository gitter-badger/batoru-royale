import math
import random


class Ningyo:

    def __init__(self, attribute_calc):
        self.name = ''
        self.type = ''
        self.typeStat = 1
        self.level = 1

        self.fightSkill = 1

        self.hitPointsBase = 100
        self.hitPoints = 0

        self.offenceReduction = 100
        self.defenceReduction = 100

        self.experience = 0

        self.experience_modifier = 1000

        self.number_attributes = 1

        self.attributeCalc = attribute_calc

    def set_experience_calculator(self, experience_calc):
        self.experienceCalc = experience_calc

    def set_attribute_calculator(self, attribute_calc):
        self.attributeCalc = attribute_calc

    def set_offence_calculator(self, offence_calc):
        self.offenceCalc = offence_calc

    def set_defence_calculator(self, defence_calc):
        self.defenceCalc = defence_calc

    def set_chance_calculator(self, chance_calc):
        self.chanceCalc = chance_calc

    def gain_experience(self, opponent_level):

        self.experience += self.experienceCalc.calculate_experience_gain(self.level, opponent_level)
        if self.level_up(self.experienceCalc.calculate_experience_need(self.level, self.experience_modifier)):
            self.level_up_stats()

    def level_up(self, calculated_experience):
        if calculated_experience <= self.experience:
            self.level += 1
            return True
        return False

    def empower(self, skill_modifier):
        self.fightSkill = int(self.fightSkill) + int(skill_modifier)

    def weaken(self, damage, skill_modifier):
        self.hitPoints = int(self.hitPoints) - int(damage)
        self.fightSkill = int(self.fightSkill) - int(skill_modifier)
        if int(self.fightSkill) < 0:
            self.fightSkill = 0

    def is_alive(self):
        if int(self.hitPoints) > 0:
            return True
        else:
            return False

    def swing(self):
        chance = math.floor(self.typeStat + self.fightSkill)
        accuracy = random.randint(0, chance) * self.chanceCalc.getChance(self)
        return accuracy

    def offensive(self):
        offence_modifier = (self.offenceCalc.getOffence(self))/self.offenceReduction
        offence = math.floor(math.fabs(self.fightSkill * offence_modifier))
        return offence

    def defensive(self):
        defence_modifier = (self.defenceCalc.getDefence(self))/self.defenceReduction
        defence = math.floor(math.fabs(self.fightSkill * defence_modifier))
        return defence
