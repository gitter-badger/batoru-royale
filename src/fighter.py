import math
import random


class Fighter:

    name = ''
    type = 'D'
    typeStat = 1
    level = 1

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

    experience = 0

    def calculate_experience_need(self):

        calculate_experience_need = 0

        for i in range(int(self.level)):
            calculate_experience_need += ((self.level + 1000) * (self.level * self.level))

        return calculate_experience_need

    def level_up(self, opponent_level):

        experience_gain = opponent_level * opponent_level + opponent_level * opponent_level - self.level * self.level

        if experience_gain < 0:
            experience_gain = 0

        self.experience += experience_gain

        calculated_experience = self.calculate_experience_need()

        if calculated_experience < self.experience:

            self.level += 1

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
        self.level = start_level

        stat_lower = 1 * self.level
        stat_upper = 3 * self.level

        if name == '':
            self.name = str(input("Give your character a name: "))
        else:
            self.name = str(name)

        stat_to_use = random.randint(1, 3)
        stat_to_use_next = random.randint(1, 2)

        rand_one = random.randint(0, stat_upper)

        rest_rand = stat_upper - int(rand_one)

        rand_two = random.randint(rest_rand, stat_upper)

        stat_to_add = stat_lower + int(rand_one) + self.level

        stat_to_add_next = stat_lower + int(rand_two)

        stat_left = int(stat_upper * 4) - int(stat_to_add) - int(stat_to_add_next)

        if stat_to_use == 1:

            self.skill = stat_to_add + skill_bonus
            if stat_to_use_next == 1:
                self.strength = stat_to_add_next + strength_bonus
                self.stamina = stat_left + stamina_bonus
            else:
                self.stamina = stat_to_add_next + stamina_bonus
                self.strength = stat_left + strength_bonus

        elif stat_to_use == 2:

            self.strength = stat_to_add + strength_bonus
            if stat_to_use_next == 1:
                self.skill = stat_to_add_next + skill_bonus
                self.stamina = stat_left + stamina_bonus
            else:
                self.stamina = stat_to_add_next + stamina_bonus
                self.skill = stat_left + skill_bonus

        else:

            self.stamina = stat_to_add + stamina_bonus
            if stat_to_use_next == 1:
                self.skill = stat_to_add_next + skill_bonus
                self.strength = stat_left + strength_bonus
            else:
                self.strength = stat_to_add_next + strength_bonus
                self.skill = stat_left + skill_bonus

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
        if offence < 1:
            offence = 1
        return offence

    def block(self):
        defence_modifier = (self.stamina * self.staminaMultiplier)/self.defenceReduction
        defence = math.floor(math.fabs(self.fightSkill * defence_modifier))
        return defence
