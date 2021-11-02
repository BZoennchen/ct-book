(sec-set)=
# Mengen - set

``Python``-Mengen (engl. [Set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)) ``set`` ist eine ungeordnete Zusammenfassung (engl. collection) von Elementen, wobei jedes Element in der Menge einzigartig ist.
Damit repräsentieren ``Python``-Mengen ``set`` *endliche* Mengen im mathematischen Sinne.
Endlich deshalb, weil die Elemente von ``Python``-Mengen explizit im Speicher liegen und wir nur endlich viel Arbeitsspeicher zur Verfügung haben.

Eine mathematische Menge $M$ ist ein abstraktes Objekt, das aus der Zusammenfassung einer Anzahl von einzelnen Elementen hervorgeht.
Dabei ist jedes Element was sich in der Menge befindet von allen anderen Elementen verschieden.
Anders als mathematische Tupel (durch die ``Python``-Tupel und den Listen motiviert sind) sind Mengen ungeordnet.

Von hier an meinen wir mit Mengen die ``Python``-Mengen ``set`` und sprechen ansonsten von mathematischen Mengen.

Mengen benutzten wir immer dann, wenn wir die Eigenschaft der Eindeutigkeit und Unordnung nutzten wollen.
Es ist an dieser Stelle anzumerken, dass der Test 

$$e \in M$$

für eine Menge deutlich weniger Rechenzeit benötigt als für eine Liste.
Dies hängt natürlich von der Größe der Liste ``list`` ab, überraschenderweise jedoch nicht von der Größe der Menge ``set``.
Befinden sich $n$ Elemente der Liste bzw. Menge so benötigen wir im schlechtesten Fall ca. $n$ Berechnungsschritte um festzustellen ob sich eine Element in der Liste befindet.
Verwenden wir hingegen eine Menge, so benötigen wir nicht mehr als eine bestimmte konstante Anzahl an Schritten.
In anderen Worten, der Test ist unabhängig von der Anzahl der Elemente die sich in der Menge befinden!

## Erstellung

Eine Menge erzeugen Sie ähnlich wie eine Liste.

numbers = {0, 1, 2, 3, 4, 5, 0}
numbers

Sie können Listen, Tupel und im Allgemeinen Sequenzen in Mengen umwandeln:

numbers = set(range(20))
print(numbers)
chars = set('aabcdddef')
print(chars)

Beachten Sie, dass hierbei doppelte Elemente nicht doppelt in der Menge vorkommen.
Beachten Sie auch, dass Sie eine leere Menge **nicht** mit ``{}`` sondern mit

emptyset = set()
emptyset

erzeugen!

## Indexierung?

Da Mengen ungeordnet sind, können wir diese nicht indexieren.
Folgender Code führt zu einem Fehler.

numbers = {0, 1, 2, 3, 4, 5}
numbers[2]

Wir können zwar testen, ob sich ein Element in der Menge befindet

numbers = {0, 1, 2, 3, 4, 5}
print(f'2 in numbers?: {2 in numbers}')
print(f'-3 in numbers?: {-3 in numbers}')

und wir können auch mit einer Schleife durch alle Elemente iterieren

numbers = {0, 1, 2, 3, 4, 5}
for number in numbers:
    print(number)

doch bleibt uns der Zugriff auf einzelne Elemente verwehrt.
Mengen bieten weder einen Index noch irgendetwas anderes durch das wir auf einzelne Mengenelemente zugreifen können.

## Mengenoperationen

Was Mengen bieten sind die sog. Mengenoperationen, welche den mathematischen Mengenoperationen gleichen.
Seien $A$ und $B$ mathematische Mengen und ``a``, ``b`` ihre entsprechenden ``Python``-Repräsentanten, dann entspricht

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(a - b)
print(a.difference(b))

$$A \setminus B$$

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(a | b)
print(a.union(b))

$$A \cup B$$

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(a & b)
print(a.intersection(b))

$$A \cap B$$

und

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(a ^ b)
print(a.symmetric_difference(b))

$$(A \cup B) \setminus (A \cap B)$$

Element in $A$ oder $B$ aber nicht in beiden, also $A$ und $B$ (entweder oder).

## Veränderung

Mengen sind **veränderlich** (engl. mutable) allerdings darf eine Menge nur **unveränderliche** (engl. immutable) Elemente enthalten!
Damit darf eine Menge keine Listen enthalten, weshalb folgender Code zu einem Fehler führt

```{admonition} Mengen in Python
:name: alert-sets-in-python
:class: warning
Eine Menge ist **veränderlich** darf jedoch lediglich **unveränderliche** Elemente enthalten.
```

myset = {0, 1, [2, 3, 4]}

Warum gilt dies?
Blicken wir auf folgendes (nicht funktionierendes) Beispiel

```python
list1 = [1,2,3]
list2 = [0,2,3]
myset = {list1, list2}
```

Es befinden sich nun zwei unterschiedliche Listen in der Menge ``myset``.
Soweit alles in Ordnung.
Was passiert allerdings wenn wir ``list2`` so verändern, dass sich ``list1 == list2`` ergibt?

```python
list2[0] = 1
```

Nach dieser Codezeile befänden sich zwei identische Elemente in der Menge, was natürlich nicht sein darf.
Die Menge müsste deshalb von dieser Änderung etwas mitbekommen und daraufhin sich selbst anpassen.
Das würde die Implementierung einer Menge immens verkomplizieren und würde zu großen Problemen führen.
Deshalb bekommt die Menge von dieser Änderung nichts mit und somit hätten wir den Salat.

Wir können mit den Funktionen ``add()`` und ``remove()`` Elemente zu einer Menge hinzufügen und löschen.

numbers = {0, 1, 2}
numbers.add(0)    # add duplicate, silently ignored
print(numbers)
numbers.add(3)    # add new element
print(numbers)
numbers.remove(1) # remove element
print(numbers)
numbers.remove(10) # remove non-existing element causes error
print(numbers)

Es gibt auch den Datentyp / Datenstrukturen ``frozenset``.
Diese ist im Gegensatz zu ``set`` **unveränderlich**.
Diese benötigen Sie wenn Ihre Menge weitere Mengen enthalten soll.

Wir können Mengen auch durch die Mengenoperationen verändern.
Wie der ``+``-Operator auf Listen und Tupel, legen die oben beschriebenen Operatoren Kopien im Speicher an.
Dies sehen wir, wie so oft, wenn wir uns die ``id``s ansehen:

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(f'id of a before difference: {id(a)}')

c = a - b
print(f'id of a after difference: {id(a)}')
print(f'id of c: {id(c)}')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

Wir können jedoch auch das Gegenstück zum ``+=``-Operator verwenden:

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9, 11}

print(f'id of a before difference: {id(a)}')

a -= b
print(f'id of a after difference: {id(a)}')
print(f'a = {a}')
print(f'b = {b}')

Wir sehen, dass in diesem Fall der Speicherbereich durch den wir zu Beginn durch ``a`` zugreifen können, verändert wird.

## Mengen und der Speicher

Wenn Sie verstanden haben wie Mengen im Speicher realisiert werden, wird Ihnen noch klarer warum diese nur **unveränderliche** Elemente enthalten dürfen.
Eine ausgiebige Beschreibung dessen finden Sie im Kapitel [Namensregister](sec-name-register), genauer im Abschnitt [Hashing und das Dictionary](sec-hashing).
Lassen Sie uns dennoch versuchen die Grundproblematik und das Grundprinzip herauszuarbeiten.

Auf dem Computer gibt es keine Hardwareeinheit, die so etwas wie eine Menge realisieren würde.
Der Speicher eines Computers ist eine sehr lange Liste auf deren Elemente wir durch Indices (**Adressen**) zugreifen können.
Kennen wir die Adresse, so ist der Zugriff enorm schnell.

Um zu testen ob sich ein Element in der Liste befindet, müssen wir es in der Liste suchen und im schlimmsten Fall alle Elemente durchgehen.

mylist = [1, 'a', 2, 5, 6, 8]
6 in mylist

entspricht folgendem Code

mylist = [1, 'a', 2, 5, 6, 8]
contains = False
for element in mylist:
    if 6 == element:
        contains = True
        break
contains

Genau dieses Durchsuchen versuchen Mengen zu verhindern.
Ok, machen wir es uns ein wenig einfacher.
Nehmen wir einmal an Sie möchten eine Menge von Zahlen haben und diese Menge auch verändern.
Sie wissen jedoch, dass die Zahlen $k$ alle zwischen 100 und 130 liegen, genauer gesagt $100 \leq k < 130$.
Wir könnten wir unter diesen Voraussetzungen eine Menge als Liste implementieren?

Wir wählen eine Liste die immer hundert Elemente enthält, sodass wir für eine gegebene Zahl $k$ den zugehörigen Listenindex

$$i \leftarrow (k-100)$$

Aber hatten wir nicht gesagt, dass eine Liste keine Lücken enthält?
Wir können künstliche Lücken einfügen.
Unsere leere Menge enthält 30 'Lücken'.
Wir verwenden hierfür das Symbol für das Nichts, d.h., ``None``.

emptyset = [None for i in range(30)]
emptyset

Um eine Element ``k`` hinzuzufügen müssen wir

1. seinen Index berechnen
2. und es hinzufügen.

myset = [None for i in range(30)]
k = 122
index = k - 100
myset[index] = k
myset

Um zu testen ob sich ein gegebenes Element in der Menge befindet reicht es 

1. seinen Index zu berechnen und
2. zu prüfen ob es an dieser Stelle in der Liste ist.

k1 = 123
index1 = k1 - 100

k2 = 122
index2 = k2 - 100

print(f'{k1} in myset?: {myset[index1] == k1}')
print(f'{k2} in myset?: {myset[index2] == k2}')

Sowohl das Hinzufügen als auch das Testen sind immens schnelle Operationen.
Wir müssen nur eine arithmetische Berechnung durchführen und sind bereits am Ziel.

Auf diesem Prinzip basieren Mengen ``set`` bzw. ``frozenset`` (und auch Wörterbücher ``dict``) in ``Python`` und anderen Programmiersprachen.
Der Index wird abhängig von Element selbst berechnet.
Eine Menge verwendet mehr Speicher als Ihre Elemente benötigen -- anders als Listen enthält enthält sie Lücken.
Dadurch sind die Elemente im Speicher breit verteilt.

Für ganze Zahlen in einem bestimmten Bereich ist das noch einfach, da die Funktion für die Berechnung des Index simpel ist.
Für beliebige Objekte wird dies deutlich schwieriger.
Wir diskutieren dies im Kapitel [Namensregister](sec-name-register) im Detail.