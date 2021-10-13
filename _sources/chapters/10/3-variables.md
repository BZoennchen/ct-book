(sec-variables)=
# Variablen

*Variablen* können wir uns intuitiv zunächst als Namen oder Bezeichnung eines Wertes vorstellen.
Mit diesem Namen können wir einen Wert im [Arbeitsspeicherspeicher](def-main-memory) des Computers identifizieren.
So können wir uns Zwischenergebnisse merken und damit weiter rechnen.


```{figure} ../../figs/python/variable.png
---
width: 600px
name: fig-variable
---
Initialisierung und Zuweisung einer Variable ``x``  mit dem Wert ``25``. Der Wert steht im Arbeitspeicher an der Speicheradresse 6. Die Variable zeigt auf diese Adresse im Speicher.
```

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
In ``Python`` reicht es wenn Sie der *Variablen* einen Wert zuweisen.
Sie wird automatisch erzeugt, d.h., *initialisiert*.
Besitzt Sie noch keinen Wert so existiert sie auch nicht bzw. ist noch nicht *initialisiert*.

```python
z + 20
```

Hier kommt es zu einem Fehler da die *Variable* ``z`` noch nicht *initialisiert* wurde.
Wir können dies beheben:

```python
z = 0
z + 20
```

```{admonition} Initialisierung mit Notebooks
:name: hint-evaluation-ordering
:class: warning
Nach Ausführung dieser Codezeilen funktioniert auch der obige Code.
Dies hängt an der funktionsweise der Notebooks zusammen.
Sobald ``z`` *initialisiert* wurde, existiert ``z`` für alle Zellen des Notebooks.
```

## Veränderung

Wie der Name bereits betont, sind *Variablen* variabel und können somit verändert werden.
Wir müssen jedoch zwischen zwei Veränderungen unterscheiden:

1. der Veränderung der *Variablen* selbst
2. der Veränderung des Speicherbereichs auf den Sie zeigt.

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