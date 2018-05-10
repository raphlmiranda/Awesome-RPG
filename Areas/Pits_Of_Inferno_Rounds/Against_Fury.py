############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                  Against Fury Round Function             #
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

from Monsters.DemonMonsters.Pits_Of_Inferno.Fury import Fury

from Global.Global_Pits_Of_Inferno import GLOBAL_FURY_LIFE, \
										  GLOBAL_FURY_NAME, \
										  GLOBAL_FURY_WEAPON_ATTACK, \
										  GLOBAL_FURY_MAGIC_ATTACK, \
										  GLOBAL_FURY_EXPERIENCE

from Functions.RolePlay import *

def Round_Against_Fury( playerAlive, Player ):

	newFuryOne = Fury(GLOBAL_FURY_LIFE, GLOBAL_FURY_NAME, GLOBAL_FURY_WEAPON_ATTACK, GLOBAL_FURY_MAGIC_ATTACK, GLOBAL_FURY_EXPERIENCE )
	newFuryTwo = Fury(GLOBAL_FURY_LIFE, GLOBAL_FURY_NAME, GLOBAL_FURY_WEAPON_ATTACK, GLOBAL_FURY_MAGIC_ATTACK, GLOBAL_FURY_EXPERIENCE )

	while True:

		playerStillAlive = Round( Player, newFuryOne )

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

		playerStillAlive = Round( Player, newFuryTwo )

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
