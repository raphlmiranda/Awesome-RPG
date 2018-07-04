############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                  Against Warlock Round Function          #
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

from Monsters.MagicMonsters.Pits_Of_Inferno.Warlock import Warlock

from Global.Global_Pits_Of_Inferno import GLOBAL_WARLOCK_LIFE

from Functions.RolePlay import *
from Functions.NPC import NPC
from Functions.Prints import *

def Round_Against_Warlock( playerAlive, Player ):

	newWarlockOne = Warlock(GLOBAL_WARLOCK_LIFE)
	newWarlockTwo = Warlock(GLOBAL_WARLOCK_LIFE)

	while True:

		playerStillAlive = Round( Player, newWarlockOne )

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

		playerStillAlive = Round( Player, newWarlockTwo )

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
