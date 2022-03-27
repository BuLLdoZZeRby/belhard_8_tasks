

class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        for bush in self.plants:
            bush.grow_all()

    def harvest(self):
        tomato_list = []
        tomato = []
        if all(self.plants[i].all_are_ripe() for i in range(len(self.plants))):
            for b in self.plants:
                tomato_list.append(b.give_away_all())
                for i in range(len(tomato_list)):
                    x = tomato_list[i]
                    for t in range(len(x)):
                        tomato.append(x[t])

            return tomato
        else:
            print("Не все томаты созрели.")
            return None
