from house import House
from townhouse import Townhouse
from person import Person

if __name__ == "__main__":
    h1 = House("Ванеева, 2", 30000, 50)
    h2 = House("Никольская, 56", 70000, 100)
    t1 = Townhouse("Солнечная 12", 60000)
    p1 = Person("Иван", 30)
    p1.earn_money(1000)
    p1.earn_money(120000)
    p1.make_deal(h2)
    p1.make_deal(t1)
    print(p1.info())
