#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#


class Final(type):
    def __init__(cls, name, bases, namespace):
        super(Final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError(str(klass.__name__) + " is final")


class FinalClass(metaclass=Final):
    pass

class InheritFinal(FinalClass):
    pass


if __name__ == '__main__':
    pass

