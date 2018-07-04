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

PascalCase = Classes and Folders

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./Characters/Druid.py

from SuperClass.Characters.Mage import Mage 

class Druid(Mage):

	'''
	--> LivingBeing Interface
	self.totalLife
	self.currentlyLife

	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	deffunction getLiveBeingTotalLife()
	'''

	'''
	--> Character Interface
	self.characterName
	self.characterVocation

	self.currentlyLevel
	self.currentlyXP
	self.xpToNextLevel

	self.totalMana
	self.currentlyMana

	self.totalCapacity
	self.currentlyCapacity

	self.magicLevel
	self.manaUsedToNextMagicLevel
	self.totalManaUsed

	def getCharacterVocation()
	def getCharacterXPToNextLevel()
	def getCharacterCurrentlyMagicLevel()
	def getCharacterCurrentlyLevel()
	def getCharacterCurrentlyMana()
	def getCharacterCurrentlyLife()
	def getCharacterCurrentlyXP()
	def getCharacterTotalManaUsedToNextLevel()
	def getCharacterXPToNextLevel()
	'''

	'''
	--> Mage Interface

	'''

	def __init__(self,
				 livingBeingLife,
				 characterName,
				 characterVocation ):

		# construct mage
		super().__init__( livingBeingLife,
						  characterName, 
			              characterVocation )


	def __str__():
		print("Character Name: " + self.getCharacterName())
		print("Vocation: " + self.getCharacterVocation())
		print("Level: ".format(self.getCharacterCurrentlyLevel()))
		print("Magic Level: ".format(self.getCharacterMagicLevel()))
		print("Currently Life: ".format(self.getLivingBeingCurrentlyLife()))
		print("Currently Mana: ".format(self.getCharacterCurrentlyMana()))
		print("Total Capacity: ".format(self.getCharacterCurrentlyCapacity()))
	
	def Status(self):
		print("\t Character Name: " + self.getCharacterName())
		print("\t Vocation: " + self.getCharacterVocation())
		print("\t Level: ".format(self.getCharacterCurrentlyLevel()))
		print("\t Magic Level: ".format(self.getCharacterCurrentlyMagicLevel()))
		print("\t Currently Life: ".format(self.getLivingBeingCurrentlyLife())) 
		print("\t Currently Mana: ".format(self.getMageCurrentlyMana()))
		print("\t Total Capacity: ".format(self.getMageCurrentlyCapacity()))