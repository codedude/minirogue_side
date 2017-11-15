#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys
    from .SomeClass.Singleton import Singleton, Unique

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)

def main():

    return 0


if __name__ == '__main__':
    pass