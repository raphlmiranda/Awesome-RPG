############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#            Against Dark Torturer Round Function          #
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

from Monsters.DemonMonsters.Pits_Of_Inferno.DarkTorturer import DarkTorturer

from Global.Global_Pits_Of_Inferno import GLOBAL_DARKTORTURER_NAME, \
										  GLOBAL_DARKTORTURER_WEAPON_ATTACK, \
										  GLOBAL_DARKTORTURER_MAGIC_ATTACK, \
										  GLOBAL_DARKTORTURER_EXPERIENCE

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
