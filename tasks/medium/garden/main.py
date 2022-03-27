from tomato import Tomatto
from tomato_bush import TomatoBush
from gardener import Gardener

if __name__ == '__main__':
    t1 = Tomatto(1)
    t2 = Tomatto(2)
    t3 = Tomatto(3)
    t4 = Tomatto(4)
    t5 = Tomatto(5)

    bush1 = TomatoBush(t1, t5)
    bush2 = TomatoBush(t4, t3, t2)

    gard = Gardener('Den', bush1, bush2)
    gard.work()
    gard.harvest()
    gard.work()
    gard.harvest()
    gard.work()
    print(len(gard.harvest()))
