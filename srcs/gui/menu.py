 #!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys
	import curses
	from gui.window import Window
	from abc import abstractmethod
	from const import *

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

class WinBackground(Window):
	def __init__(self, w, h, x, y, pActive = True):
		super().__init__(w, h, x, y, pActive)

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BG))
		self.win.border('|', '|', '-', '-', '+', '+', '+', '+')

	def drawContent(self):
		pass

class WinIntro(Window):
	def __init__(self, w, h, x, y, pActive = True):
		super().__init__(w, h, x, y, pActive)

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BW))
		self.win.border('#', '#', '#', '#', '#', '#', '#', '#')

	def drawContent(self):
		title = "Mini-rogue DX 4000"
		author = "Thomas & Valentin"
		self.printMid(title, 1)
		self.printMid(author, 2)

		txt = "The princess has been kidnapped."
		self.printMid(txt, 5)
		txt = "Only you can rescue her, brave knight!"
		self.printMid(txt, 6)
		txt = "Go to the dungeon and save her!"
		self.printMid(txt, 7)
		txt = "But beware of the dark knights..."
		self.printMid(txt, 8)

class WinMap(Window):
	def __init__(self, w, h, x, y, pMap, pActive = True):
		super().__init__(w, h, x, y, pActive)
		self.map = pMap

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BG))
		self.win.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

	def drawContent(self):
		for row in range(len(self.map.map_print) - 1):
			for col in range(len(self.map.map_print[0]) - 1):
				if row == self.map.y and col == self.map.x:
					self.win.attron(curses.color_pair(YELLOW));
					self.win.addstr(row, col, '@')
					self.win.attroff(curses.color_pair(YELLOW));
				elif self.map.map_print[row][col] == '.' or self.map.map_print[row][col] == 'S':
					self.win.addstr(row, col, ' ')
				elif self.map.map_print[row][col] == 'T':
					self.win.attron(curses.color_pair(GREEN));
					self.win.addstr(row, col, self.map.map_print[row][col])
					self.win.attroff(curses.color_pair(GREEN));
				elif self.map.map_print[row][col] == 'E':
					self.win.attron(curses.color_pair(RED));
					self.win.addstr(row, col, self.map.map_print[row][col])
					self.win.attroff(curses.color_pair(RED));
				else:
					self.win.addstr(row, col, self.map.map_print[row][col])

class WinEnd(Window):
	def __init__(self, w, h, x, y, pActive = True):
		super().__init__(w, h, x, y, pActive)

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BW))
		self.win.border('#', '#', '#', '#', '#', '#', '#', '#')

	def drawContent(self):
		title = "Congratulations !!! You saved the princess"
		self.printMid(title, 1)


class WinStats(Window):
	def __init__(self, w, h, x, y, pChar, pActive = True):
		super().__init__(w, h, x, y, pActive)
		self.char = pChar

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BG))
		self.win.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

	def drawContent(self):
		txt = "HP : " + str(self.char.carac.hp) + "  AD : " \
		+ str(self.char.carac.AP) + "  DEF : " + str(self.char.carac.armure) \
		+ "  AGL : " + str(self.char.carac.agilite) \
		+ " | LVL : " + str(self.char.lvl) \
		+ "  XP : "  + str(self.char.xp) \
		+ " | OR : "  + str(self.char.gold)
		self.win.addstr(1, 1, txt)

class WinMsg(Window):
	def __init__(self, w, h, x, y, pActive = True):
		super().__init__(w, h, x, y, pActive)
		self.msg = ""

	def drawBorder(self):
		self.win.bkgd(curses.color_pair(BG))
		self.win.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

	def upMsg(self, msg):
		self.msg = msg

	def drawContent(self):
		self.win.addstr(1, 1, self.msg)
