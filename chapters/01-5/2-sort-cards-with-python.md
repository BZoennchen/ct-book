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

(sec-sort-cards-with-python)=
# Karten sortieren in Python

Wir gehen nicht davon aus, dass Sie bereits jetzt alles verstehen was wir im Folgenden programmieren werden.
Ziel ist es aufzuzeigen, dass sich der Programmiercode kaum von unserer vorheriger Beschreibung unterscheidet und wir durch Programmiersprachen einen präzisen und vorgefertigten *Kontext* geschenkt bekommen.
Wir müssen diesen lediglich kennenlernen!
Was sich also ändert ist der *Kontext*.
Dieser ist in unserem Fall durch die Programmiersprache ``Python`` (ihrer [Syntax](def-syntax) und [Semantik](def-semantik)) und der verwendeten ``Python``-Module vorgegeben.


```{exercise} Karten sortieren in Python
:label: sort-cards-in-python-exercise
Implementieren Sie Ihren Algorithmus in ``Python``.
```

Im folgenden präsentieren wir eine Lösung.
Beachten Sie, dass es uns dabei nicht um die Laufzeit unseres Programms geht.
Die Lösung ist weder effizient noch besonders elegant und das ist für den Anfang auch in Ordnung.

## Modellierung der Karten und Hand

Da unser *Kontext* natürlich keine physikalische Hand definiert, müssen wir diese anderweitig *modellieren*.
Hierbei kommt die Abstraktion ins Spiel.

```{exercise} Modellierung
:label: exercise-sort-cards-modelling
Welche Eigenschaften der Hand benötigen wir und welche sind überflüssig?
```

Die ausschlaggebenden Eigenschaften der Karten auf der Hand sind:

1. Jede der $n$ Karten hat einen von $n$ nummerierten Plätzen auf der Hand (*Reihenfolge*)
2. Karten können von der Hand gelöscht und hinzugefügt werden
3. Es gibt eine *(totale) Ordnungsrelation* der Karten

Wir modellieren jede Karte als Zeichenkette.
Zum Beispiel steht ``'Bube'`` für einen der Buben des Kartendecks.
Je nachdem welches Kartendeck Sie verwenden, können Sie die Namen entsprechend anpassen.
Wir lassen alle unnötigen Informationen weg (*Abstraktion*).
Darunter fällt beispielweise die Kartenfarbe.

Eine Hand modellieren wir als Liste von Karten (Liste von Zeichenketten).

````{admonition} Liste (Python)
:class: remark
:name: python-list

Eine [Python Liste](sec-list) repräsentiert ein endliches **veränderbares** mathematisches Tupel.
Elemente können an jeder Position aus der Liste entfernt und eingefügt werden.
Die Position eines Elements in der Liste nennen wir *Index*.

Sei ``lst`` eine Liste und ``n`` die Anzahl ihrer Elemente, so sind 

```python
lst[0], lst[1], ..., lst[n-1]
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

Für die Modellierung der Ordnung gibt es ebenfalls viele verschiedene Möglichkeiten.
Eine Lösung besteht darin den *Index* eines weiteren Tupels als *Ordnung* zu verwenden.
Das Tupel muss lediglich alle möglichen Kartentypen geordnet enthalten.
Wir verwenden diesmal keine ``list`` sondern ein unveränderbares ``Python`` ``tuple``.

````{admonition} Tupel (Python)
:class: remark
:name: python-tuple

Ein [Python Tupel](sec-tuple) repräsentiert ein endliches **unveränderbares** mathematisches Tupel.
Die Position eines Elements im Tupel nennen wir *Index*.

Sei ``tpl`` ein Tupel und ``n`` die Anzahl seiner Elemente, so sind 

```python
tpl[0], tpl[1], ..., tpl[n-1]
```

seine Elemente.
````

```{code-cell} python3
cards = ('6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass')
```

Um die konkrete Implementierung von ``cards`` an einer zentralen Stelle ändern zu können, ist es sinnvoll eine ``Python``-[Funktion](sec-functions) zu schreiben, welche ``cards`` zurückgibt.
Sie brauchen noch ein wenig Erfahrung um den Unterschied und die Vorzüge zu verstehen.

```{code-cell} python3
def get_cards():
    return cards
```

Um die [Ordnung](exercise-sort-cards) einer Karte ``card`` zu bestimmen, iterieren wir durch alle ``cards`` und sobald wir die entsprechende Karte gefunden haben, geben wir den *Index* zurück.

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

Wir packen den Vergleich zweier Karten ``card1`` und ``card2`` in eine weitere ``Python``-[Funktion](sec-functions).

```{code-cell} python3
def is_smaller(card1, card2):
    i = index_of(card1)    # finde Position von Karte 1
    j = index_of(card2)    # finde Position von Karte 2
    return i < j           # Falls Position von Karte 1 < Position von Karte 2 gib wahr zurück, sonst falsch
```

Die Funktion ``is_smaller(card1, card2)`` gibt genau dann ``True`` (wahr) zurück, wenn die Karte ``card1`` kleiner ist als die Karte ``card2``.
Wir haben somit unseren *Kontext* erweitert.

## Sortieralgorithmus

Blicken wir zurück auf unseren Sortieralgorithmus.

```
H <- unsere Hand mit Karten
S <- ein leerer Stapel
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
Lassen Sie uns die Hand ``hand`` sortieren:

```{code-cell} python3
stack_sort(hand)
```

Was passiert wenn wir richtig viele Karten sortieren?
Der folgende Code erzeugt eine durchgemischte Hand mit ``1000`` Karten.
Wir erweitern dafür den *Kontext* um ein Paket ``random`` welches Funktionen für die Wahrscheinlichkeitsrechnung enthält.

```{code-cell} python3
---
tags: [output_scroll]
---
import random
hand = [random.choice(get_cards()) for _ in range(1000)]
hand
```

Sie werden merken, dass die Ausführung des folgenden Codes einen kurzen Moment dauert.

```{code-cell} python3
---
tags: [output_scroll]
---
stack_sort(hand)
```
