import math
import random
from combatStats import combatStats

class fighter:

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

    def calculateExperienceNeed(self):

        calculateExperienceNeed = 0

        for i in range(int(self.level)):
            calculateExperienceNeed = calculateExperienceNeed + ((self.level + 1000) * (self.level * self.level))

        return calculateExperienceNeed

    def levelUp(self, opponentLevel):

        experienceGain = (opponentLevel * opponentLevel) + (opponentLevel * opponentLevel) - (self.level * self.level)

        if experienceGain < 0:
            experienceGain = 0

        self.experience = self.experience + experienceGain

        calculatedExperience = self.calculateExperienceNeed()

        if calculatedExperience < self.experience:

            self.level = self.level + 1

            if self.type == 'A':
                self.strength = self.strength + 6
                self.stamina = self.stamina + 6

            if self.type == 'B':
                self.stamina = self.stamina + 6
                self.skill = self.skill + 6

            if self.type == 'C':
                self.skill = self.skill + 6
                self.strength = self.strength + 6

            if self.type == 'D':
                self.skill = self.skill + 6
                self.strength = self.strength + 3
                self.stamina = self.stamina + 3

            if self.type == 'E':
                self.skill = self.skill + 3
                self.strength = self.strength + 6
                self.stamina = self.stamina + 3

            if self.type == 'F':
                self.skill = self.skill + 3
                self.strength = self.strength + 3
                self.stamina = self.stamina + 6

            self.calculateStats()


    def create(self, name, startLevel, skillBonus, strengthBonus, staminaBonus):
        self.level = startLevel

        statLower = 1 * self.level
        statUpper = 3 * self.level
    
        if(name == ''):
            self.name = str(input("Give your character a name: "))
        else:
            self.name = str(name)
        
        statToUse = random.randint(1,3)
        statToUseNext = random.randint(1,2)
        
        randOne = random.randint(0,statUpper)
    
        restRand = statUpper - int(randOne)
    
        randTwo = random.randint(restRand,statUpper)
        
        statToAdd = statLower + int(randOne) + self.level
    
        statToAddNext = statLower + int(randTwo)
    
        statLeft = int(statUpper*4) - int(statToAdd) - int(statToAddNext)
        
        statTotal = statToAdd + statToAddNext + statLeft
        
        if statToUse == 1:
            
            self.skill = statToAdd + skillBonus
            if statToUseNext == 1:
                self.strength = statToAddNext + strengthBonus
                self.stamina = statLeft + staminaBonus
            else:
                self.stamina = statToAddNext + staminaBonus
                self.strength = statLeft + strengthBonus
                    
        elif statToUse == 2:
    
            self.strength = statToAdd + strengthBonus
            if statToUseNext == 1:
                self.skill = statToAddNext + skillBonus
                self.stamina = statLeft + staminaBonus
            else:
                self.stamina = statToAddNext + staminaBonus
                self.skill = statLeft + skillBonus
    
        else:
            
            self.stamina = statToAdd + staminaBonus
            if statToUseNext == 1:
                self.skill = statToAddNext + skillBonus
                self.strength = statLeft + strengthBonus
            else:
                self.strength = statToAddNext + strengthBonus
                self.skill = statLeft + skillBonus
    
        self.calculateStats()


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