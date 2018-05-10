############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                       								   #
#				 Start Function                            #
#                                                          #
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

from Functions.Prints import *
from Functions.NPC import NPC
from Functions.RolePlay import *
from Functions.SelectArea import *
from Functions.PitsOfInferno_Rounds.PitsOfInferno import *
from Functions.CharacterCreation import *

def Start():

	while True:

		Hello_Print()

		Introductions_Print()

		characterName = Character_Name()
		
		vocationOption = Choose_Vocation()

		CharacterObject = Character_Object( characterName, vocationOption )

		selectedArea = Select_Area()

		Adventure_Game_Start( selectedArea, CharacterObject )

		print('\t Play Again?')
		print('\t Enter [1] --> Yes, lets goo')
		print('\t Enter [0] --> Not now')
		playAgain = int(input('\t Option: '))

		if playAgain == 1:
			continue
		else:
			break

	print('\n\n\t Bye Bye. Come Back Later! :D\n\n')
	