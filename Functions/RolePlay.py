############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Role Play Functions                        #
#   													   #
#   Alex Galhardo Vieira                                   #
#   aleexgvieira@gmail.com                                 #
#   github.com/AlexGalhardo                                #
#														   #
#   ICMC USP - 2018 									   #
#	São Carlos - Brazil									   #
############################################################

#!/usr/bin/python3
# coding: utf-8

# Comments here

# Code Patterns
#               UPPERCASE = global variables
#               PascalCase = modules and Classes
#               camelCase = local variables, methods, attributes, parameters, arguments
#               Under_Line = functions

from Functions.Prints import *
from SuperClass.Character import Character


def Mage_Spells( Player ):

	while True:

		print('\n\t Enter [1] --> Light Attack Spell [{}'.format(Player.getMageLightSpellManaUsed()) + ']')
		print('\t Enter [2] --> Medium Attack Spell [{}'.format(Player.getMageMediumSpellManaUsed()) + ']')
		print('\t Enter [3] --> Strong Attack Spell [{}'.format(Player.getMageStrongSpellManaUsed()) + ']')
		print('\t Enter [4] --> Medium Healing [{}'.format(Player.getMageMediumHealingManaUsed()) + ']')
		print('\t Enter [5] --> Strong Healing [{}'.format(Player.getMageStrongHealingManaUsed()) + ']')
		print('\t Enter [0] --> CANCEL')
		spellOption = int(input('\t Spell: '))

		# INVALID OPTION
		if spellOption != 1 and spellOption > 3:
			print('\t Enter a valid option!')
			continue

		# CANCEL SPELL
		elif spellOption == 0:
			return 0
			break

		# Return LIGHT SPEEL
		elif spellOption == 1:
			if Player.getCharacterCurrentlyMana() >= Player.getMageLightSpellManaUsed():
				return 41
				break

			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageLightSpellManaUsed()))
				continue

		# Return MEDIUM SPEEL
		elif spellOption == 2:
			
			if Player.getCharacterCurrentlyMana() >= Player.getMageMediumSpellManaUsed():
				return 42
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageMediumSpellManaUsed()))
				continue

		# Return STRONG SPELL
		elif spellOption == 3:
			if Player.getCharacterCurrentlyMana() >= Player.getMageStrongSpellManaUsed():
				return 43
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageStrongSpellManaUsed()))
				continue
		
		# MAGE USE MEDIUM HEALING
		elif spellOption == 4:
			if Player.getCharacterCurrentlyMana() >= Player.getMediumHealingManaUsed():
				Player.useMediumHealing()
				continue
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageMediumHealingManaUsed()))
				continue

		# MAGE USE MEDIUM HEALING
		else:
			if Player.getCharacterCurrentlyMana() >= Player.getStrongHealingManaUsed():
				Player.useStrongHealing()
				continue
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageStrongHealingManaUsed()))
		break


def Warrior_Spells( Player ):

	while True:

		print('\n\t Enter [1] --> Light Spell [{}'.format(Player.getLightSpellManaUsed()) + ']')
		print('\t Enter [2] --> Medium Spell [{}'.format(Player.getMediumSpellManaUsed()) + ']')
		print('\t Enter [3] --> Strong Spell [{}'.format(Player.getStrongSpellManaUsed()) + ']')
		print('\t Enter [0] --> CANCEL')
		spellOption = int(input('\t Spell: '))

		# INVALID OPTION
		if spellOption != 1 and spellOption > 3:
			print('\t Enter a valid option!')
			continue

		# CANCEL SPELL
		elif spellOption == 0:
			return 0
			break

		# Return LIGHT SPEEL
		elif spellOption == 1:
			if Player.getCharacterCurrentlyMana() >= Player.getLightSpellManaUsed():
				return 41
				break

			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getLightSpellManaUsed()))
				continue

		# Return MEDIUM SPEEL
		elif spellOption == 2:
			
			if Player.getCharacterCurrentlyMana() >= Player.getMediumSpellManaUsed():
				return 42
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMediumSpellManaUsed()))
				continue

		# Return STRONG SPEEL
		else:
			if Player.getCharacterCurrentlyMana() >= Player.getStrongSpellManaUsed():
				return 43
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getStrongSpellManaUsed()))
				continue

		break


def Player_Action( Player ):


	while True:

		print('\n\t @ Player Round @')
		print('\t Enter [1] --> Normal Attack')
		print('\t Enter [2] --> Use Health Potion')
		print('\t Enter [3] --> Use Mana Potion')
		print('\t Enter [4] --> Use Spell')
		playerAction = int(input('\t Option: '))

		if playerAction == 1:
			return 1
			break

		elif playerAction == 2:
			return 2
			break

		elif playerAction == 3:
			return 3
			break

		elif playerAction == 4:

			if Player.getCharacterVocationType() == "WARRIOR":
				spellVerification = Warrior_Spells( Player )
			else:
				spellVerification = Mage_Spells( Player )

			return spellVerification

			break

		else:
			print('\t Enter a valid option!')
			continue


def Round( Player , Monster ):

	while True:

		# SHOW PLAYER AND MONSTER ROUND STATUS
		Player.getCharacterRoundStatus()
		Monster.getMonsterRoundStatus()


		# PLAYER ROUND --> ATTACK, USE POTIONS, SPELLS...
		playerAction = Player_Action( Player )

		Round_Status_Print()

		if playerAction == 0: # Spell Canceled
			continue

		else:

			if playerAction == 1: # PLAYER USE NORMAL ATTACK IN MONSTER
				Monster.takeDamage(Player.getNormalAttack())

			elif playerAction == 2: # PLAYER USE HEALTH POTION TO REGENERATE LIFE
				Player.useHealthPotion()

			elif playerAction == 3: # PLAYER USE MANA POTION TO REGENERATE Mana
				Player.useManaPotion()

			elif playerAction == 41:
				Monster.takeDamage(Player.useLightSpell())

			elif playerAction == 42:
				Monster.takeDamage(Player.useMediumSpell())

			else:
				Monster.takeDamage(Player.useStrongSpell())


			# MONSTER ROUND --> ATTACK PLAYER
			Player.takeDamage(Monster.Attack())



			# Verify if Player or Monster is Dead
			if Player.isDead():
				# Player still alive? False
				return False
				break

			elif Monster.isDead():

				if Monster.type() == "BOSS":
					return True
					break

				# Player is still alive and monster is dead? True -> next round
				lootMonster = Monster.getMonsterLoot()
				experienceMonster = Monster.getMonsterExperience()

				Player.getLootMonster(lootMonster)
				Player.getMonsterExperience(experienceMonster)

				print('\t Player Looted: {} gold coins.'.format(lootMonster))
				print('\t Player received: {} points of experience!'.format(experienceMonster))
				print('\t Player Currently Experience: {} points experience.'.format(Player.getCharacterCurrentlyXP()))

				Player.Update()

				return True

				break

			else:
				Player.Regenerate()
				# player and monster is still alive
				continue