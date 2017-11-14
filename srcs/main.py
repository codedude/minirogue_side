#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
    import sys
    from srcs import *

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)

def main():
	pass

if __name__ == '__main__':
    sys.exit(main())