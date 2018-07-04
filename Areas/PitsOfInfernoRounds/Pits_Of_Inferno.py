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

# ./Areas/Pits_Of_Inferno_Rounds/Pits_Of_Inferno.py


from Global.Pits_Of_Inferno_Global_Variables import *

from Monsters.NormalMonsters.PitsOfInferno import Bear, \
												  Hunter, \
												  Cyclops

from Monsters.MagicMonsters.PitsOfInferno import Dragon, \
												 Infernalist, \
												 Warlock

from Monsters.DemonMonsters.PitsOfInferno import Fury, \
														DarkTorturer, \
														Demon

from Monsters.Bosses.Morgaroth import Morgaroth

from Functions.NPC import NPC
from Functions.Prints import *
from Functions.Role_Play import *

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
