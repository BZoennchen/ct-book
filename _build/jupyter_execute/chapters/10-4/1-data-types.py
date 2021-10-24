(sec-working-with-data-types)=
# Pythons Datentypen

Beginnen wir mit der Praxis und sehen uns an welche Datentypen uns ``Python`` bietet und was wir mit diesen anfangen können.
Die von ``Python`` vorab definierten Datentypen nennt man *built-in Datentypen*.
Wir werden in diesem Abschnitt nicht alle *built-in Datentypen* besprechen, sondern jene mit denen Sie die meiste Zeit zu tun haben.
Eine vollständige Liste der Datentypen finden Sie in Abschnitt [Built-in Datentypen](sec-built-in-data-types).

Wir können die *built-in Datentypen* in weitere zwei Kategorien zerteilen:

1. *Atomare Datentypen*, also Datentypen die sich auf einen einzelnen Wert beziehen und
2. *Zusammengesetzt Datentypen*

Haben Sie bereits Programmiererfahrung werden Sie *atomare Datentypen* als *primitive Datentypen* wahrnehmen, doch streng genommen gibt es in ``Python`` keine primitiven Datentypen.
Dennoch verhalten sich *atomare Datentypen* wie *primitive Datentypen*.

*Atomare Datentypen* sind: Ganze Zahlen ``int``, Wahrheitswerte ``bool`` und Fließkommazahlen.
*Zusammengesetzte Datentypen* sind: Zeichenketten ``str``, Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict``.

## Atomare Datentypen 

Eine wesentlich Eigenschaft von *atomare Datentypen* ist, dass der **Wert** einer Variable *atomare Datentyps* unverändert im Speicher ist.
Wird der **Wert** von keiner Variablen mehr adressiert, wird er zwar gelöscht um den Speicher wieder freizugeben, doch kann er nicht verändert werden solange eine Variable den Wert noch adressiert.
Wir haben dieses Phänomen bereits im Abschnitt [Variablen](sec-variables) beobachtet.
Wir hatten festgehalten, dass Veränderungen der einen Variablen haben keinen Effekt auf die **Adresse** bzw. *Identität id anderer Variablen.
Für *atomare Datentypen* gilt noch mehr.
Ändern wir den **Wert** einer Variable vom Typ ``int``, ``bool`` oder ``float``, so kann diese Änderung nicht den **Wert** einer anderen Variablen verändern:

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

*Atomare Datentypen* bestehen nur aus einem *atomaren* Wert, den wir nicht weiter zerteilen können.

## Zusammengesetzte Datentypen

Zusammengesetzte Datentypen oder auch Datenstrukturen bestehen hingegen aus mehreren Werten.
Sie strukturieren diese Werte.

Anders als bei *atomaren Datentypen* lassen sich diese strukturierten Werte ändern.
Nehmen wir einmal an eine Datenstruktur enthält ausschließlich ganze Zahlen ``int``.
Verändern wir nun eine dieser Zahlen wird der **Wert** im Speicher der diese Zahl repräsentiert nicht verändert -- es ist ja ein *atomarer Datentyp*!
**Aber** es wird ein neuer Wert in den Speicher geschrieben und die Datenstruktur wird so manipuliert, dass Sie nun auf diesen neuen Wert zeigt.

Lassen Sie uns das noch einmal an einem Beispiel testen.
Wir wählen als Datenstruktur eine Liste ``list`` aus Zahlen.

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

Datenstrukturen sind Behälter die andere Daten aufnehmen können, ähnlich wie ein Schließfächer, Ordner oder Rucksäcke.
Nehmen wir als Analogie Schließfächer aus der echten Welt.
Stellen wir uns vor, der Platz in einem Schließfach wäre ein Teil des Speicherplatzes, welches unsere Liste benötigt.
Alle Schließfächer als ganzes benötigen so viel Speicher wie unsere Liste.
Was befindet sich nun in unseren Schließfächern?
Es sind **nicht** die Objekte/Werte selbst sondern die **Adresse** der Objekte/Werte.
Quasi ein Zettel auf dem der Hinweis steht, wo wir das Objekt was zu jenem Schließfach gehört finden.
Oder eine Schnur die von dem Schließfach auf das Objekt verweist.

```{figure} ../../figs/python-tutorial/datatypes/list.png
---
width: 600px
name: fig-data-type-list
---
Die Liste aus unsrem obigen Beispiel bevor wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Ändern wir den Wert eines Listenelements, ändern wir diesen Hinweis!

```{figure} ../../figs/python-tutorial/datatypes/list-2.png
---
width: 600px
name: fig-data-type-list-2
---
Die Liste aus unsrem obigen Beispiel nachdem wir den Wert ``3`` auf ``-20`` gesetzt haben.
```

Um dieses Konzept besser zu verstehen und herauszufinden wie sich *atomare* wich auch *zusammengesetzt Datentypen* verhalten hilft oft nur eins: Ausprobieren!

## Ganze Zahlen - int

Ganze Zahlen ``int`` ist ein *atomarer Datentyp* und verhält sich so wie wir es erwarten.

Falls Sie bereits Programmierkenntnisse so gibt es in ``Python`` eine Besonderheit: ganze Zahlen können nicht überlaufen.
Anders als Fließkommazahlen benötigen ganze Zahlen ``int`` in ``Python`` eine Variable Anzahl an Bits.
Anders ausgedrückt: Nicht jede Zahl benötigt die gleiche Anzahl an Bits im Speicher!
Solange Ihr Speicher nicht komplett belegt ist, können Sie in ``Python`` somit mit sehr großen ganzen Zahlen rechnen.

large_number = 10**100
print(type(large_number))
print(large_number)

Da wir bei mathematischen Operationen wie ``+``, ``-``, ``*``, ``/``, ``//`` und ``**`` ganze Zahlen ``int`` und Fließkommazahlen ``float`` vermischen können, müssen wir darauf achten welcher Datentyp am Ende herauskommt.
Sobald eine Fließkommazahl teil der Berechnung ist, ist das Ergebnis vom Typ ``float``.

x = 3 * 1.0     # int * float -> float   
print(type(x))
print(x)

large_number = 10.0**100
print(type(large_number))
print(large_number)

Auch bei der ganzzahligen Division ``//`` erhalten wir als Datentyp eine Fließkommazahl:

x = 3.0 // 2     # float // int -> float   
print(type(x))
print(x)

x = 3 // 2.0     # int // float -> float   
print(type(x))
print(x)

x = 3 // 2     # int // int -> int   
print(type(x))
print(x)

## Fließkommazahlen - float

Im Gegensatz zu ganzen Zahlen benötigen Fließkommazahlen immer die gleiche Anzahl an Bits.
Wie ist es unter diesen Bedingungen möglich Zahlen darzustellen deren absoluter Wert sehr verschieden ist.
Zum Beispiel können wir problemlos die Zahl $0.0000000001$ und die Zahl $10000000.0$ als Fließkommazahl definieren:

small_float = 0.0000000001
large_float = 10000000.0
print(small_float)
print(large_float)

Physiker kennen dieses Problem.
Sie möchten ebenfalls einen riesigen Zahlenbereich kompakt notieren können und haben deshalb die wissenschaftliche Notation eingeführt.
Fließkommazahlen sind aus dieser Notation entstanden.
In dieser Notation wird aus $10000000.0 = 1.0 \cdot 10^7$ und aus $0.0000000001 = 1.0 \cdot 10^{-10}$.

Ohne zu sehr ins Detail zu gehen, eine Fließkommazahl ``float`` besteht aus Bits für das Vorzeichen, die Mantisse und den Exponent.
Für $1.0 \cdot 10^7$ wäre das Vorzeichen gleich +, die Mantisse gleich 1, der Exponent gleich 7.
Da der Computer jedoch im Binärsystem rechnet, ist verwendet er als Basis die 2 anstatt die 10.

Soweit so gut.
Was passiert aber wenn jede Ziffer von 0 verschieden ist und sich endlos fortsetzt z.B. $\pi = 3.14159265359 \ldots$ oder auch $1/3 = 0.33333333333 \ldots$?
In diesem Fall wird die Zahl abgeschnitten sobald keine Bits mehr zur Verfügung stehen.

## Wahrheitswerte - bool

TODO

## Zeichenketten - str

TODO

## Listen - list

TODO

## Tupel - tuple

TODO

## Mengen - set

TODO

## Wörterbücher - dict

TODO