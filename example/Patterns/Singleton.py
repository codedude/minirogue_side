#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#


class Singleton (object):
    instances = {}
    def __new__(cls, *args, **kargs):
        if Singleton.instances.get(cls) is None:
            Singleton.instances[cls] = object.__new__(cls, *args, **kargs)
        return Singleton.instances[cls]


class Unique(Singleton):
    pass


if __name__ == '__main__':
    c1 = Unique()
    c2 = Unique()

    print(c1.__class__)
    print(c2.__class__)
    print(hash(c1))
    print(hash(c2))

