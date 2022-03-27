class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        realt_list = []
        print(f"Имя : {self.name}\nВозраст: {self.age}\nНакоплено состояния в USD: {self.money}")
        if not self.realty:
            print("Недвижимости нет")
        else:
            for house in self.realty:
                realt_list.append(f"{house.__class__.__name__}, по адресу {house.address}, площадь: {house.area}")
        print(*realt_list, sep="\n")

    def earn_money(self, money):
        self.money += money

    def make_deal(self, house):
        if house.cost <= self.money:
            self.money -= house.cost
            self.realty.append(house)
        else:
            print("Недостаточно средств")
