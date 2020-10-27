import os,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))[:-6]) #=dev first
from pybaccarat.playingcards import Card
from pybaccarat.playingcards import Shoe
from pybaccarat.baccarat import Hand
import random

# Statistics
currentRound = 0
drawRounds = 0
playerWinRounds = 0 
playerLoseRounds = 0
lastRound = 0 # -1 if lost, 0 if draw, 1 if won
currentMoney = 10000
currentBet = 20
# print ('把黑桃1-6洗入牌库!')
#shoe = Shoe([ Card(1,'s'), Card(2,'s'), Card(3,'s'), Card(4,'s'), Card(5,'s'), Card(6,'s') ])
shoe = Shoe(8)
print ('开始洗牌')
shoe.shuffle()

while (shoe.cardsLeft() >= 6):
    print ('第', currentRound ,'局开干')
    player = Hand()
    banker = Hand()
    # Play a round
    for i in range(6):
        # print ('牌库剩余牌数: ', shoe.cardsLeft())
        if (i % 2 == 0):
            if (i != 4):
                newCard = shoe.deal()
                # print ('发1张牌: ', newCard.get_rank(), '给闲')
                player.add(newCard)
            elif (player.need_hit(None)):
                newCard = shoe.deal()
                # print ('发第3张牌: ', newCard.get_rank(), '给闲')
                player.add(newCard)
        else:
            if (i != 5):
                newCard = shoe.deal()
                # print ('发1张牌: ', newCard.get_rank(), '给庄')
                banker.add(newCard)
            elif (banker.need_hit(player)):
                newCard = shoe.deal()
                # print ('发第3张牌: ', newCard.get_rank(), '给庄')
                banker.add(newCard)
    result = player.__cmp__(banker)
    if (result == 0):
        print ('平局')
        currentRound += 1
    elif (result > 0):
        print ('闲赢', '闲家手牌: ', player, '; 庄家手牌: ', banker)
        currentMoney += currentBet
        currentRound += 1
    else:
        print ('庄赢', '闲家手牌: ', player, '; 庄家手牌: ', banker)
        currentMoney -= currentBet
        currentBet *= 2
        currentRound += 1
    if (currentMoney < 0):
        print ('恭喜你破产了!')
        break