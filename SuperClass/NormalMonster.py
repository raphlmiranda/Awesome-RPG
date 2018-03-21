############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   ##                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                   Normal Monster Abstract Class          #
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
class NormalMonster(LivingBeing):

	'''
	--> LiveBeing Interface
	self.totalLife
	self.currentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	def __init__(self,
					livingBeingLife, 
					normalMonsterName, 
		    		normalMonsterAttackDamage,
				 	normalMonsterExperienceForKill):

		# construct living being
		super().__init__( livingBeingLife )

		self.normalMonsterAttackDamage = normalMonsterAttackDamage
		self.normalMonsterName = normalMonsterName
		self.normalMonsterExperienceForKill = normalMonsterExperienceForKill
		self.normalMonsterLoot = randint(50, 200)

	def setNormalMonsterName(self,  normalMonsterName ):
		self.normalMonsterName = normalMonsterName
	
	
	def getNormalMonsterName(self):
		return self.normalMonsterName;
	

	def setNormalMonsterExperienceForKill(self,  normalMonsterExperienceForKill ):
		self.normalMonsterExperienceForKill = normalMonsterExperienceForKill
	

	def getNormalMonsterExperienceForKill(self):
		return self.normalMonsterExperienceForKill
	

	def setNormalMonsterAttackDamage(self, normalMonsterAttackDamage ):
		self.normalMonsterAttackDamage = normalMonsterAttackDamage
	

	def normalMonsterAttack(self):
		return randint(1, 2) * self.normalMonsterAttackDamage
	

	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getNormalMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))
	
	def takeDamage(self, getDamage):
		self.livingBeingCurrentlyLife -= getDamage
		
	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def Attack(self):
		baseAttackOne = int(self.normalMonsterAttackDamage * 0.5)
		baseAttackTwo = int(self.normalMonsterAttackDamage * 1.5)
		return randint(baseAttackOne, baseAttackTwo)

	def getMonsterExperience(self):
		return self.normalMonsterExperienceForKill

	def getMonsterLoot(self):
		return self.normalMonsterLoot
