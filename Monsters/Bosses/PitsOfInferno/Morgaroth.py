############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Morgaroth Class                      #
#														   #
#   Alex Galhardo Vieira   								   #
#   github.com/AlexGalhardo                                #
#	aleexgvieira@gmail.com 								   #
#   MIT LICENSE                                            #
#														   #
############################################################

#!/usr/bin/python3
# coding: utf-8

#       Code Patterns
#
# UPPERCASE = global variables
# PascalCase = Classes
# camelCase = local variables, methods, attributes, parameters, arguments
# Under_Line = Functions and Modules

from SuperClass.BOSS import BOSS

from Global.Global_Pits_Of_Inferno import GLOBAL_MORGAROTH_LIFE, \
								   		  GLOBAL_MORGAROTH_NAME, \
								   		  GLOBAL_MORGAROTH_WEAPON_ATTACK, \
								   		  GLOBAL_MORGAROTH_MAGIC_ATTACK, \
								   	      GLOBAL_MORGAROTH_EXPERIENCE

class Morgaroth(BOSS):

	'''
	~ LivingBeing SuperClass
	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	~ Magic Monster SuperClass
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

		# constructor Demon Monster
		super().__init__( livingBeingLife,
							GLOBAL_MORGAROTH_NAME,
							GLOBAL_MORGAROTH_MAGIC_ATTACK,
							GLOBAL_MORGAROTH_WEAPON_ATTACK,
							GLOBAL_MORGAROTH_EXPERIENCE )
