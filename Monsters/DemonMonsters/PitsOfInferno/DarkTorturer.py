############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Dark Torturer Class                  #
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

from Global.Global_Pits_Of_Inferno import GLOBAL_DARKTORTURER_NAME, \
										  GLOBAL_DARKTORTURER_WEAPON_ATTACK, \
										  GLOBAL_DARKTORTURER_MAGIC_ATTACK, \
										  GLOBAL_DARKTORTURER_EXPERIENCE

class DarkTorturer(DemonMonster):

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

		# construct Demon Monster
		super().__init__( livingBeingLife,
							GLOBAL_DARKTORTURER_NAME,
							GLOBAL_DARKTORTURER_WEAPON_ATTACK,
							GLOBAL_DARKTORTURER_MAGIC_ATTACK,
							GLOBAL_DARKTORTURER_EXPERIENCE )
