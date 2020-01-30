# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:17 2020

@author: friesemi
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.getBox(nV)


#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply = testUtility.generateSupplies(nV, nC, supply, player_names)


#initialize the trash
trash = []

#Costruct the Player objects
players = []
players = testUtility.getPlayers(players, player_names)

#Play the game
#introduced bug to throw off the turns of the game
turn = 10
while not Dominion.gameover(supply):
    turn += 5  
    print("\r")    
    for value in testUtility.supply_order:
        print (value)
        for stack in testUtility.supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)