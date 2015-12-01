# import random number functions
import random
import elasticsearch
import redis


from ningyo.fighter import Fighter
from ningyo.attributes import Attributes
from ningyo.experience import Experience
from combat.combat_logs import CombatLogs
from combat.combat_stats import CombatStats
from combat.combat_calculations import CombatCalculations


class Battle:

    es = elasticsearch.Elasticsearch()
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def __init__(self):
        self.attributes = Attributes()
        self.levelCap = 2
        self.tournament_rounds = 1
        self.main()

    def main(self):

        tournament_round = 1

        while tournament_round <= self.tournament_rounds:
            self.r.setnx("tournament_id", 0)
            self.r.incr("tournament_id", 1)

            tournament_id = self.r.get("tournament_id")

            self.tournament(self.levelCap, tournament_id)
            tournament_round += 1

    def tournament(self, level_goal, tournament_id):
        fight = CombatLogs()
        fight.logLevel = 1

        stats = CombatStats()

        player_one = Fighter(self.attributes)
        player_one.set_experience_calculator(Experience())
        player_two = Fighter(self.attributes)

        fight.print_event("******************************************", 0)
        player_one.create('Ishino', 1, 0, 0, 0)
        fight.print_event("Player " + player_one.name + " created: < "\
                         + str(player_one.skill) + " ap | " + str(player_one.strength) + " str | "\
                         + str(player_one.stamina) + " sta | " + str(player_one.hitPoints) + " hp >", 0)
        fight.print_event("------------------------------------------", 0)

        stats.register_creation(player_one)

        fight_id = 1

        while player_one.level < level_goal:
            event_text = "At level " + str(player_one.level) + " " + player_one.name + " has < "\
                         + str(player_one.skill) + " ap | " + str(player_one.strength) + " str | "\
                         + str(player_one.stamina) + " sta | " + str(player_one.hitPoints) + " hp | "\
                         + str(player_one.experience) + " XP | needed: "\
                         + str(player_one.experienceCalc.calculate_experience_need(player_one.level,
                                                                                   player_one.experience_modifier
                                                                                   )) + " >"
            fight.log_event("tournament", event_text, 1)
            lower_opponent_level = player_one.level - 1
            if lower_opponent_level < 1:
                lower_opponent_level = 1
            upper_opponent_level = player_one.level + 2
            player_two_level = random.randint(lower_opponent_level, upper_opponent_level)
            player_two.create('Ogre', player_two_level, 0, 0, 0)
            stats.register_creation(player_two)
            event_text = "At level " + str(player_two.level) + " " + player_two.name + " has < "\
                         + str(player_two.skill) + " ap | " + str(player_two.strength) + " str | "\
                         + str(player_two.stamina) + " sta | " + str(player_two.hitPoints) + " hp >"
            fight.log_event("tournament", event_text, 1)
            self.compete(str(tournament_id) + "." + str(fight_id), player_one, player_two)

            fight.print_newline = False
            fight.print_event(".", 0)
            mod10 = fight_id % 200
            if mod10 == 0:
                fight.print_newline = True
                fight.print_event(" ( " + str(fight_id) + " )", 0)
            fight_id += 1

        fight.print_event("\n", 0)


    @staticmethod
    def compete(fight_id, player_one: Fighter, player_two: Fighter):

        fight = CombatLogs()
        fight.enabledScroll = False
        fight.logLevel = 0

        stats = CombatStats()

        swing = 1

        while True:
            skill_modifier = CombatCalculations.calc_modifier(player_one.typeStat, player_two.typeStat, 0.2)

            result = CombatCalculations.get_highest(int(player_one.swing()), int(player_two.swing()))
            if result == 1:

                damage = player_one.punch() - player_two.block()
                if damage < 1:
                    damage = 0

                player_one.award_player(skill_modifier)
                player_two.punish_player(damage, skill_modifier)

                fight.scroll(player_one, player_two, damage, skill_modifier)

            elif result == 2:

                damage = player_two.punch() - player_one.block()
                if damage < 1:
                    damage = 0

                player_two.award_player(skill_modifier)
                player_one.punish_player(damage, skill_modifier)

                fight.scroll(player_two, player_one, damage, skill_modifier)

            else:
                fight.scroll(player_two, player_one, 0, 0)

            if player_two.is_dead():
                event_text = "After " + str(swing) + " swings, " + player_one.name + " won!"
                fight.log_event("tournament", event_text, 0)
                fight.log_event("tournament", "******************************************", 0)
                stats.register_fight(player_one, player_two, swing, fight_id, 'win')
                player_one.gain_experience(player_two.level)
                player_one.calculate_stats()
                player_two.calculate_stats()
                return

            if player_one.is_dead():
                event_text = "After " + str(swing) + " swings, " + player_two.name + " won!"
                fight.log_event("tournament", event_text, 0)
                fight.log_event("tournament", "******************************************", 0)
                stats.register_fight(player_one, player_two, swing, fight_id, 'loss')
                player_one.calculate_stats()
                player_two.calculate_stats()
                return

            swing += 1

if __name__ == "__main__":
    Battle()
