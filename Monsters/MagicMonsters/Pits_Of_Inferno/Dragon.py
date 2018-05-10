############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
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


from SuperClass.MagicMonster import MagicMonster

from Global.Global_Pits_Of_Inferno import GLOBAL_DRAGON_NAME, \
										  GLOBAL_DRAGON_MAGIC_ATTACK, \
										  GLOBAL_DRAGON_EXPERIENCE

class Dragon(MagicMonster):

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

		# construct MagicMonster
		super().__init__( livingBeingLife,
							GLOBAL_DRAGON_NAME,
							GLOBAL_DRAGON_MAGIC_ATTACK,
							GLOBAL_DRAGON_EXPERIENCE )
