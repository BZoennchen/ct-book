(sec-variables)=
# Variablen

*Variablen* können wir uns intuitiv zunächst als Namen oder Bezeichnung eines Wertes vorstellen.
Mit diesem Namen können wir einen Wert im [Arbeitsspeicherspeicher](def-main-memory) des Computers identifizieren.
So können wir uns Zwischenergebnisse merken und damit weiter rechnen.

## Initialisierung und Zuweisung

Durch das ``=`` Zeichen weisen wir einer *Variablen* auf der linken Seite den Wert des *Ausdrucks* auf der rechten Seite zu.
Zum Beispiel, weist

```python
x = 3 + 10
```

den ausgewerteten Wert ``3 + 10`` also ``13`` der Variablen ``x`` zu.
Es ist äußerst wichtig, dass die den zwischen dem ``=`` und dem mathematischen $=$ unterscheiden.

$$x = 13$$

bedeutet, dass $x$ gleich $13$ ist, wohingegen

```python
x = 13
```

den Wert der Variablen ``x`` auf ``13`` setzt oder genaue die Variable auf einen Speicherbereich verweisen lässt, welcher den Wert ``13`` enthält.
Um das mathematisch auszurücken verwendet man oft $\leftarrow$, also 

$$x \leftarrow 13.$$

Dies verdeutlicht, dass es sich um eine *Zuweisung* handelt.
Mit

```python
x = None
```

weisen wir ``x`` den Wert ``None`` d.h. 'Nichts' zu. Doch ist dieses 'Nichts' nicht nichts ;). Versuchen wir eine *Variable* zu verarbeiten, die noch nicht initialisiert wurde, so erhalten wir einen Fehler:

```python
v + 20
```

Hierbei kommt es zu dem Fehler ``name 'v' is not defined``, da die *Variable* ``v`` noch nicht *initialisiert* wurde.


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

```{figure} ../../figs/python-tutorial/variable.png
---
width: 800px
name: fig-variable
---
Initialisierung und Zuweisung einer Variable ``x``  mit dem Wert ``25``. Der Wert steht im Arbeitspeicher an der Speicheradresse 6. Die Variable zeigt auf diese Adresse im Speicher.
```

``id``: Mit der *built-in*-Funktion ``id`` können Sie sich eine Identifikationsnummer einer Variablen ausgeben lassen. Für zwei *Variablen* ist diese genau dann gleich, wenn deren **Arbeitsspeicheradressen** gleich sind.

```python
x = 25
z = 25
print(id(x))
print(id(z))
```

Sie sehen dass die ``id`` der Variablen ``x`` und ``z`` identisch sind. Ebenso ist ihr Wert identisch.
Diese Situation sieht demnach wie folgt aus:

```{figure} ../../figs/python-tutorial/variable-equal-idable.png
---
width: 800px
name: fig-variable-equal-id
---
Initialisierung und Zuweisung einer Variablen ``x`` und ``z``  mit dem Wert ``25``. Die Adresse beider Variablen ist identisch.
```

``Python``-erkennt, dass es ausreicht, wenn beide *Variablen* auf den gleichen Speicherbereich zeigen. Wir als Programmierer\*innen bekommen davon gar nichts mit. Verändern wir den Wert von ``z`` dann verändert sich auch deren ``id``:

```python
x = 25
z = 24
print(id(x))
print(id(z))
```

Die Situation könnte in etwa wie folgt aussehen:

```{figure} ../../figs/python-tutorial/variable-unequal-id.png
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

```python
x = 2131313
z = 2131313
print(id(x))
print(id(z))
```

Hmm?? 
Warum war die ``id`` beim Wert ``25`` identisch aber beim Wert ``2131313`` nicht?
Hier kommen wir in tiefen Details von ``Python``, welche fürs erste nicht so wichtig sind.
Zur Optimierung der Laufzeit legt ``Python`` alle kleinen ganze Zahlen bei Start der Ausführung in den Speicher, sodass Speicherplatz gespart wird.
Das geht jedoch nur für eine endliche Anzahl an Zahlen (deshalb für die ersten $k$ kleinen Zahlen). 
``2131313`` zählt nicht dazu und somit wird der Wert jedesmal neu in den Speicher geschrieben.

Folgender Code berechnet die erste Zahl die nicht bereits bei der Ausführung im Speicher liegt:

```python
x = 0
z = 0
while(id(x) == id(z)):
    x = x + 1
    z = z + 1
x
```

Wie sieht es mit negativen Zahlen aus?:

```python
x = 0
z = 0
while(id(x) == id(z)):
    x = x - 1
    z = z - 1
x
```

## Veränderung

Wie der Name bereits betont, sind *Variablen* variabel und können somit verändert werden.
Wir müssen jedoch zwischen zwei Veränderungen unterscheiden:

1. der Veränderung ihrer Speicheradresse 
2. der Veränderung des Speicherbereichs auf den sie durch ihre Speicheradresse zeigt.

Den zweiten Punkt (2) sehen wir uns später noch an.

Eine *Variable* kann immer nur einen Wert bzw. auf einen bestimmten Speicherbereich *zeigen*.
Weisen wir einer *Variablen* erneut einen Wert zu, überschreiben wir den alten Wert.

```python
quarter = 1/4
half = 2 * quarter
half
```

*Variablen* behalten ihren Wert über das gesamte Notebook hinweg.

```python
quarter = quarter * 2
quarter
```

Veränderungen der einen *Variablen* haben keinen Effekt auf andere *Variablen*.

```python
half
```

## Das Nichts

Um einer *Variable* 'keinen' Wert zuzuweisen gibt es das Signalwort ``None``.
Dies steht für 'kein' Wert bzw. das Nichts.
Dennoch besitzt die *Variable* einen Wert, eben den Wert ``None`` 'kein' Wert.
``None`` repräsentiert somit das Nichts.

```python
z = 0
z + 20
z = None
z
```

Die Ausgabemechanik des Notebooks ignoriert ``None``, jedoch können wir die *Variable* in eine Zeichenkette umwandeln und dann ausgeben:

```python
z = None
print(z)
```

``None`` wird uns wieder begegnen wenn wir uns ``Python``-Funktionen ansehen.
Vorab sei gesagt, dass falls eine Funktionen keinen Rückgabewert besitzt sie dann ``None`` zurückliefert.

## Namenskonvention

Namen müssen mit einem Klein- oder Großbuchstaben beginnen und können aus Zahlen und Buchstaben bestehen.
Aus Gründen der Lesbarkeit folgen wir der Konvention von ``Python`` und schreiben *Variablen* komplett in Kleinbuchstaben, Zahlen und dem ``_``.
Außerdem verwenden wir die englische Sprache, alle Signalwörter von ``Python`` in englisch formuliert werden müssen.
Mit dem ``_`` trennen wir zusammengesetzte Namen.
Beispiele für *Variablen* wären: ``x``, ``x1``, ``x2``, ``number``, ``x_direction``, ``temperature``.