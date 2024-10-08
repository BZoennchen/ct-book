---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(sec-variables)=
# Variablen

*Variablen* können wir uns intuitiv zunächst als Namen oder Bezeichnung eines Wertes vorstellen.
Mit diesem Namen können wir einen Wert im [Arbeitsspeicherspeicher](def-main-memory) des Computers identifizieren.
So können wir uns Zwischenergebnisse merken und damit weiter rechnen.

(sec-assignment)=
## Initialisierung und Zuweisung

Durch das ``=`` Zeichen weisen wir einer *Variablen* (auf der linken Seite) den Wert des *Ausdrucks* (auf der rechten Seite) zu.
Zum Beispiel, weist

```{code-cell} ipython3
x = 3 + 10
```

den ausgewerteten Wert ``3 + 10`` also ``13`` der Variablen ``x`` zu.
Es ist äußerst wichtig, dass Sie zwischen dem ``=`` und dem mathematischen $=$ unterscheiden.

$$x = 13$$

bedeutet, dass $x$ gleich $13$ ist, wohingegen

```{code-cell} ipython3
x = 13
```

den Wert der Variablen ``x`` auf ``13`` setzt bzw. die Variable auf einen Speicherbereich verweisen lässt, welcher den Wert ``13`` enthält.
Um eine *Zuweisung* mathematisch auszurücken, verwendet man oft $\leftarrow$, also 

$$x \leftarrow 13.$$

Mit

```{code-cell} ipython3
x = None
```

weisen wir ``x`` den Wert ``None`` ´, d.h. "Nichts" zu. Doch ist dieses "Nichts" nicht nichts ;).
Es [repräsentiert](sec-representation) lediglich das Nichts.

Versuchen wir eine *Variable* zu verarbeiten, die noch nicht initialisiert wurde, so erhalten wir einen Fehler:

```{code-cell} ipython3
---
tags: [raises-exception]
---
v + 20
```

Die Fehlermeldung ``name 'v' is not defined`` weißt uns darauf hin, dass die *Variable* ``v`` noch nicht *initialisiert* wurde.
In anderen Worten ``v`` gibt es noch gar nicht und zeigt auch nicht auf eine Stelle im Speicher, hat also keinen Wert.
In ``Python`` reicht es wenn Sie der *Variablen* einen Wert zuweisen.
Sie wird automatisch erzeugt, d.h., *initialisiert*.
Besitzt Sie noch keinen Wert so existiert sie auch nicht bzw. ist noch nicht *initialisiert*.

```{admonition} Initialisierung mit Notebooks
:name: remark-evaluation-ordering
:class: remark
Nach Ausführung dieser Codezeilen funktioniert auch der obige Code.
Dies hängt mit der Funktionsweise der Notebooks zusammen.
Sobald ``z`` *initialisiert* wurde, existiert ``z`` für alle Zellen des Notebooks.
```

(sec-vars-equality-and-identity)=
## Variablen und der Arbeitsspeicher

Eine *Variable* können wir als Paar von **Wert** und **Arbeitsspeicheradresse** verstehen.
Der Wert der Variablen steht im [Arbeitsspeicher](def-main-memory) an einer bestimmten Arbeitsspeicheradresse.
Den Arbeitsspeicher können wir uns als lange Liste von Bits vorstellen:

```{figure} ../../figs/python-tutorial/variables/ram.png
---
width: 400px
name: fig-ram
---
Der Arbeitsspeicher ist eine sehr lange Liste bestehend aus [Bits](def-bit).
Die Adresse ist im Wesentlichen die Nummer / der Index eines bestimmten Speicherplatzes.
```


```{admonition} Pythons Typisierung
:name: remark-python-type-mem
:class: remark
Eine ``Python`` *Variable* verweist durch eine Adresse eigentlich nicht nur auf einen Wert sondern auch auf einen [Datentyp](sec-typing-in-python) und auf den Referenzzähler, welcher angibt wie viele Variablen auf den Wert verweisen.
Dies werden wir aber vorerst ignorieren.
```

Variablen abstrahieren den Zusammenhang zwischen Wert und Adresse, sodass Sie uns die Arbeit mit dem Arbeitsspeicher erleichtern.
Wir müssen nicht wissen welche Speicheradressen belegt und welche noch frei sind.
In ``Python`` kommen wir mit der eigentlichen Speicheradresse normalerweise gar nicht in Kontakt.

Mit

```{code-cell} ipython3
x = 25
```

Wird der **Wert** ``25`` in den Arbeitsspeicher an eine freie **Speicheradresse** geschrieben.
Diese **Adresse** erhält die *Variable* ``x``. ``x`` *zeigt* auf den Speicherbereich in dem der **Wert** ``25`` steht!
Folgende Abbildung verdeutlicht die Situation:

```{figure} ../../figs/python-tutorial/variables/variable.png
---
width: 800px
name: fig-variable
---
Initialisierung und Zuweisung einer Variable ``x``  mit dem Wert ``25``. Der Wert steht im Arbeitsspeicher (rechts) an der Speicheradresse 6. Die Variable zeigt auf diese Adresse im Speicher.
```

Mit der *built-in*-Funktion ``id`` können Sie sich eine Identifikationsnummer einer Variablen ausgeben lassen. Für zwei *Variablen* ist diese genau dann gleich, wenn deren **Arbeitsspeicheradressen** gleich sind.

```{code-cell} ipython3
x = 25
z = 25
print(id(x))
print(id(z))
```

Sie sehen dass die ``id`` der Variablen ``x`` und ``z`` identisch sind.
Ebenso ist ihr Wert identisch.
Diese Situation sieht demnach wie folgt aus:

```{figure} ../../figs/python-tutorial/variables/variable-equal-id.png
---
width: 800px
name: fig-variable-equal-id
---
Initialisierung und Zuweisung einer Variablen ``x`` und ``z``  mit dem Wert ``25``. Die Adresse beider Variablen ist identisch.
```

```{admonition} Identität
:name: def-identity
:class: python
Zwei *Variablen* ``x`` und ``y`` sind *identisch* genau dann wenn sie den gleichen Speicherbereich adressieren.
```

```{admonition} Gleichheit
:name: def-equality
:class: python
Zwei *Variablen* ``x`` und ``y`` sind *gleich* genau dann wenn der Speicherbereich auf den sie verweisen den gleichen Wert beinhaltet.
```

``Python``-erkennt, dass es ausreicht, wenn beide *Variablen* auf den gleichen Speicherbereich zeigen.
Wir als Programmierer\*innen bekommen davon gar nichts mit. Verändern wir den Wert von ``z`` dann verändert sich auch die ``id``:

```{code-cell} python3
x = 25
z = 24
print(id(x))
print(id(z))
```

Die Situation könnte in etwa wie folgt aussehen:

```{figure} ../../figs/python-tutorial/variables/variable-unequal-id.png
---
width: 800px
name: fig-variable-unequal-id
---
Initialisierung und Zuweisung einer Variablen ``x`` und ``z``  mit dem Wert ``25`` und ``24``. Die Adresse beider Variablen ist nicht identisch.
```

````{admonition} Aus Identität folgt Gleichheit
:name: theorem-equality-and-identity
:class: theorem

Zwei Variablen ``x`` und ``y``, die auf die gleiche Speicheradresse zeigen haben auch den gleichen Wert.
Das heißt aus

```python
id(x) == id(y)
```

folgt

```python
x == y
```

Zwei Variablen können jedoch den gleichen Wert haben, allerdings auf verschiedene Speicherbereiche verweisen.
````


Ein Beispiel für zwei Variablen mit gleichem Wert und unterschiedlicher Identität ist leicht konstruiert:

```{code-cell} ipython3
x = 2131313
z = 2131313
print(id(x))
print(id(z))
```

Hmm?? 
Warum war die ``id`` beim Wert ``25`` identisch aber beim Wert ``2131313`` nicht?
Hier kommen wir in die tiefen Details von ``Python``, welche fürs erste nicht so wichtig sind.
Zur Optimierung der Laufzeit legt ``Python`` alle kleinen ganzen Zahlen bei Start der Ausführung in den Speicher, sodass Speicherplatz gespart wird.
Das geht jedoch nur für eine endliche Anzahl an Zahlen (deshalb für die ersten k kleinsten Zahlen). 
``2131313`` zählt nicht dazu und somit wird der Wert jedesmal neu in den Speicher geschrieben.

Folgender Code berechnet die erste Zahl die nicht bereits bei der Ausführung im Speicher liegt:

```{code-cell} ipython3
x = 0
z = 0
while(id(x) == id(z)):
    x = x + 1
    z = z + 1
x
```

Wie sieht es mit negativen Zahlen aus?:

```{code-cell} ipython3
x = 0
z = 0
while(id(x) == id(z)):
    x = x - 1
    z = z - 1
x
```

## Veränderung

Wie der Name bereits betont, sind *Variablen* **variabel** und können somit verändert werden.
Wir müssen jedoch zwischen zwei Veränderungen einer Variablen ``x`` unterscheiden:

1. der Veränderung ihrer Wertes ``x``
2. der Veränderung ihrer Speicheradresse ``id(x)`` (die auf den Wert zeigt)

```{admonition} Veränderlich und Un­ver­än­der­lich­keit
:name: def-mutable
:class: definition

Wir nennen eine Variable, *veränderlich* (engl. *mutable*) wenn wir deren Wert verändern können indem wir den Speicherbereich der Variable verändern können.
Ein Variable ist dagegen *unveränderlich* (engl. *immutable*) wenn wir deren Speicherbereich nicht verändern können.

Ist eine Variable *unveränderlich*, so wird deren Veränderung durch eine Kopie (einen neuen Speicherbereich) realisiert.
Das Ursprungsobjekt bleibt *unverändert*.
```

### Zuweisung eines neuen Werts

Eine *Variable* kann immer nur einen **Wert** bzw. auf einen bestimmten Speicherbereich *zeigen*.
Weisen wir einer *Variablen* erneut einen **Wert** zu, wird dieser **Wert** in den Speicher an eine freie **Adresse** geschrieben und die **Adresse** der Variablen auf jene neue **Adresse** gesetzt.

```{code-cell} ipython3
half = 1/2
print(f'value of half = {half}')
print(f'id of half = {id(half)}')

x = 25
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

x = 24
print(f'value of x = {x}')
print(f'id of x = {id(x)}')
```

````{admonition} Adressänderung
:name: theorem-change-of-variable
:class: theorem

Veränderungen der einen *Variablen* haben keinen Effekt auf die **Adresse** bzw. *Identität* ``id`` anderer *Variablen*.
````


```{code-cell} ipython3
print(f'value of half = {half}')
print(f'id of half = {id(half)}')
```

Verändern wir *Variablen* nicht, so behalten sie ihre **Adresse** über das gesamte Notebook hinweg.

### Zuweisung einer neuen Adresse

Weisen wir einer Variablen ``x`` eine andere Variable ``y`` zu, so ändern wir die **Adresse** von ``x`` auf jene von ``y``. Das heißt, nach der *Zuweisung* zeigen beide Variablen auf den gleichen Speicherbereich und damit auf den gleichen **Wert**.

```{code-cell} ipython3
x = 2131313
y = 10
z = 2131313

print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of y = {y}')
print(f'id of y = {id(y)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
```


```{code-cell} python3
y = x

print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of y = {y}')
print(f'id of y = {id(y)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
```

### Seiteneffekte

Wie bereits erwähnt: Verändern wir eine *Variable* so können wir dadurch nicht die **Adresse** / *Identität* ``id`` einer anderen Variablen ändern! Wie verhält es sich jedoch mit dem **Wert** einer *Variablen*?

Die Antwort ist etwas komplizierter und ist erst dann begreiflich wenn wir das Thema [Datentypen](sec-python-data-types) besprechen.
Dennoch versuchen wir unser Glück:
Eine Variable kann nicht nur einen einzelnen atomaren **Wert**, wie eine Zahl, enthalten, sondern auch einen **Wert** der sich aus anderen **Werten** [zusammensetzt](def-data-structures).
Zum Beispiel:

```{code-cell} ipython3
x = [1,2,3,4,5]
x
```

Der Variablen ``x`` weisen wir hierbei eine sog. [Liste](sec-list) ``list`` zu, also ein geordnetes, veränderliches Tupel an Zahlen.
In unserem Fall besteht die Liste, und somit ``x``, aus den Werten ``1, 2, 3, 4`` und ``5``.
Um auf einen bestimmten **Wert** der Liste zuzugreifen brauchen wir seinen Index. Zum Beispiel liefert uns der Index ``1`` den Wert ``2``:

```{code-cell} ipython3
x[1]
```

Wie sieht das nun im Speicher aus??? Welche Adresse hat ``x`` und wie sieht der Speicher an der Adresse von ``x`` aus? Der Aufruf

```{code-cell} ipython3
id(x)
```

Liefert uns eine ``id``, allerdings lieft uns der Aufruf

```{code-cell} ipython3
id(x[1])
```

ebenfalls eine (andere) ``id``.

```{code-cell} ipython3
id(x[2])
```

Eine Liste ``list`` mit $n$ Elementen besteht in ``Python`` aus $n$ Adressen. Jede dieser Adressen zeigt auf den Wert des Listenelements. Das heißt, eigentlich sieht unsere Liste ``x`` wie folgt aus:

```python
[id(x[0]), id(x[1]), id(x[2]), id(x[3]), id(x[4])]
```

Doch ``Python`` vereinfacht uns den Umgang mit Listen und verbirgt diese Tatsache geschickt.

Was aber passiert mit ``x`` wenn wir eines seiner Listenelemente verändern? Hier wird es spannend:

```{code-cell} ipython3
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
```

Die Adresse von ``x`` ändert sich nicht!!! Es ändert sich nur die Adresse von ``x[1]``!!! Mit anderen Worten durch die *Zuweisung* von ``x[1] = -10`` wird keine neue Liste im Speicher angelegt, sondern nur ein neues Element!
Dieses Element wird an eine freie Speicherstelle platziert und die entsprechende Adresse kommt in die Liste.

Warum? 
Listen können groß werden und würden wir bei jeder Änderung eines Listenelements die gesamte Liste im Speicher kopieren, wäre das, im Bezug auf die Laufzeit, zu teuer und verschwenderisch.

Dieses Verhalten hat jedoch Konsequenzen! 
Folgender Code führt zur Veränderung des Wertes der Variablen ``y`` von ``y == [[1, 2, 3], [1, 2, 3], [1,2,3]]`` nach ``y == [[-10, 2, 3], [-10, 2, 3], [1,2,3]]`` obwohl wir nicht direkt mit ``y`` interagieren.

```{code-cell} ipython3
x = [1, 2, 3]
y = [x, x, [1,2,3]]
print(y)

x[0] = -10
print(y)
```

Solche Veränderungen eines Wertes einer Variablen durch die Veränderung eines Werts einer anderen Variablen, nennen wir *Seiteneffekt*.

````{admonition} Seiteneffekt
:name: remark-change-of-variable-value
:class: remark

Handelt es sich beim Wert der Variablen um **keinen** [atomaren Datentyp](sec-atom-data-type), so kann die Veränderung des Werts dazu führen, dass sich der Wert einer anderen Variable verändert.
````

## Das Nichts

Um einer *Variablen* "keinen" Wert zuzuweisen gibt es das Signalwort ``None``.
Dies [repräsentiert](sec-representation) "keinen Wert" bzw. das Nichts.
Dennoch besitzt die *Variable* einen Wert, eben den Wert ``None``.

```{code-cell} ipython3
z = 0
z + 20
z = None
z
```

Die Ausgabemechanik des Notebooks ignoriert ``None``, jedoch können wir die *Variable* in eine Zeichenkette umwandeln und dann ausgeben:

```{code-cell} ipython3
z = None
print(id(z))
print(z)
```

``None`` wird uns wieder begegnen, wenn wir uns ``Python``-Funktionen ansehen.
Vorab sei gesagt, dass falls eine [Funktion](sec-functions) keinen Rückgabewert besitzt, sie ``None`` zurückliefert.

## Namenskonvention

Namen müssen mit einem Klein- oder Großbuchstaben beginnen und können aus Zahlen und Buchstaben bestehen.
Aus Gründen der Lesbarkeit folgen wir der Konvention von ``Python`` und schreiben *Variablen* komplett in Kleinbuchstaben, Zahlen und dem ``_``.
Außerdem verwenden wir die englische Sprache, da alle Signalwörter von ``Python`` ohnehin in englisch formuliert werden müssen.
Mit dem ``_`` trennen wir zusammengesetzte Namen.

Beispiele für *Variablen* wären: ``x``, ``x1``, ``x2``, ``number``, ``x_direction``, ``temperature``.