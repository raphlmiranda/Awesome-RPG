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

# ./Functions/Prints.py 

from Functions.NPC import NPC

'''
Game introductions
'''
def Game_Introduction():
	print('\n\t\t Alex Galhardo Vieira')
	print('\t\t github.com/AlexGalhardo')
	print('\t\t aleexgvieira@gmail.com')
	print("\n\t\t Welcome to Awesome RPG\n")
	print("\t\t A Fan Game Inspired in \n\t\t Tibia Online and\n\t\t Final Fantasy Classics.")



'''
Introductions to how to play the game
'''
def How_To_Play_Introduction():
	print('\n\t\t Introductions here')



def Fight_Round_Print():
	print('\n\t --------> FIGHT ROUND <--------')

def Round_Status_Print():
	print('\n\t -------- ROUND STATUS --------')

def Player_Defeated_Monster():
	print('\n\n\t ....Player Defeated the Monster!\n\n')



def After_Fight( Player ):
	Player_Defeated_Monster()
	NPC( Player )
	Fight_Round_Print()