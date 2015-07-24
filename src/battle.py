# import math and random number functions
import random
import math
import time
from fighter import fighter
from combatLogs import combatLogs

def createCharacter(name, level, skillBonus, strengthBonus, staminaBonus):

    statLower = 1 * level
    statUpper = 3 * level

    character = fighter()
    fight = combatLogs()

    if(name == ''):
        character.name = str(input("Give your character a name: "))
    else:
        character.name = str(name)
    
    statToUse = random.randint(1,3)
    statToUseNext = random.randint(1,2)
    
    randOne = random.randint(0,statUpper)
          
    restRand = statUpper - int(randOne)
    
    randTwo = random.randint(restRand,statUpper)
    
    statToAdd = statLower + int(randOne)

    statToAddNext = statLower + int(randTwo)

    statLeft = int(statUpper*3) - int(statToAdd) - int(statToAddNext)
    
    statTotal = statToAdd + statToAddNext + statLeft
    
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

    character.calculateSecondaryStats()

    eventText = "Created " + character.name + " has < " + str(character.skill) + " ap | " + str(character.strength) + " str | " + str(character.stamina) + " sta | " + str(character.hitPoints) + " hp >"
    fight.logEvent(eventText,0)

    return character


def fightRound(playerOnePunch, playerTwoPunch):
    
    if not playerOnePunch == playerTwoPunch:
        if playerOnePunch > playerTwoPunch:
            return 1
        else:
            return 2
    else:
        return 0


def calcModifier(valueOne, valueTwo, multiplier):
    difference = int(valueOne) - int(valueTwo)
    modifier = math.floor(math.fabs(difference) * multiplier)
    if modifier == 0:
        modifier = 1
    return int(modifier)


def battle(playerOne,playerTwo):

    fight = combatLogs()
    fight.enabledScroll = False
    
    swing = 1
    
    while True:
       strengthModifier = calcModifier(playerOne.strength,playerTwo.strength,1)
       skillModifier = calcModifier(playerOne.skill,playerTwo.skill,0.2)

       result = fightRound(int(playerOne.swing()),int(playerTwo.swing()))
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
           fight.logEvent(eventText + "\n",1)
           fight.logEvent("******************************************",1)
           playerTwo.win()
           playerOne.calculateSecondaryStats()
           playerTwo.calculateSecondaryStats()
           break
       elif not playerTwo.isAlive():
           eventText = "After " + str(swing) + " swings, " + playerOne.name + " won!"
           fight.logEvent(eventText,1)
           fight.logEvent("******************************************",1)
           playerOne.win()
           playerOne.calculateSecondaryStats()
           playerTwo.calculateSecondaryStats()
           break
       # You can slow the fight down by un-commenting the line below.
       time.sleep(0.0)
       swing = swing+1

def tournament(rounds):
    fight = combatLogs()
    fight.logEvent("\n******************************************",0)

    playerOne = createCharacter('Ishino',12,10,10,10)
    playerTwo = createCharacter('Akira',15,0,0,0)

    #playerOne = fighter()
    #playerOne.name = 'Ishino'
    #playerOne.skill = 55
    #playerOne.strength = 10
    #playerOne.stamina = 30
    #playerOne.calculateSecondaryStats()

    #eventText = "Created " + playerOne.name + " has < " + str(playerOne.skill) + " ap | " + str(playerOne.strength) + " str | " + str(playerOne.stamina) + " sta | " + str(playerOne.hitPoints) + " hp >"
    #fight.logEvent(eventText,0)

    #playerTwo = fighter()
    #playerTwo.name = 'Akira'
    #playerTwo.skill = 10
    #playerTwo.strength = 55
    #playerTwo.stamina = 30
    #playerTwo.calculateSecondaryStats()

    #eventText = "Created " + playerTwo.name + " has < " + str(playerTwo.skill) + " ap | " + str(playerTwo.strength) + " str | " + str(playerTwo.stamina) + " sta | " + str(playerTwo.hitPoints) + " hp >"
    #fight.logEvent(eventText,0)

    # log the start stats

    fight.logEvent("------------------------------------------",0)

    time.sleep(1)

    for i in range(int(rounds)):
        battle(playerOne,playerTwo)

    fight.logEvent(playerOne.name + ": " + str(playerOne.wins) + "\n",0)
    fight.logEvent(playerTwo.name + ": " + str(playerTwo.wins) + "\n",0)

tournament(100000)
