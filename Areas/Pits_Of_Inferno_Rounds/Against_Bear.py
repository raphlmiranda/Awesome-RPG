############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Against Bear Round Function              #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#   MIT LICENSE                                            #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

#       Code Patterns
#
# UPPERCASE = global variables
# PascalCase = Classes
# camelCase = local variables, methods, attributes, parameters, arguments
# Under_Line = Functions and Modules

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

	#bears = []
	#bears.add(newBearOne)
	#bears.add(newBearTwo)

	#rounds = 2
	while True:

		playerStillAlive = Round( Player, newBearOne )

		if playerStillAlive:
			break
		else:
			print('\n\n\t ... YOU ARE DEAD...')
			print('\n\n\t ... GAME OVER ...\n\n')
			playerAlive = False
			return playerAlive
			break

	After_Fight( Player )


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
	
