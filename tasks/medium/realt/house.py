class House:
    address: str
    area: float
    cost: float

    def __init__(self, address, coast, area):
        self.address = address
        self.area = area
        self.cost = coast

    def increase_cost(self, inc):
        self.cost += float(inc)

    def decrease_cost(self, dec):
        self.cost -= float(dec)
