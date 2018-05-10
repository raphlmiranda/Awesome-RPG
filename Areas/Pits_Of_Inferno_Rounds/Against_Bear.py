############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Against Bear Round Function                #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#   Alex Galhardo Vieira   								   #
#   ICMC USP - 2018                                        #
#   São Carlos - Brazil									   #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

# Comments here

# Code Patterns
#               UPPERCASE = global variables
#               PascalCase = modules and Classes
#               camelCase = local variables, methods, attributes, parameters, arguments
#               Under_Line = functions

'''
from Root Folder Monsters -> Folder Normal Monster -> Area Pits of Inferno -> File Bear -> import Class Bear
'''
from Monsters.NormalMonsters.Pits_Of_Inferno.Bear import Bear

'''
Import Bear Life Global Variable
'''
from Global.Global_Pits_Of_Inferno import GLOBAL_BEAR_LIFE

from Functions.RolePlay import *
from Functions.NPC import NPC
from Functions.Prints import *

def Round_Against_Bear( playerAlive, Player ):

	newBearOne = Bear(GLOBAL_BEAR_LIFE)
	newBearTwo = Bear(GLOBAL_BEAR_LIFE)

	bears = []
	bears.push(newBearOne)
	bears.push(newBearTwo)

	rounds = 2
	while rounds:

		playerStillAlive = Round( Player, bears.pop() )

		if playerStillAlive:
			break
		else:
			print('\n\n\t ... YOU ARE DEAD...')
			print('\n\n\t ... GAME OVER ...\n\n')
			playerAlive = False
			return playerAlive
			break

		After_Fight( Player )
		rounds -= 1
	'''
	while True:

		playerStillAlive = Round( Player, newBearTwo )

		if playerStillAlive:
			break
		else:
			print('\n\n\t ... YOU ARE DEAD...')
			print('\n\n\t ... GAME OVER ...\n\n')
			playerAlive = False
			return playerAlive
			break

	After_Fight( Player )
	return True
	'''
