############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Select Area Function                 #
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
# Under_Line = functions

'''
from modules.area.file import *
'''
from Areas.Pits_Of_Inferno_Rounds.Pits_Of_Inferno import *
from Areas.Game_Of_Thrones_Rounds.Game_Of_Thrones import *
from Areas.Star_Wars_Rounds.Star_Wars import *

def Select_Area():

	while True:

		print('\n\t Chose a Area Below')
		print('\t Enter [1] --> Pits of Inferno [EASY]')
		print('\t Enter [2] --> Inquisition Quest [MEDIUM]')
		print('\t Enter [3] --> Ferumbras Tower [HARD]')
		areaOption = int(input('\t Option: '))

		if areaOption < 1 or areaOption > 3:
			print('\t Choose a valid option!')
			continue
		elif areaOption == 1:
			return 1
			break
		elif areaOption == 2:
			return 2
			break
		else:
			return 3
			break

def Adventure_Game_Start( selectedArea, Player ):

	if selectedArea == 1:
		Pits_Of_Inferno_Start_Game( Player )

	elif selectedArea == 2:
		Game_Of_Thrones_Start_Game( Player )

	else:
		Star_Wars__Start_Game( Player )
