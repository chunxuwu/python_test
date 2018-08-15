# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:00:43 2018

10.8 调试硬币抛掷

一个简单的硬币抛掷猜测游戏，玩家有俩次猜测机会

@author: NEVERGUVEIP
"""

import random
guess = ''
while guess not in ('hands','tails'):
    print('guess the coin toss! Enter hands or tails')
    guess = input()

num = random.randint(0,1)
if num==1:
    toss='hands'
else:
    toss='tails'
        
if toss == guess:
    print('you got it!')
else:
    print('Nope! guess again!')
    guess = input()
    if toss == guess:
        print('you got it')
    else:
        print('Nope.you are really bad at this game.')
        