

class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for tomat in self.tomato_list:
            tomat.grow()

    def all_are_ripe(self):
        if all(self.tomato_list[i].is_ripe() for i in range(len(self.tomato_list))):
            return True
        else:
            return False

    def give_away_all(self):
        copy_tomato_list = self.tomato_list.copy()
        self.tomato_list.clear()
        return copy_tomato_list
