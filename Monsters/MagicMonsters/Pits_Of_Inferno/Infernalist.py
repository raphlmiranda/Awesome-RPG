############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                     Infernalist Class                    #
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
# Under_Line = functions


from SuperClass.MagicMonster import MagicMonster

from Global.Global_Pits_Of_Inferno import GLOBAL_INFERNALIST_NAME, \
                                          GLOBAL_INFERNALIST_MAGIC_ATTACK, \
                                          GLOBAL_INFERNALIST_EXPERIENCE

class Infernalist(MagicMonster):

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
				 livingBeingLife):

		# constructor Magic Monster
		super().__init__( livingBeingLife,
							GLOBAL_INFERNALIST_NAME,
							GLOBAL_INFERNALIST_MAGIC_ATTACK,
							GLOBAL_INFERNALIST_EXPERIENCE )
