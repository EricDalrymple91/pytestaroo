from rocksteady.utils import takeback


class SteadyRocking(object):
    def __init__(self, x):
        self.x = x

    def bebop(self):
        return self.x * takeback(self.x)


class Villain(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_health(self):
        return self.health


def get_top_villain_health(villains):
    return max(villains, key=lambda x: x.get_health())
