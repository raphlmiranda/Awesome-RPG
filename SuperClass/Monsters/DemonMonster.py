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
		self.demonMonsterLoot = randint(500, 1200)

	
	def setDemonMonsterName(self, magicMonsterName ):
		self.demonMonsterName = demonMonsterName

	def getDemonMonsterName(self):
		return self.demonMonsterName

	def getDemonMonsterExperienceForKill(self):
		return self.demonMonsterExperienceForKill

	def getDemonMonsterWeaponAttack(self):
		baseWeaponAttackOne = randint(1, 2) * self.demonAttackDamage
		baseWeaponAttackTwo = randint(3, 4) * self.demonAttackDamage
		return randint(baseWeaponAttackOne, baseWeaponAttackTwo)
	

	def demonMonsterLightSpell(self):
		baseLightSpellDamageOne = randint(1, 2) * self.demonMonsterSpellDamage
		baseLightSpellDamageTwo = randint(2, 3) * self.demonMonsterSpellDamage
		return randint(baseLightSpellDamageOne, baseLightSpellDamageTwo)
	

	def demonMonsterMediumSpell(self):
		baseMediumSpellDamageOne = randint(2, 3) * self.demonMonsterSpellDamage
		baseMediumSpellDamageTwo = randint(3, 4) * self.demonMonsterSpellDamage
		return randint(baseMediumSpellDamageOne, baseMediumSpellDamageTwo)
	

	def demonMonsterStrongSpell(self):
		baseStrongSpellDamageOne = randint(4, 5) * self.demonMonsterSpellDamage
		baseStrongSpellDamageTwo = randint(5, 6) * self.demonMonsterSpellDamage
		return randint(baseStrongSpellDamageOne, baseStrongSpellDamageTwo)

	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getDemonMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def type(self):
		return "DEMON"

	def Attack(self):
		'''
		docstring here
		'''
		attackType = randint(1, 100)

		if attackType >= 1 and attackType <= 30: # 40% chance to use weapon attack
			monsterDamage = self.getDemonMonsterWeaponAttack()
			print('\t Monster Used Weapon Attack.')
			#print('\t Light Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		elif attackType > 30 and attackType <= 60: # 30% chance to use light spell

			monsterDamage = self.demonMonsterLightSpell()
			print('\t Monster Used Light Spell.')
			#print('\t Medium Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		elif attackType > 60 and attackType <= 85: # 25% chance to use medium spell

			monsterDamage = self.demonMonsterMediumSpell()
			print('\t Monster Used Medium Spell.')
			#print('\t Medium Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		else: # 15% chance to use strong spell

			monsterDamage = self.demonMonsterStrongSpell()
			print('\t Monster Used Strong Spell.')
			#print('\t Strong Spell Damage: {}'.format(monsterDamage))
			return monsterDamage


	def takeDamage(self, getDamage):
		self.livingBeingCurrentlyLife -= getDamage

	def getMonsterLoot(self):
		return self.demonMonsterLoot

	def getMonsterExperience(self):
		return self.demonMonsterExperienceForKill
	