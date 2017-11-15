#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#


class Observer():
    def __init__(self):
        self.__list = dict()

    def subscribe(self, obj):
        self.__list[str(hash(obj))] = obj

    def unsubscribe(self, obj):
        del self.__list[str(hash(obj))]

    def notify(self, msg):
        for obj in self.__list.values():
            obj.notify(msg)

class Guy():
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "I am %s" % self.__name

    def notify(self, msg):
        print("%s got %s" % (self.__name, msg))


if __name__ == '__main__':
    observer = Observer()

    bob = Guy("Bob")
    mike = Guy("Mike")
    robbie = Guy("Robbie")

    observer.subscribe(bob)
    observer.subscribe(mike)
    observer.subscribe(robbie)

    observer.notify("Hello !")

    observer.unsubscribe(mike)

    observer.notify("Bye !")