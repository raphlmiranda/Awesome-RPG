'''
The MIT License (MIT)

Copyright (c) 2018 Alex Galhardo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

############################################################
#                                                          #
#      				    AWESOME RPG                        #
#                                                          #
#                                                          #
#                Console Version ~ Python3                 #
#                                                          #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

'''
Code Patterns

UPPERCASE = global variables

PascalCase = Classes

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./Functions/Start.py 

from Functions.Prints import *
from Functions.Character_Creation import *
from Functions.Role_Play import *
from Functions.Select_Area import *
from Functions.NPC import *

def Start():

	'''
	While the player don't enter 0 to stop the game
	continue the game
	'''
	while True:

		'''
		This function call Prints.py inside ./Functions/
		This function say a brief introduction to the game
		'''
		Game_Introduction()

		'''
		This function call Prints.py inside ./Functions/
		This function says how to play the game
		'''
		How_To_Play_Introduction()

		'''
		This function call Character_Creation inside ./Functions/
		This function create the character name
		'''
		characterName = Create_Character_Name()

		'''
		This function call Character_Creation inside ./Functions/
		This function get character vocation
		'''
		vocationOption = Choose_Character_Vocation()

		'''
		This function call Character_Creation inside ./Functions/
		This function get character objet
		'''
		CharacterObject = Create_Character( characterName, vocationOption )

		'''
		This function call Character_Creation inside ./Functions/
		This function get character objet
		'''
		selectedArea = Select_Area()


		'''
		This function call Adventure_Game_Start inside ./Functions/
		This function start main game loop 
		'''
		Adventure_Game_Start( selectedArea, CharacterObject )

		'''
		When the game loop above is done
		'''
		print('\t Would you like to play again?')
		print('\t Enter [1] --> Yes, lets goo')
		print('\t Enter [0] --> No, I am happy whit my perfomance today')
		
		playAgain = int(input('\t Option: '))

		if playAgain == 1:
			continue
		else:
			break

	print('\n\n\t Bye Bye. Come Back Later! :D\n\n')
