############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#             Against DarkTorturer Round Function          #
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

from Monsters.DemonMonster.DarkTorturer import DarkTorturer

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_LIFE
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_WEAPON_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_MAGIC_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_EXPERIENCE

from Functions.RolePlay import *

def Round_Against_DarkTorturer( playerAlive, Player ):

	newDarkTorturerOne = DarkTorturer(GLOBAL_DARKTORTURER_LIFE,
									  GLOBAL_DARKTORTURER_NAME,
									  GLOBAL_DARKTORTURER_MAGIC_ATTACK,
									  GLOBAL_DARKTORTURER_WEAPON_ATTACK,
									  GLOBAL_DARKTORTURER_EXPERIENCE)

	newDarkTorturerTwo = DarkTorturer(GLOBAL_DARKTORTURER_LIFE,
									  GLOBAL_DARKTORTURER_NAME,
									  GLOBAL_DARKTORTURER_MAGIC_ATTACK,
									  GLOBAL_DARKTORTURER_WEAPON_ATTACK,
									  GLOBAL_DARKTORTURER_EXPERIENCE)

	while True:

		playerStillAlive = Round( Player, newDarkTorturerOne )

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

		playerStillAlive = Round( Player, newDarkTorturerTwo )

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