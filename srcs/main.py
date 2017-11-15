#!/usr/bin/env/ python3.4
#-*- coding: utf-8 -*-
#
#Launch the app

try:
	import sys
	from gui.screen import Screen
	from game.game import Game

except ImportError as e:
	print("Failed to load modules : {0}".format(e))
	sys.exit(2)

def main():
	screen = Screen()
	game = Game(screen)
	game.start()

	screen.end()

if __name__ == '__main__':
	sys.exit(main())