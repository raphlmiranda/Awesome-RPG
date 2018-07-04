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
from random import randint

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
		self.bossMonsterLoot = randint(2000, 5000)


	def getBOSSMonsterName(self):
		return self.bossMonsterName

	def getBOSSMonsterExperienceForKill(self):
		return self.bossMonsterExperienceForKill
	
	def getBOSSMonsterAttackDamage(self):
		return self.bossMonsterAttackDamage

	def getBOSSMonsterLightSpell(self):
		baseLightSpellDamageOne = randint(1, 2) * self.bossMonsterSpellDamage
		baseLightSpellDamageTwo = randint(2, 3) * self.bossMonsterSpellDamage
		return randint(baseLightSpellDamageOne, baseLightSpellDamageTwo)

	def getBOSSMonsterMediumSpell(self):
		baseMediumSpellDamageOne = randint(1, 2) * self.bossMonsterSpellDamage
		baseMediumSpellDamageTwo = randint(2, 3) * self.bossMonsterSpellDamage
		return randint(baseMediumSpellDamageOne, baseMediumSpellDamageTwo)
	

	def getBOSSMonsterStrongSpell(self):
		baseStrongtSpellDamageOne = randint(1, 2) * self.bossMonsterSpellDamage
		baseStrongSpellDamageTwo = randint(2, 3) * self.bossMonsterSpellDamage
		return randint(baseStrongtSpellDamageOne, baseStrongSpellDamageTwo)

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getBOSSMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def Attack(self):
		'''
		docstring here
		'''
		attackType = randint(1, 100)

		if attackType >= 1 and attackType <= 30: # 40% chance to use weapon attack
			monsterDamage = self.getBOSSMonsterAttackDamage()
			print('\t Monster Used Weapon Attack.')
			#print('\t Light Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		elif attackType > 30 and attackType <= 60: # 30% chance to use light spell

			monsterDamage = self.getBOSSMonsterLightSpell()
			print('\t Monster Used Light Spell.')
			#print('\t Medium Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		elif attackType > 60 and attackType <= 85: # 25% chance to use medium spell

			monsterDamage = self.getBOSSMonsterMediumSpell()
			print('\t Monster Used Medium Spell.')
			#print('\t Medium Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		else: # 15% chance to use strong spell

			monsterDamage = self.getBOSSMonsterStrongSpell()
			print('\t Monster Used Strong Spell.')
			#print('\t Strong Spell Damage: {}'.format(monsterDamage))
			return monsterDamage


	def takeDamage(self, getDamage):
		self.livingBeingCurrentlyLife -= getDamage

	def getMonsterLoot(self):
		return self.bossMonsterLoot

	def getMonsterExperience(self):
		return self.bossMonsterExperienceForKill

	def type(self):
		return "BOSS"