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

# ./SuperClass/GameStatistics.py

class GameStatistics(object):

	# totalGameTimeUntilPlayerDies = 0
	totalDamageToMonsters = 0
	totalDamageTakenFromMonsters = 0
	totalManaUsed = 0
	totalSpellsUsed = 0
	totalAttacksUsed = 0
	totalHealthPotionsUsed = 0
	totalManaPotionsUsed = 0
	totalHealthPotionsBought = 0
	totalManaPotionsBought = 0
	totalGoldCoinsLooted = 0
	totalGoldCoinsUsed = 0

	# @staticmethod
	# def getTotalGameTimeUntilPlayerDies():
		# print('\t Total Game Time Until Player Dies: {}'.format(GameStatistics.totalGameTimeUntilPlayerDies))
	
	@staticmethod
	def getTotalDamageToMonsters():
		print('\t Total Damage To Monsters: {}'.format(GameStatistics.totalDamageToMonsters))

	@staticmethod
	def getTotalDamageTakenFromMonsters():
		print('\t Total Damage Taken From Monsters: {}'.format(GameStatistics.totalDamageToMonsters))

	@staticmethod
	def getTotalManaUsed():
		print('\t Total Mana Used: {}'.format(GameStatistics.totalManaUsed))

	@staticmethod
	def getTotalSpellsUsed():
		print('\t Total Spells Used: {}'.format(GameStatistics.totalSpellsUsed))

	@staticmethod
	def getTotalAttacksUsed():
		print('\t Total Attacks Used: {}'.format(GameStatistics.totalAttacksUsed))

	@staticmethod
	def getTotalHealthPotionsUsed():
		print('\t Total Health Potions Used: {}'.format(GameStatistics.totalHealthPotionsUsed))

	@staticmethod
	def getTotalManaPotionsUsed():
		print('\t Total Mana Potions Used: {}'.format(GameStatistics.totalManaPotionsUsed))

	@staticmethod
	def getTotalHealthPotionsBought():
		print('\t Total Health Potions Bought: {}'.format(GameStatistics.totalHealthPotionsBought))

	@staticmethod
	def getTotalManaPotionsBought():
		print('\t Total Mana Potions Bought: {}'.format(GameStatistics.totalManaPotionsBought))

	@staticmethod
	def getTotalGoldCoinsLooted():
		print('\t Total Gold Coins Looted: {}'.format(GameStatistics.totalGoldCoinsLooted))

	@staticmethod
	def getTotalGoldCoinsUsed():
		print('\t Total Gold Coins Used: {}'.format(GameStatistics.totalGoldCoinsUsed))

	@staticmethod
	def getGameStatistics():
		#GameStatistics.getTotalGameTimeUntilPlayerDies
		print('\n\t --- Game Statistics ---')
		GameStatistics.getTotalDamageToMonsters()
		GameStatistics.getTotalDamageTakenFromMonsters()
		GameStatistics.getTotalManaUsed()
		GameStatistics.getTotalSpellsUsed()
		GameStatistics.getTotalAttacksUsed()
		GameStatistics.getTotalHealthPotionsUsed()
		GameStatistics.getTotalManaPotionsUsed()
		GameStatistics.getTotalHealthPotionsBought()
		GameStatistics.getTotalManaPotionsBought()
		GameStatistics.getTotalGoldCoinsLooted()
		GameStatistics.getTotalGoldCoinsUsed()
		print('\n\n')