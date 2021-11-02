(sec-list)=
# Listen - list

Listen (engl. [List](https://docs.python.org/3/library/stdtypes.html#list)) ``list`` sind eine der wichtigsten *Datentypen* und zugleich einfachsten *Datenstrukturen* in ``Python``.
Sobald Sie irgendetwas sinnvolles programmieren möchten, kommen Sie um die Liste kaum herum.
Das Grundkonzept einer Liste ist einfach und doch so fundamental wichtig!

Listen sind eng mit der Wiederholung und somit mit Schleifen verbunden.
Auch wir können Schleifen an dieser Stelle nicht vermeiden, auch wenn wir sie noch nicht im Detail besprochen haben.

Nehmen wir einmal an wir bekämen den Auftrag ein Programm zu schreiben, welches ``n`` ganze Zahlen aufaddiert, wobei wir weder ``n`` noch die Zahlen kennen.
Zugegeben, das Programm ist nicht gerade interessant aber aller Anfang ist klein.
Eine variable Anzahl an Zahlen lässt sich hervorragend durch eine *Liste* modellieren.
Wir gehen also davon aus, dass wir eine Liste ``numbers`` bekommen und daraus die Summe berechnen müssen.
Folgender Code löst die Aufgabe.
``numbers`` ist eine Liste, welche zwei Zahlen (1 und 2) enthält.

numbers = [1, 2]

result = 0
for x in numbers:
  result += x

result

Der Code funktioniert auch noch wenn ``numbers`` mehr, weniger oder andere Zahlen enthält!
Probieren Sie es aus.

Wie alle Datenstrukturen in ``Python``, können Listen Werte mit unterschiedlichen Datentypen enthalten.

mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
mylist

Listen können selbstverständlich andere Listen (bzw. Datenstrukturen) enthalten:

mylist = [['a','b','c'], 2, 3, [1, 2, 3]]
mylist

## Erstellung

Es gibt unterschiedliche Möglichkeiten eine Liste zu erzeugen.
Wir können z.B. mit einer leeren Liste starten und diese füllen:

numbers = []
numbers.append(0)
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers

oder kürzer

numbers = []
for i in range(6):
  numbers.append(i)

numbers

Oder wir starten mit einer vollen Liste.

numbers = [0, 1, 2, 3, 4, 5]
numbers

Die *built-in* Funktion ``range()`` erzeugt einen sog. Zahlenbereich (engl. [Range](https://docs.python.org/3/library/stdtypes.html#typesseq-range)), welchen wir im Abschnitt [Bereich - range](sec-range) erörtern.
Wir können diesen Bereich, der auch eine Sequenz ist, in eine Liste packen bzw. in eine Liste umwandeln:

numbers = [i for i in range(10)]
numbers

oder noch kürzer:

numbers = list(range(10))
numbers

(sec-list-index)=
## Indexierung

Wir können auf die Elemente einer Liste mit einem Index zugreifen.
Dieser Index beginnt bei 0 und endet bei der Länge der Liste - 1, d.h. ``len(mylist) - 1``.
``len(mylist)`` gibt eine natürliche Zahl (0 inklusive) zurück, welche die Länge der Liste ``mylist`` angibt.

mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
len(mylist)

In anderen Worten: Die Elemente einer Liste sind in aufsteigender Reihenfolge angeordnet.
Jedes Element hat seinen Platz bzw. Index und kein Platz ist leer!

print(mylist[0])
print(mylist[len(mylist)-1])

In ``Python`` können wir statt ``mylist[len(mylist)-1]``  auch ``mylist[-1]`` schreiben.

print(mylist[len(mylist)-1])
print(mylist[-1])

``Python`` bietet eine angenehme und mächtige Syntax um einen Teil der Liste in eine neue Liste zu kopieren.
Mit ``mylist[start:ende:i]`` nehmen wir jedes ``i``-te Element beginnend von ``start`` bis ``ende``.
Dabei ist ``i`` optional und ist gleich ``1``, wenn es nicht angegeben wird.
Bei diesem Operationen bleibt ``mylist`` unverändert.

mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(mylist[1:8:2])
print(mylist[1:8:1])
print(mylist[1:8])
print(mylist)

Auch eine negative Indexierung ist erlaubt.

mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(mylist[8:1:-2])
print(mylist[-3:-8:-2])

## Veränderung

Anders als Tupel ``tuple`` sind Listen veränderbar, d.h. wir können Elemente löschen und hinzufügen.

chars = ['a','b','c']
print(f'chars: {chars} before append.')
chars.append('d')
print(f'chars: {chars} before remove.')
chars.remove('b')
print(f'chars: {chars} after remove.')

Dabei fügt ``append`` das neue Element hinten an.
Um ein Listenelement anhand seines Indexes zu löschen können wir ``del`` (delete) verwenden.

chars = ['a','b','c']
print(f'chars: {chars} before del.')
del chars[1]
print(f'chars: {chars} after del.')

``del`` funktioniert ebenfalls mit dem Indexieren, d.h. wir können viele Elemente mit einem Befehl löschen.
Im folgenden löschen wir jedes 2-te Element wodurch nur ungerade Zahlen übrig bleiben.

numbers = list(range(20))
print(f'numbers: {numbers} before del.')
del numbers[::2]
print(f'numbers: {numbers} after del.')

Sobald ein Element gelöscht wird, verkleinert sich auch die Liste.
Es entstehen keine Lücken.

Wir können auch ein Element an einer bestimmten Stelle einfügen.

chars = ['a','b','c']
print(f'chars: {chars} before insert.')
chars.insert(1, 'd')
print(f'chars: {chars} after insert.')

Dies fügt das Element ``'d'`` an vor das Element mit dem Index 1 ein.
Anders ausgedrückt, das eingefügte Element hat nach der Operation den Index, welchen wir bei ``insert`` angeben.

(sec-list-and-memory)=
## Listen und der Speicher

Wie funktioniert eine Liste im tieferen Sinne?
Also wie ist sie im Speicher abgelegt, was passiert wenn wir sie verändern und wie greifen wir auf sie und ihre Elemente über **Adressen** zu?

Um zu verstehen wie und warum Listen funktionieren müssen wir wichtige Tatsache festhalten, die wir bereits im Abschnitt [Variablen](sec-variables) unbemerkt verwendet haben:
Kennen wir eine **Adresse** eines **Wertes**, kurz gesagt die *Variable* welche auf den Wert zeigt, so ist der Zugriff auf diesen Wert extrem schnell!
Solange wir die **Adressen** kennen, ist er Zugriff in den **Arbeitsspeicher** generell extrem schnell.
Es gibt kleine 'Strafen' wenn **Adressen** weit auseinander liegen.

Mit dieser Information, lassen Sie uns anhand eines Beispiel testen, wie sich die **Adressen** und **Werte** einer ``list`` (aus Zahlen) verhalten.

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

Im obigen Code erstellen wir eine Liste, welche die Zahlen 1 bis 5 enthält.
Dann verändern wir das zweite Element der Liste (eine Liste startet mit dem 0-ten Element).
Die **Adresse** der *Variable* ``numbers`` ändert sich bei diesem Vorgang nicht!
Allerdings ändert sich die Adresse des Elements ``numbers[2]`` und der **Wert** von ``numbers``.

```{figure} ../../figs/python-tutorial/datatypes/list.png
---
width: 600px
name: fig-data-type-list
---
Die Liste aus unsrem obigen Beispiel **bevor** wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Ändern wir den Wert eines Listenelements, ändern wir diesen Hinweis!

```{figure} ../../figs/python-tutorial/datatypes/list-2.png
---
width: 600px
name: fig-data-type-list-2
---
Die Liste aus unsrem obigen Beispiel **nachdem** wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Alle *Datenstrukturen* sind *Behälter*, die andere Daten aufnehmen können, ähnlich wie Schließfächer, Ordner oder Rucksäcke.
Nehmen wir als Analogie Schließfächer aus der echten Welt.
Stellen wir uns vor, der Platz in einem Schließfach wäre ein Teil des Speicherplatzes, welcher von unserer Liste benötigt wird.
Was befindet sich nun in unseren Schließfächern?
In ``Python`` sind es **nicht** die Objekte/Werte selbst sondern die **Adresse** der Objekte/Werte.
Es befindet sich quasi ein Zettel auf dem der Hinweis steht, wo wir das Objekt, was zu jenem Schließfach gehört, finden.
Oder aber wir stellen uns eine Schnur vor, die von dem Schließfach auf das Objekt verweist.

Das besondere einer Liste, bzw. die Charakteristik welches Sie auszeichnet ist, dass die **Adressen** Ihrer Elemente im Speicher ohne Lücke nebeneinander liegen.
Da **Adressen** immer die gleiche feste Anzahl an Bits benötigen, kann man für eine gegebene Adresse einer Liste und den Index eines Elements, die Speicheradresse der Speicheradresse, die auf das Element zeigt berechnen.

Angenommen die Adresse der Liste ``mylist`` ist $Start$ und jede Adresse benötigt 4 Byte und wir können 1 Byte adressieren, dann befindet sich die Adresse $adr_i$ des $i$-ten Elements an der Speicheradresse:

$$Start + i \cdot 4.$$

Diese Rechnung kann der Rechner sehr schnell durchführen und deshalb können wir auf Elemente einer Liste deren Index wir kennen extrem schnell zugreifen.

Um dieses Konzept besser zu verstehen und herauszufinden wie sich *atomare* wie auch *zusammengesetzt Datentypen* verhalten, hilft oft nur eins: Ausprobieren!

Im Kapitel [Speicher - alles ist eine Liste](sec-memory) erstellen wir unser eigenes Speichermanagementsystem durch ``Python``-Listen.
Diese Übung bietet detaillierte Einblicke in die funktionsweise des Speichers und wie es gelingt Listen voller **Adressen** zu verwalten.

## Der Unterschied zwischen + und +=

Der ``+`` und auch der ``+=``-Operator ist in ``Python`` auch für Listen definiert.
Ähnlich wie bei Zeichenketten, verkettet er zwei Listen.
Überraschenderweise bewirkt jedoch folgender Code

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f' id before concat: {id(list1)}')
list1 = list1 + list2
print(f' id after concat: {id(list1)}')
list1

nicht das selbe wie

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f' id before concat: {id(list1)}')
list1 += list2
print(f' id after concat: {id(list1)}')
list1

auch wenn ``list1`` in beiden Fällen die gleichen Werte enthält so ändert sich im ersten Fall die **Adresse** von ``list1``.
Im zweiten Fall bleibt die ``id`` und damit die **Adresse** unverändert.
Was bedeutet das?

Verwenden wir ``liste1 + liste2`` so wird eine neue Liste im Speicher angelegt und die Verkettung der beiden Listen wird dort abgelegt.
D.h. die Listenelemente der beiden Listen werden **kopiert**!
Die beiden Listen die bei der Operation teilnehmen bleiben unverändert.

Verwenden wir hingegen ``liste1 += liste2`` so werden die Elemente von ``liste2`` kopiert und an ``liste1`` angehängt.
Damit wird ``list1`` verändert und es wird keine neue Liste angelegt!
``liste1 += liste2`` entspricht somit

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x in list2:
    list1.append(x)
list1

und ``concat_list = liste1 + liste2`` entspricht

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concat_list = []
for x in list1:
    concat_list.append(x)
for x in list2:
    concat_list.append(x)
concat_list

## Tiefe und flache Kopien

Kopieren wir eine Liste durch Indexierung oder durch die Funktion ``mylist.copy()`` so wird eine sogenannte *flache* (engl. shallow) Kopie angelegt.
Was bedeutet das?
Das bedeutet, dass lediglich die **Adressen** welche sich in der Liste befinden kopiert werden, siehe {numref}`Abbildung {number} <fig-data-type-list>`.
Zeigen diese **Adressen** auf Werte *atomare Datentypen*, so ist dies in jedem Fall ausreichend.

Folgender Code zeigt, dass die **Adressen** der Elemente der Kopie identisch sind:

numbers = [1, 2, 3]
numbers_shallow_copy = numbers[:]

print('ids of numbers')
for x in numbers:
    print(id(x))

print('ids of numbers_shallow_copy')
for x in numbers_shallow_copy:
    print(id(x))

Problematisch kann es werden, wenn wir in einer *Datenstruktur* eine weitere *Datenstruktur* halten und eine *flache Kopie* anfertigen.
Blicken Sie auf folgendes Beispiel:

numbers = [1, 2, [3, 4, 5]]
numbers_shallow_copy = numbers[:]

numbers[2][0] = 'b' 
numbers_shallow_copy

Wir ändern etwas in der Liste ``number`` und diese Änderung wird auch in ``numbers_shallow_copy`` übernommen.
Warum?
Nunja, die **Adressen**

print(id(numbers[2]))
print(id(numbers_shallow_copy[2]))

sind identisch!
Wir verändern den Speicherbereich der sich an **Adresse** befindet und da beide Listen auf diesen Bereich zeigen, werden beide Listen verändert.

Dieses Verhalten kann auch durchaus wünschenswert sein.
Allerdings wollen wir häufig eine echte d.h. *tiefe Kopie* einer Datenstruktur erhalten.
Um dies zu erreichen reicht es nicht nur die *Datenstruktur* zu kopieren, Sie müssen alle *Datenstrukturen* die diese *Datenstruktur* enthält kopieren und auch alle *Datenstrukturen* die diese enthalten und so weiter und so fort.

Für unser obiges Beispiel erstellen wir wie folgt eine *tiefe Kopie*:

numbers = [1, 2, [3, 4, 5]]
numbers_deep_copy = []

for x in numbers:
    if type(x) != list:
        numbers_deep_copy.append(x)
    else:
        numbers_deep_copy.append(x.copy())


print('ids of numbers')
for x in numbers:
    print(id(x))

print('ids of numbers_deep_copy')
for x in numbers_deep_copy:
    print(id(x))

numbers_deep_copy

Wir sehen dass sich bei der *tiefen Kopie* die Adresse des letzten Elements verändert hat, da es eine *Datenstruktur* ist.
Ändern wir nun ``numbers`` so hat diese Änderung keine Auswirkung auf ``numbers_deep_copy``

numbers[2][0] = 'b' 
numbers_deep_copy

Und was machen wir wenn wir eine dreidimensionale oder gar vierdimensionale Liste haben?
Wir bräuchten eine sog. rekursive Funktion, welche uns eine Kopie erstellt.
Glücklicherweise bietet uns ``Python`` durch das ``copy``-Modul bereits Funktionen zur Erstellung *flacher* und *tiefer Kopien*.
Die Funktion ``copy()`` liefert eine *flache* und die Funktion ``deepcopy()`` eine *tiefe Kopie*:

import copy

numbers = [1, 2, [3, [4, 5]]]
numbers_shallow_copy = copy.copy(numbers)
numbers_deep_copy = copy.deepcopy(numbers)

numbers[2][1][0] = 'b'

print(f'shallow copy: {numbers_shallow_copy}')
print(f'deep copy: {numbers_deep_copy}')