#!/usr/bin/env python
# coding: utf-8

# # Allgemeines Sortieren in Python
# 
# Wie könnten wir unsere Implementierung ändern, sodass wir alle möglichen Listen von vergleichbaren Elementen sortieren können?
# 
# ```{exercise} Allgemeines Sortieren in Python
# Ändern oder erweitern Sie Ihren Programmiercode um Listen bestehend aus Zahlen oder Karten zu sortieren.
# ```
# 
# Wir können den Vergleichsoperator ``is_smaller`` als Argument übergeben!
# Beachten Sie dass wir eine Funktion und keine reinen Daten übergeben.

# In[1]:


def stack_sort(hand, is_smaller):
    stack = [];                          
    while len(hand) > 0:                 
        card = remove_smallest_card(hand, is_smaller)
        stack.append(card)
    return stack

def remove_smallest_card(hand, is_smaller):
    i = find_smallest_index(hand, is_smaller)
    card = hand[i]
    del hand[i]
    return card

def find_smallest_index(hand, is_smaller):
    index = 0                                
    for i in range(len(hand)):               
        if is_smaller(hand[i], hand[index]): 
            index = i
    return index


# Den restlichen Code haben wir nicht verändert.

# In[2]:


def is_smaller(card1, card2):
    i = index_of(card1) 
    j = index_of(card2) 
    return i < j

def get_cards():
    return ('6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass')

def index_of(card):
    cards = get_cards()
    for index in range(len(cards)):
        if cards[index] == card:
            return index


# Mit dem richtigen Vergleichsoperator lassen sich noch immer Karten sortieren.

# In[3]:


hand = ['Bube', '6', 'Ass', '7', '9', '6']
stack_sort(hand, is_smaller)


# Mit einem anderen Vergleichsoperator lassen sich noch immer Zahlen sortieren.

# In[4]:


numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
def is_smaller_number(a, b):
    return a < b

stack_sort(numbers, is_smaller_number)

