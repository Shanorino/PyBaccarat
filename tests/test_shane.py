import os,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))[:-6]) #=dev first
from pybaccarat.playingcards import Card
from pybaccarat.playingcards import Shoe
from pybaccarat.baccarat import Hand
import random

player = Hand()
banker = Hand()
print ('给我黑桃1-6!')
shoe = Shoe([ Card(1,'s'), Card(2,'s'), Card(3,'s'), Card(4,'s'), Card(5,'s'), Card(6,'s') ])
#shoe = Shoe(1)
print ('开始洗牌')
shoe.shuffle()
for i in range(6):
    newCard = shoe.deal()
    if (i % 2 == 0):
        print ('发1张牌: ', newCard, '给闲')
        player.add(newCard)
    else:
        print ('发1张牌: ', newCard, '给庄')
        banker.add(newCard)
result = player.__cmp__(banker)
if (result == 0):
    print ('平局')
elif (result > 0):
    print ('闲赢')
else:
    print ('庄赢')
print (player.value())
print (banker.value())