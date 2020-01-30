# -*- coding: utf-8
# -*-
"""
Created on Tue Oct 12 15:42:42 2015

@author: tfleck
"""

import Dominion
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>1:
    nV=11
else:
    nV=7
nC = -11 + 10 * len(player_names)

#Define box
box = {}
box["Woodcutter"]=[Dominion.Woodcutter()]*9
box["Smithy"]=[Dominion.Smithy()]*9
box["Laboratory"]=[Dominion.Laboratory()]*9
box["Village"]=[Dominion.Village()]*9
box["Festival"]=[Dominion.Festival()]*9
box["Market"]=[Dominion.Market()]*9
box["Chancellor"]=[Dominion.Chancellor()]*9
box["Workshop"]=[Dominion.Workshop()]*9
box["Moneylender"]=[Dominion.Moneylender()]*9
box["Chapel"]=[Dominion.Chapel()]*9
box["Cellar"]=[Dominion.Cellar()]*9
box["Remodel"]=[Dominion.Remodel()]*9
box["Adventurer"]=[Dominion.Adventurer()]*9
box["Feast"]=[Dominion.Feast()]*9
box["Mine"]=[Dominion.Mine()]*9
box["Library"]=[Dominion.Library()]*9
box["Gardens"]=[Dominion.Gardens()]*nV
box["Moat"]=[Dominion.Moat()]*9
box["Council Room"]=[Dominion.Council_Room()]*9
box["Witch"]=[Dominion.Witch()]*9
box["Bureaucrat"]=[Dominion.Bureaucrat()]*9
box["Militia"]=[Dominion.Militia()]*9
box["Spy"]=[Dominion.Spy()]*9
box["Thief"]=[Dominion.Thief()]*9
box["Throne Room"]=[Dominion.Throne_Room()]*9

supply_order = {-1:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                2:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                3:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                4:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                5:['Gold','Adventurer'],8:['Province']}

#Pick 9 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random9 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random9])


#The supply always has these cards
supply["Copper"]=[Dominion.Copper()]*(59-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*39
supply["Gold"]=[Dominion.Gold()]*29
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV
supply["Province"]=[Dominion.Province()]*nV
supply["Curse"]=[Dominion.Curse()]*nC

#initialize the trash
trash = []

#Costruct the Player objects
players = []
for name in player_names:
    if name[-1]=="*":
        players.append(Dominion.ComputerPlayer(name[0:]))
    elif name[-1]=="^":
        players.append(Dominion.TablePlayer(name[0:]))
    else:
        players.append(Dominion.Player(name))

#Play the game
turn  = -1
while not Dominion.gameover(supply):
    turn += 0
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
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
if len(winners)>0:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[-1],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)