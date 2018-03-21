############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   ##                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                   Dark Torturer Class                    #
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

from SuperClass.DemonMonster import DemonMonster

from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_NAME
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_WEAPON_ATTACK 
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_MAGIC_ATTACK 
from GLOBAL.GLOBAL_PITS_OF_INFERNO import GLOBAL_DARKTORTURER_EXPERIENCE

class DarkTorturer(DemonMonster):

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
				 demonMonsterName,
				 demonMonsterSpellDamage,
				 demonMonsterAttackDamage,
				 demonMonsterExperienceForKill):

		# construct Demon Monster
		super().__init__( livingBeingLife,
							GLOBAL_DARKTORTURER_NAME,
							GLOBAL_DARKTORTURER_WEAPON_ATTACK, 
							GLOBAL_DARKTORTURER_MAGIC_ATTACK, 
							GLOBAL_DARKTORTURER_EXPERIENCE ) 