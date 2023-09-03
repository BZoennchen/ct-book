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

(sec-function-calls)=
# Funktionsaufrufe

Wenn Sie das Buch von vorne bis hierhin gelesen haben, werden Ihnen so einige Funktionsdefinitionen über den Weg gelaufen sein.
Wie wir eigene Funktionen definieren, werden wir uns noch genauer ansehen.
Vorerst begnügen wir uns mit dem *Aufrufen* von bereits existierenden *Funktionen*.

Vorab sei betont, dass eine *mathematische Funktion* sich von einer ``Python``-Funktion wesentlich unterscheidet.
Wir diskutieren dies genaue im Abschnitt [Reinheit](sec-purity).

Wollen wir eine bestimmte Abfolge von [Ausdrücken](sec-expressions) wieder und wieder aufrufen, so können wir diese Ausdrücke in einer Funktion *kapseln*.
Diese Funktion erfüllt einen bestimmten Zweck.

Benutzten wir bereits existierende Funktionen, so kennen wir (jedenfalls sollte das so sein) das **WAS** aber nicht unbedingt das **WIE**.
Das bedeutet für geübte Programmierer\*innen, dass diese sich viel mit Dokumentationen diverser Module beschäftigen.
Einerseits um das **WAS** in Erfahrung zu bringen und andererseits um eine Vorstellung vom **WIE** zu erhalten.

Wir rufen eine Funktion mit dem Namen ``name`` auf, indem wir an den Namen runde Klammern anfügen: ``name(par1, par2)``.
Funktionen erwarten eine bestimmte Anzahl an *Parametern* (hier ``par1``, ``par2``), wobei es manchmal auch *optionale Parameter* geben kann.

```{admonition} Parameter und Argumente
:name: def-parameter
:class: definition

Die in der Funktionsdefinition angegebenen Namen (Variablen) heißen *Parameter*.
Die Werte, welche diese Parameter erhalten bezeichnen wir als *Argumente* des Funktionsaufrufs.
```

Argumente sind Werte, welche die Funktion erwartet und die wir übergeben müssen.
Diese Argumente werden von der Funktion verarbeitet.

Zum Beispiel, bietet ``Python`` die vordefinierte Funktion ``abs`` an, welche eine Zahl als Argument erwartet.

```{code-cell} python3
abs(-23)
```

In diesem Fall realisiert diese ``Python``-Funktion eine *mathematische Funktion*, nämlich den [Betrag](def-math-abs) $\text{abs}(x) = |x|$.
Weitere Beispiele sind die ``Python``-Funktionen ``round`` und ``max``.

```{code-cell} python3
round(5 - 1.3)
```

```{code-cell} python3
max(2, 3, 5 - 3, 3 * 3)
```

```{code-cell} python3
max(2, -10)
```

``round`` erwartet ebenfalls eine Zahl als Argument.
Die Funktion berechnet aus dem Argument die am nächsten liegende ganze Zahl und liefert diese zurück.
In anderen Worten, ``round`` rundet zur nächst liegenden ganzen Zahl.

``max`` erwartet zwei oder mehr Zahlen als Argumente und liefert die größere Zahl zurück.

Bemerkenswert ist beim obigen *Funktionsaufruf*, dass die *Ausdrücke* ``5-3`` und ``3 * 3`` ausgewertet werden bevor die Funktion aufgerufen wird.
Das heißt, die Funktion wird mit den Argumenten ``2, 3, 2`` und ``9`` aufgerufen.
Wir sehen auch, dass ``max`` mit einer unterschiedlichen Anzahl an Argumenten umgehen kann.

## Module

Es gibt nur wenige vordefinierte Funktionen, die keine Argumente besitzen.
Ein Beispiel hierfür ist die Funktion ``random()`` des *Moduls* ``random``.

```{admonition} Module
:name: def-module
:class: python

Ein ``Python``-Modul ist eine Ansammlung von Funktionalität.
Es ist eine Zusammenstellung von Funktionen, welche zusammengehören.
```

Im Modul ``random`` befinden sich, zum Beispiel, viele Funktionen die Operatoren aus der Wahrscheinlichkeitstheorie realisieren.

Um ein Modul nutzten zu können muss es, d.h. dessen Quellcode, auf Ihrem System installiert sein.
Manche Module, wie beispielsweise ``random``, gehören zur Standardbibliothek von ``Python`` und werden mit ``Python`` selbst installiert.
Ist das Modul installiert, müssen wir es in unseren Code *importieren*.
Wir machen es unserem Code bekannt, sodass wir es auch nutzten können.
Dies geschieht mit dem *Schlüsselwort* ``import``.

```{code-cell} python3
import random
random.random()
```

Mit 

```python
import random
```

machen wir das Modul ``random`` unter dem Namen ``random`` bekannt.
In der zweiten Zeile des Codes rufen wir die Funktion ``random`` des Moduls ``random`` auf.
Diese kann ohne Argumente aufgerufen werden.

Wir können dem Modul auch einen anderen Namen verpassen.
Mit

```python
import random as rnd
```

machen wir das Modul ``random`` unter dem Namen ``rnd`` bekannt.

```{code-cell} python3
import random as rnd
rnd.random()
```

Was macht diese Funktion?
Wenn Sie die obige Zelle mehrfach ausführen werden Sie feststellen, dass sie uns eine zufällige Fließkommazahl zwischen 0 und 1 zurückliefert.

Funktionen, Module und auch Funktionen von Modulen enthalten oft eine Dokumentation in Form von Kommentaren.
Wir können uns deshalb Informationen zu dem **WAS** (und manchmal auch zu dem **WIE**) einer Funktion holen.
Hierzu schreiben wir den Funktionsnamen ohne die runden Klammern und fügen ein ``?`` an.
Alternativ können Sie auch die Hilfefunktion ``help`` verwenden: ``help(random.random)``.

```{code-cell} python3
import random
help(random.random)
```

Die Ausgabe lautet:

```
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).
```

``random() -> x`` bedeutet, dass ``random()`` den Wert ``x`` zurückgibt, wobei ``x`` im halb offenen Intervall $[0;1)$ liegt.
In anderen Worten: Die Funktion ``random()`` liefert einen Wert zwischen 0 und 1 zurück, wobei die 1 ausgeschlossen ist.

```{exercise} Hilfe
:label: help-exercise
Nutzten Sie die eingebaute Hilfe und betrachten Sie die Ausgabe von ``help(max)`` bzw. ``max?``.
Beschreiben Sie die möglichen Argumente der Funktion ``max`` und das **WAS** jener Funktion.
Sie müssen nicht jedes Wort verstehen aber ziehen Sie ihre Schlüsse.
```

```{solution} help-exercise
:label: help-solution
:class: dropdown

Neben der optionalen Argumente, erwartet ``max`` entweder ein iterierbares Argument oder aber mindestens zwei Argumente.
Im ersten Fall gibt ``max`` das größte Element des iterierbaren Arguments zurück.
D.h., ein iterierbares Argument ist wohl so etwas wie eine Sequenz, Liste, Menge an Elementen.

```

## Auswertungsreihenfolge

Ein *Funktionsaufruf* ist ebenfalls ein *Ausdruck* und, wie beim Rechnen, werden Ausdrücke von innen nach außen *ausgewertet*.
Blicken Sie auf folgenden Ausdruck:

```{code-cell} python3
round(max(abs(-abs(-3)), 3, 5 + 3) - 0.6)
```

Dieser Ausdruck besteht aus mehreren Ausdrücken.
Die Auswertung des gesamten Ausdrucks erfolgt von links nach rechts, wobei die notwendigen Argumente, welche durch einen Ausdruck berechnet werden, ausgewertet werden.
Deshalb springen wir von außen nach innen und werten dann von innen nach außen aus.

```{figure} ../../figs/python-tutorial/variables/eval.png
---
width: 400px
name: fig-eval
---
Skizze der Auswertung / Evaluierung des obigen Ausdrucks.
```

Um ``round`` auszuwerten muss zu aller erst der Ausdruck ``max(abs(-abs(-3)), 3, 5 + 3) - 0.6`` ausgewertet werden.
Deshalb wird ``max(abs(-abs(-3)), 3, 5 + 3)`` ausgewertet.
Um jedoch ``max`` auszuwerten werden alle Argumente von links nach rechts berechnet.
Es beginnt mit dem ersten Argument: ``abs(-abs(-3))`` wird zu ``abs(-3)`` wird zu ``3`` und wir erhalten ``max(3, 3, 5 + 3)``.
Das zweite Argument ist bereits ausgewertet und aus ``5+3`` wird ``8``.
Schlussendlich wird ``max(3, 3, 8)`` zu ``8``.
Was bleibt ist ``round(8 - 0.6)`` was zu ``round(7.4)`` ausgewertet wird.
Dieser Ausdruck ergibt ``7``.

Wir können jeder [Variablen](sec-variables) auch einen Ausdruck zuweisen.
Dieser wird ausgewertet und das Ergebnis wird der Variablen zugewiesen.

```{code-cell} python3
x = round(max(abs(-abs(-3)), 3, 5 + 3) - 0.6)
x
```

Auch können wir Funktionsausdrücke mit anderen Ausdrucken wie etwa [arithmetische Operatoren](sec-python-operator-arithmetic) kombinieren.
Durch die folgende Abfolge von Ausdrücken berechnen wir den prozentualen Anteil der Einwohner in Deutschland, die in München wohnen und zwar auf zwei Nachkommastellen gerundet: 

```{code-cell} python3
population_munich = 1_553_373
population_germany = 83_121_363
persentage = round(10000 * 1_553_373 / 83_121_363) / 100
persentage
```

## Das Kennenlernen

Programmieren beginnt oft mit dem Durchwühlen von Dokumentationen fremder Module und Pakete.
Bevor wir loslegen müssen wir erst in Erfahrung bringen **WAS** überhaupt möglich ist.
Welche vordefinierten Funktionen und welche Module gibt es bzw. welche dieser Module könnten für meine Zwecke nützlich sein.

Selbst nach Jahren an Programmierkenntnissen hört dieser Lernprozess nie auf.
Ständig werden neue nützliche Module programmiert und auch Sie werden noch irgendwann Ihre eigenen Module implementieren und nutzten.
Einer der wichtigsten Fähigkeiten ist es, Dokumentationen zu finden und richtig zu lesen.

Mit zunehmender Erfahrung klappt auch dies immer besser.
Zum Beispiel würden erfahrene Programmierer*innen richtigerweise vermuten, dass das Modul ``random`` auch eine Funktion bieten wird, welche eine zufällige natürliche Zahl zurückliefert.
Durchforsten wir das Internet nach diesem Modul so stoßen wir möglicherweise auf [diese Seite](https://docs.python.org/3/library/random.html).
Dort finden wir eine Funktion ``random.randint``.

Wir finden diese auch in der Hilfe, die wir duch ``help`` ausgeben können.

```{code-cell} python3
---
tags: [output_scroll]
---
import random
help(random)
```

```{exercise} Dokumentation
:label: documentation-exercise
Finden Sie die Dokumentation der Funktion ``random.shuffle`` und beschreiben Sie anhand der Dokumentation das **WAS** dieser Funktion.
```

```{solution} documentation-exercise
:label: documentation-solution
:class: dropdown

Diese Funktion mischt eine gegebene Sequenz.
Die übergebene Sequenz ``x`` wird dadurch verändert (durchgemischt).

```