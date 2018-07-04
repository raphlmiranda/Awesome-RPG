############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#           Against Morgaroth Boss Round Function          #
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

from Monsters.Bosses.Morgaroth import Morgaroth

from Global.Global_Pits_Of_Inferno import GLOBAL_MORGAROTH_LIFE, \
								   		  GLOBAL_MORGAROTH_NAME, \
								   		  GLOBAL_MORGAROTH_WEAPON_ATTACK, \
								   		  GLOBAL_MORGAROTH_MAGIC_ATTACK, \
								   	      GLOBAL_MORGAROTH_EXPERIENCE

from Functions.RolePlay import *


def Round_Against_Morgaroth( playerAlive, Player ):

	newMorgaroth = Morgaroth(GLOBAL_MORGAROTH_LIFE,
		                     GLOBAL_MORGAROTH_NAME,
		                     GLOBAL_MORGAROTH_MAGIC_ATTACK,
		                     GLOBAL_MORGAROTH_WEAPON_ATTACK,
		                     GLOBAL_MORGAROTH_EXPERIENCE)

	while True:

		print('\n\n\t XXXXXXXXXXXXXXXXXXXXX')
		print('\t .... BOSS FIGHT .... ')
		print('\t XXXXXXXXXXXXXXXXXXXXX')

		print('\n\n\t ......................')
		print('\t ......................')
		print('\t ...HAHAHAHAHAHAHAHAAH!')
		print('\t ......................')
		print('\t ......................')
		print('\t ......I will kill you!')

		playerStillAlive = Round( Player, newMorgaroth )

		if playerStillAlive:
			break
		else:
			print('\n\n\t ... YOU ARE DEAD...')
			print('\n\n\t ... GAME OVER ...\n\n')
			playerAlive = False
			return playerAlive
			break

	return True
