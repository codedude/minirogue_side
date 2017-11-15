#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


class Animal():
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    def __str__(self):
        return "Je suis %s l'animal" % self.nom

class Lion(Animal):

    def __init__(self, nom):
        super().__init__(nom)

    def __str__(self):
        return "Roar je suis %s" % self.nom



if __name__ == '__main__':
    pass