'''
The MIT License (MIT)

Copyright (c) 2018 Alex Galhardo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

############################################################
#                                                          #
#      				    AWESOME RPG                        #
#                                                          #
#                                                          #
#                Console Version ~ Python3                 #
#                                                          #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

'''
Code Patterns

UPPERCASE = Global Variables

PascalCase = Classes and Folders

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./SuperClass/Monsters/MagicMonster.py

from SuperClass.LivingBeing import LivingBeing
from random import randint
from SuperClass.GameStatistics import GameStatistics

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
		self.magicMonsterLoot = randint(250, 700)


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

	def type(self):
		return "MAGIC"

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
		GameStatistics.totalDamageToMonsters += getDamage
		self.livingBeingCurrentlyLife -= getDamage

	def getMonsterLoot(self):
		return self.magicMonsterLoot

	def getMonsterExperience(self):
		return self.magicMonsterExperienceForKill
