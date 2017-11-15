#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys, time, random
	from const import *
	from gui.menu import *
	from gui.map import *
	from chars.personnage import *
	import curses

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

class Game():
	def __init__(self, gui):
		self.gui = gui
		self.player = None
		self.map = None
		self.state = STATE_INTRO

	def start(self):
		while True:
			self.gui.removeAllWin()
			self.gui.addWin("bg", WinBackground(100, 42, 0, 0))
			if self.state == STATE_INTRO:
				self.intro()
				self.state = STATE_GAME
			elif self.state == STATE_MENU:
				if self.menu() == False:
					break
			elif self.state == STATE_GAME:
				if self.game() == True:
					self.state = STATE_END
				else:
					break
			else:
				self.end()
				break

	def intro(self):
		self.gui.addWin("intro", WinIntro(60, 30, 20, 4))
		self.gui.draw()
		c = 0
		while 1:
			c = self.gui.getCh()
			if c == 32:
				return True

	def menu(self):
		pass

	def game(self):
		turn = 0
		self.player = Personnage("Bobby", guerrier)
		self.map = Map(MAP_1, "Level 1")
		self.gui.addWin("carte", WinMap(98, 30, 1, 1, self.map))
		self.gui.addWin("stats", WinStats(98, 3, 1, 31, self.player))
		self.gui.addWin("msg", WinMsg(98, 6, 1, 33))
		msg_scr = self.gui.getWin("msg")

		self.gui.draw()
		while True:
			c = self.gui.getCh()
			if c == ord('q'):
				return False
			r = -1
			if c == curses.KEY_UP or c == curses.KEY_DOWN \
			or c == curses.KEY_LEFT or c == curses.KEY_RIGHT:
				r = self.map.move(c)
				if r == 0:
					return True
				self.gui.draw()
				self.gui.refresh()

			if r != -1:
				if r == 'T':
					self.map.erasePos()
					t = random.randint(5, 20)
					self.player.gold += t
					msg_scr.upMsg("You found " + str(t) + " gold")
					self.gui.draw()
					self.gui.refresh()

				if r == 'E':
					msg_scr.upMsg("A black night with taunts you")
					self.gui.draw()
					time.sleep(2)
					while 1:
						t = random.randint(2, 7)
						msg_scr.upMsg("You hit the black night with "+str(t))
						self.gui.draw()
						time.sleep(1)
						t = random.randint(1, 3)
						msg_scr.upMsg("The black knight hits you : - "+str(t)+"HP")
						self.player.carac.hp -= t
						self.gui.draw()
						time.sleep(1)
						if self.player.carac.hp <= 0:
							msg_scr.upMsg("YOU DIED")
							self.gui.draw()
							time.sleep(3)
							return False
						t = random.randint(2, 8)
						msg_scr.upMsg("You hit the black night with "+str(t))
						self.gui.draw()
						time.sleep(1)
						msg_scr.upMsg("You gain 10XP")
						self.player.xp += 10
						self.gui.draw()
						time.sleep(1)
						if self.player.xp > 15 and self.player.lvl == 1:
							self.player.lvl += 1
							msg_scr.upMsg("You level UP !!!")
							self.player.carac.agilite += 2
							self.player.carac.armure += 1
							self.gui.draw()
							time.sleep(2)
						self.map.eraseMonster()
						self.gui.draw()
						break



	def end(self):
		self.gui.addWin("end", WinEnd(60, 4, 20, 4))
		self.gui.draw()
		time.sleep(5)
		return False

if __name__ == '__main__':
	pass