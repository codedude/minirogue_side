#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys, os
	import curses

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

MAP_1 = "\
--------------.........................................\n\
|    %       |.........................................\n\
|            +######...................................\n\
|       E    |.....###.--------...........-------......\n\
|            |.......##+  E  T|........###+ E   |......\n\
--------------.........|      |........#..|    T|......\n\
.......................|      +#########..-------......\n\
.......................|      |........................\n\
.......................|     T|........................\n\
.......................----+---........................\n\
...........................#...........................\n\
....------------------.....#...........................\n\
....|  S             |.....#...........................\n\
....|                +######...........................\n\
....|             E  |.................................\n\
....|T               |.................................\n\
....------------------.................................\n\
.......................................................\n\
"

class Map():
	def __init__(self, pmap, pname):
		self.name = pname
		self.map = [list(row) for row in pmap.split("\n")]
		self.map_print = [["."] * len(row) for row in pmap.split("\n")]
		self.x, self.y = self.getStart()[0], self.getStart()[1]
		self.addRoom(self.x, self.y)

	def getStart(self):
		y = 0
		for row in self.map:
			x = 0
			for col in row:
				if self.map[y][x] == "S":
					return (x, y)
				x += 1
			y += 1
		return (0, 0)

	def getEnd(self):
		y = 0
		for row in self.map:
			x = 0
			for col in row:
				if self.map[y][x] == "%":
					return (x, y)
				x += 1
			y += 1
		return (0, 0)

	def print(self):
		for row in self.map_print:
			for col in row:
				print(col, end='')
			print("")

	def addRoom(self, s, t):
		if self.map_print[t][s] != '.':
			return
		while self.map[t][s] != '|' and self.map[t][s] != '+':
			s -= 1
		while self.map[t][s] != '-':
			t -= 1
		x = s
		while self.map[t][x] == '-' or self.map[t][x] == '+':
			x += 1
		w = x - s
		y = t + 1
		while self.map[y][s] == '|' or self.map[y][s] == '+':
			y += 1
		h = (y + 1) - t

		for i in range(h):
			for j in range(w):
				self.map_print[t + i][s + j] = self.map[t + i][s + j]

	def addCouloir(self):
		if self.map[self.y + 1][self.x] == '#':
			self.map_print[self.y + 1][self.x] = '#'
		if self.map[self.y][self.x + 1] == '#':
			self.map_print[self.y][self.x + 1] = '#'
		if self.map[self.y - 1][self.x] == '#':
			self.map_print[self.y - 1][self.x] = '#'
		if self.map[self.y][self.x - 1] == '#':
			self.map_print[self.y][self.x - 1] = '#'

	def erasePos(self):
		self.map_print[self.y][self.x] = ' '
		self.map[self.y][self.x] = ' '

	def eraseMonster(self):
		if self.map[self.y + 1][self.x] == 'E':
			self.map_print[self.y + 1][self.x] = ' '
			self.map[self.y + 1][self.x] = ' '
		if self.map[self.y][self.x + 1] == 'E':
			self.map_print[self.y][self.x + 1] = ' '
			self.map[self.y][self.x + 1] = ' '
		if self.map[self.y - 1][self.x] == 'E':
			self.map_print[self.y - 1][self.x] = ' '
			self.map[self.y - 1][self.x] = ' '
		if self.map[self.y][self.x - 1] == 'E':
			self.map_print[self.y][self.x - 1] = ' '
			self.map[self.y][self.x - 1] = ' '

	def move(self, c):
		x = 0
		y = 0
		if c == curses.KEY_UP:
			y = -1
		elif c == curses.KEY_DOWN:
			y = 1
		elif c == curses.KEY_LEFT:
			x = -1
		elif c == curses.KEY_RIGHT:
			x = 1
		q = self.map[self.y + y][self.x + x]
		if q == ' ' or q == '+' or q == '#' or q == 'T' or q == '%':
			self.y += y
			self.x += x

		if q == '+' and self.map[self.y - y][self.x - x] == '#':
			self.addRoom(self.x + x, self.y + y)
		if (q == '+' and self.map[self.y - y][self.x - x] == ' ') \
		or (q == '#' and self.map[self.y - y][self.x - x] == '+') \
		or (q == '#' and self.map[self.y - y][self.x - x] == '#'):
			self.addCouloir()

		if q == '%':
			return 0

		return q


if __name__ == '__main__':
	map1 = Map(MAP_1, "Level 1")
	map1.print()
