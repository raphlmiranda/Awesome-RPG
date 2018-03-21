############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Characters Creation Function             #
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

from SuperClass.Character import Character
from SuperClass.Warrior import Warrior
from random import randint

from GLOBAL.GLOBAL_CHARACTERS import KNIGHT_INITIAL_MANA
from GLOBAL.GLOBAL_CHARACTERS import KNIGHT_ADD_MANA_FOR_LEVEL, KNIGHT_ADD_LIFE_FOR_LEVEL
from GLOBAL.GLOBAL_CHARACTERS import KNIGHT_REG_LIFE_EACH_TURN, KNIGHT_REG_MANA_EACH_TURN

class Knight(Warrior):

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

		self.knightTotalMana = 100

		self.characterVocation = "Aquiles"

		self.characterCurrentlyMana = KNIGHT_INITIAL_MANA

		self.knightManaUsedToNextMagicLevel = 500

	def getLightSpellManaUsed(self):
		return 100

	def getMediumSpellManaUsed(self):
		return 200

	def getStrongSpellManaUsed(self):
		return 340

	def getKnightTotalMana(self):
		return self.knightTotalMana

	def getCharacterCurrentlyMana(self):
		return self.characterCurrentlyMana

	def useLightSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getLightSpellManaUsed():

			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 1.2
			baseAttackSecond = baseAttack * 1.5

			print('\n\t ' + self.getCharacterName() + " says: EXORI ICO")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= self.getLightSpellManaUsed()

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getLightSpellManaUsed()))


	def useMediumSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getMediumSpellManaUsed():

			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 1.7
			baseAttackSecond = baseAttack * 2.5

			print('\n\t ' + self.getCharacterName() + " says: EXORI")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= self.getMediumSpellManaUsed()

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getMediumSpellManaUsed()))
			return 0


	def useStrongSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getStrongSpellManaUsed():

			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = baseAttack * 2.2
			baseAttackSecond = baseAttack * 3.0

			print('\n\t ' + self.getCharacterName() + " says: EXORI GRAN")

			spellDamage = randint(baseAttackFirst, baseAttackFirst)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= self.getStrongSpellManaUsed()

			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getStrongSpellManaUsed()))
			return 0


	def Regenerate(self):

		self.livingBeingCurrentlyLife += KNIGHT_REG_LIFE_EACH_TURN
		print('\t Player Regenerate {} points of life.'.format(KNIGHT_REG_LIFE_EACH_TURN))
		if self.getLivingBeingCurrentlyLife() > self.getLivingBeingTotalLife():
			print('\t Health is full.')
			self.livingBeingCurrentlyLife = self.livingBeingTotalLife

		self.characterCurrentlyMana += KNIGHT_REG_MANA_EACH_TURN
		print('\t Player Regenerated {} points of mana.'.format(KNIGHT_REG_MANA_EACH_TURN))
		if self.getCharacterCurrentlyMana() > self.getKnightTotalMana():
			print('\t Mana is full.')
			self.characterCurrentlyMana = self.knightTotalMana

	def Update(self):

		if self.getCharacterCurrentlyXP() >= self.getCharacterXPToNextLevel():
			self.characterXPToNextLevel *= 2
			self.characterCurrentlyLevel += 1
			self.knightTotalMana += KNIGHT_ADD_MANA_FOR_LEVEL
			self.livingBeingTotalLife += KNIGHT_ADD_LIFE_FOR_LEVEL
			print('\t ... PLAYER UPED LEVEL!')
			print('\t Total Life + {} points!'.format(KNIGHT_ADD_LIFE_FOR_LEVEL))
			print('\t Total Mana + {} points!'.format(KNIGHT_ADD_MANA_FOR_LEVEL))
			print('\t Currently Player Level: {}'.format(self.getCharacterCurrentlyLevel()))
			print('\t Experince to next level: {}'.format(self.getCharacterXPToNextLevel()))

		if self.getWarriorTotalAttacks() >= self.getWarriorTotalAttacksToNextWeaponSkillLevel():
			print("\t ...Weapon Skill UPED!")
			print('\t Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
			self.warriorTotalAttacksToNextWeaponSkillLevel *= 2
			print('\t Total Hits to next Level: {}'.format(self.getWarriorTotalAttacksToNextWeaponSkillLevel()))

	