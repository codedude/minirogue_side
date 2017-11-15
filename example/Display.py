#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys, time
    import curses
    from curses import wrapper
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
    def draw(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        pass

class Composite(Component):
    def __init__(self, name, clist):
        super().__init__(name)
        self.__list = OrderedDict()
        for el in clist:
            self.__list[str(hash(el))] = el

    def draw(self):
        pass




def main(stdscr):
    # Clear screen
    curses.start_color()
    curses.use_default_colors()
    stdscr.clear()
    curses.cbreak()

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
    while True:
        c = stdscr.getch()
        if c == ascii.SP:
            break
        elif c == curses.KEY_RESIZE:
            (y, x) = stdscr.getmaxyx()
            stdscr.addstr(0, 0, "%d - %d\t" % (x, y))

    stdscr.refresh()



if __name__ == '__main__':
    wrapper(main)

    sys.exit(0)