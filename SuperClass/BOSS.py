############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                   Abstract Class BOSS                    #
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


class BOSS(LivingBeing):

	'''
	--> LiveBeing Interface
	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	--> Magic Monster Interface
	self.magicMonsterSpellDamage = magicMonsterSpellDamage
	self.magicMonsterName = magicMonsterName
	self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self,
				 livingBeingLife,
				 bossMonsterName,
				 bossMonsterSpellDamage,
				 bossMonsterAttackDamage,
				 bossMonsterExperienceForKill):

		# construct living being
		super().__init__( livingBeingLife )

		self.bossMonsterName = bossMonsterName
		self.bossMonsterSpellDamage = bossMonsterSpellDamage
		self.bossMonsterAttackDamage = bossMonsterAttackDamage
		self.bossMonsterExperienceForKill = bossMonsterExperienceForKill


	def getBossMonsterExperienceForKill(self):
		return self.bossMonsterExperienceForKill
	

	def setBossMonsterSpellDamage(self, bossMonsterSpellDamage ):
		self.bossMonsterSpellDamage = bossMonsterSpellDamage
	

	def bossMonsterLightSpell(self):
		baseLightSpellDamage = randint(1, 2) * self.bossMonsterSpellDamage
		return baseSpellDamage
	

	def bossMonsterMediumSpell(self):
		baseMediumSpellDamage = randint(2, 3) * self.demonMonsterSpellDamage
		return baseMediumSpellDamage
	

	def bossMonsterStrongSpell(self):
		baseStrongSpellDamage = raindint(4, 5) * self.demonMonsterSpellDamage
		return baseStrongSpellDamage

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False