############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Pits Of Inferno Function                   #
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

from GLOBAL.GLOBAL_PITS_OF_INFERNO import *

from Monsters.NormalMonster.Bear import Bear
from Monsters.NormalMonster.Hunter import Hunter
from Monsters.NormalMonster.Cyclops import Cyclops

from Monsters.MagicMonster.Dragon import Dragon
from Monsters.MagicMonster.Infernalist import Infernalist
from Monsters.MagicMonster.Warlock import Warlock

from Monsters.DemonMonster.Fury import Fury
from Monsters.DemonMonster.DarkTorturer import DarkTorturer
from Monsters.DemonMonster.Demon import Demon

from Monsters.BOSS.Morgaroth import Morgaroth 

from Functions.NPC import NPC
from Functions.Prints import *
from Functions.RolePlay import *

from Functions.PitsOfInferno_Rounds.Against_Bear import *
from Functions.PitsOfInferno_Rounds.Against_Hunter import *
from Functions.PitsOfInferno_Rounds.Against_Cyclops import *
from Functions.PitsOfInferno_Rounds.Against_Dragon import *
from Functions.PitsOfInferno_Rounds.Against_Infernalist import *
from Functions.PitsOfInferno_Rounds.Against_Warlock import *
from Functions.PitsOfInferno_Rounds.Against_Fury import *
from Functions.PitsOfInferno_Rounds.Against_DarkTorturer import *
from Functions.PitsOfInferno_Rounds.Against_Demon import *
from Functions.PitsOfInferno_Rounds.Against_Morgaroth import *


def After_Fight( Player ):
	Player_Defeated_Monster()
	NPC( Player )
	Fight_Round_Print()


def Pits_Of_Inferno_Start_Game( Player ):

	playerAlive = True

	NPC( Player )
	Fight_Round_Print()

	while playerAlive:

		playerAlive = Round_Against_Fury(  playerAlive, Player )
		
		if playerAlive: # Alive against bears?

			playerAlive = Round_Against_Hunter( playerAlive, Player )

			if playerAlive: # Alive against hunters?

				playerAlive = Round_Against_Cyclops( playerAlive, Player )

				if playerAlive: # Alive against Cyclops?

					playerAlive = Round_Against_Dragon( playerAlive, Player )

					if playerAlive: # Alive against Dragons?

						playerAlive = Round_Against_Infernalist( playerAlive, Player )

						if playerAlive: # Alive against Infernalists?

							playerAlive = Round_Against_Warlock( playerAlive, Player )

							if playerAlive: # Alive against Warlocks?

								playerAlive = Round_Against_Fury( playerAlive, Player )
							
								if playerAlive: # Alive against Furys?

									playerAlive = Round_Against_DarkTorturer( playerAlive, Player )
								
									if playerAlive: # Alive against DarkTorturers?

										playerAlive = Round_Against_Demon( playerAlive, Player )
									
										if playerAlive: # Alive against Demons? GO BOSS

											playerAlive = Round_Against_Morgaroth( playerAlive, Player )
										else:
											break
									else:
										break
								else:
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
			else:
				break
		else:
			break

		print('\t YOU WIN THE GAME!')