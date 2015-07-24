class combat:

    enabledScroll = 'true'

    def scroll(self, winner, looser, damage, gain):

        if self.enabledScroll == 'false':
            return

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