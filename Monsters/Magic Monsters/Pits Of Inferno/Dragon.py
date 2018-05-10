############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                         #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                    Dragon Class                          #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
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


from SuperClass.MagicMonster import MagicMonster

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DRAGON_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DRAGON_MAGIC_ATTACK
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DRAGON_EXPERIENCE

class Dragon(MagicMonster):

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
				 livingBeingLife):

		# construct MagicMonster
		super().__init__( livingBeingLife,
							GLOBAL_DRAGON_NAME,
							GLOBAL_DRAGON_MAGIC_ATTACK,
							GLOBAL_DRAGON_EXPERIENCE )
