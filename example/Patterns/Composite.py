#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    from abc import ABC, abstractmethod
    from collections import OrderedDict

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


class Component(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def print(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print("Je suis %s" % self.name)

class Composite(Component):
    def __init__(self, name, clist):
        super().__init__(name)
        self.__list = OrderedDict()
        for el in clist:
            self.__list[str(hash(el))] = el

    def print(self):
        print("Je suis %s, je contiens :" % self.name)
        for el in self.__list.values():
            el.print()


if __name__ == '__main__':
    p0 = Leaf("Bebe")
    p1 = Leaf("Frere")
    p2 = Leaf("Soeur")
    p3 = Leaf("Pere")
    p4 = Leaf("Mere")
    p5 = Leaf("Grand-Mere 1")
    p6 = Leaf("Grand-Mere 2")
    p7 = Leaf("Grand-Pere 1")
    p8 = Leaf("Grand-Pere 2")

    c1 = Composite("Grands parents 1", [p5, p7, p3])
    c2 = Composite("Grands parents 2", [p6, p8, p4])
    c3 = Composite("Enfants", [p0, p1, p2])
    c4 = Composite("Famille", [c1, c2, c3])

    c3.print()

