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

# ./Characters/Paladin.py

from SuperClass.Characters.Character import Character
from SuperClass.Characters.Warrior import Warrior
from random import randint

from Global.Characters_Global_Variables import   PALADIN_INITIAL_LIFE, \
												 PALADIN_ADD_LIFE_FOR_LEVEL, \
												 PALADIN_ADD_MANA_FOR_LEVEL, \
												 PALADIN_REG_LIFE_EACH_TURN, \
												 PALADIN_REG_MANA_EACH_TURN


class Paladin(Warrior):

	'''
	~ LivingBeing SuperClass
	self.totalLife
	self.currentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	deffunction getLiveBeingTotalLife()
	'''

	'''
	~ Character SuperClass
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
	~ Warrior SuperCassl
	self.warriorWeaponAttack
	self.warriorWeaponSkillLevel
	self.warriorTotalAttacks
	self.warriorTotalAttacksToNextWeaponSkillLevel

	def setWarriorWeaponAttack(self, characterWeaponAttack )
	def getWarriorWeaponAttack(self)
	def getWarriorTotalAttacksToNextWeaponSkillLevel(self)
	def getWarriorWeaponSkillLevel(self)
	'''

	def __init__(self,
				 characterName,
				 warriorWeaponAttack):

		# constructor warrior
		super().__init__( PALADIN_INITIAL_LIFE,
			              characterName,
						  'WARRIOR',
						  warriorWeaponAttack )

		self.paladinTotalMana = 100

		self.characterVocation = "Paladin"

		self.characterCurrentlyMana = 100

		self.paladinManaUsedToNextMagicLevel = 500


	def getPaladinTotalMana(self):
		return self.paladinTotalMana


	def getLightSpellManaUsed(self):
		return 150

	def getMediumSpellManaUsed(self):
		return 250

	def getStrongSpellManaUsed(self):
		return 500

	def getPaladinTotalMana(self):
		return self.paladinTotalMana


	def useLightSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getLightSpellManaUsed():

			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 1.2
			baseAttackSecond = baseAttack * 1.5

			print('\n\t ' + self.getCharacterName() + " says: Expelliarmus")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= 100

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getLightSpellManaUsed()))



	def useMediumSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getMediumSpellManaUsed():
			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 1.5
			baseAttackSecond = baseAttack * 2.0

			print('\n\t ' + self.getCharacterName() + " says: Wingardium Leviosa")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= 100

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getMediumSpellManaUsed()))



	def useStrongSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getStrongSpellManaUsed():
			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 2.2
			baseAttackSecond = baseAttack * 3.0

			print('\n\t ' + self.getCharacterName() + " says: Expecto PATRONUUUMMM")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= 100

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getStrongSpellManaUsed()))


	def Regenerate(self):

		self.livingBeingCurrentlyLife += PALADIN_REG_LIFE_EACH_TURN

		print('\t Player Regenerate {} points of life.'.format(PALADIN_REG_LIFE_EACH_TURN))

		if self.getLivingBeingCurrentlyLife() > self.getLivingBeingTotalLife():
			print('\t Health is full.')
			self.livingBeingCurrentlyLife = self.livingBeingTotalLife

		self.characterCurrentlyMana += PALADIN_REG_MANA_EACH_TURN

		print('\t Player Regenerated {} points of mana.'.format(PALADIN_REG_MANA_EACH_TURN))

		if self.getCharacterCurrentlyMana() > self.getPaladinTotalMana():
			print('\t Mana is full.')
			self.characterCurrentlyMana = self.paladinTotalMana

	def Update(self):

		if self.getCharacterCurrentlyXP() >= self.getCharacterXPToNextLevel():
			self.characterXPToNextLevel *= 2.5
			self.characterCurrentlyLevel += 1
			self.paladinTotalMana += PALADIN_ADD_MANA_FOR_LEVEL
			self.livingBeingTotalLife += PALADIN_ADD_LIFE_FOR_LEVEL
			print('\t ... PLAYER UPED LEVEL!')
			print('\t Total Life + 35 points!')
			print('\t Total Mana + 35 points!')
			print('\t Currently Player Level: {}'.format(self.getCharacterCurrentlyLevel()))
			print('\t Experince to next level: {}'.format(self.getCharacterXPToNextLevel()))
