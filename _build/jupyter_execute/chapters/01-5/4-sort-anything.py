# Allgemeines Sortieren in Python

Wie könnten wir unsere Implementierung ändern, sodass wir alle möglichen Listen von vergleichbaren Elementen sortieren können?

```{exercise} Allgemeines Sortieren in Python
Ändern oder erweitern Sie Ihren Programmiercode um Listen bestehend aus Zahlen oder Karten zu sortieren.
```

Wir können den Vergleichsoperator ``is_smaller()`` als Argument übergeben!

def find_smallest_index(hand, is_smaller):
    index = 0                                
    for i in range(len(hand)):               
        if is_smaller(hand[i], hand[index]): 
            index = i
    return index

def remove_smallest_card(hand, is_smaller):
    i = find_smallest_index(hand, is_smaller)
    card = hand[i]
    del hand[i]
    return card

def stack_sort(hand, is_smaller):
    stack = [];                          
    while len(hand) > 0:                 
        card = remove_smallest_card(hand, is_smaller)
        stack.append(card)
    return stack

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

hand = ['Bube', '6', 'Ass', '7', '9', '6']
stack_sort(hand, is_smaller)

numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
stack_sort(numbers, lambda a, b: a < b)

Lassen Sie sich von dem Ausdruck

lambda a,b : a < b

nicht verwirren. 
Dieser Ausdruck definiert eine Funktion der wir keinen Namen geben.
Diese nennen wir [anonyme Funktionen](sec-anonymous-function).
Um solch eine Funktion nutzen zu können müssen wir sie entweder direkt als Argument weiterreichen oder sie in eine Variable speichern.

Wir sparen uns damit ein paar Zeilen Code, da wir die definierte Funktion außerhalb des Aufrufs

numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
stack_sort(numbers, lambda a, b: a < b)

nicht benötigen.
Der folgende Code wäre äquivalent:

numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
def is_smaller_numbers(a, b):
    return a < b

stack_sort(numbers, is_smaller_numbers)