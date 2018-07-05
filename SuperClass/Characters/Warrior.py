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

# ./SuperClass/Characters/Warrior.py

from SuperClass.Characters.Character import Character
from random import randint

class Warrior(Character):

	'''
	--> LivingBeing Interface
	protected $totalLife
	protected $currentlyLife
	public function setLiveBeingTotalLife( $setLiveBeingTotalLife )
	public function getLiveBeingTotalLife():int
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

	def __init__( self,
				  livingBeingLife,
				  characterName,
				  warriorWeaponAttack):

		# construct abstract class character
		super().__init__( livingBeingLife, 
		                  characterName,
		                  'Warrior') 

		self.warriorWeaponAttack = warriorWeaponAttack

		self.warriorWeaponSkillLevel = 1

		self.warriorTotalAttacks = 0

		self.warriorTotalAttacksToNextWeaponSkillLevel = 3

		self.warriorDefense = 10

		self.characterVocationType = "WARRIOR"

	
	def getCharacterVocationType(self):
		return self.characterVocationType

	def getWarriorTotalAttacks(self):
		return self.warriorTotalAttacks

	def getWarriorWeaponAttack(self):
		return self.warriorWeaponAttack
	
	def getWarriorTotalAttacksToNextWeaponSkillLevel(self):
		return self.warriorTotalAttacksToNextWeaponSkillLevel

	def getWarriorWeaponSkillLevel(self):
		return self.warriorWeaponSkillLevel

	def getWarriorStatus(self):
		print("\t Character Name: " + self.getCharacterName())
		print("\t Vocation: " + self.getCharacterVocation())
		print("\t Level: {}".format(self.getCharacterCurrentlyLevel()))
		print("\t Magic Level: {}".format(self.getCharacterCurrentlyMagicLevel()))
		print('\t Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
		print("\t Currently Life: {}".format(self.getLivingBeingCurrentlyLife())) 
		print("\t Currently Mana: {}".format(self.getCharacterCurrentlyMana()))

	def getNormalAttack(self):

		print('\t Player attacked the monster.')

		baseAttackOne = int(self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack() * 0.5)
		baseAttackTwo = int(self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack() * 1.5)
		normalAttackDamage = randint(baseAttackOne, baseAttackTwo)
		
		print('\t Normal attack damage: {}'.format(normalAttackDamage))
		
		self.warriorTotalAttacks += 1

		# update weapon skill level
		if( self.getWarriorTotalAttacks() >= self.getWarriorTotalAttacksToNextWeaponSkillLevel() ):
			self.warriorWeaponSkillLevel += 1
			print('\n\t ...Weapon Skill Level UPED!')
			print('\t Currently Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
			self.warriorTotalAttacksToNextWeaponSkillLevel *= 2
			print('\t Currently total attacks: {}'.format(self.getWarriorTotalAttacks()))
			print('\t Total Attacks to next Weapon Skill Level: {}\n'.format(self.getWarriorTotalAttacksToNextWeaponSkillLevel()))


		return normalAttackDamage
	
