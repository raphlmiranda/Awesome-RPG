
############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Sorcerer Class                           #
#                                                          #
#   aleexgvieira@gmail.com                                 #
#   github.com/AlexGalhardo                                #
#   Alex Galhardo Vieira
#   ICMC USP - 2018                                        #
############################################################

#!/usr/bin/python3
# coding: utf-8

# Comments here

# Code Patterns
#               UPPERCASE = global variables
#               PascalCase = modules and Classes
#               camelCase = local variables, methods, attributes, parameters, arguments
#               Under_Line = functions

from SuperClass.Mage import Mage 

class Sorcerer(Mage):

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

	def Update(self):

		if self.getCharacterCurrentlyXP() >= self.getCharacterXPToNextLevel():
			self.characterXPToNextLevel *= 2.5
			self.characterCurrentlyLevel += 1
			self.mageTotalMana += 75
			self.livingBeingTotalLife += 25
			print('\t ... PLAYER UPED LEVEL!')
			print('\t Total Life + 30 points!')
			print('\t Total Mana + 15 points!')
			print('\t Currently Player Level: {}'.format(self.getCharacterCurrentlyLevel()))
			print('\t Experince to next level: {}'.format(self.getCharacterXPToNextLevel()))