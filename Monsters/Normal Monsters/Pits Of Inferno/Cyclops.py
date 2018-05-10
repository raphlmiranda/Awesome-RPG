############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                   Cyclops  Class                         #
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


from SuperClass.NormalMonster import NormalMonster

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_CYCLOPS_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_CYCLOPS_WEAPON_ATTACK 
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_CYCLOPS_EXPERIENCE

class Cyclops(NormalMonster):

	'''
	--> LiveBeing Interface
	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	--> Normal Monster Interface
	self.magicMonsterSpellDamage = magicMonsterSpellDamage
	self.magicMonsterName = magicMonsterName
	self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self,
				 livingBeingLife):

		# construct MagicMonster
		super().__init__( livingBeingLife, 
							GLOBAL_CYCLOPS_NAME, 
							GLOBAL_CYCLOPS_WEAPON_ATTACK, 
							GLOBAL_CYCLOPS_EXPERIENCE ) 

