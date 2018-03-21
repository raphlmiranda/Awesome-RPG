############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Abstract Class Demon Monster         #
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


from SuperClass.LivingBeing import LivingBeing
from random import randint

# abstract class that knights, paladins, druids and sorcerer must inherit 
class DemonMonster(LivingBeing):

	'''
	--> Living Being Interface
	self.totalLife
	self.currentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	def __init__(self,
				 livingBeingLife,
				 demonMonsterName,
				 demonMonsterSpellDamage,
				 demonMonsterAttackDamage,
				 demonMonsterExperienceForKill):

		# construct super class living being
		super().__init__( livingBeingLife )

		self.demonMonsterName = demonMonsterName
		self.demonMonsterSpellDamage = demonMonsterSpellDamage
		self.demonAttackDamage = demonMonsterAttackDamage
		self.demonMonsterExperienceForKill = demonMonsterExperienceForKill

	
	def setDemonMonsterName(self, magicMonsterName ):
		self.demonMonsterName = demonMonsterName

	def getDemonMonsterName(self):
		return self.demonMonsterName
	

	def setDemonMonsterExperienceForKill(self, demonMonsterExperienceForKill ):
		self.demonMonsterExperienceForKill = demonMonsterExperienceForKill
	

	def getDemonMonsterExperienceForKill(self):
		return self.demonMonsterExperienceForKill
	

	def setDemonMonsterSpellDamage(self, demonMonsterSpellDamage ):
		self.demonMonsterSpellDamage = demonMonsterSpellDamage
	

	def demonMonsterLightSpell(self):
		baseLightSpellDamage = randint(1, 2) * self.demonMonsterSpellDamage
		return baseSpellDamage
	

	def demonMonsterMediumSpell(self):
		baseMediumSpellDamage = randint(2, 3) * self.demonMonsterSpellDamage
		return baseMediumSpellDamage
	

	def demonMonsterStrongSpell(self):
		baseStrongSpellDamage = raindint(4, 5) * self.demonMonsterSpellDamage
		return baseStrongSpellDamage

	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getDemonMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False
	