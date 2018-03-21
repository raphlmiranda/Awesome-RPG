############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   ##                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Abstract Class Living Being                #
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

# class that both characters and monsters must inherit 
class LivingBeing():

	def __init__(self, 
		         livingBeingLife ):

		self.livingBeingTotalLife = livingBeingLife
		self.livingBeingCurrentlyLife = livingBeingLife

	def setLivingBeingTotalLife(self, setLivingBeingTotalLife ):
		self.livingBeingTotalLife = setLivingBeingTotalLife

	def getLivingBeingTotalLife(self):
		return self.livingBeingTotalLife

	def getLivingBeingCurrentlyLife(self):
		return self.livingBeingCurrentlyLife