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

UPPERCASE = global variables

PascalCase = Classes

camelCase = local variables, methods, attributes, parameters, arguments

Under_Line = Functions and Modules
'''

# ./Functions/Character_Creation.py

from Characters.Knight import Knight
from Characters.Paladin import Paladin
from Characters.Druid import Druid
from Characters.Sorcerer import Sorcerer

from Global.Characters_Global_Variables import KNIGHT_INITIAL_LIFE, \
											   PALADIN_INITIAL_LIFE, \
											   MAGE_INITIAL_LIFE


'''
This function return a string --> character name
'''
def Create_Character_Name():
	
	characterName = str(input('\n\n\t Enter your character name: '))
	return characterName





'''
This function return a integer --> vocation choosen
1 -> knight
2 -> paladin
3 -> druid
4 -> sorcerer
'''
def Choose_Character_Vocation():

	while True:

		print('\n\t Chose a vocation below: ')
		print('\t Enter [1] --> Knight')
		print('\t Enter [2] --> Paladin')
		print('\t Enter [3] --> Druid')
		print('\t Enter [4] --> Sorcerer')

		vocationOption = int(input('\t Vocation option: '))

		if vocationOption < 1 or vocationOption > 4:
			print('\n\t Choose a valid option!')
			continue
		else:
			break

	if( vocationOption == 1 ):
		return 1 # knight
	elif vocationOption == 2:
		return 2 # paladin
	elif vocationOption == 3:
		return 3 # druid
	elif vocationOption == 4:
		return 4 # sorcerer








def Choose_Knight_Weapon():

	while True:
		print("\n\t Choose a Weapon Below")
		print("\t Enter [1] --> Sword [Attack: 30 | Defefense: 30")
		print("\t Enter [2] --> Axe [Attack: 35 | Defense: 20")
		print("\t Enter [3] --> Club [Attack: 25 | Defense: 35")
		weaponOption = int(input("\t Weapon Option: "))

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



def Create_Character( characterName, vocationOption ):

	if vocationOption == 1:

		warriorWeaponAttack = Choose_Knight_Weapon()

		Character = Knight( characterName,
			                warriorWeaponAttack )

	elif vocationOption == 2:

		warriorWeaponAttack = Choose_Paladin_Weapon()

		Character = Paladin( characterName,
			                 warriorWeaponAttack )

	elif vocationOption == 3:

		Character = Druid( characterName,
			               "Druid" )

	else:

		Character = Sorcerer( characterName,
			                  "Sorcerer")


	print('\n\t Character Created!')
	print('\n\t --- SHOWING CHARACTER STATUS ---')
	Character.toString()

	return Character
