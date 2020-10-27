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
# 改:赌本
currentMoney = 5120
minBet = 20 # 改: 单注底金
currentBet = 20 # 改: 单注底金
bankrupt = False
currentGuess = '庄'
# print ('把黑桃1-6洗入牌库!')
#shoe = Shoe([ Card(1,'s'), Card(2,'s'), Card(3,'s'), Card(4,'s'), Card(5,'s'), Card(6,'s') ])
shoe = Shoe(8)
print ('开始洗牌')
shoe.shuffle()

def winAndPay(currentMoney, currentBet, currentRound):
    currentMoney = currentMoney + currentBet * 2
    currentRound = currentRound + 1
    currentBet = minBet

def loseAndPay(currentMoney, currentBet, currentRound):
    currentBet = currentBet * 2
    if (currentBet > 10000):
        currentBet = 5120
    currentRound = currentRound + 1
# 改:打多少靴
for j in range(10 * 3650):
    currentBet = minBet
    # 改:刀多少张牌. 加井号取消刀牌
    shoe.set_cut_card(-36)
    if (bankrupt):
        print ('破产强退!')
        break
    while (shoe.cardsLeft() >= 6):
        print ('第', currentRound + 1,'局开干', '剩余赌本: ', currentMoney)
        currentMoney -= currentBet
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
            currentMoney = currentMoney + currentBet
            currentRound = currentRound + 1
        elif (result > 0):
            print ('闲赢', ' 当前下注:', currentGuess, currentBet)
            # print ('闲赢', '闲家手牌: ', player, '; 庄家手牌: ', banker, '注金: ', currentBet)
            if (currentGuess == '庄'):
                currentBet = currentBet * 2
                if (currentBet == 5120): # 如果每注都开始押5120了
                    currentBet = 20      # 则跳回20
                currentRound = currentRound + 1
            else:
                currentMoney = currentMoney + currentBet * 2
                currentRound = currentRound + 1
                currentBet = minBet
        else:
            print ('庄赢', ' 当前下注:', currentGuess, currentBet)
            # print ('庄赢', '闲家手牌: ', player, '; 庄家手牌: ', banker, '注金: ', currentBet)
            if (currentGuess == '闲'):
                currentBet = currentBet * 2
                if (currentBet == 5120): # 如果每注都开始押5120了
                    currentBet = 20      # 则跳回20
                currentRound = currentRound + 1
            else:
                currentMoney = currentMoney + currentBet * 2
                currentRound = currentRound + 1
                currentBet = minBet
        # 改:跳闲跳庄
        if ((currentRound + 1) % 3 == 0):
            if (currentGuess == '闲'):
                currentGuess = '庄'
            else:
                currentGuess = '闲'
        if (currentRound % 6 == 0):
            shoe.reset()
            shoe.shuffle()
            break
        if (currentMoney < 0):
            print ('恭喜你破产了!')
            bankrupt = True
            break