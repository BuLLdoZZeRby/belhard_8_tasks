class Tomatto:
    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        i = self.states.index(self.ripeness)
        self.ripeness = self.states[i + 1]

    def is_ripe(self):
        if self.ripeness == self.states[len(self.states) - 1]:
            return True
        else:
            return False
