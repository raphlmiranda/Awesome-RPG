############################################################
#                                                          #
#      Awesome RPG ~ A Fan Game inspired in Tibia Online   #                                                          #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#                 Character Creation Functions             #
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

from Characters.Knight import Knight
from Characters.Druid import Druid
from Characters.Paladin import Paladin
from Characters.Sorcerer import Sorcerer

from Global.Global_Characters import *

def Character_Name():
	characterName = str(input('\n\n\t Enter your character name: '))
	return characterName


def Choose_Vocation():

	while True:

		print('\n\t Chose a vocation below: ')
		print('\t Enter [1] --> Aquiles')
		print('\t Enter [2] --> Robin Hood')
		print('\t Enter [3] --> Dumbledore')
		print('\t Enter [4] --> Gandalf')

		vocationOption = int(input('\t Vocation: '))

		if vocationOption < 1 or vocationOption > 4:
			print('\n\t Choose a valid option!')
			continue
		else:
			break

	if( vocationOption == 1 ):
		return 1
	elif vocationOption == 2:
		return 2
	elif vocationOption == 3:
		return 3
	elif vocationOption == 4:
		return 4


def Choose_Knight_Weapon():

	while True:
		print("\n\t Choose a Weapon Below")
		print("\t Enter [1] --> Sword [Attack: 30 | Defefense: 30")
		print("\t Enter [2] --> Axe [Attack: 35 | Defense: 20")
		print("\t Enter [3] --> Club [Attack: 25 | Defense: 35")
		weaponOption = int(input("\t Option: "))

		if weaponOption < 1 or weaponOption > 3:
			print("\t Choose a valid option!")
			continue
		else:
			break

	if weaponOption == 1:
		#return "Sword"
		return 30
	elif weaponOption == 2:
		#return "Axe"
		return 35
	else:
		#return "Club"
		return 25

def Choose_Paladin_Weapon():

	while True:
		print("\n\t Choose a Weapon Below")
		print("\t Enter [1] --> Crossbow [Attack: 50]")
		print("\t Enter [2] --> Bow [Attack: 40]")
		print('\t Enter [3] --> Spear [Attack 25]')
		weaponOption = int(input("\t Option: "))

		if weaponOption < 1 or weaponOption > 2:
			print("\t Choose a valid option!")
			continue
		else:
			break

	if weaponOption == 1:
		return 50
	elif weaponOption == 2:
		return 40
	else:
		return 25


def Character_Object( characterName, vocationOption ):

	if vocationOption == 1:

		warriorWeaponAttack = Choose_Knight_Weapon()

		Character = Knight( KNIGHT_INITIAL_LIFE,
			                characterName,
			                "WARRIOR",
			                warriorWeaponAttack )

	elif vocationOption == 2:

		warriorWeaponAttack = Choose_Paladin_Weapon()

		Character = Paladin( PALADIN_INITIAL_LIFE,
			                 characterName,
			                 "WARRIOR",
			                 warriorWeaponAttack )

	elif vocationOption == 3:

		Character = Druid( MAGE_INITIAL_LIFE,
			               characterName,
			               "Dumbledore" )

	else:

		Character = Sorcerer( MAGE_INITIAL_LIFE,
			                  characterName,
			                  "Gandalf")


	print('\n\t Character Created!')
	print('\n\t --- SHOWING CHARACTER STATUS ---')
	Character.toString()

	return Character
