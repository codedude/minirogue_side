#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    from abc import ABC, ABCMeta, abstractmethod

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


class Character(ABC):

    def __init__(self, name, strategy):
        self.__name = name
        self.__fightStrategy = strategy

    @property
    def name(self):
        return self.__name

    def setFight(self, fight):
        self.__fightStrategy = fight

    def fight(self):
        self.__fightStrategy.fight()

    @abstractmethod
    def who(self):
        pass

class Wizard(Character):
    def __init__(self, name, strategy):
        super().__init__(name, strategy)

    def who(self):
        print("I am %s, a powerful wizard" % self.name)

class Rogue(Character):
    def __init__(self, name, strategy):
        super().__init__(name, strategy)

    def who(self):
        print("I am %s, king of stealth" % self.name)

class fightStrategy(metaclass=ABCMeta):
    @abstractmethod
    def fight(self):
        pass

class Fireball(fightStrategy):
    def fight(self):
        print("Owwwazaaa fireball")
class Lightspark(fightStrategy):
    def fight(self):
        print("THUNDER !!!")

class Knife(fightStrategy):
    def fight(self):
        print("Kouik cutting your fingers")

if __name__ == '__main__':
    wizard = Wizard("Balto", Fireball())
    rogue = Rogue("Sneak", Knife())

    wizard.who()
    wizard.fight()
    rogue.fight()

    wizard.setFight(Lightspark())
    wizard.fight()