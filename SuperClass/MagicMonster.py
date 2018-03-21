############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   ##                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                  Abstract Class Magic Monster            #
#														   #
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
class MagicMonster(LivingBeing):

	'''
	--> LiveBeing Interface
	protected $totalLife
	protected $currentlyLife
	public function setLiveBeingTotalLife( $setLiveBeingTotalLife )
	public function getLiveBeingTotalLife():int
	'''
	def __init__(self,
		         livingBeingLife,
		         magicMonsterName,
		         magicMonsterSpellDamage,
		         magicMonsterExperienceForKill):

		# construct living being
		super().__init__( livingBeingLife )

		self.magicMonsterSpellDamage = magicMonsterSpellDamage
		self.magicMonsterName = magicMonsterName
		self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
		self.magicMonsterLoot = randint(200, 500)

	
	def setMagicMonsterName(self,  magicMonsterName ):
		self.magicMonsterName = magicMonsterName
	

	def getMagicMonsterName(self):
		return self.magicMonsterName
	

	def setMagicMonsterExperienceForKill(self,  magicMonsterExperienceForKill ):
		self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	

	def getMagicMonsterExperienceForKill(self):
		return self.magicMonsterExperienceForKill
	

	def setMagicMonsterSpellDamage(self, magicMonsterSpellDamage ):
		self.magicMonsterSpellDamage = magicMonsterSpellDamage;
	

	def magicMonsterLightSpell(self):
		magicMonsterLightSpellDamage = randint(1, 2) * self.magicMonsterSpellDamage
		return magicMonsterLightSpellDamage
	

	def magicMonsterMediumSpell(self):
		magicMonsterMediumSpellDamage = randint(3, 4) * self.magicMonsterSpellDamage
		return magicMonsterMediumSpellDamage

	def magicMonsterStrongSpell(self):
		magicMonsterStrongSpellDamage = randint(5,6) * self.magicMonsterSpellDamage
		return magicMonsterStrongSpellDamage

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

		if attackType >= 1 and attackType <= 50: # 50% chance to use light spell
			monsterDamage = self.magicMonsterLightSpell()
			print('\t Monster Used Light Spell.')
			#print('\t Light Spell Damage: {}'.format(monsterDamage))
			return monsterDamage
		elif attackType > 50 and attackType <= 80: # 30% chance to use medium spell

			monsterDamage = self.magicMonsterMediumSpell()
			print('\t Monster Used Medium Spell.')
			#print('\t Medium Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

		else: # 20% chance to use strong spell

			monsterDamage = self.magicMonsterStrongSpell()
			print('\t Monster Used Strong Spell.')
			#print('\t Strong Spell Damage: {}'.format(monsterDamage))
			return monsterDamage

	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getMagicMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))
	
	def takeDamage(self, getDamage):
		self.livingBeingCurrentlyLife -= getDamage

	def getMonsterLoot(self):
		return self.magicMonsterLoot

	def getMonsterExperience(self):
		return self.magicMonsterExperienceForKill