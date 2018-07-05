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

# ./SuperClass/Monsters/NormalMonster.py

from SuperClass.LivingBeing import LivingBeing
from random import randint
from SuperClass.GameStatistics import GameStatistics

# abstract class that knights, paladins, druids and sorcerer must inherit
class NormalMonster(LivingBeing):

	'''
	~ LivingBeing SuperClass
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
		GameStatistics.totalDamageToMonsters += getDamage
		self.livingBeingCurrentlyLife -= getDamage

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def type(self):
		return "NORMAL"

	def Attack(self):
		baseAttackOne = int(self.normalMonsterAttackDamage * 0.5)
		baseAttackTwo = int(self.normalMonsterAttackDamage * 1.5)
		return randint(baseAttackOne, baseAttackTwo)

	def getMonsterExperience(self):
		return self.normalMonsterExperienceForKill

	def getMonsterLoot(self):
		return self.normalMonsterLoot
