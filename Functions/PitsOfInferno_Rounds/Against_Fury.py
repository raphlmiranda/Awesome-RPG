############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Against Fury Round Function                #
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

from Monsters.DemonMonster.Fury import Fury

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_FURY_LIFE
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_FURY_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_FURY_WEAPON_ATTACK 
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_FURY_MAGIC_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_FURY_EXPERIENCE 

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