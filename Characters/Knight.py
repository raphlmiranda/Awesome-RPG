############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                    Knight Class                          #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#   MIT LICENSE                                            #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

#       Code Patterns
#
# UPPERCASE = global variables
# PascalCase = Classes
# camelCase = local variables, methods, attributes, parameters, arguments
# Under_Line = functions

from SuperClass.Character import Character
from SuperClass.Warrior import Warrior
from random import randint

from Global.Global_Characters import KNIGHT_INITIAL_MANA, \
									 KNIGHT_ADD_MANA_FOR_LEVEL, \
									 KNIGHT_ADD_LIFE_FOR_LEVEL, \
									 KNIGHT_REG_LIFE_EACH_TURN, \
									 KNIGHT_REG_MANA_EACH_TURN

from Global.Global_Characters import KNIGHT_LIGHT_SPELL_MANA_USED, \
									 KNIGHT_MEDIUM_SPELL_MANA_USED, \
									 KNIGHT_STRONG_SPELL_MANA_USED


class Knight(Warrior):
	'''
	~ LiveBeing SuperClass
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

		# constructor warrior superclass
		super().__init__( livingBeingLife,
			              characterName,
						  characterVocation,
						  warriorWeaponAttack )

		self.knightTotalMana = 100

		self.characterVocation = "Aquiles"

		self.characterCurrentlyMana = KNIGHT_INITIAL_MANA

		self.knightManaUsedToNextMagicLevel = 200

	def getLightSpellManaUsed(self):
		return KNIGHT_LIGHT_SPELL_MANA_USED

	def getMediumSpellManaUsed(self):
		return KNIGHT_MEDIUM_SPELL_MANA_USED

	def getStrongSpellManaUsed(self):
		return KNIGHT_STRONG_SPELL_MANA_USED

	def getKnightTotalMana(self):
		return self.knightTotalMana

	def getKnightManaUsedToNextMagicLevel(self):
		return self.knightManaUsedToNextMagicLevel

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

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getKnightManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.mageManaUsedToNextMagicLevel *= 5
				print('\t Mana to Use to next Magic Level: {}\n'.format(self.getMageManaUsedToNextMagicLevel()))


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

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getKnightManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.knightManaUsedToNextMagicLevel *= 5
				print('\t Mana to Use to next Magic Level: {}\n'.format(self.getKnightManaUsedToNextMagicLevel()))


			return spellDamage

		else:
			print('\t Dont have sufficient mana! Need at least {} mana points.'.format(self.getMediumSpellManaUsed()))
			return 0


	def useStrongSpell(self):

		if self.getCharacterCurrentlyMana() >= self.getStrongSpellManaUsed():

			baseAttack = self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack()
			baseAttackFirst = int(baseAttack * 2.2)
			baseAttackSecond = int(baseAttack * 3.0)

			print('\n\t ' + self.getCharacterName() + " says: EXORI GRAN")

			spellDamage = randint(baseAttackFirst, baseAttackSecond)

			print('\t Spell Damage: {}'.format(spellDamage))

			self.characterCurrentlyMana -= self.getStrongSpellManaUsed()

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getKnightManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.mageManaUsedToNextMagicLevel *= 5
				print('\t Mana to Use to next Magic Level: {}\n'.format(self.getMageManaUsedToNextMagicLevel()))

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
			print('\n\t ... PLAYER UPED LEVEL!')
			print('\t Total Life + {} points!'.format(KNIGHT_ADD_LIFE_FOR_LEVEL))
			print('\t Total Mana + {} points!'.format(KNIGHT_ADD_MANA_FOR_LEVEL))
			print('\t Currently Player Level: {}'.format(self.getCharacterCurrentlyLevel()))
			print('\t Experince to next level: {}'.format(self.getCharacterXPToNextLevel()))

		if self.getWarriorTotalAttacks() >= self.getWarriorTotalAttacksToNextWeaponSkillLevel():
			print("\t ...Weapon Skill UPED!")
			print('\t Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
			self.warriorTotalAttacksToNextWeaponSkillLevel *= 2
			print('\t Total Hits to next Level: {}'.format(self.getWarriorTotalAttacksToNextWeaponSkillLevel()))
