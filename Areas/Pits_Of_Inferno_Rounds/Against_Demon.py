############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Against Demon Round Function               #
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

from Monsters.DemonMonsters.Pits_Of_Inferno.Demon import Demon

from Global.Global_Pits_Of_Inferno import GLOBAL_DEMON_NAME, \
										  GLOBAL_DEMON_MAGIC_ATTACK, \
										  GLOBAL_DEMON_WEAPON_ATTACK, \
										  GLOBAL_DEMON_EXPERIENCE

from Functions.RolePlay import *

def Round_Against_Demon( playerAlive, Player ):

	newDemonOne = Demon(GLOBAL_DEMON_LIFE,
		                GLOBAL_DEMON_NAME,
		                GLOBAL_DEMON_MAGIC_ATTACK,
		                GLOBAL_DEMON_WEAPON_ATTACK,
		                GLOBAL_DEMON_EXPERIENCE)

	newDemonTwo = Demon(GLOBAL_DEMON_LIFE,
		                GLOBAL_DEMON_NAME,
		                GLOBAL_DEMON_MAGIC_ATTACK,
		                GLOBAL_DEMON_WEAPON_ATTACK,
		                GLOBAL_DEMON_EXPERIENCE)

	while True:

		playerStillAlive = Round( Player, newDemonOne )

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

		playerStillAlive = Round( Player, newDemonTwo )

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
