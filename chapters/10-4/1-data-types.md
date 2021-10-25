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

(sec-working-with-data-types)=
# Pythons Datentypen

Beginnen wir mit der Praxis und sehen uns an welche Datentypen uns ``Python`` bietet und was wir mit diesen anfangen können.
Die von ``Python`` vorab definierten Datentypen nennt man *built-in Datentypen*.
Wir werden in diesem Abschnitt nicht alle *built-in Datentypen* besprechen, sondern jene mit denen Sie die meiste Zeit zu tun haben.
Eine vollständige Liste der Datentypen finden Sie im Abschnitt [Built-in Datentypen](sec-built-in-data-types).

Wir können die *built-in Datentypen* in weitere zwei Kategorien zerteilen:

1. *Atomare Datentypen*, also Datentypen die sich auf einen einzelnen Wert beziehen und
2. *Zusammengesetzt Datentypen*

Haben Sie bereits Programmiererfahrung, so werden Sie *atomare Datentypen* als *primitive Datentypen* wahrnehmen, doch streng genommen gibt es in ``Python`` keine primitiven Datentypen.
Dennoch verhalten sich *atomare Datentypen* ähnlich wie *primitive Datentypen*.

*Atomare Datentypen* sind: Ganze Zahlen ``int``, Wahrheitswerte ``bool`` und Fließkommazahlen.
*Zusammengesetzte Datentypen* sind: Zeichenketten ``str``, Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict``.

Den Datentyp einer Variable oder eines Wertes erfragen Sie mit der *built-in* Funktion ``type``.

```{code-cell} python3
x = 5
text = 'Hello'
print(type(x))
print(type(text))
print(type(3.1))
```

## Atomare Datentypen 

Eine wesentlich Eigenschaft von *atomaren Datentypen* ist, dass der **Wert** einer Variable eines *atomaren Datentyps* **unverändert** im Speicher liegt.
Wird der **Wert** von keiner Variablen mehr adressiert, wird er zwar gelöscht, um den Speicher wieder freizugeben, doch kann er nicht verändert werden solange eine Variable den Wert noch adressiert.

Wir haben dieses Phänomen bereits im Abschnitt [Variablen](sec-variables) beobachtet.
Wir hatten festgehalten, dass Veränderungen der einen Variablen keinen Effekt auf die **Adresse** bzw. *Identität* ``id`` anderer Variablen haben.
Für *atomare Datentypen* gilt noch mehr.
Ändern wir den **Wert** einer Variable vom Typ ``int``, ``bool`` oder ``float``, so kann diese Änderung nicht den **Wert** einer anderen Variablen verändern: 

```{code-cell} python3
x = 12313
z = x
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
print('change value of x')
x = 11341
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
```

*Atomare Datentypen* bestehen nur aus einem *atomaren* **Wert**, den wir nicht weiter zerteilen können.

## Zusammengesetzte Datentypen

*Zusammengesetzte Datentypen* oder auch *Datenstrukturen* bestehen hingegen aus mehreren Werten.
Sie strukturieren diese Werte.

Anders als bei *atomaren Datentypen* lässt sich der Wert einer Datenstruktur verändern.
Damit ist gemeint, dass es sich verändern lässt, was die Datenstruktur enthält.

Nehmen wir einmal an, eine Datenstruktur enthält ausschließlich ganze Zahlen ``int``.
Verändern wir nun eine dieser Zahlen, so wird der **Wert** im Speicher, der diese Zahl repräsentiert, nicht verändert -- es ist ja ein *atomarer Datentyp*!
**Aber** es wird ein neuer Wert in den Speicher geschrieben und die Datenstruktur wird so manipuliert, dass Sie nun auf diesen neuen Wert zeigt.

Im Abschnitt [Wie funktioniert eine Liste](sec-list-and-memory) sehen wir uns an was genau im Speicher vor sich geht, wenn wir mit Listen arbeiten.

## Ganze Zahlen - int

Ganze Zahlen ``int`` ist ein *atomarer Datentyp* und verhält sich so wie wir es erwarten.

Falls Sie bereits Programmierkenntnisse besitzen, so gibt es in ``Python`` eine Besonderheit: Ganze Zahlen können nicht überlaufen.
Anders als Fließkommazahlen benötigen ganze Zahlen ``int`` in ``Python`` eine variable Anzahl an Bits.
Anders ausgedrückt: Nicht jede Zahl benötigt die gleiche Anzahl an Bits im Speicher!
Solange Ihr Speicher nicht komplett belegt ist, können Sie in ``Python`` somit mit sehr großen ganzen Zahlen rechnen.

```{code-cell} python3
large_number = 10**100
print(type(large_number))
print(large_number)
```

Da wir bei mathematischen Operationen wie ``+``, ``-``, ``*``, ``/``, ``//`` und ``**`` ganze Zahlen ``int`` und Fließkommazahlen ``float`` vermischen können, müssen wir darauf achten welcher Datentyp am Ende herauskommt.
Sobald eine Fließkommazahl teil der Berechnung ist, ist das Ergebnis vom Typ ``float``.

```{code-cell} python3
x = 3 * 1.0     # int * float -> float   
print(type(x))
print(x)
```

```{code-cell} python3
large_number = 10.0**100
print(type(large_number))
print(large_number)
```

Auch bei der ganzzahligen Division ``//`` erhalten wir als Datentyp eine Fließkommazahl sofern eine Fließkommazahl bei der Operation teilnimmt:

```{code-cell} python3
x = 3.0 // 2     # float // int -> float   
print(type(x))
print(x)
```

```{code-cell} python3
x = 3 // 2.0     # int // float -> float   
print(type(x))
print(x)
```

```{code-cell} python3
x = 3 // 2     # int // int -> int   
print(type(x))
print(x)
```

## Fließkommazahlen - float

Zunächst ist zu sagen, dass Sie für Fließkommazahlen nicht das Komma ``,`` sondern den (englischsprachigen) Punkt ``.`` verwenden.

Im Gegensatz zu ganzen Zahlen benötigen Fließkommazahlen immer die gleiche Anzahl an Bits.
Da stellt sich die Frage: Wie ist es unter diesen Bedingungen möglich Zahlen darzustellen deren absoluter Wert sehr verschieden ist?
Zum Beispiel können wir problemlos die Zahl $0.0000000001$ und die Zahl $10000000.0$ als Fließkommazahl definieren:

```{code-cell} python3
small_float = 0.0000000001
large_float = 10000000.0
print(small_float)
print(large_float)
```

``1e-10`` bedeutet $1 \cdot 10^{-10}$.
Diese Darstellung liefert uns bereits die Antwort.
Physiker\*innen kennen das Problem der Zahlen aus sehr unterschiedlichen Skalen.
Die Lichtgeschwindigkeit in km/h ist eine sehr große Zahl, wohingegen die Ladung eines Elektrons in Coulomb eine sehr kleine Zahl ist.
Physiker\*innen möchten ebenfalls in einem riesigen Zahlenbereich rechnen und dabei Zahlen kompakt notieren können.
Deshalb haben sie die wissenschaftliche Notation eingeführt.
Fließkommazahlen sind aus dieser Notation entstanden.
In dieser Notation schreiben wir $10000000.0$ als $0.1 \cdot 10^8$ und aus $0.0000000001$ wird $0.1 \cdot 10^{-9}$.

Ohne zu sehr ins Detail zu gehen, besteht eine Fließkommazahl ``float`` aus Bits für die einzelnen Teile dieser Schreibweise:

+ das *Vorzeichen*, 
+ die *Mantisse* und 
+ den Exponenten.

Für $0.1 \cdot 10^8$ wäre das *Vorzeichen* gleich +, die *Mantisse* gleich 0.1 und der *Exponent* gleich 7.
Da der Computer jedoch im Binärsystem rechnet, verwendet er als Basis die 2 anstatt die 10.

Nehmen wir die Zahl 

$$0.875_{10} = 8 \cdot 10^{-1} + 7 \cdot 10^{-2} + 5 \cdot 10^{-3}.$$

Binär können wir die Zahl wie folgt ausdrücken:

$$0.111_2 = 1 \cdot 2^{-1} + 1 \cdot 2^{-2} + 1 \cdot 3^{-3}.$$

Soweit so gut.
Was passiert aber wenn jede Ziffer von 0 verschieden ist und sich endlos fortsetzt z.B. $\pi = 3.14159265359 \ldots$ oder auch $1/3 = 0.33333333333 \ldots$?
In diesem Fall wird die Zahl abgeschnitten sobald keine Bits mehr zur Verfügung stehen.
Demnach ist eine Fließkommazahl immer nur eine gute **Annäherung** des echten Werts!!!

Weshalb folgende Rechnung nicht 0.3 ergibt erklärt sich durch diese **Annäherung** in Kombination mit der Binärdarstellung!

```{code-cell} python3
0.2 + 0.1
```

Denn 

$$0.1_{10} = 0.0001100110011 \ldots_2.$$

Dieses Verhalten kann nicht nur zu kleinen Ungenauigkeiten, sondern zu großen Fehlern führen.
Folgender Code subtrahiert 20 mal $1.0 \cdot 10^{-14}$ von $1.0 \cdot 10^10$.
Doch verändern diese Subtraktionen ``x`` nicht.

```{code-cell} python3
x = 1e10
epsilon = 1e-14

print(f'epsilon = {epsilon}')
print(f'x = {x} before subtraction')

for i in range(20):
  x = x - epsilon

print(f'x = {x} after subtraction')
```

Das zeigt, dass der (akkumulierte) Fehler theoretisch unendlich groß werden kann.
Besonders kritisch ist die Subtraktion und Addition.
Die Multiplikation und Division ist für Fließkommazahlen sehr viel ungefährlicher.

```{code-cell} python3
x = 1e10
epsilon = 1e-14

print(f'epsilon = {epsilon}')
print(f'x = {x} before multiplication')
x = x * epsilon
print(f'x = {x} after multiplication')
```

Obiger Code liefert das korrekte Ergebnis von: 

$$(1.0 \cdot 10^{10}) \cdot (1.0 \cdot 10^{-14}) = 1.0 \cdot 10^{10-14} = 1.0 \cdot 10^{-4} = 0.0001.$$

## Wahrheitswerte - bool

Ein Wahrheitswert ``bool`` kann, genau wie ein [Bit](def-bit) einen von zwei Wahrheitswerten ``True`` (1) oder ``False`` (0) annehmen.
``True`` bedeutet wahr und ``False`` falsch.
Sehr selten verwenden wir explizit ``True`` oder ``False`` vielmehr wird ein logischer Ausdruck, nach *Auswertung* entweder ``True`` oder ``False`` ist.

```{code-cell} python3
x = 9
is_lesser_than_10 = x < 10
print(is_lesser_than_10)
```

In diesem Beispiel verwenden wir einen [Vergleichsoperator](sec-python-operator-compare), der den Ausdruck $x < 10$ zu ``True`` auswertet, da $x = 9 < 10$ gilt.
*Boolsche* bzw. *logische Ausdrücke* lassen sich durch [logische Operatoren](sec-logic-expressions) verknüpfen.

*Boolsche Ausdrücke* und damit Wahrheitswerte ``bool`` benötigen wir für die Steuerung unseres Programmablaufs.
*Kontrollstrukturen* führen, je nach Auswertung eines *boolschen Ausdrucks*, unterschiedliche Code-Teile aus.

```{code-cell} python3
for x in range(11):
  if x < 10:      # is True if and only if x < 10
    print(f'{x} is less than 10')
  else:
    print(f'{x} not is less than 10')
```

## Listen - list

Listen sind eine der wichtigsten *Datentypen* und zugleich einfachsten *Datenstrukturen* in ``Python``.
Sobald Sie irgendetwas sinnvolles programmieren möchten, kommen Sie um die Liste kaum herum.
Das Grundkonzept einer Liste ist einfach und doch so fundamental wichtig!

Listen sind eng mit der Wiederholung und somit mit Schleifen verbunden.
Auch wir können Schleifen an dieser Stelle nicht vermeiden, auch wenn wir sie noch nicht im Detail besprochen haben.

Nehmen wir einmal an wir bekämen den Auftrag ein Programm zu schreiben, dass ``n`` ganze Zahlen aufaddiert, wobei wir weder ``n`` noch die Zahlen kennen.
Zugegeben, das Programm ist nicht gerade interessant aber aller Anfang ist klein.
Eine variable Anzahl an Zahlen lässt sich hervorragend durch eine *Liste* modellieren.
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

Der Code funktioniert auch noch wenn ``numbers`` mehr, weniger oder andere Zahlen enthält!
Probieren Sie es aus.

Wie alle Datenstrukturen in ``Python`` können Listen Werte mit unterschiedlichen Datentypen enthalten.

```{code-cell} python3
mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
mylist
```

Listen können selbstverständlich andere Listen enthalten:

```{code-cell} python3
mylist = [['a','b','c'], 2, 3, [1, 2, 3]]
mylist
```

### Erstellung

Es gibt unterschiedliche Möglichkeiten eine Liste zu erzeugen.
Wir können z.B. mit einer leeren Liste starten und diese füllen:

```{code-cell} python3
numbers = []
numbers.append(0)
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
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

Für Fälle in denen wir eine Liste aus einer anderen Sequenz generieren gibt es eine sehr kompakte Schreibweise.
``range(10)`` ist eine sog. lazy Sequenz, dahinter steckt eine Funktion, die immer wieder aufgerufen wird und die Zahl die sie zurückgibt immer um eins erhöht.
Wir können diese Sequenz in eine Liste packen:

```{code-cell} python3
numbers = [i for i in range(10)]
numbers
```

oder noch kürzer:

```{code-cell} python3
numbers = list(range(10))
numbers
```

### Indexierung

Wir können auf die Elemente einer Liste mit einem Index zugreifen.
Dieser Index beginnt bei 0 und endet bei der Länge der Liste - 1, d.h. ``len(mylist) - 1``.
``len(mylist)`` gibt eine natürliche Zahl (0 inklusive) zurück, welche die Länge der Liste ``mylist`` angibt.

```{code-cell} python3
mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
len(mylist)
```

In anderen Worten: Die Elemente einer Liste sind in aufsteigender Reihenfolge angeordnet.
Jedes Element hat seinen Platz bzw. Index und kein Platz ist leer!

```{code-cell} python3
print(mylist[0])
print(mylist[len(mylist)-1])
```

In ``Python`` können wir statt ``mylist[len(mylist)-1]``  auch ``mylist[-1]`` schreiben.

```{code-cell} python3
print(mylist[len(mylist)-1])
print(mylist[-1])
```

``Python`` bietet eine angenehme und mächtige Syntax um einen Teil der Liste in eine neue Liste zu kopieren.
Mit ``mylist[start:ende:i]`` nehmen wir jedes ``i``-te Element beginnend von ``start`` bis ``ende``.
Dabei ist ``i`` optional und ist gleich ``1``, wenn es nicht angegeben wird.
Bei diesem Operationen bleibt ``mylist`` unverändert.

```{code-cell} python3
mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(mylist[1:8:2])
print(mylist[1:8:1])
print(mylist[1:8])
print(mylist)
```

Auch eine negative Indexierung ist erlaubt.

```{code-cell} python3
mylist = [1,2,3,'a','b','c',1.0,2.0,3.0]
print(mylist[8:1:-2])
print(mylist[-3:-8:-2])
```

### Veränderung

Anders als Tupel ``tuple`` sind Listen veränderbar, d.h. wir können Elemente löschen und hinzufügen.

```{code-cell} python3
chars = ['a','b','c']
print(f'chars: {chars} before append.')
chars.append('d')
print(f'chars: {chars} before remove.')
chars.remove('b')
print(f'chars: {chars} after remove.')
```

Dabei fügt ``append`` das neue Element hinten an.
Um ein Listenelement anhand seines Indexes zu löschen können wir ``del`` (delete) verwenden.

```{code-cell} python3
chars = ['a','b','c']
print(f'chars: {chars} before del.')
del chars[1]
print(f'chars: {chars} after del.')
```

``del`` funktioniert ebenfalls mit dem Indexieren, d.h. wir können viele Elemente mit einem Befehl löschen.
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

Dies fügt das Element ``'d'`` an vor das Element mit dem Index 1 ein.
Anders ausgedrückt, das eingefügte Element hat nach der Operation den Index, welchen wir bei ``insert`` angeben.

(sec-list-and-memory)=
### Wie funktioniert eine Liste?

Wie funktioniert eine Liste im tieferen Sinne?
Also wie ist sie im Speicher abgelegt, was passiert wenn wir sie verändern und wie greifen wir auf sie und ihre Elemente über **Adressen** zu?

Um zu verstehen wie und warum Listen funktionieren müssen wir wichtige Tatsache festhalten, die wir bereits im Abschnitt [Variablen](sec-variables) unbemerkt verwendet haben:
Kennen wir eine **Adresse** eines **Wertes**, kurz gesagt die *Variable* welche auf den Wert zeigt, so ist der Zugriff auf diesen Wert extrem schnell!
Solange wir die **Adressen** kennen, ist er Zugriff in den **Arbeitsspeicher** generell extrem schnell.
Es gibt kleine 'Strafen' wenn **Adressen** weit auseinander liegen.

Mit dieser Information, lassen Sie uns anhand eines Beispiel testen, wie sich die **Adressen** und **Werte** einer ``list`` (aus Zahlen) verhalten.

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

## Tupel - tuple

TODO

## Zeichenketten - str

Eine Zeichenkette ist eine *Sequenz* von Zeichen.
Wie ein Tupel ist eine Zeichenkette **unveränderlich** (engl. immutable). 
``Python`` bietet uns viele nützliche Funktionen um auf Zeichenketten zu operieren.
Zeichenketten können durch einfache ``'text'`` oder doppelte ``"text"`` Anführungszeichen umschlossen sein.

```{code-cell} python3
text = 'Hello World!'
text = "Hello World!"
```

Was wir bereits exzessive genutzt haben ist die Ausgabe von Zeichenketten durch die *built-in* Funktion ``print``.

```{code-cell} python3
text = 'Hello World!'
print(text)
```

Um Variablen oder Werte anderer Datentypen mit ``print`` auszugeben mussen wir diese immer mit der *built-in Funktion* ``str`` in eine Zeichenkette umwandeln.
Da dies so häufig gemacht werden musst, haben die Entwickler\*innen von ``Python`` sich etwas einfallen lassen.
Stellen wir vor unsere Zeichenkette ein ``f`` so handelt es sich um eine formatierte Zeichenkette.
Die hilft uns Variablen oder Werte direkt in diese formatierte Zeichenkette einzufügen:

```{code-cell} python3
x = 5
y = 10
print('x + y = ' + str(x) + ' + ' + str(y) + ' = ' + str(x+y)) # ugly
print(f'x + y = {x} + {y} = {x+y}')                            # beautiful
```

Das vereinfacht das Schreiben und Lesen solcher Ausgaben ungemein.
Sie können formatierte Zeichenketten auch ohne ``print`` verwenden.

```{code-cell} python3
x = 5
y = 10
formatted_str = f'x + y = {x} + {y} = {x+y}'
formatted_str
```

Zwei Zeichenketten lassen sich mit dem ``+``-Operator verketten.

```{code-cell} python3
prefix = 'Hello'
suffix = ' Welt!'
text = prefix + suffix
print(prefix)
print(suffix)
print(text)
```

Bestimmte Zeichen kontrollieren die Darstellung des Textes, z.B. ob eine Leerzeile ein Leerzeichen oder ein Tab eingefügt werden soll.

```{code-cell} python3
space = ' '
space_line = '\n'

print('Hello' + space + 'World' + space_line + '!')
```

Die *leere Zeichenkette* verändert bei der Verkettung eine andere Zeichenkette nicht.
Es ist das neutrale Element der Zeichenverkettung.

```{code-cell} python3
empty_str = ''

print('The correct answer is 42!')
print('The correct' + empty_str + empty_str + empty_str + ' answer is 42!')

'Hello' == 'Hello' + empty_str
```

Zeichenketten lassen sich wie Listen und Tupel indexieren und mit der *built-in Funktion* ``len``, kann man die Länge einer Zeichenkette erfragen.
Folgender Code gibt jedes einzelne Zeichen einer Zeichenkette aus.

```{code-cell} python3
text = 'Hello World!'

for i in range(len(text)):
  print(text[i])
```

Das lässt sich jedoch auch einfacher schreiben:

```{code-cell} python3
text = 'Hello World!'

for char in text:
  print(char)
```

Auch bei Zeichenketten können wir negative Indices verwenden.
``text[-1]`` gibt uns das letzte und ``text[-2]`` das vorletzte Zeichen.

```{code-cell} python3
text = 'Zeichensalat'

print(text[-1])
print(text[-2])
```

Lassen Sie uns eine Zeichenkette umdrehen:


```{code-cell} python3
text = 'Zeichensalat'
reverse_text = ''

for i in range(len(text)):
  reverse_text += text[-(i+1)]

print(text)
print(reverse_text)
```

Wie bei Listen und Tupeln können wir auch einen Teil einer Zeichenkette ausschneiden (indexieren).

```{code-cell} python3
text = 'Zeichensalat'
print(text[0:2])
print(text[0:len(text)])   # take it all
print(text[0:-3])          # negative indexing
print(text[1:-1])          # skip first and last
print(text[-3:-1])         # negative indexing
print(text[2:])            # skip the first 2 and take the rest
```

Dabei ist ``text[2:]`` eine Kurzschreibweise für ``text[2:len(text)]`` und ``text[:2]`` für ``text[0:2]``.

Hin und wieder kann es vorkommen, dass Sie Zeichen schreiben möchten, welche bereits in ``Python`` mit einer Bedeutung belegt sind.
Wie schreiben wir beispielsweise ``Anna sagte: 'Wie geht es dir'``?
Dafür müssen wir das ``'``-Zeichen mit einem ``\`` maskieren:

```{code-cell} python3
print('Anna sagte: \'Wie geht es dir\'')
```

Auf Zeichenketten können wir viele nützliche Funktionen aufrufen.
Zu beachten ist, dass Zeichenketten unveränderlich sind, d.h. die Funktionen liefern eine neue Zeichenkette zurück, die ursprüngliche bleibt unverändert.
Mit ``text.upper()`` können wir beispielsweise alle Zeichen einer Zeichenkette in Großbuchstaben transformieren.

```{code-cell} python3
text = 'Zeichensalat'
text_upper = text.upper()
print(text)
print(text_upper)
```

Wir die Vorkommnisse eines Zeichen in einer Zeichenkette zählen oder ganze Zeichenfolgen ersetzten:

```{code-cell} python3
text = 'Zeichensalat'
print(text.count('a'))
print(text.replace('salat', 'spinat'))
```

Es würde zu weit gehen alle Funktionen zu besprechen -- das wäre auch ziemlich langweilig.
Schauen Sie sich einfach die [Dokumentation](https://docs.python.org/3/library/string.html) an, wenn Sie nach einer Funktion suchen oder verwenden Sie die eingebaute Hilfe ``help(str)``.

## Mengen - set

TODO

## Wörterbücher - dict

TODO


