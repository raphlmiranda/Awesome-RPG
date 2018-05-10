############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#           Against Morgaroth BOSS Round Function          #
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

from Monsters.BOSS.Morgaroth import Morgaroth

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_MORGAROTH_LIFE
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_MORGAROTH_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_MORGAROTH_WEAPON_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_MORGAROTH_MAGIC_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_MORGAROTH_EXPERIENCE

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