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

UPPERCASE = Global Variables

PascalCase = Classes and Folders

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./SuperClass/Characters/Character.py

from SuperClass.LivingBeing import LivingBeing
from random import randint
from SuperClass.GameStatistics import GameStatistics

# abstract class that knights, paladins, druids and sorcerer must inherit 
class Character(LivingBeing):

	'''
	--> Living Being Interface
	self.livingBeingTotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( setLiveBeingTotalLife )
	def getLiveBeingTotalLife()
	'''

	def __init__( self,
				  livingBeingLife,
		          characterName,
		          characterVocation):

		super().__init__( livingBeingLife )

		self.characterName = characterName
		self.characterVocation = characterVocation

		self.characterCurrentlyLevel = 1
		self.characterCurrentlyXP = 0
		self.characterXPToNextLevel = 100

		self.characterCurrentlyMagicLevel = 1
		self.characterTotalManaUsed = 0

		self.characterCurrentlyMana = 0

		self.characterCurrentlyHealthPotions = 0
		self.characterCurrentlyManaPotions = 0

		self.characterCurrentlyGoldCoins = 0

	def getCharacterCurrentlyMana(self):
		return self.characterCurrentlyMana

	def getCharacterVocationType(self):
		if self.characterVocation == 'Warrior':
			return "WARRIOR"
		else:
			return "MAGE"

	def getCharacterName(self):
		return self.characterName

	def getCharacterCurrentlyHealthPotions(self):
		return self.characterCurrentlyHealthPotions

	def getCharacterCurrentlyManaPotions(self):
		return self.characterCurrentlyManaPotions

	def toString(self):
		print("\t Character Name: " + self.getCharacterName())
		print("\t Vocation: " + self.getCharacterVocation())
		print("\t Level: {}".format(self.getCharacterCurrentlyLevel()))
		print("\t Magic Level: {}".format(self.getCharacterCurrentlyMagicLevel()))
		print("\t Currently Life: {}".format(self.getLivingBeingCurrentlyLife()))
		print("\t Currently Mana: {}".format(self.getCharacterCurrentlyMana()))

	def getCharacterRoundStatus(self):
		print('\n\t --- PLAYER STATUS ---')
		print('\t Life: {}'.format(self.getLivingBeingCurrentlyLife()))
		print('\t Mana: {}'.format(self.getCharacterCurrentlyMana()))
		print('\t Health Potions: {}'.format(self.getCharacterCurrentlyHealthPotions()))
		print('\t Mana Potions: {}'.format(self.getCharacterCurrentlyManaPotions()))

	def getCharacterCurrentlyGoldCoins(self):
		return self.characterCurrentlyGoldCoins

	def getCharacterTotalManaUsed(self):
		return self.characterTotalManaUsed

	def getCharacterVocation(self):
		return self.characterVocation;

	def getCharacterCurrentlyMagicLevel(self):
		return self.characterCurrentlyMagicLevel

	def getCharacterCurrentlyLevel(self):
		return self.characterCurrentlyLevel

	def getCharacterXPToNextLevel(self):
		return self.characterXPToNextLevel

	def getCharacterCurrentlyGoldCoins(self):
		return self.characterCurrentlyGoldCoins

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def addHealthPotions(self, healthPotions):
		self.characterCurrentlyHealthPotions += healthPotions

	def addManaPotions(self, manaPotions):
		self.characterCurrentlyManaPotions += manaPotions

	def useHealthPotion(self):

		while True:

			print('\n\t You have: {} health potions.'.format(self.getCharacterCurrentlyHealthPotions()))
			print('\t Enter 0 to stop use health potions.')
			healthPotionsToUse = int(input('\t How many Health Potions you want to use: '))

			if healthPotionsToUse == 0:
				break

			elif healthPotionsToUse <= self.getCharacterCurrentlyHealthPotions():
				GameStatistics.totalHealthPotionsUsed += healthPotionsToUse
				print('\n')
				while healthPotionsToUse != 0:
					healthCure = randint(75, 125)
					self.livingBeingCurrentlyLife += healthCure
					self.characterCurrentlyHealthPotions -= 1
					print('\t You healed {} points of life!'.format(healthCure))
					healthPotionsToUse -= 1
			else:
				print('\n\t You dont have sufficient health potions!')
				continue

	def useManaPotion(self):

		while True:

			print('\n\t You have: {} mana potions.'.format(self.getCharacterCurrentlyManaPotions()))
			
			print('\t Enter 0 to stop use mana potions.')
			
			manaPotionsToUse = int(input('\t How many Mana Potions you want to use: '))

			if manaPotionsToUse == 0:
				break			

			elif manaPotionsToUse <= self.getCharacterCurrentlyManaPotions():
				GameStatistics.totalHealthPotionsUsed += manaPotionsToUse
				print('\n')
				while manaPotionsToUse != 0:
					manaCure = randint(75, 125)
					self.characterCurrentlyMana += manaCure
					self.characterCurrentlyManaPotions-= 1
					print('\t You healed {} points of mana!'.format(manaCure))
					manaPotionsToUse -= 1
			else:
				print('\n\t You dont have sufficient mana potions!')
				continue

	def takeDamage(self, monsterDamage ):
		GameStatistics.totalDamageTakenFromMonsters += monsterDamage
		self.livingBeingCurrentlyLife -= monsterDamage
		print('\t Monster Damage: {}'.format(monsterDamage))
		
	def getLootMonster(self, lootMonster ):
		GameStatistics.totalGoldCoinsLooted += lootMonster
		self.characterCurrentlyGoldCoins += lootMonster

	def getMonsterExperience(self, experienceMonster ):
		self.characterCurrentlyXP += experienceMonster

	def usedGoldCoinsInNPC(self, usedGoldCoinsInNPC ):
		GameStatistics.totalGoldCoinsUsed += usedGoldCoinsInNPC
		self.characterCurrentlyGoldCoins -= usedGoldCoinsInNPC

	def getCharacterCurrentlyXP(self):
		return self.characterCurrentlyXP

