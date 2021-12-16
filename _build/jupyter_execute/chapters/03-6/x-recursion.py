(sec-recursive-functions)=
# Rekursive Funktionen

Bevor Sie fortfahren sollten Sie sich den Abschnitt [Wiederholung und Rekursion](sec-repetition-and-recursion) durchgelesen haben.

Wir werden in diesem Abschnitt nicht über Rekursion an sich sprechen, sondern wie *rekursive Funktionen* in den allermeisten Programmiersprachen realisiert werden.
Wie realisiert der Computer rekursion? 
Was passiert bei einem rekursiven Aufruf?
Und was sind überhaupt *rekursive Funktionen*?

```{admonition} Rekursive Funktionen
Als *rekursive Funktion* wird eine Funktion bezeichnet, welche sich selbst für bestimmte Argumente aufruft.
```

Die folgende Berechnung der Fakultät ist eine rekursive Funktion, welche wir bereits eingeführt haben.

def fac(n):
    if n <= 1:    # Base cases!
        return 1
    else:         # Recursive case
        return n * fac(n-1) # Recursive call 

fac(4)

Damit eine rekursive Funktion terminiert benötigt sie mindestens einen *Basisfall*, d.h. einen Pfad an Anweisungen, welcher **keinen** Funktionsaufruf der Funktion selbst enthält.
Das ist eine notwendige aber noch nicht hinreichende Bedingung.
Um formal zu beweisen, dass eine rekursive Funktion terminiert und auch das richtig berechnet, verwendet man die sog. *Induktion*.

Im obigen Fall sehen wir recht schnell, dass alles korrekt ablaufen sollte, sofern ``n`` eine natürliche Zahl ist.
Da wir ``n`` bei jedem rekursiven Aufruf um 1 verkleinern, muss irgendwann die ``if``-Bedingung zutreffen.
In anderen Worten kommen wir immer irgendwann in den *Basisfall*!

Wie aber werden die Variablen der unterschiedlichen Funktionsaufrufe verwaltet?
Gibt es nur ein einzelnes ``n``, welches von allen Funktionsaufrufen verwendet wird?
Dieser Punkt ist äußerst wichtig.
Lassen Sie uns den Funktionsaufruf ``fac(4)`` einmal 'ausbreite':
``fac(4)`` wird zu ``4 * fac(3)`` wird zu ``4 * fac(2)`` wird zu ``4 * 3 * fac(1)`` wird schließlich zu ``4 * 3 * 2 * 1``.

## Stack und Heap

Es ist äußerst wichtig zu begreifen, dass bei jedem rekursiven Aufruf ein neuer [lokaler Namensraum](sec-local-namespace) eröffnet wird!
Das bedeutet, jeder Funktionsaufruf verwendet einen frischen Satz an Variablen.
Dieser Namensraum befindet sich auf dem sog. *Stack*, zu deutsch *Stapel*.

```{admonition} Stack (Arbeitsspeicher)
:name: def-stack
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
Es ließt sein ``n`` aus seinem Namensraum (in {numref}`Abbildung {number} <fig-stack_fil>` ist das der ``namespace4``), prüft ``n <= 1`` und liefert ``1`` zurück.
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
Außerdem ist der Stack ein zusammenhängender Speicherbereich, d.h., aufeinanderfolgende Zugriffe benötigen naheliegende Speicherbereiche.

```{admonition} Stack und Funktionsaufrufe
:class: hint
Damit wir als Programmierer\*innen nicht vor der Entscheidung stehen einen Codeblock nicht in eine Funktion auszulagern, da sich dadurch die Laufzeit verschlechtert, muss der *Stack* sehr effizient sein!
```

Die Größe des *Stacks* ist einen bestimmte Anzahl an Byte begrenzt.
Ist unsere Rekursion zu tief, läuft dieser Speicher voll:

fac(5000)

Wir können die maximale erlaubte Rekursionstiefe auch anpassen:

import sys
sys.setrecursionlimit(10**5)

fac(5000)

Der andere Speicherbereich, welcher nicht zum *Stack* gehört, bezeichnen wir als *Heap*.

```{admonition} Heap (Arbeitsspeicher)
:name: def-heap
Der *Heap* ist ein Speicherbereich für die *dynamische Speicherverwaltung*.
Anders als beim *Stack* gibt es kein Muster mit dem der *Heap* gefüllt bzw. geleert werden muss.
```

Im den *Heap* kann man kreuz und quer Speicher reservieren und freigeben.
Das macht die Verwaltung des *Heaps* komplexer.
Im vergleich zum *Stack* ist es deutlich aufwendiger zu protokollieren, welche Speicherbereiche frei und welche belegt sind.

## Laufzeit

Obwohl der *Stack* enorm effizient ist, sind iterative Lösungen fast immer schneller in ihrer Ausführung.
Übersetzten wir den Code in Maschinencode, also in die niedrigste bzw. konkreteste Form, so benötigen rekursive Lösungen fast immer mehr Sprungbefehle.

Auch benötigt ein Funktionsaufruf mehr Ressourcenmanagement als ein Sprung zum Anfang einer Schleife.
Vergleichen wir unsere rekursive Lösung mit der iterativen:

def fac_it(n):
    result = 1
    for i in range(1,n+1):
        result += i
    return result

Die iterative Lösung verwendet lediglich drei Variablen nämlich ``n``, ``i`` und ``result``, wohingegen wir bei der rekursiven Lösung für ``fac(n)`` ca. ``n`` Variablen benötigen.

Zusätzlich sind [CPU's](def-cpu) in der von [Neumann Architektur](sec-von-neumann) auf Schleifen optimiert.
Rücksprünge kann die CPU nur vorhersagen, wenn es von ihnen nicht zu viele hintereinander gibt.
Dazu verwendet die CPU einen begrenzten Speicher.
Läuft dieser voll, schlägt die Vorhersage fehl und die Ausführungszeit verlängert sich drastisch.

Lassen Sie uns die Laufzeiten der beiden Implementierungen vergleichen:

%timeit fac_it(5000)

%timeit fac(5000)

Der rekursive Aufruf benötigt ca. 8 Millisekunden, wohingegen die iterative Berechnung ca. 340 Nanosekunden benötigt.
Das heißt die iterative Berechnung ist um einen Faktor von

$$\frac{8000}{340} \approx 24$$

schneller!

## Endrekursionen (in Python?)

Der Laufzeitvergleich hängt jedoch auch mit der verwendeten Programmiersprache zusammen.
Funktionale Sprachen bieten, zum Beispiel, das Konzept der optimierten *Endrekursion* (engl. *Tail Recursion*).

```{admonition} Endrekursion
:name: def-tail-recursion
*Endrekursion*  ist eine bestimmte Form der Rekursion bei der der rekursive Aufruf einer Funktion auch ihre **letzte Anweisung** ist.
```

Trifft dies zu eliminieren die [Compiler](def-compiler) oder [Interpreter](def-interpreter) von funktionalen Sprachen die rekursiven Aufrufe der Funktion -- der *Stack* bleibt (bis auf einen Eintrag) leer.
Unsere ``fac``-Funktion ist keine *Endrekursion*, denn nach dem rekursiven Aufruf wird die multipliziert.
Wir können daraus jedoch leicht eine *Endrekursion* machen:

def fac_tail(n, acc=1):
    if n <= 1:
        return acc
    else:
        return fac_tail(n-1, acc*n)

fac_tail(4)

Alle Arbeit ist getan und dann folgt der rekursive Aufruf.
Deshalb können wir eigentlich alle Namensräume, welche auf dem *Stack* liegen vergessen.
Wir haben ``n`` bereits verarbeitet und brauchen es nicht mehr.
Deshalb belastet diese Rekursion den *Stack* nicht, sofern unser Compiler oder Interpreter dies auch optimiert.
Der ``Python``-Interpreter optimiert dies nicht!
D.h. obwohl wir ``n`` vergessen könnten, wird es auf den *Stack* gelegt.
Warum sich die Entwickler\*innen gegen *elimination von Endrekursionen* (engl. *Tail Recursion Elimination (TRE)*) entschieden haben hat verschiedene Gründe:

+ TRE zerstört den sog. Stack Trace (wichtig für Fehlermeldungen)
+ TRE als Option würde Entwickler\*innen motivieren die Rekursion häufiger zu verwenden, doch würde der Code dann nicht überall gleich effizient laufen
+ Entwickler\*innen von ``Python`` glauben nicht an die Rekursion als Basis jeder Programmierung
+ In ``Python`` wäre die Realisierung durch dessen Dynamik äußerst kompliziert, hier ein einfaches Beispiel was bereits zu Problemen führt:

def f(x):
    if x > 0:
        return f(x-1)
    return 0

g = f
def f(x):
    return x
g(5)

Wir binden ``g`` an das erste ``f``.
Dann aber definieren wir ``f`` neu.
Aus ``g(5)`` ruft das alte ``f`` auf, nennen wir es ``f_old``.
Somit wird ``g(5)`` zu ``f_old(5)`` doch diese Funktion ruft nun das nicht rekursive neue ``f`` auf, d.h. ``f(5-1)`` wird zu ``f(4)`` wird zu ``4``.
Wie soll der Interpreter mit protokollieren welche Funktionen rekursiv sind und welche nicht oder nicht mehr?

```{admonition} Endrekursion und Python
:class: warning
``Python`` optimiert bzw. eliminiert keine Endrekursion!
```

An diesem Beispiel wird deutlich, dass die Flexibilität und Dynamik einer Sprache ihren Preis hat.
Für Interpreter und Compiler wird es schwerer und schwerer Optimierungen durchzuführen!