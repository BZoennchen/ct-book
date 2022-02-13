(sec-typing-in-python)=
# Python's Typisierung

Für statisch getypte Sprachen (siehe Abschnitt [Dynamische und statische Typisierung](sec-type-systems)) wie beispielsweise ``C/C++`` und ``Java`` wird die Typinformation zur Laufzeit nicht benötigt.
Die Typinformation, also welche Variable welchen Datentyp annimmt, wird beim Starten eines Programms vergessen bzw. weggelassen.
Falls wir als Programmierer\*innen zum Beispiel versuchen eine Zeichenkette mit einer Zahl zu addieren, so weißt uns der [Compiler](def-compiler) auf diesen Fehler hin und der Programmcode kann gar nicht erst gestartet werden.
Unser Fehler fällt auf bevor unser Code ausgeführt wird.

Anders verhält es sich jedoch bei dynamisch getypten Sprachen wie etwa ``Python`` und ``JavaScript``.
Für diese Sprachen kann sich, während das Programm läuft, der Typ einer Variablen ändern.
Anders ausgedrückt, kann sich zur Laufzeit ändern wie der Interpreter jene Variable zu interpretieren hat (siehe Abschnitt [Interpretation](sec-interpretation)).
Deshalb werden die Typen auf ihre Korrektheit zur Laufzeit getestet.
Demnach muss die Typinformation, d.h. der Datentyp einer Variable, auch im Arbeitsspeicher liegen.
Unser Fehler fällt erst auf, wenn unser Code ausgeführt wird.

Für dynamisch getypte Sprachen, erweitern wir unsere Sichtweise um die Datentypinformation.
Eine *Variable* kann demnach als Tripel, bestehend aus

+ **Wert**
+ **Datentyp**
+ **Adresse**

verstanden werden.
Die **Speicheradresse** der Variable zeigt in den Arbeitsspeicher an eine bestimmte Stelle.
Dort steht jedoch nicht nur der **Wert** sondern auch der **Datentyp**, d.h. die *Information* wie dieser **Wert** zu interpretieren ist.

```{figure} ../../figs/python-tutorial/datatypes/data-type-key-pair.png
---
width: 800px
name: fig-data-type-key-pair-2
---
Variablen für dynamische Typisierung: Eine *Variable* dargestellt als Tripel aus (Adresse, Datentyp, Wert). 
Datentyp und Wert stehen im Speicher. Die Variable 'kennt' ihre Adresse.
In diesem Beispiel benötigt die Datentypinformation 3 Bit und der Wert 8 Bit.
```

Woher wissen wir und der [Interpreter](def-interpreter), an welcher Stelle im Speicher die Datentypinformation endet?
Eine Möglichkeit ist es eine feste Anzahl an Bits für Datentypen festzulegen.
In {numref}`Abbildung {number} <fig-data-type-key-pair-2>` wären dies 3 [Bits](def-bit).

Dynamische Typisierung, wie sie in ``Python`` besteht, ähnelt dem Konzept der Dateiformate.
So könnten wir ein Bild im ``PNG`` oder ``JPEG``-Format als *(Wert, Dateiformat)* Tupel ansehen.
Der *Wert* ist durch die Bits, die das Bild als solches ausmachen definiert.
Das *Dateiformat* ``PNG`` oder ``JPEG`` gibt an, wie diese Bits von der Computerhardware wie auch Software interpretiert werden müssen, um das Bild auch als Bild verarbeiten zu können.

```{admonition} Datentypen
:name: def-datatypes
:class: definition
Ein *Datentyp* oder auch kurz *Typ* ist ein Attribut eines Werts, welches dem [Compiler](def-compiler) oder [Interpreter](def-interpreter) angibt, wie der Wert zu verwenden bzw. zu interpretieren ist.

```

Blicken wir auf folgenden Code und fragen uns was der Interpreter daraus macht.

```python
x = 3       # <x, int>
y = 5       # <y, int>
z = x + y   # int + int -> int

x = 1.3     # <x, float>
y = 3.5     # <y, float>
z = x + y   # float + float -> float
```

Für die erste Addition von ``x`` und ``y`` holt sich der Interpreter die Datentypinformation.
Er weiß demnach, dass ``x + y`` bedeutet, dass eine Addition von zwei ganzen Zahlen auszuführen ist.
Er wandelt den Code so um, dass die CPU angewiesen wird, zwei ganze Zahlen zu addieren.
Der Addierer der CPU wird aktiv und addiert die beiden Zahlen.
Für die zweiten Addition führt der Interpreter die gleiche Übersetzung durch, jedoch für zwei Fließkommazahlen.
Eine **andere** Einheit, die Fließkomma-Einheit, der CPU wird aktiviert!

## Übungsaufgabe

Um das Konzept um die Datentypen für dynamisch getypte Sprachen zu durchdringen empfehlen wir zu einem späteren Zeitpunkt die Übung [Speicher - alles ist eine Liste](sec-memory).
Diese Übung ist sehr umfangreich und benötigt ein gutes Verständnis von [Variablen](sec-variables), [Funktionen](sec-functions), [Listen](sec-list) und [Rekursion](sec-recursive-functions).