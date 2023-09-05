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

(sec-expressions)=
# Ausdrücke

Im Vergleich zu natürlichen Sprachen, sind Programmiersprachen sind viel einfacher aufgebaut.
Entwickler\*innen der Sprachen versuchen ihre [Syntax](def-syntax) so unmissverständlich, elegant, kurz und ausdrucksstark wie möglich zu gestalten.
In der Vergangenheit gelang das nicht immer und über die Jahre haben wir viel dazu gelernt.
In diesem Kurs verwenden wir ``Python`` insbesondere deshalb, weil es eine der leserlichsten und zugleich mächtigsten Sprachen unserer Zeit ist.

Jedes Programm, bzw. jeder Algorithmus besteht aus vielen *Ausdrücken*.
Ein *Ausdruck* beschreibt wie Daten (die Eingabe) verarbeitet werden sollen.

Die Multiplikation ``3 * 5`` ist beispielsweise ein Ausdruck der zwei Dezimalzahlen multipliziert.
Der *Ausdruck* besteht aus dem Symbol ``*`` und zwei nummerischen *Ausdrücken*.
Die Multiplikation wird durch den Computer, genauer die [CPU](def-cpu) berechnet.
``3 * 5`` ergibt ``15``.

```{code-cell} python3
3 * 5
```

Die [Syntax](def-syntax) einer Programmiersprache ist strikt.
Sie wird durch eine sog. *Grammatik* definiert.å
Zum Beispiel ist folgender *Ausdruck* fehlerhaft, da er nicht durch die *Grammatik* von ``Python`` definiert ist.
Man sagt auch, dass die Sprache, welche durch die Grammatik definiert ist, den folgenden Ausdruck nicht enthält.

```{code-cell} python3
---
tags: [raises-exception]
---
3 * * 5
```

Der Computer bzw. ``Python``-[Interpreter](def-interpreter) weiß mit dieser Folge an Symbolen nichts anzufangen.
Wir werden vom Interpreter sachlich auf die mögliche Fehlerursache hingewiesen.
Bereits kleine Änderungen an der [Syntax](def-syntax) können zu einer neuen Bedeutung ([Semantik](def-semantik)) führen.
In ``Python`` ist der *Ausdruck*

```{code-cell} python3
3 ** 5
```

syntaktisch korrekt.
Seine [Semantik](def-semantik) ist die Berechnung von $3^5$, was $243$ ergibt.
In kaum einer anderen Sprache gibt es für die Potenz eine derart kurze Schreibweise.

(sec-python-operator-arithmetic)=
## Arithmetische Operatoren

Die Multiplikation ``*`` wie auch die Potenz ``**`` bezeichnen wir als *arithmetische Operatoren*, da sie numerische Werte (Zahlen) verarbeiten.
Es gibt jedoch noch eine ganze Reihe von weiteren *arithmetische Operatoren*:

| Operator |     Beschreibung     |  Beispiel  |                     Bedeutung                      |
| :------: | :------------------: | :--------: | :------------------------------------------------: |
|   `+`    |       Addition       | ``3 + 4``  |                      $3 + 4$                       |
|   `-`    |     Subtraktion      | ``3 - 4``  |                      $3 - 4$                       |
|   `*`    |    Multiplikation    | ``3 * 4``  |                    $3 \cdot 4$                     |
|   `/`    |       Division       | ``3 / 4``  |                      $3 / 4$                       |
|   `**`   |     Potenzierung     |  ``3**4``  |                       $3^4$                        |
|   `//`   | ganzzahlige Division | ``3 // 4`` |         $\left \lfloor{3/4}\right \rfloor$         |
|   `%`    |        Modulo        | ``10 % 4`` | $10 - (4 \cdot \left \lfloor{10/4}\right \rfloor)$ |

Jeder dieser Operatoren ``op`` erwartet zwei Zahlen, eine links und eine rechts von ``op``.

Die Bedeutung der Modulo-Operation ``%`` sieht kompliziert aus, doch bedeutet dies schlicht, dass ``10 % 4`` der *ganzzahlige Rest* der [Restwertdivision](def-euclid-division) ist.

Die ganzzahlige Division [rundet](sec-math-rounding) das Ergebnis der Division auf die nächst kleinere ganze Zahl (Integer).
Beachten Sie

```{code-cell} python3
-2 // 3
```

ergibt ``-1`` und

```{code-cell} python3
2 // 3
```

ergibt ``0``.

*Arithmetische Operationen* werden von der *arithmetischen Einheit* der [CPU](def-cpu) ausgewertet.
Mit ihnen können wir numerische Gleichungen lösen aber auch Indices manipulieren.

(sec-python-operator-compare)=
## Vergleichsoperatoren

Objekte können über Vergleichsoperatoren miteinander verglichen werden. 
Das Ergebnis ist ein boolscher Wert ``True`` oder ``False``.

| Operator  | Beschreibung                      |
| :-------: | :-------------------------------- |
| `x == y ` | ist `x` gleich `y`?               |
| `x != y`  | ist `x` ungleich `y`?             |
|  `x > y`  | ist `x` größer als `y`?           |
| `x >= y`  | ist `x` größer oder gleich `y`?   |
|  `x < y`  | ist `x` kleiner `y`?              |
| `x <= y`  | ist `x` kleiner gleich `y`?       |
| `x is y`  | ist `x` [identisch](def-identity) zu `y`? |

Erneut ist ``Python`` hier ein wenig speziell, da es die mathematische Schreibweise $0 < x < 5$ zulässt.
Dies erhöht die Lesbarkeit, da wir solche Verkettungen von Vergleichsoperatoren gewohnt sind.

```{code-cell} python3
5 < 7 < 10 # True
```

```{code-cell} python3
5 < 7 and 7 < 10 # True
```

```{code-cell} python3
5 < 7 < 5 # False
```

*Vergleichsoperatoren* können auch auf nicht-numerischen Werten (ganze Zahlen ``int``, Fließkommazahlen ``float``) definiert sein.
So können wir in ``Python`` auch Zeichenketten ``str`` mit den Vergleichsoperatoren lexikographisch vergleichen:

```{code-cell} python3
'Anna' < 'Emma' # True
```

Generell vergleichen wir Objekte einer [Menge](sec-math-set) immer bezüglich einer [(totalen) Ordnung](def-math-order).
Diese Ordnung muss irgendwo definiert worden sein, ob durch die Standardbibliothek von ``Python``, impliziet, oder durch uns Entwickler\*innen.

(sec-logic-expressions)=
## Logische Operatoren

Der obige *Ausdruck* ist aus weiteren Ausdrücken zusammengesetzt.
Er behinhaltet den *Ausdruck* ``and``, d.h., dem logischen UND ($\land$).
Dieser erwartet auf der linken und rechte Seite jeweils einen Wahrheitswert (*boolschen Ausdruck*).
Zum Beispiel, liefern [Vergleichsoperatoren](sec-python-operator-compare) *boolsche Ausdrücke* zurück.

```{code-cell} python3
x = True
y = False

x and y
```

``x and y`` ergibt genau dann ``True`` wenn die Auswertung von ``x`` und ``y`` jeweils ``True`` ergeben.
Wir haben diese Operatoren bereits im Abschnitt [Manipulation](sec-manipulation) besprochen.
Sie werden in Computern durch Gatter realisiert.
Lassen Sie uns diese nochmals zusammenfassen:

| Operator  | Beschreibung                                               |
| :-------: | :--------------------------------------------------------- |
|  `not x`  | ist `True` genau dann wenn `x == False`.                   |
| `x and y` | ist `True` genau dann wenn `x == True` und `y == True`.    |
| `x or y`  | ist `True` genau dann wenn ``x == True`` oder `y == True`. |

(sec-bit-operations)=
## Bitoperatoren

Zur Vollständigkeit listen wir auch noch die sog. *Bitoperatoren* auf.
Diese manipulieren ganze Zahlen in ihrer [Binärdarstellung](sec-binary-numbers).

Erinnern Sie sich an den Abschnitt [Repräsentation](sec-representation)?
Dort haben wir beschrieben wie schlussendlich jeder Wert, egal ob Zahl, Zeichen, Bild, Ton als Binärcode im Speicher liegt.
*Bitoperatoren* nehmen diesen Binärwert und verarbeiten bzw. kombinieren ihn.
Dabei wird jedes [Bit](def-bit) des einen Werts mit dem Bit des anderen Werts kombiniert.
Unsere Gatter aus dem Abschnitt [Manipulation](sec-manipulation) bilden den Grundstock für eine derartige Verarbeitung.

``Python`` bietet uns an diese maschinennahen Operationen auf Zahlen anzuwenden.
Zum Beispiel, kombinieren wir mit ``5 & 4`` jedes Bit der Zahl ``5`` mit dem ``and`` der Zahl ``4``.
Dies nennen wir das *bitweise* UND.

```{code-cell} python3
5 & 4
```

Jedes Bit der Zahl $5_{10} = 0101_2$ und $4_{10} = 0100_2$ wird durch eine AND-Gatter gejagt.
Dies nennen wir auch *bitweises* UND der Binärzahlen $0101_2$ und $0010_2$:

```{math}
  \begin{split}
	  0101_2&\\
	  \land\ \ 0010_2&\\ \hline \hline
	  = 0100_2&=4_{10}
	\end{split}
```

Wenn Sie an dieser Stelle Probleme mit Binärzahlen haben, lesen sie Abschnitt [Zahlen im Binärsystem](sec-binary-numbers).
Folgende *bitweisen Operationen* stehen Ihnen in zur Verfügung:

| Operator | Beschreibung                                       | Beispiel | Ergebnis |
| :------: | :------------------------------------------------- | :------- | :------- |
| `x & y`  | UND von `x` mit `y`                                | `10 & 3` | `2`      |
| `x \| y`  | ODER von `x` mit `y`                               | `10 \| 3` | `11`     |
| `x ^ y`  | exklusives ODER von `x`  mit `y`                   | `10 ^ 3` | `9`      |
| `x << y` | Bitverschiebung von `x` um `y` Stellen nach links  | `8 << 3` | `64`     |
| `x >> y` | Bitverschiebung von `x` um `y` Stellen nach rechts | `8 >> 2` | `2`      |

Weshalb ist ``10 ^ 3`` gleich ``9``?
Die ``^``-Operation steht für das sog. *exklusive ODER* gesprochen *entweder oder*.
Das exklusive oder $x \oplus y$ ergibt 1 genau dann wenn *entweder* $x$ *oder* $y$ (nicht aber beide) gleich 1 sind.
Es gilt $10_{10} = 01010_2$ und $3_{10} = 00011_2$.

```{math}
  \begin{split}
	  01010_2&\\
	  \oplus\ \ 00011_2&\\ \hline \hline
	  = 01001_2&=9_{10}
	\end{split}
```

Für ganze Zahlen entspricht die Bitverschiebung um ein Bit nach links der Multiplikation mit 2.
Die Verschiebung um ein Bit nach rechts, hingegen der [ganzzahligen Division](sec-python-operator-arithmetic) mit 2.
Deshalb ist `8 << 3` gleich 

$$8 \cdot 2 \cdot 2 \cdot 2 = 8 \cdot 2^3 = 64$$

und ``8 >> 2`` gleich 

$$\left \lfloor{8 \cdot 2^{-2}}\right \rfloor = 2.$$

