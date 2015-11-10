import redis


class CombatStats:

    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def register_win(self, player):

        self.r.setnx(player.name + ":" + player.type, 0)
        self.r.incr(player.name + ":" + player.type, 1)
