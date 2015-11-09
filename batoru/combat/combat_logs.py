import time
import redis


class CombatLogs:

    def __init__(self):
        self.enabledScroll = True
        self.verboseEvent = True
        self.logLevel = 1
        self.scrollSpeed = 0.4
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def scroll(self, winner, looser, damage, gain):

        if not self.enabledScroll:
            return

        if gain > 0:
            if damage > 0:
                print(winner.name + " has knocked " + str(damage) + " hit points from " + looser.name + "!")
            else:
                print(winner.name + " checked " + looser.name + " for weaknesses!")

            print(winner.name + " gained " + str(gain) + " attack points!")
        else:
            print("Both fighters miss their swings! Pathetic!")

        print("After this round " + winner.name + " has < " + str(winner.fightSkill) + " ap | "
              + str(winner.hitPoints) + " hp >")
        print("After this round " + looser.name + " has < " + str(looser.fightSkill) + " ap | "
              + str(looser.hitPoints) + " hp >\n")

        time.sleep(self.scrollSpeed)

    def log_event(self, text, level):

        if level < self.logLevel:

            self.r.lpush('log', text)

            if self.verboseEvent:
                print(text + "\n")

        return
