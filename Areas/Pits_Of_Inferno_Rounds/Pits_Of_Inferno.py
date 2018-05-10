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

from Global.Global_Pits_Of_Inferno import *

from Monsters.NormalMonsters.Pits_Of_Inferno.Bear import Bear
from Monsters.NormalMonsters.Pits_Of_Inferno.Hunter import Hunter
from Monsters.NormalMonsters.Pits_Of_Inferno.Cyclops import Cyclops

from Monsters.MagicMonsters.Pits_Of_Inferno.Dragon import Dragon
from Monsters.MagicMonsters.Pits_Of_Inferno.Infernalist import Infernalist
from Monsters.MagicMonsters.Pits_Of_Inferno.Warlock import Warlock

from Monsters.DemonMonsters.Pits_Of_Inferno.Fury import Fury
from Monsters.DemonMonsters.Pits_Of_Inferno.DarkTorturer import DarkTorturer
from Monsters.DemonMonsters.Pits_Of_Inferno.Demon import Demon

from Monsters.Bosses.Morgaroth import Morgaroth

from Functions.NPC import NPC
from Functions.Prints import *
from Functions.RolePlay import *

from Areas.Pits_Of_Inferno_Rounds.Against_Bear import *
from Areas.Pits_Of_Inferno_Rounds.Against_Hunter import *
from Areas.Pits_Of_Inferno_Rounds.Against_Cyclops import *
from Areas.Pits_Of_Inferno_Rounds.Against_Dragon import *
from Areas.Pits_Of_Inferno_Rounds.Against_Infernalist import *
from Areas.Pits_Of_Inferno_Rounds.Against_Warlock import *
from Areas.Pits_Of_Inferno_Rounds.Against_Fury import *
from Areas.Pits_Of_Inferno_Rounds.Against_DarkTorturer import *
from Areas.Pits_Of_Inferno_Rounds.Against_Demon import *
from Areas.Pits_Of_Inferno_Rounds.Against_Morgaroth import *


def After_Fight( Player ):
	Player_Defeated_Monster()
	NPC( Player )
	Fight_Round_Print()


def Pits_Of_Inferno_Start_Game( Player ):

	playerAlive = True

	NPC( Player )
	Fight_Round_Print()

	while playerAlive:

		playerAlive = Round_Against_Bear(  playerAlive, Player )

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

											if playerAlive:

												print('\n\n\n\t YOU WIN THE GAME!\n\n\n')
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
			else:
				break
		else:
			break
