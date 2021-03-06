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

(sec-recursive-functions)=
# Rekursive Funktionen

Bevor Sie fortfahren sollten Sie sich den Abschnitt [Wiederholung](sec-repetition-and-recursion) durchgelesen haben.

Wir werden in diesem Abschnitt nicht über Rekursion an sich sprechen, sondern wie *rekursive Funktionen* in den allermeisten Programmiersprachen realisiert werden.

>Wie realisiert der Computer Rekursion? 

>Was passiert bei einem rekursiven Aufruf?

>Und was sind überhaupt *rekursive Funktionen*?

```{admonition} Rekursive Funktionen
:class: definition
:name: def-recursive-function
Als *rekursive Funktion* wird eine Funktion bezeichnet, welche sich für bestimmte Argumente selbst aufruft.
```

Die folgende Berechnung der Fakultät ist eine rekursive Funktion, welche wir bereits eingeführt hatten.

```{code-cell} python3
def fac(n):
    if n <= 1:    # Base cases!
        return 1
    else:         # Recursive case
        return n * fac(n-1) # Recursive call 

fac(4)
```

Damit eine rekursive Funktion terminiert benötigt sie mindestens einen *Basisfall*, d.h. einen Pfad an Anweisungen, welcher **keinen** Funktionsaufruf der Funktion selbst enthält.
Das ist eine notwendige aber noch nicht hinreichende Bedingung.
Um formal zu beweisen, dass eine rekursive Funktion terminiert und auch das richtig berechnet, verwendet man die sog. [Induktion](sec-induction).

Im obigen Fall sehen wir recht schnell, dass alles korrekt ablaufen sollte, sofern ``n`` eine natürliche Zahl ist.
Da wir ``n`` bei jedem rekursiven Aufruf um 1 verkleinern, muss irgendwann die ``if``-Bedingung zutreffen.
In anderen Worten kommen wir immer irgendwann in den *Basisfall*!

Wie aber werden die Variablen der unterschiedlichen Funktionsaufrufe verwaltet?
Gibt es nur ein einzelnes ``n``, welches von allen Funktionsaufrufen verwendet wird?
Dieser Punkt ist äußerst wichtig.
Lassen Sie uns den Funktionsaufruf ``fac(4)`` einmal 'ausbreiten':
``fac(4)`` wird zu ``4 * fac(3)`` wird zu ``4 * fac(2)`` wird zu ``4 * 3 * fac(1)`` wird schließlich zu ``4 * 3 * 2 * 1``.

## Stack und Heap

Es ist äußerst wichtig zu begreifen, dass bei jedem rekursiven Aufruf ein neuer [lokaler Namensraum](sec-local-namespace) eröffnet wird!
Das bedeutet, jeder Funktionsaufruf verwendet einen frischen Satz an Variablen.
Dieser Namensraum befindet sich auf dem sog. *Stack*, zu deutsch *Stapel*.

```{admonition} Stack (Arbeitsspeicher)
:name: def-stack
:class: definition

Der *Stack* ist ein spezieller Bereich des Arbeitsspeichers, auf welchem die Variablen des lokalen Namensraums liegen.
Bei jedem Funktionsaufruf wird ein Namensraum automatisch auf den Stack gelegt und bei jedem Rücksprung (``return``) wird der entsprechende Namensraum automatisch vom Stack gelöscht.
```

Immer wenn wir ``fac`` aufrufen, wird ein neuer lokaler Namensraum auf den Stack gelegt.
Dieser enthält die Variable ``n``.
Da die Funktionen rekursiv aufgerufen werden, füllt sich der Stack bis wir uns im Aufruf von ``fac(1)`` befinden.

```{figure} ../../figs/python-tutorial/functions/stack_fill.png
---
width: 500px
name: fig-stack_fill
---
Befüllung des *Stacks* durch den Aufruf der *rekursiven Funktion* ``fac(4)``.
```

``fac(1)`` gelangt in den *Basisfall* und beendet die Rekursionskette.
Es ließt sein ``n`` aus seinem Namensraum (in {numref}`Abbildung {number} <fig-stack_fill>` ist das der ``namespace4``), prüft ``n <= 1`` und liefert ``1`` zurück.
Durch diesen Rücksprung, wird der Namensraum gelöscht und der nächste Namensraum auf dem *Stack* definiert den Namensraum des aktuellen Funktionsaufrufs.
In diesem hat ``n`` den Wert ``2`` und wir befinden uns bereits an der Stelle ``return n * fac(1)`` und da ``fac(1)`` soeben den Wert ``1`` zurückgeliefert hat, wird dieser Ausdruck zu ``return n * 1`` und somit zu ``return 2 * 1``.

Sukzessive leert sich der Stack.

```{figure} ../../figs/python-tutorial/functions/stack_clear.png
---
width: 500px
name: fig-stack_clear
---
Der *Stacks* leert sich beim Rücksprung.
```

Wann immer eine Funktion aufgerufen wird (egal ob rekursiv oder nicht) wird oben auf dem Stack ein Speicherblock für den lokalen Namensraum reserviert und wann immer die Funktion terminiert/zurückspringt der Speicherblock wird wieder freigegeben.
Der Zugriff auf den Stack ist schnell, da die Reservierung und das Freigeben wenig Verwaltungsinformation benötigt.
Außerdem ist der Stack ein zusammenhängender Speicherbereich, d.h., aufeinanderfolgende Speicherzugriffe liegen nahe im Speicher beisammen.

```{admonition} Stack und Funktionsaufrufe
:class: remark
:name: remark-stack-speed
Damit wir als Programmierer\*innen Codeblöcke aus Gründen der Laufzeit Funktionen vermeiden, muss der *Stack* sehr effizient sein!
```

Die maximale Tiefe des *Stacks* ist an eine bestimmte Zahl gebunden.
Ist unsere Rekursion zu tief, läuft der Stacks voll:

```{code-cell} python3
---
tags: [raises-exception]
---

fac(1000)
```

Wir können die maximale erlaubte Rekursionstiefe auch anpassen:

```{code-cell} python3
---
tags: [raises-exception]
---
import sys
sys.setrecursionlimit(5000)

fac(1000)
```

Der andere Speicherbereich, welcher nicht zum *Stack* gehört, bezeichnen wir als *Heap*.

```{admonition} Heap (Arbeitsspeicher)
:name: def-heap
:class: definition
Der *Heap* ist ein Speicherbereich für die *dynamische Speicherverwaltung*.
Anders als beim *Stack* gibt es kein Muster mit dem der *Heap* gefüllt bzw. geleert werden muss.
```

Im *Heap* kann man kreuz und quer Speicher reservieren und freigeben.
Das macht die Verwaltung des *Heaps* komplexer.
Im Vergleich zum *Stack* ist es deutlich aufwendiger zu protokollieren, welche Speicherbereiche frei und welche belegt sind.

## Laufzeit

Obwohl der *Stack* enorm effizient ist, sind iterative Lösungen fast immer schneller in ihrer Ausführung.
Übersetzten wir den Code in Maschinencode, also in die niedrigste bzw. konkreteste Form, so benötigen rekursive Lösungen fast immer mehr Sprungbefehle.

Auch benötigt ein Funktionsaufruf mehr Ressourcenmanagement als ein Sprung zum Anfang einer Schleife.
Vergleichen wir unsere rekursive Lösung mit der iterativen:

```{code-cell} python3
def fac_it(n):
    result = 1
    for i in range(1,n+1):
        result += i
    return result
```

Die iterative Lösung verwendet lediglich drei Variablen nämlich ``n``, ``i`` und ``result``, wohingegen wir bei der rekursiven Lösung für ``fac(n)`` ca. ``n`` Variablen benötigen.

Zusätzlich sind [CPU's](def-cpu) in der von [Neumann Architektur](sec-von-neumann) auf Schleifen optimiert.
Rücksprünge kann die CPU nur vorhersagen, wenn es von ihnen nicht zu viele hintereinander gibt.
Dazu verwendet die CPU einen begrenzten Speicher.
Läuft dieser voll, schlägt die Vorhersage fehl und die Ausführungszeit verlängert sich drastisch.

Lassen Sie uns die Laufzeiten der beiden Implementierungen vergleichen:

```{code-cell} python3
%timeit fac_it(1000)
```

```{code-cell} python3
%timeit fac(1000)
```

Der rekursive Aufruf benötigt ca. 473 Nanosekunden, wohingegen die iterative Berechnung ca. 60 Nanosekunden benötigt.
Das heißt die iterative Berechnung ist um einen Faktor von

$$\frac{473}{60} \approx 7.8$$

schneller!

## Endrekursionen (in Python?)

Der Laufzeitvergleich hängt jedoch auch mit der verwendeten Programmiersprache zusammen.
Funktionale Sprachen bieten, zum Beispiel, das Konzept der optimierten *Endrekursion* (engl. *Tail Recursion*).

```{admonition} Endrekursion
:name: def-tail-recursion
:class: definition
*Endrekursion*  ist eine bestimmte Form der Rekursion bei der der rekursive Aufruf einer Funktion auch ihre **letzte Anweisung** ist.
```

Ist eine Funktion endrekursiv, eliminieren die [Compiler](def-compiler) oder [Interpreter](def-interpreter) von funktionalen Sprachen die rekursiven Aufrufe der Funktion -- der *Stack* bleibt (bis auf einen Eintrag) leer.
Unsere ``fac``-Funktion ist keine *Endrekursion*, denn nach dem rekursiven Aufruf folgt eine Multiplikation.
Wir können daraus jedoch leicht eine *Endrekursion* machen:

```{code-cell} python3
def fac_tail(n, acc=1):
    if n <= 1:
        return acc
    else:
        return fac_tail(n-1, acc*n)

fac_tail(4)
```

Alle Arbeit ist getan und dann folgt der rekursive Aufruf.
Deshalb können wir eigentlich alle Namensräume, welche auf dem [Stack](def-stack) liegen vergessen.
Wir haben ``n`` bereits verarbeitet und brauchen es nicht mehr.
Deshalb belastet diese Rekursion den *Stack* nicht, sofern unser [Compiler](def-compiler) oder [Interpreter](def-interpreter) dies auch optimiert.

```{admonition} Endrekursion in Python
:name: remark-tail-recursion-python
:class: remark
Der ``Python``-Interpreter nutzt die *Endrekursion* nicht aus.
```

Der ``Python``-Interpreter optimiert dies nicht!
D.h. obwohl wir ``n`` vergessen könnten, wird es auf den *Stack* gelegt.
Warum sich die Entwickler\*innen gegen *elimination von Endrekursionen* (engl. *Tail Recursion Elimination (TRE)*) entschieden haben, hat verschiedene Gründe:

+ TRE zerstört den sog. Stack Trace (wichtig für Fehlermeldungen)
+ TRE als Option würde Entwickler\*innen motivieren die Rekursion häufiger zu verwenden, doch würde der Code dann nicht überall gleich effizient laufen
+ Entwickler\*innen von ``Python`` glauben nicht an die Rekursion als Basis jeder Programmierung
+ In ``Python`` wäre die Realisierung durch dessen Dynamik äußerst kompliziert, hier ein einfaches Beispiel was bereits zu Problemen führt:

```{code-cell} python3
def f(x):
    if x > 0:
        return f(x-1)
    return 0

g = f
def f(x):
    return x
g(5)
```

Wir binden ``g`` an das erste ``f``.
Dann aber definieren wir ``f`` neu.
``g(5)`` ruft das alte ``f`` auf, nennen wir es ``f_old``.
Somit wird ``g(5)`` zu ``f_old(5)``.
Diese Funktion ruft nun das nicht rekursive neue ``f`` auf, d.h. ``f(5-1)`` wird zu ``f(4)`` wird zu ``4``.
Wie soll der Interpreter protokollieren welche Funktionen rekursiv sind und welche nicht oder nicht mehr?
Dadurch, dass wir Funktionsnamen in ``Python`` zur Laufzeit ändern können, wäre dies unglaublich aufwendig.

An diesem Beispiel wird deutlich, dass die Flexibilität und Dynamik einer Sprache ihren Preis hat.
Für Interpreter und Compiler wird es schwerer und schwerer Optimierungen durchzuführen!