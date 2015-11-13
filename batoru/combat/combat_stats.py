import redis
import elasticsearch
import datetime


class CombatStats:

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    es = elasticsearch.Elasticsearch()

    def register_fight(self, player, opponent, swings, fight_id, outcome):

        win_doc = {
            'fighter_name': player.name,
            'fighter_type': player.type,
            'fighter_level': player.level,
            'opponent_name': opponent.name,
            'opponent_type': opponent.type,
            'opponent_level': opponent.level,
            'swings': swings,
            'outcome': outcome,
            'timestamp': datetime.datetime.now(),
        }

        self.es.index(index="fights", doc_type='fight', id=fight_id, body=win_doc)

    def register_creation(self, player):

        self.r.setnx(player.name, 0)
        self.r.incr(player.name, 1)

        character_id = str(self.r.get(player.name))

        character_doc = {
            'character_name': player.name,
            'character_type': player.type,
            'character_level': player.level,
            'timestamp': datetime.datetime.now(),
        }

        self.es.index(index="creation", doc_type='character', id=character_id, body=character_doc)
