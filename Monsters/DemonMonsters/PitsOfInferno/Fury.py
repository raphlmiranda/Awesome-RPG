############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Fury Class                           #
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

from SuperClass.DemonMonster import DemonMonster

from Global.Global_Pits_Of_Inferno import GLOBAL_FURY_NAME, \
										  GLOBAL_FURY_WEAPON_ATTACK, \
										  GLOBAL_FURY_MAGIC_ATTACK, \
										  GLOBAL_FURY_EXPERIENCE

class Fury(DemonMonster):

	'''
	~ LivingBeing SuperClass
	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	~ Demon Monster SuperClass
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
						  GLOBAL_FURY_NAME,
						  GLOBAL_FURY_MAGIC_ATTACK,
						  GLOBAL_FURY_WEAPON_ATTACK,
					      GLOBAL_FURY_EXPERIENCE )
