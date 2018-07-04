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

UPPERCASE = global variables

PascalCase = Classes and Folders

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./Monsters/NormalMonsters/PitsOfInferno/Hunter.py


from SuperClass.NormalMonster import NormalMonster

from Global.Pits_Of_Inferno_Global_Variables import GLOBAL_HUNTER_NAME, \
										            GLOBAL_HUNTER_WEAPON_ATTACK, \
										  			GLOBAL_HUNTER_EXPERIENCE

class Hunter(NormalMonster):

	'''
	~ LiveBeing SuperClass
	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	~ Normal Monster SuperClass
	self.magicMonsterSpellDamage = magicMonsterSpellDamage
	self.magicMonsterName = magicMonsterName
	self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self,
				 livingBeingLife):

		# constructor Normal Monster
		super().__init__( livingBeingLife,
							GLOBAL_HUNTER_NAME,
							GLOBAL_HUNTER_WEAPON_ATTACK,
							GLOBAL_HUNTER_EXPERIENCE )
