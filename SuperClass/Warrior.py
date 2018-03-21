############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   ##                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Abstract Class Warrior                   #
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
				  characterVocation, 
				  warriorWeaponAttack ):

		# construct abstract class character
		super().__init__( livingBeingLife, 
		                  characterName, 
		                  characterVocation ) # construct character 

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
	
