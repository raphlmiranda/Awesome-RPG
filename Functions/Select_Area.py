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

# ./Functions/Select_Area.py


from Areas.PitsOfInfernoRounds.Pits_Of_Inferno import *


def Select_Area():

	while True:

		print('\n\t --- Chose a area to play ---')
		print('\n\t Enter [1] --> Pits of Inferno --> EASY')
		print('\t Enter [2] --> Inquisition Quest --> MEDIUM')
		print('\t Enter [3] --> Ferumbras Tower --> HARD')
		print('\t Enter [4] --> Play all areas --> Full Game Experience')
		
		areaOption = int(input('\t Area Option: '))

		if areaOption < 1 or areaOption > 4:
			print('\t Choose a valid option!')
			continue
		elif areaOption == 1:
			return 1
			break
		elif areaOption == 2:
			return 2
			break
		elif areaOption == 3:
			return 3
			break
		else:
			return 4
			break

def Adventure_Game_Start( selectedArea, Player ):

	if selectedArea == 1:
		Pits_Of_Inferno_Start_Game( Player )

	elif selectedArea == 2:
		Game_Of_Thrones_Start_Game( Player )

	elif selectedArea == 3:
		Star_Wars__Start_Game( Player )
	
	else:
		Full_Game_Start( Player )
