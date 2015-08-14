import math
import random


class Fighter:

    def __init__(self, attribute_calc):
        self.name = ''
        self.type = 'D'
        self.typeStat = 1
        self.level = 1

        self.skill = 1
        self.fightSkill = 1
        self.strength = 1
        self.stamina = 1

        self.hitPointsBase = 100

        self.hitPoints = 0

        self.strengthMultiplier = 10
        self.staminaMultiplier = 100
        self.chanceMultiplier = 1

        self.offenceReduction = 100
        self.defenceReduction = 100

        self.experience = 0

        self.experience_modifier = 1000

        self.attributeCalc = attribute_calc

    def set_experience_calculator(self, experience_calc):
        self.experienceCalc = experience_calc

    def set_attribute_calculator(self, attribute_calc):
        self.attributeCalc = attribute_calc

    def gain_experience(self, opponent_level):

        self.experience += self.experienceCalc.calculate_experience_gain(self.level, opponent_level)
        if self.level_up(self.experienceCalc.calculate_experience_need(self.level, self.experience_modifier)):
            self.level_up_stats()

    def level_up(self, calculated_experience):
        if calculated_experience <= self.experience:
            self.level += 1
            return True
        return False

    def level_up_stats(self):
        if self.type == 'A':
            self.strength += 6
            self.stamina += 6

        if self.type == 'B':
            self.stamina += 6
            self.skill += 6

        if self.type == 'C':
            self.skill += 6
            self.strength += 6

        if self.type == 'D':
            self.skill += 6
            self.strength += 3
            self.stamina += 3

        if self.type == 'E':
            self.skill += 3
            self.strength += 6
            self.stamina += 3

        if self.type == 'F':
            self.skill += 3
            self.strength += 3
            self.stamina += 6

        self.calculate_stats()

    def create(self, name, start_level, skill_bonus, strength_bonus, stamina_bonus):

        if name == '':
            self.name = str(input("Give your character a name: "))
        else:
            self.name = str(name)

        self.level = start_level

        number_attributes = 3
        attributes_modifier = 1

        random_attribute_order = self.attributeCalc.choose_attribute_order(number_attributes)
        random_attribute_values = self.attributeCalc.generate_attribute_values(
            self.level, number_attributes, attributes_modifier
        )

        # Skill is attribute 1
        # Strength is attribute 2
        # Stamina is attribute 3

        i = 0
        while i < number_attributes:
            if random_attribute_order[i] == 1:
                self.skill = random_attribute_values[i] + skill_bonus

            if random_attribute_order[i] == 2:
                self.strength = random_attribute_values[i] + strength_bonus

            if random_attribute_order[i] == 3:
                self.stamina = random_attribute_values[i] + stamina_bonus
            i += 1

        self.calculate_stats()

    def calculate_stats(self):
        self.hitPoints = self.hitPointsBase * self.stamina
        self.fightSkill = self.skill

        primary_stat = self.skill
        secondary_stat = (self.strength + self.stamina)
        primary_type = 'A'
        secondary_type = 'D'

        if self.strength > primary_stat:
            primary_stat = self.strength
            secondary_stat = (self.skill + self.stamina)
            primary_type = 'B'
            secondary_type = 'E'

        if self.stamina > primary_stat:
            primary_stat = self.stamina
            secondary_stat = (self.strength + self.skill)
            primary_type = 'C'
            secondary_type = 'F'

        self.type = primary_type
        self.typeStat = primary_stat
        self.fightSkill = primary_stat

        if secondary_stat > primary_stat:
            self.typeStat = secondary_stat
            self.type = secondary_type

    def award_player(self, skill_modifier):
        self.fightSkill = int(self.fightSkill) + int(skill_modifier)

    def punish_player(self, damage, skill_modifier):
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
        accuracy = random.randint(0, chance) * self.chanceMultiplier
        return accuracy

    def punch(self):
        offence_modifier = (self.strength * self.strengthMultiplier)/self.offenceReduction
        offence = math.floor(math.fabs(self.fightSkill * offence_modifier))
        return offence

    def block(self):
        defence_modifier = (self.stamina * self.staminaMultiplier)/self.defenceReduction
        defence = math.floor(math.fabs(self.fightSkill * defence_modifier))
        return defence
