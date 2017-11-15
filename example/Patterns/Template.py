#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    from abc import ABC, abstractmethod

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


class JeuDeCartes(ABC):
    @abstractmethod
    def piocher(self):
        pass
    @abstractmethod
    def points(self):
        pass
    @abstractmethod
    def jouer(self, carte):
        pass

    def play(self):
        carte = self.piocher()
        self.jouer(carte)
        self.points()

class Bataille(JeuDeCartes):
    def __init__(self):
        self.__points = 0

    def piocher(self):
        return "Carte As"
    def points(self):
        self.__points += 1
        return self.__points

    def jouer(self, carte):
        print("You play %s" % carte)

class Hazard(JeuDeCartes):
    def __init__(self):
        pass

    def piocher(self):
        return 10
    def points(self):
        return 15

    def jouer(self, carte):
        print("You roll %s" % carte)

if __name__ == '__main__':
    jeu = Bataille()
    jeu.play()
    haz = Hazard()
    haz.play()

