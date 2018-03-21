############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Abstract Class Mage                      #
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

from SuperClass.Character import Character
from random import randint

from GLOBAL.GLOBAL_CHARACTERS import MAGE_INITIAL_MANA, MAGE_LIGHT_SPELL_MANA_USED

from GLOBAL.GLOBAL_CHARACTERS import MAGE_ADD_LIFE_FOR_LEVEL, MAGE_ADD_MANA_FOR_LEVEL

from GLOBAL.GLOBAL_CHARACTERS import MAGE_REG_LIFE_EACH_TURN, MAGE_REG_MANA_EACH_TURN

from GLOBAL.GLOBAL_CHARACTERS import MAGE_MEDIUM_SPELL_MANA_USED, MAGE_STRONG_SPELL_MANA_USED

from GLOBAL.GLOBAL_CHARACTERS import MAGE_STRONG_HEALING_MANA_USED, MAGE_MEDIUM_HEALING_MANA_USED

class Mage(Character):

	'''
	--> LivingBeing Interface
	self.totalLife
	self.currentlyLife
	
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
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

	def __init__(self,
				 livingBeingLife,
				 characterName,
				 characterVocation ):

		# character construct
		super().__init__( livingBeingLife,
						  characterName,
			              characterVocation)

		# abstract class mage attributes
		self.mageTotalMana = MAGE_INITIAL_MANA

		self.characterCurrentlyMana = MAGE_INITIAL_MANA

		self.mageManaUsedToNextMagicLevel = 100


	def getMageManaUsedToNextMagicLevel(self):
		return self.mageManaUsedToNextMagicLevel

	def getMageTotalMana(self):
		return self.mageTotalMana

	def getMageLightSpellManaUsed(self):
		return MAGE_LIGHT_SPELL_MANA_USED

	def getMageMediumSpellManaUsed(self):
		return MAGE_MEDIUM_SPELL_MANA_USED

	def getMageStrongSpellManaUsed(self):
		return MAGE_STRONG_SPELL_MANA_USED

	def getMageMediumHealingManaUsed(self):
		return MAGE_MEDIUM_HEALING_MANA_USED

	def getMageStrongHealingManaUsed(self):
		return MAGE_STRONG_HEALING_MANA_USED

	def getMageLightSpellManaUsed(self):
		return MAGE_LIGHT_SPELL_MANA_USED

	def getMageMediumSpellManaUsed(self):
		return MAGE_MEDIUM_SPELL_MANA_USED

	def getMageStrongSpellManaUsed(self):
		return MAGE_STRONG_SPELL_MANA_USED

	def Update(self):
		# update level
		if( self.getCharacterCurrentlyXP() >= self.getCharacterXPToNextLevel() ):
			self.characterCurrentlyLevel += 1
			self.characterXPToNextLevel *= 2.5
			self.livingBeingTotalLife += MAGE_ADD_LIFE_FOR_LEVEL
			self.mageTotalMana += MAGE_ADD_MANA_FOR_LEVEL
			print('\n\t ... PLAYER UPED LEVEL!')
			print('\t Total Life + {} points!'.format(MAGE_ADD_LIFE_FOR_LEVEL))
			print('\t Total Mana + {} points!'.format(MAGE_ADD_MANA_FOR_LEVEL))
			print('\t Currently Player Level: {}'.format(self.getCharacterCurrentlyLevel()))
			print('\t Experince to next level: {}'.format(self.getCharacterXPToNextLevel()))
		

		# update magic level
		if( self.getCharacterTotalManaUsed() >= self.getMageManaUsedToNextMagicLevel() ):
			self.characterCurrentlyMagicLevel += 1
			print('\n\t ...Magic Level UPED!')
			print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
			self.mageManaUsedToNextMagicLevel *= 2.5
			print('\t Mana to Use to next Magic Level: {}'.format(self.getMageManaUsedToNextMagicLevel()))
		
	

	def getNormalAttack(self):
		print('\t Player attacked the monster.')
		normalAttackDamage = randint(20, 40)
		print('\t Normal attack damage: {}'.format(normalAttackDamage))
		return normalAttackDamage
	

	# interface Spells -> weak spell 
	def useLightSpell(self):

		if( self.getCharacterCurrentlyMana() >= MAGE_LIGHT_SPELL_MANA_USED ):

			print('\t Player says: BAZINGAAA')
		
			self.characterCurrentlyMana -= MAGE_LIGHT_SPELL_MANA_USED
			self.characterTotalManaUsed += MAGE_LIGHT_SPELL_MANA_USED

			mageLightSpellDamageOne = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 7
			mageLightSpellDamageTwo = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 15
			mageLightSpellDamage = randint(mageLightSpellDamageOne, mageLightSpellDamageTwo)

			print('\t Spell Damage: {}'.format(mageLightSpellDamage))

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getMageManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.mageManaUsedToNextMagicLevel *= 2.5
				print('\t Mana to Use to next Magic Level: {}'.format(self.getMageManaUsedToNextMagicLevel()))

			return mageLightSpellDamage 
		
		else:
			print("No have sufficient mana. Need at least 100 mana for used weak spell")
		
	

	# interface Spells -> medium spell 
	def useMediumSpell(self):

		if( self.getCharacterCurrentlyMana() >= 200 ):

			print('\t Player says: RADUKEEEEEEEEN')

			self.characterCurrentlyMana -= 200
			self.characterTotalManaUsed += 200

			mageMediumSpellDamageOne = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 12
			mageMediumSpellDamageTwo = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 22
			mageMediumSpellDamage = randint(mageMediumSpellDamageOne, mageMediumSpellDamageTwo)

			print('\t Spell Damage: {}'.format(mageMediumSpellDamage))

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getMageManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.mageManaUsedToNextMagicLevel *= 2.5
				print('\t Mana to Use to next Magic Level: {}'.format(self.getMageManaUsedToNextMagicLevel()))

			return mageMediumSpellDamage
		
		else:
			print("No have sufficient mana. Need at least 100 mana for used weak spell")
		
	
	# interface Spells -> strong spell 
	def useStrongSpell(self):

		if( self.getCharacterCurrentlyMana() >= MAGE_STRONG_SPELL_MANA_USED ):

			print('\t Player says: KAMEE...HAMEEE....HAAAAAAAAAAAAAAAAA')

			self.characterCurrentlyMana -= MAGE_STRONG_SPELL_MANA_USED
			self.characterTotalManaUsed += MAGE_STRONG_SPELL_MANA_USED


			mageStrongSpellDamageOne = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 18
			mageStrongSpellDamageTwo = self.getCharacterCurrentlyLevel() * self.getCharacterCurrentlyMagicLevel() * 30
			mageStrongSpellDamage = randint(mageStrongSpellDamageOne, mageStrongSpellDamageTwo)

			print('\t Spell Damage: {}'.format(mageStrongSpellDamage))

			# update magic level
			if( self.getCharacterTotalManaUsed() >= self.getMageManaUsedToNextMagicLevel() ):
				self.characterCurrentlyMagicLevel += 1
				print('\n\t ...Magic Level UPED!')
				print('\t Currently Magic Level: {}'.format(self.getCharacterCurrentlyMagicLevel()))
				self.mageManaUsedToNextMagicLevel *= 2.5
				print('\t Mana to Use to next Magic Level: {}'.format(self.getMageManaUsedToNextMagicLevel()))

			return mageStrongSpellDamage
		
		else:
			print("No have sufficient mana. Need at least 100 mana for used weak spell")



	def Regenerate(self):

		self.livingBeingCurrentlyLife += MAGE_REG_LIFE_EACH_TURN
		print('\t Player Regenerate {} points of life.'.format(MAGE_REG_LIFE_EACH_TURN))
		# verify if life is already full
		if self.getLivingBeingCurrentlyLife() > self.getLivingBeingTotalLife():
			print('\t Health is full.')
			self.livingBeingCurrentlyLife = self.livingBeingTotalLife

		self.characterCurrentlyMana += MAGE_REG_MANA_EACH_TURN
		print('\t Player Regenerated {} points of mana.'.format(MAGE_REG_MANA_EACH_TURN))
		# verify if mana is already full
		if self.getCharacterCurrentlyMana() > self.getMageTotalMana():
			print('\t Mana is full.')
			self.characterCurrentlyMana = self.mageTotalMana

		
	
