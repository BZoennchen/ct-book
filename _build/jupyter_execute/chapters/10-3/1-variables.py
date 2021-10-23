(sec-variables)=
# Variablen

*Variablen* können wir uns intuitiv zunächst als Namen oder Bezeichnung eines Wertes vorstellen.
Mit diesem Namen können wir einen Wert im [Arbeitsspeicherspeicher](def-main-memory) des Computers identifizieren.
So können wir uns Zwischenergebnisse merken und damit weiter rechnen.

## Initialisierung und Zuweisung

Durch das ``=`` Zeichen weisen wir einer *Variablen* auf der linken Seite den Wert des *Ausdrucks* auf der rechten Seite zu.
Zum Beispiel, weist

x = 3 + 10

den ausgewerteten Wert ``3 + 10`` also ``13`` der Variablen ``x`` zu.
Es ist äußerst wichtig, dass die den zwischen dem ``=`` und dem mathematischen $=$ unterscheiden.

$$x = 13$$

bedeutet, dass $x$ gleich $13$ ist, wohingegen

x = 13

den Wert der Variablen ``x`` auf ``13`` setzt oder genaue die Variable auf einen Speicherbereich verweisen lässt, welcher den Wert ``13`` enthält.
Um das mathematisch auszurücken verwendet man oft $\leftarrow$, also 

$$x \leftarrow 13.$$

Dies verdeutlicht, dass es sich um eine *Zuweisung* handelt.
Mit

x = None

weisen wir ``x`` den Wert ``None`` d.h. 'Nichts' zu. Doch ist dieses 'Nichts' nicht nichts ;). Versuchen wir eine *Variable* zu verarbeiten, die noch nicht initialisiert wurde, so erhalten wir einen Fehler:

v + 20

Hierbei würde es zu einem Fehler ``name 'v' is not defined`` kommen, da die *Variable* ``v`` noch nicht *initialisiert* wurde.


In ``Python`` reicht es wenn Sie der *Variablen* einen Wert zuweisen.
Sie wird automatisch erzeugt, d.h., *initialisiert*.
Besitzt Sie noch keinen Wert so existiert sie auch nicht bzw. ist noch nicht *initialisiert*.

```{admonition} Initialisierung mit Notebooks
:name: warning-evaluation-ordering
:class: warning
Nach Ausführung dieser Codezeilen funktioniert auch der obige Code.
Dies hängt an der funktionsweise der Notebooks zusammen.
Sobald ``z`` *initialisiert* wurde, existiert ``z`` für alle Zellen des Notebooks.
```

## Variablen und der Arbeitsspeicher

Eine Variable können wir als Paar von **Wert** und **Arbeitsspeicheradresse** verstehen.
Der **Wert** der Variablen steht im [Arbeitspeicher](def-main-memory)) an einer bestimmten **Arbeitsspeicheradresse**.
Variablen abstrahieren diesen Zusammenhang, sodass Sie uns die Arbeit mit dem Arbeitsspeicher erleichtern.

Mit

x = 25

Wird der **Wert** ``25`` in den Arbeitsspeicher an eine freie **Speicheradresse** geschrieben. Diese **Adresse** erhält die *Variable* ``x``. ``x`` *zeigt* auf den Speicherbereich in dem der **Wert** ``25`` steht!

Folgende Abbildung verdeutlicht die Situation:

```{figure} ../../figs/python-tutorial/variables/variable.png
---
width: 800px
name: fig-variable
---
Initialisierung und Zuweisung einer Variable ``x``  mit dem Wert ``25``. Der Wert steht im Arbeitspeicher an der Speicheradresse 6. Die Variable zeigt auf diese Adresse im Speicher.
```

``id``: Mit der *built-in*-Funktion ``id`` können Sie sich eine Identifikationsnummer einer Variablen ausgeben lassen. Für zwei *Variablen* ist diese genau dann gleich, wenn deren **Arbeitsspeicheradressen** gleich sind.

x = 25
z = 25
print(id(x))
print(id(z))

Sie sehen dass die ``id`` der Variablen ``x`` und ``z`` identisch sind. Ebenso ist ihr Wert identisch.
Diese Situation sieht demnach wie folgt aus:

```{figure} ../../figs/python-tutorial/variables/variable-equal-id.png
---
width: 800px
name: fig-variable-equal-id
---
Initialisierung und Zuweisung einer Variablen ``x`` und ``z``  mit dem Wert ``25``. Die Adresse beider Variablen ist identisch.
```

``Python``-erkennt, dass es ausreicht, wenn beide *Variablen* auf den gleichen Speicherbereich zeigen. Wir als Programmierer\*innen bekommen davon gar nichts mit. Verändern wir den Wert von ``z`` dann verändert sich auch deren ``id``:

x = 25
z = 24
print(id(x))
print(id(z))

Die Situation könnte in etwa wie folgt aussehen:

```{figure} ../../figs/python-tutorial/variables/variable-unequal-id.png
---
width: 800px
name: fig-variable-unequal-id
---
Initialisierung und Zuweisung einer Variablen ``x`` und ``z``  mit dem Wert ``25`` und ``24``. Die Adresse beider Variablen ist nicht identisch.
```

```{admonition} Gleichheit und Identität
:name: warning-equality-and-identity
:class: warning
Ist die ``id`` (*Identität*) zweier Variablen gleich, so ist auch deren Wert identisch.
Jedoch kann der Wert der Variablen identisch sein und deren ``id`` (*Identität*) nicht.
```

Ein Beispiel für zwei Variablen mit gleichem **Wert** und unterschiedlicher **Identität** ist leicht konstruiert:

x = 2131313
z = 2131313
print(id(x))
print(id(z))

Hmm?? 
Warum war die ``id`` beim Wert ``25`` identisch aber beim Wert ``2131313`` nicht?
Hier kommen wir in tiefen Details von ``Python``, welche fürs erste nicht so wichtig sind.
Zur Optimierung der Laufzeit legt ``Python`` alle kleinen ganze Zahlen bei Start der Ausführung in den Speicher, sodass Speicherplatz gespart wird.
Das geht jedoch nur für eine endliche Anzahl an Zahlen (deshalb für die ersten $k$ kleinen Zahlen). 
``2131313`` zählt nicht dazu und somit wird der Wert jedesmal neu in den Speicher geschrieben.

Folgender Code berechnet die erste Zahl die nicht bereits bei der Ausführung im Speicher liegt:

x = 0
z = 0
while(id(x) == id(z)):
    x = x + 1
    z = z + 1
x

Wie sieht es mit negativen Zahlen aus?:

x = 0
z = 0
while(id(x) == id(z)):
    x = x - 1
    z = z - 1
x

## Veränderung

Wie der Name bereits betont, sind *Variablen* **variabel** und können somit verändert werden.
Wir müssen jedoch zwischen zwei Veränderungen einer Variablen ``x`` unterscheiden:

1. der Veränderung ihrer Wertes ``x``
2. der Veränderung ihrer Speicheradresse ``id(x)`` (die auf den Wert zeigt)

### Zuweisung eines neuen Werts

Eine *Variable* kann immer nur einen **Wert** bzw. auf einen bestimmten Speicherbereich *zeigen*.
Weisen wir einer *Variablen* erneut einen **Wert** zu, wird dieser **Wert** in den Speicher an eine freie **Adresse** geschrieben und die **Adresse** der Variablen auf jene neue **Adresse** gesetzt.

half = 1/2
print(f'value of half = {half}')
print(f'id of half = {id(half)}')

x = 25
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

x = 24
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

Veränderungen der einen *Variablen* haben keinen Effekt auf die **Adresse** bzw. *Identität ``id`` anderer *Variablen*.

print(f'value of half = {half}')
print(f'id of half = {id(half)}')

Verändern wir *Variablen* nicht so behalten ihre **Adresse** über das gesamte Notebook hinweg.

### Zuweisung einer neuen Adresse

Weisen wir einer Variblen ``x`` eine andere Variable ``y`` zu, so ändern wir die **Adresse** von ``x`` auf jene von ``y``. Das heißt, nach der *Zuweisung* zeigen beide Variablen auf den gleichen Speicherbereich und damit auf den gleichen **Wert**.

x = 2131313
y = 10
z = 2131313

print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of y = {y}')
print(f'id of y = {id(y)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')

y = x

print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of y = {y}')
print(f'id of y = {id(y)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')

### Seiteneffekte

Wie bereits erwähnt: Verändern wir eine *Variable* so können wir dadurch nicht die **Adresse** / *Identität* ``id`` einer anderen Variablen ändern! Wie verhält es sich jedoch mit dem **Wert** einer *Variablen*?

Die Antwort ist etwas komplizierter und ist erst dann begreiflich wenn wir das Thema Datentypen besprechen. Dennoch versuchen wir unser Glück:

Eine Variable kann nicht nur einen einzelnen atomaren **Wert** wie eine Zahl enthalten, sondern auch einen **Wert** der sich aus anderen **Werten** zusammensetzt. Zum Beispiel:

x = [1,2,3,4,5]
x

Der Variablen ``x`` weisen wir hierbei eine sog. *Liste* ``list`` zu, also eine geordnete Menge an Zahlen. In unserem Fall besteht die Liste und somit ``x`` aus den Werten ``1, 2, 3, 4`` und ``5``.

Um auf einen bestimmten **Wert** der Liste zuzugreifen brauchen wir seinen Index. Zum Beispiel liefert uns der Index ``1`` den Wert ``2``:

x[1]

Wie sieht das nun im Speicher aus??? Welche Adresse hat ``x`` und wie sieht der Speicher an der Adresse von ``x`` aus? Der Aufruf

id(x)

Liefert uns eine ``id``, allerdings lieft uns der Aufruf

id(x[1])

ebenfalls eine (andere) ``id``.

id(x[2])

Eine Liste ``list`` mit $n$ Elementen besteht in ``Python`` aus $n$ Adressen. Jede dieser Adressen zeigt auf den Wert des Listenelements. Das heißt, eigentlich sieht unsere Liste ``x`` wie folgt aus:

```python
[id(x[0]), id(x[1]), id(x[2]), id(x[3]), id(x[4])]
```

Doch ``Python`` vereinfacht uns den Umgang mit Listen und verbirgt diese Tatsache geschickt.

Was aber passiert mit ``x`` wenn wir eines seiner Listenelemente verändern? Hier wird es spannend:

print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of x[1] = {x[1]}')
print(f'id of x[1] = {id(x[1])}')

print()

x[1] = -10
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of x[1] = {x[1]}')
print(f'id of x[1] = {id(x[1])}')

Die Adresse von ``x`` ändert sich nicht!!! Es ändert sich nur die Adresse von ``x[1]``!!! Mit anderen Worten durch die *Zuweisung* von ``x[1] = -10`` wird keine neue Liste im Speicher angelegt sondern nur ein neues Element!

Warum? Listen können groß werden und würden wir bei jeder Änderung eines Listenelements die gesamte Liste im Speicher kopieren, wäre das zu teuer was die Laufzeit angeht.

Dieses Verhalten hat jedoch Konsequenzen! Folgender Code führt zur Veränderung des Wertes der Variablen ``y`` von ``y = [[1, 2, 3], [1, 2, 3], [1,2,3]]`` nach ``y` = [[-10, 2, 3], [-10, 2, 3], [1,2,3]]`` obwohl wir nicht direkt mit ``y`` interagieren.

x = [1, 2, 3]
y = [x, x, [1,2,3]]
print(y)

x[0] = -10
print(y)

Solche Veränderungen eines Wertes einer Variablen durch die Veränderung eines Werts einer anderen Variablen, nennen wir *Seiteneffekt*.

## Das Nichts

Um einer *Variable* 'keinen' Wert zuzuweisen gibt es das Signalwort ``None``.
Dies steht für 'kein' Wert bzw. das Nichts.
Dennoch besitzt die *Variable* einen Wert, eben den Wert ``None`` 'kein' Wert.
``None`` repräsentiert somit das Nichts.

z = 0
z + 20
z = None
z

Die Ausgabemechanik des Notebooks ignoriert ``None``, jedoch können wir die *Variable* in eine Zeichenkette umwandeln und dann ausgeben:

z = None
print(z)

``None`` wird uns wieder begegnen wenn wir uns ``Python``-Funktionen ansehen.
Vorab sei gesagt, dass falls eine Funktionen keinen Rückgabewert besitzt sie dann ``None`` zurückliefert.

## Namenskonvention

Namen müssen mit einem Klein- oder Großbuchstaben beginnen und können aus Zahlen und Buchstaben bestehen.
Aus Gründen der Lesbarkeit folgen wir der Konvention von ``Python`` und schreiben *Variablen* komplett in Kleinbuchstaben, Zahlen und dem ``_``.
Außerdem verwenden wir die englische Sprache, alle Signalwörter von ``Python`` in englisch formuliert werden müssen.
Mit dem ``_`` trennen wir zusammengesetzte Namen.
Beispiele für *Variablen* wären: ``x``, ``x1``, ``x2``, ``number``, ``x_direction``, ``temperature``.