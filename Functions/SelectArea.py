############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                Select Area Functions                     #
#                                                          #
#   aleexgvieira@gmail.com                                 #
#   github.com/AlexGalhardo                                #
#   Alex Galhardo Vieira                                   #
############################################################

#!/usr/bin/python3
# coding: utf-8

# Comments here

# Code Patterns
#               UPPERCASE = global variables
#               PascalCase = modules and Classes
#               camelCase = local variables, methods, attributes, parameters, arguments
#               Under_Line = functions


from Functions.PitsOfInferno_Rounds.PitsOfInferno import *
from Functions.GameOfThrones_Rounds.GameOfThrones import *
from Functions.StarWars_Rounds.StarWars import *

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