#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import operator
from itertools import groupby


# In[2]:


def initcard():
    pokers = [['joker1', "0"], ['joker2', "1"]]
    poker = []
    for i in ['diamond', 'spade', 'heart', 'club']:
        for j in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
            poker = []
    return pokers


# In[3]:


def sort_card(player):
    temp = []
    for g in groupby(player, lambda x: x[0]):
        groups = []
        for i in g:
            groups.append(i)
        temp.append(groups)
    return temp


# In[4]:


def judge(x):
    if (len(x) < 5):
        return False
    for i0, i1 in zip(x[:4], x[1:]):
        if int(i0[1]) + 1 != int(i1[1]):
            return False
    return True


# In[5]:


def tonghua(res1):
    ans = False
    for i in res1:
        ans = ans or judge(i)
    return ans


# In[6]:


def onesession():
    cards = initcard()
    random.shuffle(cards)
    player1 = cards[0:18]
    player2 = cards[18:36]
    player3 = cards[36:54]
    player1 = sorted(player1, key=lambda x: (x[0] + f"{x[1] if len(x[1]) == 2 else '0' + x[1]}"))
    player2 = sorted(player2, key=lambda x: (x[0] + f"{x[1] if len(x[1]) == 2 else '0' + x[1]}"))
    player3 = sorted(player3, key=lambda x: (x[0] + f"{x[1] if len(x[1]) == 2 else '0' + x[1]}"))
    p1 = sort_card(player1)
    p2 = sort_card(player2)
    p3 = sort_card(player3)
    ans1 = tonghua(p1)
    ans2 = tonghua(p2)
    ans3 = tonghua(p3)
    ans = ans1 or ans2 or ans3
    return ans


# In[7]:


count = 0
# random.seed(3)
for i in range(0, 100000):
    tmpans = onesession()
    if tmpans:
        count = count + 1
print(count)

print(count/100000)
