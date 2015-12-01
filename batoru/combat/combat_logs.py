import time
import redis


class CombatLogs:

    def __init__(self):
        self.enabledScroll = True
        self.verboseEvent = True
        self.logLevel = 1
        self.scrollSpeed = 0.4
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.print_newline = True

    def scroll(self, winner, loser, damage, gain):

        if not self.enabledScroll:
            return

        if gain > 0:
            if damage > 0:
                self.log_event("Fight", winner.name + " has knocked " + str(damage) + " hit points from " + loser.name + "!", 0)
            else:
                self.log_event("Fight", winner.name + " checked " + loser.name + " for weaknesses!", 0)

            self.log_event("Fight", winner.name + " gained " + str(gain) + " attack points!", 0)
        else:
            self.log_event("Fight", "Both fighters miss their swings! Pathetic!", 0)

        self.log_event("Fight", "After this round " + winner.name + " has < " + str(winner.fightSkill) + " ap | "
                       + str(winner.hitPoints) + " hp >", 0)
        self.log_event("Fight", "After this round " + loser.name + " has < " + str(loser.fightSkill) + " ap | "
                       + str(loser.hitPoints) + " hp >", 0)
        self.print_event("\n", 0)

        time.sleep(self.scrollSpeed)

    def log_event(self, key, text, level):

        if level < self.logLevel:

            self.r.lpush(key, text)

            if self.verboseEvent:
                self.print_event(text, level)

    def print_event(self, text, level):
        if level < self.logLevel:
            print(text, end="", flush=True)
            if self.print_newline:
                print("\n", end="")