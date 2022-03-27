from house import House


class Townhouse(House):

    def __init__(self, address, coast):
        super().__init__(address, coast, area=60)
