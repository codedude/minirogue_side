#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    from abc import ABC, abstractmethod

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


class Character(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def attack(self):
        pass

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print("I put a spell on you !")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print("I hit your face !")

#Decorator
class SpecialAbility(ABC):
    def __init__(self, char):
        self.char = char

class WizardHealer(SpecialAbility):
    def __init__(self, char):
        super().__init__(char)

    def heal(self):
        print("%s : je me heal !" % self.char.name)

    def attack(self):
        print("Je n'attaque pas")


if __name__ == '__main__':
    mage = Wizard("Balto")
    war = Warrior("Igor")

    mage = WizardHealer(mage)
    mage.heal()
    mage.attack()