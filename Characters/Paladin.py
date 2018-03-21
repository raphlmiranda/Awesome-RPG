############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Class Paladin                            #
#                                                          #
#   aleexgvieira@gmail.com                                 #
#   github.com/AlexGalhardo                                #
#   Alex Galhardo Vieira 								   #
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

from SuperClass.Character import Character
from SuperClass.Warrior import Warrior
from random import randint

from GLOBAL.GLOBAL_CHARACTERS import PALADIN_ADD_LIFE_FOR_LEVEL
from GLOBAL.GLOBAL_CHARACTERS import PALADIN_ADD_MANA_FOR_LEVEL
from GLOBAL.GLOBAL_CHARACTERS import PALADIN_REG_LIFE_EACH_TURN
from GLOBAL.GLOBAL_CHARACTERS import PALADIN_REG_MANA_EACH_TURN


class Paladin(Warrior):

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
	--> Warrior Interface
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
				 livingBeingLife,
				 characterName,
				 characterVocation, 
				 warriorWeaponAttack):

		# construct warrior
		super().__init__( livingBeingLife,
			              characterName, 
						  characterVocation, 
						  warriorWeaponAttack ) 

		self.paladinTotalMana = 100

		self.characterVocation = "Robin Hood"

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

			print('\n\t ' + self.getCharacterName() + " says: EXORI ICO")

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

			print('\n\t ' + self.getCharacterName() + " says: EXORI")

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

			print('\n\t ' + self.getCharacterName() + " says: EXORI ICO")

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