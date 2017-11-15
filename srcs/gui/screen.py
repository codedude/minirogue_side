#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys, time
	import curses
	from gui.window import *
	from gui.menu import *
	from const import *
	from collections import OrderedDict

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

class Screen():
	def __init__(self):
		self.stdscr = curses.initscr()
		self.win = OrderedDict()

		curses.curs_set(0)
		curses.cbreak()
		self.stdscr.nodelay(True)
		self.stdscr.keypad(True)
		curses.noecho()

		if curses.has_colors() == False:
			curses.endwin()
			print("Le terminal ne prend pas en charge les couleurs")
			sys.exit()
		curses.start_color()

		curses.init_pair(BG, curses.COLOR_WHITE, curses.COLOR_BLACK);
		curses.init_pair(BW, curses.COLOR_BLACK, curses.COLOR_WHITE);
		curses.init_pair(WB, curses.COLOR_WHITE, curses.COLOR_BLACK);
		curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK);
		curses.init_pair(GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK);
		curses.init_pair(BLUE, curses.COLOR_BLUE, curses.COLOR_WHITE);
		curses.init_pair(ORANGE, curses.COLOR_CYAN, curses.COLOR_WHITE);
		curses.init_pair(YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK);
		curses.init_pair(PINK, curses.COLOR_MAGENTA, curses.COLOR_WHITE);

		self.refresh()

	def refresh(self):
		self.stdscr.refresh()
		for win in self.win:
			self.win[win].refresh()

	def draw(self):
		for win in self.win:
			self.win[win].draw()
		self.refresh()

	def end(self):
		curses.endwin()

	def getWin(self, pWin):
		return self.win[pWin]

	def addWin(self, pWin, cWin):
		self.win[pWin] = cWin

	def removeWin(self, pWin):
		self.win[pWin].clear()

	def removeAllWin(self):
		self.stdscr.clear()
		for win in self.win:
			self.removeWin(win)
		self.win = OrderedDict()

	def getCh(self):
		return self.stdscr.getch()

if __name__ == '__main__':
	scr = Screen()
	scr.addWin("menu", WinBackground(100, 36, 0, 0))
	scr.addWin("intro", WinIntro(60, 4, 20, 4))
	scr.draw()

	time.sleep(3)

	scr.end()

	sys.exit()