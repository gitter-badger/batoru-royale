# import math and random number functions
import random
import math
import time
from fighter import fighter
from combatLogs import combatLogs
from stats import combatStats

def createCharacter(name, level, skillBonus, strengthBonus, staminaBonus):

    statLower = 1 * level
    statUpper = 3 * level

    character = fighter()
    fight = combatLogs()
    fight.logLevel = 1

    if(name == ''):
        character.name = str(input("Give your character a name: "))
    else:
        character.name = str(name)
    
    statToUse = random.randint(1,3)
    statToUseNext = random.randint(1,2)
    
    randOne = random.randint(0,statUpper)

    restRand = statUpper - int(randOne)

    randTwo = random.randint(restRand,statUpper)
    
    statToAdd = statLower + int(randOne) + level

    statToAddNext = statLower + int(randTwo)

    statLeft = int(statUpper*4) - int(statToAdd) - int(statToAddNext)
    
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

    character.calculateStats()

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
    fight.logLevel = 0

    stats = combatStats()
    
    swing = 1
    
    while True:
       strengthModifier = calcModifier(playerOne.strength,playerTwo.strength,1)
       skillModifier = calcModifier(playerOne.typeStat,playerTwo.typeStat,0.2)

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
           stats.registerWin(playerTwo)
           playerOne.calculateStats()
           playerTwo.calculateStats()
           break
       elif not playerTwo.isAlive():
           eventText = "After " + str(swing) + " swings, " + playerOne.name + " won!"
           fight.logEvent(eventText,1)
           fight.logEvent("******************************************",1)
           stats.registerWin(playerOne)
           playerOne.levelUp()
           playerOne.calculateStats()
           playerTwo.calculateStats()
           break
       swing = swing+1

def tournament(rounds):
    fight = combatLogs()
    fight.logLevel = 1

    fight.logEvent("\n******************************************",0)
    playerOne = createCharacter('Ishino',1,0,0,0)
    fight.logEvent("------------------------------------------",0)

    stats = combatStats()

    for i in range(int(rounds)):
        eventText = "At level " + str(playerOne.level) + " " + playerOne.name + " has < " + str(playerOne.skill) + " ap | " + str(playerOne.strength) + " str | " + str(playerOne.stamina) + " sta | " + str(playerOne.hitPoints) + " hp >"
        fight.logEvent(eventText,0)
        playerTwo = createCharacter('Ogre',playerOne.level,0,0,0)
        battle(playerOne,playerTwo)

    tournament = stats.getStats()

    for player in tournament:
        for type in tournament[player]:
            print(str(player) + " - Type " + str(type) + ": " + str(tournament[player][type]))

tournament(1000)
