import redis
import elasticsearch
import datetime


class CombatStats:

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    es = elasticsearch.Elasticsearch()

    def register_win(self, player):

        self.r.setnx(player.name + ":" + player.type, 0)
        self.r.incr(player.name + ":" + player.type, 1)

        doc = {
            'author': player.name,
            'type': player.type,
            'timestamp': datetime.datetime.now(),
        }

        self.es.index(index="stats", doc_type='stat', id=1, body=doc)
