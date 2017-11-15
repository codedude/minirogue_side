#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys
	import curses
	from abc import ABC, abstractmethod

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

class Window(ABC):
	def __init__(self, w, h, x, y, pActive = True):
		self.h = h
		self.w = w
		self.x = x
		self.y = y
		self.active = pActive
		self.win = curses.newwin(h, w, y, x)

	def refresh(self):
		if self.active:
			self.win.refresh()

	def clear(self):
		if self.active:
			self.win.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
			self.win.clear()

	def activate(self):
		self.active = True
	def deactivate(self):
		self.active = False
	def isActive(self):
		return self.active
	def getWin(self):
		return self.win

	def draw(self, reset=False):
		if not self.active:
			return
		self.clear()
		if reset:
			curses.delwin(self.win)
			self.win = curses.newwin(self.h, self.w, self.y, self.x)
		self.drawBorder()
		self.drawContent()

	def printMid(self, text, y):
		self.win.addstr(y, int((self.w - len(text)) / 2), text)

	@abstractmethod
	def drawBorder(self):
		pass

	@abstractmethod
	def drawContent(self):
		pass