import os,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))[:-6]) #=dev first
from pybaccarat.playingcards import Card
from pybaccarat.playingcards import Shoe
from pybaccarat.baccarat import Hand
import random

player = Hand()
banker = Hand()
print ('把黑桃1-6洗入牌库!')
shoe = Shoe([ Card(1,'s'), Card(2,'s'), Card(3,'s'), Card(4,'s'), Card(5,'s'), Card(6,'s') ])
#shoe = Shoe(1)
print ('开始洗牌')
shoe.shuffle()
for i in range(6):
    if (i % 2 == 0):
        if (i != 4):
            newCard = shoe.deal()
            print ('发1张牌: ', newCard.get_rank(), '给闲')
            player.add(newCard)
        elif (player.need_hit(None)):
            newCard = shoe.deal()
            print ('发第3张牌: ', newCard.get_rank(), '给闲')
            player.add(newCard)
    else:
        if (i != 5):
            newCard = shoe.deal()
            print ('发1张牌: ', newCard.get_rank(), '给庄')
            banker.add(newCard)
        elif (banker.need_hit(player)):
            newCard = shoe.deal()
            print ('发第3张牌: ', newCard.get_rank(), '给庄')
            banker.add(newCard)
result = player.__cmp__(banker)
if (result == 0):
    print ('平局')
elif (result > 0):
    print ('闲赢')
else:
    print ('庄赢')