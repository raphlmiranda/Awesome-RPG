############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                Prints Functions                          #
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


from Functions.NPC import NPC


def Hello_Print():
	print('\n\t\t Alex Galhardo Vieira')
	print('\t\t github.com/AlexGalhardo')
	print('\t\t aleexgvieira@gmail.com')
	print('\t\t ICMC USP - 2018')
	print('\t\t São Carlos - Brazil')
	print("\n\n\n\t\t Welcome to Tibians RPG.")
	print("\t\t A Fan Game Based in Tibia Online.")


def Introductions_Print():

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