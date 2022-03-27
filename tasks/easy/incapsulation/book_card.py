"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __lt__(self, year):
        return self < year

    def __gt__(self, year):
        return self > year

    def __le__(self, year):
        return self <= year

    def __ge__(self, year):
        return self >= year

    def __eq__(self, year):
        return self == year

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, a):
        if not isinstance(a, str):
            raise ValueError
        else:
            self.__author = a

    @title.setter
    def title(self, a):
        if not isinstance(a, str):
            raise ValueError
        else:
            self.__title = a

    @year.setter
    def year(self, a):
        if not isinstance(a, int) or a < 1 or a > CURRENT_YEAR:
            raise ValueError
        else:
            self.__year = a
