# import math and random number functions
import random
import math
import time

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



def combatScroll(winner, looser, damage, gain):
    
    if gain > 0:
        if damage > 0:
            print(winner.name + " has knocked " + str(damage) + " hit points from " + looser.name + "!")
        else:
            print(winner.name + " checked " + looser.name + " for weaknesses!")
              
              
        print(winner.name + " gained " + str(gain) + " attack points!")
    else:
        print("Both fighters miss their swings! Pathetic!")

    print("After this round " + winner.name + " has < " + str(winner.skill) + " ap | " + str(winner.stamina) + " hp >")
    print("After this round " + looser.name + " has < " + str(looser.skill) + " ap | "  + str(looser.stamina) + " hp >\n")



def createCharacter(name, statLower, statUpper, skillBonus, strengthBonus, staminaBonus):
    
    character = fighter()
    
    if(name == ''):
        character.name = str(raw_input("Give your character a name: "))
    else:
        character.name = str(name)
    
    statToUse = random.randint(1,3)
    statToUseNext = random.randint(1,2)
    
    randOne = random.randint(0,statUpper)
    # print("First random: " + str(randOne)  + "\n")
          
    restRand = statUpper - int(randOne)
    # print("Rest random: " + str(restRand)  + "\n")
    
    randTwo = random.randint(restRand,statUpper)
    #print("Second random: " + str(randTwo)  + "\n")
    
    statToAdd = statLower + int(randOne)
    #print("First stat: " + str(statToAdd) + "\n")

    statToAddNext = statLower + int(randTwo)
    #print("Second stat: " + str(statToAddNext) + "\n")

    statLeft = int(statUpper*3) - int(statToAdd) - int(statToAddNext)
    #print("Third stat: " + str(statLeft) + "\n")
    
    statTotal = statToAdd + statToAddNext + statLeft
    #print("Total stat: " + str(statTotal) + "\n")
    
    if statToUse == 1:
        
        character.skill = statToAdd + skillBonus
        if statToUseNext == 1:
            character.strength = statToAddNext + strengthBonus
            character.stamina = statLeft + staminaBonus
        else:
            character.stamina = statToAddNext + staminaBonus
            character.strength = statLeft + strengthBonus
                
    elif statToUse == 2:

        character.strength = statToAdd + strengthBonus
        if statToUseNext == 1:
            character.skill = statToAddNext + skillBonus
            character.stamina = statLeft + staminaBonus
        else:
            character.stamina = statToAddNext + staminaBonus
            character.skill = statLeft + skillBonus

    else:
        
        character.stamina = statToAdd + staminaBonus
        if statToUseNext == 1:
            character.skill = statToAddNext + skillBonus
            character.strength = statLeft + strengthBonus
        else:
            character.strength = statToAddNext + strengthBonus
            character.skill = statLeft + skillBonus

    eventText = "Created " + character.name + " has < " + str(character.skill) + " ap | " + str(character.strength) + " str | " + str(character.stamina) + " hp >"
    logEvent(eventText)
    print(eventText)

    return character


def fightRound(playerOnePunch,playerTwoPunch):
    
    if not playerOnePunch == playerTwoPunch:
        if playerOnePunch > playerTwoPunch:
            return 1
        else:
            return 2
    else:
        return 0


def calcModifier(valueOne,valueTwo):
    difference = int(valueOne) - int(valueTwo)
    modifier = math.floor(math.fabs(difference)/5)
    if modifier == 0:
        modifier = 1
    return int(modifier)



def logEvent(text):
    with open("battle_log.txt", "a") as charFile:
        charFile.write(text + "\n")


def battle():
    
    logEvent("\n******************************************")

    
    playerOne = createCharacter('',10,70,25,0,0)
    playerTwo = createCharacter('Ogre',20,60,0,0,0)
    
    # log the start stats
    
    logEvent("------------------------------------------")
    print("\n\n")
   
    time.sleep(2)
    
    round = 1
    
    while True:
       strengthModifier = calcModifier(playerOne.strength,playerTwo.strength)
       skillModifier = calcModifier(playerOne.skill,playerTwo.skill)

       result = fightRound(int(playerOne.swing()),int(playerTwo.swing()))
       if result == 1:
           
           damage = playerOne.punch() - playerTwo.block()
           if(damage < 1):
                damage = 0

           playerOne.awardPlayer(skillModifier)
           playerTwo.punishPlayer(damage,skillModifier)
    
           # combatScroll(playerOne, playerTwo, damage, skillModifier)

       elif result == 2:
           
           damage = playerTwo.punch() - playerOne.block()
           if(damage < 1):
               damage = 0

           playerTwo.awardPlayer(skillModifier)
           playerOne.punishPlayer(damage,skillModifier)
           
           # combatScroll(playerTwo, playerOne, damage, skillModifier)

       # else:
           # combatScroll(playerTwo, playerOne, 0, 0)

       if not playerOne.isAlive():
           eventText = "After " + str(round) + " rounds, " + playerTwo.name + " won!"
           logEvent(eventText + "\n")
           print(eventText)
           logEvent("******************************************")
           break
       elif not playerTwo.isAlive():
           eventText = "After " + str(round) + " rounds, " + playerOne.name + " won!"
           logEvent(eventText)
           print(eventText + "\n")
           logEvent("******************************************")
           break
       # You can slow the fight down by uncommenting below line.
       # time.sleep(0.5)
       round = round+1

battle()