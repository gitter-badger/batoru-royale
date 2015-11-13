import redis
import elasticsearch
import datetime


class CombatStats:

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    es = elasticsearch.Elasticsearch()

    def register_win(self, player, opponent, swings, fight_id):

        self.r.setnx(player.name + ":" + player.type, 0)
        self.r.incr(player.name + ":" + player.type, 1)

        doc = {
            'name': player.name,
            'type': player.type,
            'level': player.level,
            'opponent_name': opponent.name,
            'opponent_type': opponent.type,
            'opponent_level': opponent.level,
            'swings': swings,
            'timestamp': datetime.datetime.now(),
        }

        self.es.index(index="stats", doc_type='stat', id=fight_id, body=doc)
