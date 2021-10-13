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

(sort-cards-with-python)=
# Karten sortieren in Python

Wir gehen nicht davon aus, dass Sie bereits jetzt alles verstehen was wir im Folgenden programmieren werden.
Ziel ist es aufzuzeigen, dass sich der Programmiercode kaum von unserer obigen Beschreibung unterscheidet und wir durch Programmiersprachen einen präzisen und vorgefertigten *Kontext* bekommen.
Wir müssen diesen lediglich kennenlernen!
Was sich also ändert ist der *Kontext*.
Dieser ist in unserem Fall durch die Programmiersprache ``Python`` (ihrer *Syntax* und *Semantik*) und importierter Pakte vorgegeben.


```{exercise} Karten sortieren in Python
:label: sort-cards-in-python-exercise
Implementieren Sie Ihren Algorithmus in ``Python``.
```

## Modellierung der Karten und Hand
Da unser *Kontekt* natürlich keine physikalische Hand definiert, müssen wir diese anderweitig definieren bzw. *modellieren*.
Hierbei kommt die Abstraktion ins Spiel.

```{admonition} Modellierung der Hand
:class: attention
Welche Eigenschaften der Hand benötigen wir und welche sind überflüssig?
```

Die ausschlaggebenden Eigenschaften der Karten auf der Hand sind:

1. Jede der $n$ Karten hat einen von $n$ nummerierten Plätzen auf der Hand (*Reihenfolge*)
2. Karten können von der Hand gelöscht und hinzugefügt werden
3. Es gibt eine *(totale) Ordnungsrelation* der Karten

Wir modellieren jede Karte als Zeichenkette.
Zum Beispiel steht ``'Bube'`` für einen der Buben des Kartendecks.
Je nachdem welches Kartendeck Sie verwenden, können Sie die Namen anpassen.
Wir lassen alle unnötigen Informationen, wie zum Beispiel die Kartenfarbe, weg (*Abstraktion*).

Eine Hand modellieren wir als Liste von Karten (Liste von Zeichenketten).

````{admonition} Mathematisches Tupel

Ein *mathematisches Tupel* besteht aus endlich vielen, nicht notwendigerweise voneinander verschiedenen Objekte. 
Dabei spielt, im Gegensatz zu Mengen, die Reihenfolge der Objekte eine Rolle.
````


````{admonition} Liste (Python)

Eine *Python Liste* repräsentiert ein endliches veränderbares *mathematisches Tupel*.
Elemente können an jeder Position aus der Liste entfernt, und eingefügt werden.
Die Position eines Elements in der Liste nennen wir *Index*.
Beinhaltet die Liste ``l``, ``n`` Elemente, so sind 

```python
l[0], l[1], ..., l[n-1]
```

ihre Elemente.
````

Folgende Liste ist ein Beispiel für eine Hand mit 6 Karten.

```{code-cell} python3
hand = ['9', '6', '6', 'Bube', 'Ass', '7']
hand
```

Der Befehl

```{code-cell} python3
del hand[3]
hand
```

löscht das vierte Element (das Element mit Index 3) aus der Liste.
Um das Element wieder einzufügen können wir

```{code-cell} python3
hand.insert(3, 'Bube')
hand
```

verwenden.

## Modellierung der Ordungsrelation

Auch hier gibt es viele verschiedene Möglichkeiten.
Eine Lösung besteht darin den *Index* eines Tupels als *Ordnung* zu verwenden.
Das Tupel muss lediglich alle möglichen Kartentypen geordnet enthalten.
Wir verwenden diesmal keine ``list`` sondern ein unveränderbares Python ``tuple``.

````{admonition} Tupel (Python)

Ein *Python-Tupel* repräsentiert ein endliches unveränderbares *mathematisches Tupel*.
Die Position eines Elements im Tupel nennen wir *Index*.
Beinhaltet das Tupel ``l``, ``n`` Elemente, so sind 
```python
l[0], l[1], ..., l[n-1]
```
ihre Elemente.
````

```{code-cell} python3
cards = ('6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass')
```

Um die konkrete Implementierung von ``cards`` an einer zentralen Stelle ändern zu können, ist es sinnvoll eine Funktion zu schreiben, welche ``cards`` zurückgibt.
Sie brauchen noch ein wenig Erfahrung um den Unterschied und die Vorzüge zu verstehen.

```{code-cell} python3
def get_cards():
    return cards
```

Um die *Ordnung* einer Karte ``card`` zu bestimmen iterieren wir durch alle ``cards`` und sobald wir die entsprechende Karte gefunden haben, geben wir den *Index* zurück.

```{code-cell} python3
def index_of(card):
    for index in range(len(get_cards())):
        if cards[index] == card:
            return index

index_of('Bube')
```

Um zwei Karten vergleichen zu können, vergleichen wir ihre Indices.

```{code-cell} python3
index_of('7') < index_of('König')
```

Wir packen den Vergleich zweier Karten ``card1`` und ``card2`` in eine weitere Funktion.

```{code-cell} python3
def is_smaller(card1, card2):
    i = index_of(card1)    # finde Position von Karte 1
    j = index_of(card2)    # finde Position von Karte 2
    return i < j           # Falls Position von Karte 1 < Position von Karte 2 gib wahr zurück, sonst falsch
```

## Sortieralgorithmus

Blicken wir zurück auf unseren Sortieralgorithmus.

```
Sei H unsere Hand mit Karten
Sei S ein leerer Stapel
Solange noch Karten auf der Hand H sind:
    Lege kleinste Karte auf der Hand H auf Stapel S 
```

In ``Python`` sieht das ganz wie folgt aus.

```{code-cell} python3
def stack_sort(hand):                               # Sei H unsere Hand mit Karten (Argument der Funktion)
    stack = [];                                     # Sei S ein leerer Stapel
    while len(hand) > 0:                            # Solange noch Karten auf der Hand H sind:
        stack.append(remove_smallest_card(hand))    # Lege kleinste Karte auf der Hand H auf Stapel S 
    return stack                                    # Gib den Stapel zurück (Rückgabewert)
```

Wir haben die Logik in eine Funktion gepackt, sodass wir diese bequem Aufrufen können.
Wir haben unseren *Kontext* um diese Funktion erweitert.
Leider ist die Funktion ``remove_smallest_card`` in unserem *Kontext* noch nicht definiert.
Das holen wir nach.

```{code-cell} python3
def remove_smallest_card(hand):    # Sei H unsere Hand mit Karten (Argument der Funktion)
    i = find_smallest_index(hand)  # Finde Position der kleinsten Karte auf der Hand
    card = hand[i]                 # Merke dir Karte an der Position der kleinsten Karte auf der Hand
    del hand[i]                    # Lösche Karte an der Position der kleinsten Karte auf der Hand
    return card                    # Gib gemerkte Karte zurück (Rückgabewert)
```

Wir haben das Problem ``remove_smallest_card`` in Unterprobleme aufgeteilt (*Dekomposition*).
Die Funktion ``find_smallest_index`` soll uns den *Index* der kleinsten Karte auf der Hand zurückgeben.

```{code-cell} python3
def find_smallest_index(hand):
    index = 0                                # Merke dir Position 0
    for i in range(len(hand)):               # Gehe durch alle Positionen 0 bis (Anzahl der Karten auf der Hand) - 1
        if is_smaller(hand[i], hand[index]): # Falls Karte an Position i kleiner ist als an der gemerkten Position
            index = i                        # Merke dir Position i
    return index                             # Gib gemerkte Position zurück  
```

Jetzt ist alles in unserem *Kontext* definiert was notwendig ist und wir können den Sortieralgorithmus ``stack_sort`` ausführen.
Lasst uns unsere Hand ``hand`` sortieren.

```{code-cell} python3
stack_sort(hand)
```

Was passiert wenn wir richtig viele Karten sortieren?
Der folgende Code erzeugt eine durchgemischte Hand mit ``1000`` Karten.
Wir erweitern dafür den *Kontext* um ein Paket ``random`` welches Funktionen für die Wahrscheinlichkeitsrechnung enthält.

```{code-cell} python3
import random
hand = [random.choice(get_cards()) for _ in range(1000)]
hand
```

Sie werden merken, dass die Ausführung des folgenden Codes einen kurzen Moment dauert.

```{code-cell} python3
stack_sort(hand)
```
