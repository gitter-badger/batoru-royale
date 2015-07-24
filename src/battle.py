# import math and random number functions
import random
import math
import time
from fighter import fighter
from combat import combat

def createCharacter(name, statLower, statUpper, skillBonus, strengthBonus, staminaBonus):
    
    character = fighter()
    
    if(name == ''):
        character.name = str(input("Give your character a name: "))
    else:
        character.name = str(name)
    
    statToUse = random.randint(1,3)
    statToUseNext = random.randint(1,2)
    
    randOne = random.randint(0,statUpper)
    print("First random: " + str(randOne)  + "\n")
          
    restRand = statUpper - int(randOne)
    print("Rest random: " + str(restRand)  + "\n")
    
    randTwo = random.randint(restRand,statUpper)
    print("Second random: " + str(randTwo)  + "\n")
    
    statToAdd = statLower + int(randOne)
    print("First stat: " + str(statToAdd) + "\n")

    statToAddNext = statLower + int(randTwo)
    print("Second stat: " + str(statToAddNext) + "\n")

    statLeft = int(statUpper*3) - int(statToAdd) - int(statToAddNext)
    print("Third stat: " + str(statLeft) + "\n")
    
    statTotal = statToAdd + statToAddNext + statLeft
    print("Total stat: " + str(statTotal) + "\n")
    
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

    fight = combat()
    fight.enabledScroll = 'true'
    
    logEvent("\n******************************************")
    
    playerOne = createCharacter('Ishino',20,80,0,0,0)
    playerTwo = createCharacter('Ogre',20,80,0,0,0)
    
    # log the start stats
    
    logEvent("------------------------------------------")
    print("\n\n")
   
    time.sleep(1)
    
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
       # You can slow the fight down by un-commenting the line below.
       time.sleep(0.0)
       round = round+1

battle()
