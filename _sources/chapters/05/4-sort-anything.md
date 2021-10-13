---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Allgemeines Sortieren in Python

Wie könnten wir unsere Implementierung ändern, sodass wir alle möglichen Listen von vergleichbaren Elementen sortieren können?

```{exercise} Allgemeines Sortieren in Python
Ändern oder erweitern Sie Ihren Programmiercode um Listen bestehend aus Zahlen oder Karten zu sortieren.
```

Wir können den Vergleichsoperator ``is_smaller()`` als Argument übergeben!

```{code-cell} python3
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
```

```{code-cell} python3
hand = ['Bube', '6', 'Ass', '7', '9', '6']
stack_sort(hand, is_smaller)
```

```{code-cell} python3
numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
stack_sort(numbers, lambda a, b: a < b)
```

Lassen Sie sich von dem Ausdruck

```{code-cell} python3
lambda a,b : a < b
```

nicht verwirren. 
Dieser Ausdruck definiert eine Funktion der wir keinen Namen geben.
Um solch eine Funktion nutzen zu können müssen wir sie entweder direkt als Argument weiterreichen oder sie in eine Variable speichern.

````{admonition} Anonyme Funktionen
:name: def-anonym-function
Eine Funktion die keinen eigenen Namen hat, nennen wir *annonyme Funktion*.
````

````{admonition} Anonyme Funktionen in Python
:name: python-anonym-function
:class: hint

In Python definiert man diese durch das Schlüsselwort ``lambda`` gefolgt von den Funktionsargumenten und der Funktionsdefinition separiert durch den ``:``.
Anonyme Funktionen sind eine reine Erweiterung der *Syntax*.

**Beispiel:** 
```python 
addmul = lambda a, b : a + a * b
addmul(2,5)
````

Wir sparen uns damit ein paar Zeilen Code, da wir die definierte Funktion außerhalb des Aufrufs

```{code-cell} python3
stack_sort(numbers, lambda a, b: a < b)
```

nicht benötigen.
Der folgende Code wäre äquivalent:

```{code-cell} python3
numbers = [-33, -22, 123, 1, 13, 533, -23, 124]
def is_smaller_numbers(a, b):
    return a < b

stack_sort(numbers, is_smaller_numbers)
```