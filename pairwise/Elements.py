class element:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.weights = []

    def __str__(self):
        return str(self.__dict__)