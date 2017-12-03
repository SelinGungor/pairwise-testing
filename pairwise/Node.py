class node:
    def __init__(self, id):
        self.id = id
        self.counter = 0
        self.in_ = set()
        self.out = set()

    def __str__(self):
        return str(self.__dict__)


def key(items):
    return "->".join([x.id for x in items])