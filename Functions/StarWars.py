############################################################
#                                                          #
#      Tibians RPG ~ A Fan Game inspired in Tibia Online   #
#                                                          #
#                       ALPHA                              #
#                                                          #
#                VERSION Console ~ PYTHON3                 #
#                                                          #
#               Star Wars Rounds Function                  #
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

from Functions.GLOBAL_VARIABLES import *

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

from Functions.FerumbrasTower_Rounds.Against_Rotworm import *
from Functions.FerumbrasTower_Rounds.Against_Hunter import *
from Functions.FerumbrasTower_Rounds.Against_Cyclops import *
from Functions.FerumbrasTower_Rounds.Against_Wyvern import *
from Functions.FerumbrasTower_Rounds.Against_DragonLord import *
from Functions.FerumbrasTower_Rounds.Against_Warlock import *
from Functions.FerumbrasTower_Rounds.Against_Fury import *
from Functions.FerumbrasTower_Rounds.Against_DarkTorturer import *
from Functions.FerumbrasTower_Rounds.Against_HellHound import *
from Functions.FerumbrasTower_Rounds.Against_DarthVader import *


def After_Fight( Player ):
	Player_Defeated_Monster()
	NPC( Player )
	Fight_Round_Print()


def Ferumbras_Tower_Start_Game( Player ):

	playerAlive = True

	NPC( Player )
	Fight_Round_Print()

	while playerAlive:

		playerAlive = Round_Against_Warlock(  playerAlive, Player )
		
		if playerAlive: # Alive against bears?

			playerAlive = Round_Against_Warlock( playerAlive, Player )

			if playerAlive: # Alive against hunters?

				playerAlive = Round_Against_Fury( playerAlive, Player )

				if playerAlive: # Alive against Cyclops?

					playerAlive = Round_Against_Demon( playerAlive, Player )

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