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

(sec-list)=
# Listen - list

Listen (engl. [List](https://docs.python.org/3/library/stdtypes.html#list)) ``list`` sind eine der wichtigsten *Datentypen* und zugleich einfachsten [Datenstrukturen](sec-data-structures) in ``Python``.
Sobald Sie irgendetwas sinnvolles programmieren möchten, kommen Sie um die Liste kaum herum.
Das Grundkonzept einer Liste ist einfach und doch so fundamental wichtig!

## Motivation

Nehmen wir einmal an wir bekämen den Auftrag ein Programm zu schreiben, welches ``n`` ganze Zahlen aufaddiert, wobei wir weder ``n`` noch die Zahlen kennen.
Zugegeben, das Programm ist nicht gerade interessant aber aller Anfang ist klein.
Eine variable Anzahl an unbekannten Zahlen lässt sich hervorragend durch eine Liste *modellieren*.
Wir gehen also davon aus, dass wir eine Liste ``numbers`` bekommen und daraus die Summe berechnen müssen.

Folgender Code löst die Aufgabe.
``numbers`` ist eine Liste, welche zwei Zahlen (1 und 2) enthält.

```{code-cell} python3
numbers = [1, 2]

result = 0
for x in numbers:
  result += x

result
```

Der Code funktioniert auch dann noch, wenn ``numbers`` mehr, weniger oder andere Zahlen enthält!
Probieren Sie es aus.

```{admonition} Python's Datenstrukturen
:class: remark
:name: remark-python-ds
In ``Python`` können *Datenstrukturen* Werte von unterschiedlichen *Datentypen* enthalten.
```

Wie alle Datenstrukturen in ``Python``, können Listen Werte mit unterschiedlichen Datentypen enthalten.

```{code-cell} python3
mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
mylist
```

Listen können selbstverständlich andere Listen (bzw. Datenstrukturen) enthalten:

```{code-cell} python3
mylist = [['a','b','c'], 2, 3, [1, 2, 3]]
mylist
```

So können wir beispielsweise eine (mathematische) $m \times n$ Matrix ``A`` als zweidimensionale Liste *modellieren*:

```{code-cell} python3
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

In diesem Fall repräsentiert ``A`` die Identitätsmatrix

$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.$$

## Erstellung

Es gibt unterschiedliche Möglichkeiten um eine Liste zu erzeugen.
Wir können, z.B., mit einer leeren Liste starten und diese füllen:

```{code-cell} python3
numbers = []
numbers.append(0)
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers
```

oder kürzer

```{code-cell} python3
numbers = []
for i in range(6):
  numbers.append(i)

numbers
```

Oder wir starten mit einer vollen Liste.

```{code-cell} python3
numbers = [0, 1, 2, 3, 4, 5]
numbers
```

Die *built-in* Funktion ``range()`` erzeugt einen sog. Zahlenbereich (engl. [Range](https://docs.python.org/3/library/stdtypes.html#typesseq-range)), welchen wir im Abschnitt [Bereich - range](sec-range) noch erörtern werden.
Wir können diesen Bereich, der auch eine Sequenz ist, in eine Liste packen bzw. in eine Liste umwandeln:

```{code-cell} python3
numbers = [i for i in range(10)]
numbers
```

Oder noch kürzer:

```{code-cell} python3
numbers = list(range(10))
numbers
```
(sec-list-index)=
## Indexierung

Wir können auf die Elemente einer Liste mit einem *Index* zugreifen.
Dieser Index beginnt bei $0$ und endet bei der $n - 1$, wobei $n$ gleich der Länge der Liste ist (``n = len(lst) - 1``).
``len(lst)`` gibt eine natürliche Zahl (0 inklusive) zurück, welche die Länge der Liste ``lst`` angibt.

```{code-cell} python3
lst = [1,2,3,'a','b','c',1.0,2.0,3.0]
len(lst)
```

In anderen Worten: Die Elemente einer Liste sind in aufsteigender Reihenfolge angeordnet.
Jedes Element hat seinen Platz bzw. Index und kein Platz ist leer!

```{code-cell} python3
print(lst[0])
print(lst[len(lst)-1])
```

In ``Python`` können wir statt ``lst[len(lst)-1]``  auch ``lst[-1]`` schreiben.

```{code-cell} python3
print(lst[len(lst)-1])
print(lst[-1])
```

``Python`` bietet eine angenehme und mächtige [Syntax](def-syntax) um einen Teil der Liste in eine neue Liste zu **kopieren** ([flache Kopie](sec-copy-of-ds)).
Mit ``lst[start:ende:i]`` nehmen wir jedes ``i``-te Element beginnend von ``start`` bis ``ende``.
Dabei ist ``i`` optional und ist gleich ``1``, wenn es nicht angegeben wird.
Bei diesen Operationen bleibt ``lst`` unverändert.

```{code-cell} python3
lst = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(lst[1:8:2])
print(lst[1:8:1])
print(lst[1:8])
print(lst)
```

Auch eine negative Indexierung ist erlaubt.

```{code-cell} python3
lst = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(lst[8:1:-2])
print(lst[-3:-8:-2])
```

## Veränderung

Anders als [Tupel](sec-tuple) ``tuple`` sind Listen *veränderbar*, d.h. wir können Elemente löschen und hinzufügen.

```{code-cell} python3
chars = ['a','b','c']
print(f'chars: {chars} before append.')
chars.append('d')
print(f'chars: {chars} before remove.')
chars.remove('b')
print(f'chars: {chars} after remove.')
```

Dabei fügt ``append`` das neue Element hinten an.
Um ein Listenelement anhand seines Indexes zu löschen können wir ``del`` (engl. delete) verwenden.

```{code-cell} python3
chars = ['a','b','c']
print(f'chars: {chars} before del.')
del chars[1]
print(f'chars: {chars} after del.')
```

``del`` funktioniert in Kombination mit dem Indexieren, d.h. wir können viele Elemente mit einem Befehl löschen.
Im folgenden löschen wir jedes 2-te Element wodurch nur ungerade Zahlen übrig bleiben.

```{code-cell} python3
numbers = list(range(20))
print(f'numbers: {numbers} before del.')
del numbers[::2]
print(f'numbers: {numbers} after del.')
```

Sobald ein Element gelöscht wird, verkleinert sich auch die Liste.
Es entstehen keine Lücken.

Wir können auch ein Element an einer bestimmten Stelle einfügen.

```{code-cell} python3
chars = ['a','b','c']
print(f'chars: {chars} before insert.')
chars.insert(1, 'd')
print(f'chars: {chars} after insert.')
```

Dieser Code fügt das Element ``'d'`` vor das Element mit dem Index 1 ein.
Anders ausgedrückt: Das eingefügte Element ``element`` hat nach der Operation ``insert(index, element)`` den Index ``index``.

(sec-list-and-memory)=
## Listen und der Speicher

Wie funktioniert eine Liste im tieferen Sinne?
Also wie ist sie im Speicher abgelegt, was passiert wenn wir sie verändern und wie greifen wir auf sie und ihre Elemente über **Adressen** zu?

### Anordnung im Speicher

Um zu verstehen wie und warum Listen funktionieren müssen wir eine wichtige Tatsache festhalten, die wir bereits im Abschnitt [Variablen](sec-variables) unbemerkt verwendet haben:
Kennen wir eine **Adresse** eines **Werts**, kurz gesagt die *Variable* welche auf den Wert zeigt, so ist der Zugriff auf diesen Wert extrem schnell!

```{admonition} Speicheradressierung
:name: remark-mem-addr-speed
:class: remark

Kennen wir die Speicheradresse, so können wir die Adressierung als Operation mit konstanter Laufzeit $\mathcal{O}(1)$ annehmen.
```

Es gibt kleine 'Strafen', wenn **Adressen**, die wir nacheinander verwenden, weit auseinander liegen.
Diese Strafen sind jedoch in den meisten Anwendungen vernachlässigbar.

Lassen Sie uns mit dieser Information anhand eines Beispiel testen, wie sich die **Adressen** und **Werte** einer ``list`` (aus Zahlen) verhalten.

```{code-cell} python3
numbers = [1, 2, 3, 4, 5]
print(f'value of numbers = {numbers}')
print(f'id of numbers = {id(numbers)}')

print(f'value of numbers[2] = {numbers[2]}')
print(f'id of numbers[2] = {id(numbers[2])}')
print('change value of numbers[2]')

numbers[2] = -20

print(f'value of numbers = {numbers}')
print(f'id of numbers = {id(numbers)}')
print(f'value of numbers[2] = {numbers[2]}')
print(f'id of numbers[2] = {id(numbers[2])}')
```

Im obigen Code erstellen wir eine Liste, welche die Zahlen 1 bis 5 enthält.
Dann verändern wir das zweite Element der Liste (eine Liste startet mit dem 0-ten Element).
Die **Adresse** der *Variable* ``numbers`` ändert sich bei diesem Vorgang nicht!
Allerdings ändert sich die Adresse des Elements ``numbers[2]`` und somit der **Wert** von ``numbers``.

```{figure} ../../figs/python-tutorial/datatypes/list.png
---
width: 600px
name: fig-data-type-list
---
Die Liste aus unserem obigen Beispiel **bevor** wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Ändern wir den **Wert** eines Listenelements, so verändern wir die **Adresse** am Index dieses Elements.
In unserem Beispiel ändern wir den Wert am Index 2 von 5 auf -20.
Dadurch verändert sich die Adresse von $adr_2^*$ auf $adr_2'$.
Vergleichen Sie die {numref}`Abbildung {number} <fig-data-type-list>` und {numref}`{number} <fig-data-type-list-2>`.

```{figure} ../../figs/python-tutorial/datatypes/list-2.png
---
width: 600px
name: fig-data-type-list-2
---
Die Liste aus unserem obigen Beispiel **nachdem** wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Alle *Datenstrukturen* sind *Behälter*, die andere Daten aufnehmen können, ähnlich wie Schließfächer, Ordner oder Rucksäcke.
Nehmen wir als Analogie die Schließfächer aus der echten Welt.
Stellen wir uns vor, der Platz in einem Schließfach wäre ein Teil des Speicherplatzes, welcher von unserer Liste benötigt wird.
Was befindet sich nun in unseren Schließfächern?
In ``Python`` sind es **nicht** die Objekte/Werte selbst sondern die **Adresse** der Objekte/Werte.
Es befindet sich quasi ein Zettel auf dem der Hinweis steht, wo wir das Objekt, was zu jenem Schließfach gehört, finden.
Oder aber wir stellen uns eine Schnur vor, die von dem Schließfach auf das Objekt verweist.

Blicken wir auf ein etwas komplizierteres Beispiel: eine Liste die wiederum eine Liste enthält.

```{code-cell} python3
mylist = [1, ['a', 'b'], 5]
print(f'value of mylist = {mylist}')
print(f'id of mylist = {id(mylist)}')

print(f'value of mylist[1] = {mylist[1]}')
print(f'id of mylist[1] = {id(mylist[1])}')
print('change value mylist[1][0]')

mylist[1][0] = 'c'

print(f'value of mylist = {mylist}')
print(f'id of mylist = {id(mylist)}')
print(f'value of mylist[1] = {mylist[1]}')
print(f'id of numbers[1] = {id(mylist[1])}')
```

In diesem Beispiel verändern wir ein Element der Datenstruktur, welche unsere Liste ``mylist`` enthält.
Der Effekt ist ein anderer als zuvor, denn die Adresse $adr_1^*$ ändert sich diesmal nicht!
Stattdessen verändern wir die Adresse $adr_{1,0}^*$ der Datenstruktur, welche unsere Liste enthält.

```{figure} ../../figs/python-tutorial/datatypes/list-in-list.png
---
width: 400px
name: fig-data-type-list-in-list
---
Die Liste aus unserem obigen Beispiel **bevor** wir den Wert ``'a'`` auf ``'c'`` gesetzt haben.
```

Die **Adressen** welche ``mylist`` enthält bleiben **unverändert** und trotzdem ändern wir den Inhalt von ``mylist``.
Vergleichen Sie die {numref}`Abbildung {number} <fig-data-type-list-in-list>` und {numref}`{number} <fig-data-type-list-in-list-2>`.

```{figure} ../../figs/python-tutorial/datatypes/list-in-list-2.png
---
width: 400px
name: fig-data-type-list-in-list-2
---
Die Liste aus unserem obigen Beispiel **nachdem** wir den Wert ``'a'`` auf ``'c'`` gesetzt haben.
```

Selbst wenn wir anstatt einer Liste ein **unveränderliches** [Tupel](sec-tuple) verwenden würden, könnten wir diese Veränderung durchführen.

```{admonition} Unveränderlichkeit in Python
:class: attention
:name: attention-immutable-in-python
Ist eine Datenstruktur ``ds`` *unveränderlich* bedeutet dies lediglich, dass sich die Adressen, welche ``ds`` enthält nicht ändern können.
Enthält die Datenstruktur jedoch eine weitere *veränderliche* Datenstruktur ``mut_ds``, so können sich die Adressen von ``mut_ds`` und damit der Wert von ``ds`` durchaus ändern!
```

Das besondere einer Liste, bzw. die Charakteristik welches Sie auszeichnet ist, dass 

1. die **Adressen** Ihrer Elemente ohne Lücke nebeneinander im Speicher liegen und
2. diese **Adressen** veränderlich sind.

### Adressenberechnung

Da **Adressen** immer die gleiche feste Anzahl an [Bits](def-bit) benötigen, kann man für eine gegebene

+ Adresse $adr$ einer Liste und
+ einem Index $i$ eines Elements,

die Speicheradresse $adr_i^*$, welche die Speicheradresse $adr_i$ enthält, die auf das $i$-te Element zeigt, extrem schnell berechnen.
Das klingt verwirrend, ist im Grunde aber ganz simpel.

Angenommen die Adresse der Liste ``lst`` ist $adr$ und jede Adresse benötigt 4 Byte und wir können 1 Byte adressieren.
Nehmen wir zusätzlich an, die Länge der Liste befindet sich ganz vorne im Speicherbereich der Liste und verbraucht einen Adressenplatz. 
Dann befindet sich die Adresse $adr_i^*$ des $i$-ten Elements an der Speicheradresse:

$$adr_i = 4 + adr + i \cdot 4 = adr + (i+1) \cdot 4.$$

Vergleichen Sie die {numref}`Abbildung {number} <fig-data-type-list-in-list>` und {numref}`{number} <fig-data-type-list-in-list-2>`.
Diese Rechnung kann der Rechner sehr schnell durchführen und deshalb können wir auf ein Element einer Liste dessen Index wir kennen extrem schnell zugreifen.

### Übung

Um dieses Konzept besser zu verstehen und herauszufinden wie sich [atomare](def-atomare-data-types) wie auch [zusammengesetzte Datentypen](def-data-structures) verhalten, hilft oft nur eins: Ausprobieren!

Im Kapitel [Speicher - alles ist eine Liste](sec-memory) erstellen wir unser eigenes Speicherverwaltungssystem durch ``Python``-Listen.
Diese Übung bietet detaillierte Einblicke in die funktionsweise des Speichers und wie es gelingt Listen voller **Adressen** zu verwalten.

## Der Unterschied zwischen + und +=

Die Operatoren ``+`` und ``+=`` sind in ``Python`` auch für Listen definiert.
Ähnlich wie bei [Zeichenketten](sec-string), verkettet er zwei Listen.
Überraschenderweise bewirkt jedoch folgender Code

```{code-cell} python3
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f' id before concat: {id(list1)}')
list1 = list1 + list2
print(f' id after concat: {id(list1)}')
list1
```

nicht das selbe wie 

```{code-cell} python3
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f' id before concat: {id(list1)}')
list1 += list2
print(f' id after concat: {id(list1)}')
list1
```

auch wenn ``list1`` in beiden Fällen die gleichen Werte enthält, so ändert sich im ersten Fall die **Adresse** von ``list1``.
Im zweiten Fall bleibt die ``id`` und damit die **Adresse** unverändert.
Was bedeutet das?

Verwenden wir ``liste1 + liste2`` so wird eine neue Liste im Speicher angelegt und die Verkettung der beiden Listen wird dort abgelegt.
D.h. die **Adressen** $adr_0^*, adr_1^0, \ldots$ der Listenelemente der beiden Listen werden **kopiert**!
Die beiden Listen, die bei der Operation teilnehmen, bleiben unverändert.

Verwenden wir hingegen ``liste1 += liste2`` so werden die **Adressen** der Elemente von ``liste2`` kopiert und an ``liste1`` angehängt.
Damit wird ``list1`` verändert und es wird keine neue Liste angelegt!
``liste1 += liste2`` entspricht somit

```{code-cell} python3
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x in list2:
    list1.append(x)
list1
```

und ``concat_list = liste1 + liste2`` entspricht

```{code-cell} python3
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concat_list = []
for x in list1:
    concat_list.append(x)
for x in list2:
    concat_list.append(x)
concat_list
```

```{admonition} Die += und + Operatoren
:class: remark
:name: remark-plus-and-plusequal
Nicht nur ``+=`` und ``+`` verhalten sich in dieser Art und Weise, sondern auch ``-=`` und ``-`` oder ``|=`` und ``|`` und viele weitere Operatoren.
```

(sec-copy-of-ds)=
## Tiefe und flache Kopien

Wir müssen uns noch einmal dem wichtigen Unterschied zwischen [Identität und Gleichheit](sec-vars-equality-and-identity) widmen.

### Identität und Gleichheit

Wollen wir einen Wert einer Variablen ``x`` kopieren, so stellt sich die Frage: 
Sollen das Original ``x`` und die Kopie ``y`` **gleich** oder **identisch** sein?
Ein Beispiel:

```{code-cell} python3
# shallow copy
x = 100_000
y = x
print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
```

```{code-cell} python3
# deep copy
x = 100_000
y = 100_000
print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
```

Im ersten Fall setzen wir die Adresse von ``y`` auf die Adresse von ``x``.
Somit *zeigen* beide Variablen auf die gleiche Adresse d.h. auf den *identischen* Wert.
Sind zwei Variablen identisch so sind sie immer auch gleich.

Im zweiten Fall setzten wir den Wert beider Variablen auf den gleichen Wert.
Jedoch *zeigen* die Variablen ``x`` und ``y`` auf unterschiedliche Speicherbereiche.
Somit sind die Variablen gleich aber nicht identisch.

Kopieren wir eine Variable, so gibt es diese beiden Möglichkeiten.
Entweder ist die Kopie *identisch* oder aber *gleich*.
Und je nachdem was wir erzielen, sprechen wir von einer *flachen* (Kopie ist identisch) oder *tiefen Kopie* (Kopie ist gleich).

Im ersten Fall, handelt es sich um eine *flache* und im zweiten obigen Fall um eine *tiefe Kopie*.
Im Fall von *atomaren Datentypen* spielt es keine Rolle ob wir eine flache oder tiefe Kopie machen.
Warum? Weil wir den Wert im Speicher eines *atomaren Datentyps* ohnehin nicht verändern können.
Egal auf welche Speicheradresse ``y`` im obigen Beispiel zeigt, solange ihr Wert den richtigen Wert ``100_000`` hat, kann nichts schief gehen.

Diese Gleichgültigkeit ist wesentlich für die digitale Welt, welche ausschließlich aus [Repräsentanten](sec-representation) besteht.
In der Realwelt macht es einen riesigen Unterschied ob sich, zum Beispiel, zwei Menschen ein Bett teilen -- ob also ihr Bett identisch ist -- oder ob sie das exakt gleiche Bett besitzen.
Da auf dem digitalen Computer nur Repräsentanten existieren, welche auf etwas 'Echtes' verweisen, ergibt sich diese Gleichgültigkeit.
Um Speicherplatz zu sparen sind deshalb *flache Kopien* im Fall von *atomare Datentypen* besser geeignet.

Anders als für *atomare Datentypen* ist es für *Datenstrukturen* ganz und gar nicht egal ob wir eine *flache* oder *tiefe Kopie* erzeugen.
[Datenstrukturen](def-data-structures) sind Repräsentanten die andere Repräsentanten strukturieren.
Doch ändert sich die Struktur, d.h., der Inhalt der Datenstruktur, so ändert sich auch das was die Datenstruktur repräsentiert.
Anders als *atomare Datentypen* kann sich die [Bedeutung](def-semantik) der Datenstruktur ändern (siehe auch Abschnitt [Interpretation](sec-interpretation)).

```{code-cell} python3
# shallow copy
x = [1,2,3]
y = x

print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
y[0] = -20
print(f'change y')
print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
print(f'value of x: {x}')
print(f'value of y: {y}')
```

Handelt es sich um eine *flache Kopie* so zeigen beide **Adressen** der Datenstrukturen auf den jeweils gleichen Speicherbereich.
Ändern wir diesen Speicherbereich, so wirkt sich das auf beide Variablen gleichermaßen aus.

```{code-cell} python3
# deep copy
x = [1,2,3]
y = [1,2,3]

print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
y[0] = -20
print(f'change y')
print(f'x and y are identical? answer: {x is y}')
print(f'x and y are equals? answer: {x == y}')
print(f'value of x: {x}')
print(f'value of y: {y}')
```

Im Fall einer *tiefen Kopie* wirkt sich die Änderung des Werts der einen Variablen nicht auf die andere aus.
Vergleichen Sie das obige Beispiel.

### Datenstrukturen kopieren

Für Datenstrukturen gibt es nicht nur die eine *flache Kopie*.
Stattdessen kommt es ganz darauf an, wie tief wir Kopien anlegen.

```{admonition} Tiefe Kopie einer Datenstruktur
:class: python
:name: python-deep-copy-ds
Wir sprechen nur dann von einer *tiefen Kopie* (engl. deep copy) ``x_copy`` von einer *Datenstruktur* ``x``, wenn alle **Adresse** von, welche ``x_copy`` und deren *Kinder* enthalten, zu den **Adressen** die ``x`` und dessen *Kinder* enthalten, verschieden sind.
```

Eine Datenstruktur ``z``, die sich in einer anderen Datenstruktur ``x`` befindet, bezeichnen wir als *Kind* von ``x``.
Alle *Kinder* von ``z`` sind wiederum auch *Kinder* von ``x`` und so weiter und so fort.

```{admonition} Flache Kopie einer Datenstruktur
:class: python
:name: python-shallow-copy-ds
Wir sprechen nur dann von einer *flachen Kopie* (engl. shallow copy) ``x_copy`` von einer *Datenstruktur* ``x``, wenn ``x_copy`` keine *tiefe Kopie* ist.
```

Kopieren wir eine Liste durch Indexierung oder durch die Funktion ``mylist.copy()`` so wird eine eine *flache* (engl. shallow) Kopie angelegt.
Es werden dabei lediglich die **Adressen**, welche sich in der Liste befinden kopiert, siehe {numref}`Abbildung {number} <fig-data-type-list>` oder {numref}`{number} <fig-data-type-list-in-list>`.

Eine flache Kopie ist in jedem Fall ausreichend sofern alle **Adressen** auf Werte *atomarer Datentypen* zeigen.
In diesem Fall macht es keinen Unterschied ob die *atomaren Datentypen* Kopien sind oder nicht.

Folgender Code zeigt, dass die **Adressen** der Elemente der Kopie identisch sind:

```{code-cell} python3
numbers = [1, 2, 3]
numbers_shallow_copy = numbers[:]

print('ids of numbers')
for x in numbers:
    print(id(x))

print('ids of numbers_shallow_copy')
for x in numbers_shallow_copy:
    print(id(x))
```

Problematisch kann es werden, *Datenstrukturen* andere *Datenstrukturen* halten.
Fertigen wir dann lediglich eine *flache Kopie* an, so kann es zu einem unerwünschten *Seiteneffekt* kommen.
Blicken Sie auf folgendes Beispiel:

```{code-cell} python3
numbers = [1, 2, [3, 4, 5]]
numbers_shallow_copy = numbers[:]

numbers[2][0] = 'b' 
numbers_shallow_copy
```

Wir ändern einen Eintrag in der Liste ``numbers`` und diese Änderung wird auch in ``numbers_shallow_copy`` übernommen.
Warum?
Nunja, die **Adressen** 

```{code-cell} python3
print(id(numbers[2]))
print(id(numbers_shallow_copy[2]))
```

sind identisch!
Wir verändern den Speicherbereich, der sich an einer **Adresse** befindet und da beide Listen auf diesen Bereich zeigen, werden beide Listen verändert.

Dieses Verhalten kann auch durchaus wünschenswert sein.
Allerdings wollen wir häufig eine echte d.h. *tiefe Kopie* einer Datenstruktur erstellen.
Um dies zu erreichen, reicht es nicht, nur die *Datenstruktur* zu kopieren.
Sie müssen stattdessen alle *Datenstrukturen*, die diese *Datenstruktur* enthält, ebenfalls kopieren und auch alle *Datenstrukturen* die diese enthalten und so weiter und so fort.
Anders ausgedrückt: Sie müssen alle *Kinder* der Datenstruktur kopieren.

Für unser obiges Beispiel erstellen wir wie folgt eine *tiefe Kopie*:

```{code-cell} python3
mylist = [1, 2, ['a', 'b', 'c']]
mylist_deep_copy = []

for x in mylist:
    if type(x) != list:
        mylist_deep_copy.append(x)
    else:
        mylist_deep_copy.append(x.copy())


print('ids of numbers:')
for x in mylist:
    print(id(x))

print('\nids of numbers_deep_copy:')
for x in mylist_deep_copy:
    print(id(x))

mylist_deep_copy
```

Es hat sich nicht nur die Adresse der kopierten Liste sondern auch des letzten Elements der Liste verändert.
Wie sieht es mit den Adressen der Elemente des Kindes aus?:

```{code-cell} python3
print('ids of mylist[2]')
for x in mylist[2]:
    print(id(x))

print('\nids of mylist_deep_copy[2]')
for x in mylist_deep_copy[2]:
    print(id(x))
```

Diese sind gleich geblieben, da es sich um *atomare Datentypen* handelt und somit eine Kopie lediglich Speicher verbrauchen würde.

Und was machen wir wenn wir eine dreidimensionale oder gar vierdimensionale Liste haben?
Wir bräuchten eine sog. [rekursive Funktion](sec-recursive-functions), welche uns eine Kopie erstellt.
Glücklicherweise bietet uns ``Python`` durch das ``copy``-Modul bereits Funktionen zur Erstellung *flacher* und *tiefer Kopien*.
Die Funktion ``copy()`` liefert eine *flache* und die Funktion ``deepcopy()`` eine *tiefe Kopie*:

```{code-cell} python3
import copy

numbers = [1, 2, [3, [4, 5]]]
numbers_shallow_copy = copy.copy(numbers)
numbers_deep_copy = copy.deepcopy(numbers)

numbers[2][1][0] = 'b'

print(f'shallow copy: {numbers_shallow_copy}')
print(f'deep copy: {numbers_deep_copy}')
```

```{exercise} Tiefe Kopie
:label: deep-copy-list-exercise
Definieren Sie eine Funktion ``deep_copy(lst)``, die eine *tiefe Kopie* einer $n$-dimensionalen Liste anlegt.
```

````{solution} deep-copy-list-exercise
:label: deep-copy-list-solution
:class: dropdown

```python
def deep_copy(lst):
    lst_copy = []
    for element in lst:
        if type(element) == list:
            element_copy = deep_copy(element)
        else:
            element_copy = element
        lst_copy.append(element_copy)
    return lst_copy
```

````