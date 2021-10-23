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

# Funktionsaufrufe

Wie wir eigene Funktionen definieren werden wir uns noch genauer ansehen.
Vorerst begnügen wir uns mit dem *Aufrufen* von bereits existierenden *Funktionen*.

Vorab sei betont, dass eine *mathematische Funktion* sich von einer ``Python``-Funktion unterscheidet.
Wollen wir eine bestimmte Abfolge von [Ausdrücken](sec-expressions) wieder und wieder aufrufen, so können wir diese Ausdrücke in einer Funktion *kapseln*.
Diese Funktion erfüllt einen bestimmten Zweck.
Benutzten wir bereits existierende Funktionen, so kennen wir (jedenfalls sollte das so sein) **Wie** aber nicht unbedingt das **Wie**.

Wir rufen eine Funktion mit dem Namen ``name`` auf indem wir an den Namen Runde Klammern anfügen: ``name()``.
Funktionen erwarten eine bestimmte Anzahl an *Argumenten*, wobei es manchmal auch *optionale Argumente* geben kann.
Argumente sind Werte, welche die Funktion erwartet und die wir übergeben müssen.
Diese Argumente werden von der Funktion verarbeitet.

Zum Beispiel bietet ``Python`` die vordefinierte Funktion ``abs`` an, welche ein Argument erwartet, eine Zahl, erwartet.

```{code-cell} python3
abs(-23)
```

In diesem Fall realisiert diese ``Python``-Funktion eine *mathematische Funktion*, nämlich den Betrag $abs(x) = |x|$.
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
``max`` erwartet zwei Zahlen oder als Argumente und liefert die größte Zahl zurück.
Bemerkenswert beim obigen *Funktionsaufruf* ist, dass die *Ausdrücke* ``5-3`` und ``3 * 3`` ausgewertet werden bevor die Funktion aufgerufen wird.
Das heißt die Funktion wird mit den Argumenten ``2, 3, 2`` und ``9`` aufgerufen.
Wir sehen auch, dass ``max`` mit einer unterschiedlichen Anzahl an Argumenten umgehen kann.

## Module

Es gibt nur wenige vordefinierte Funktionen, die keine Argumente besitzen.
Ein Beispiel hierfür ist die Funktion ``random()`` des *Moduls* ``random``.
Ein ``Python``-Modul ist eine Ansammlung von Funktionalität, es ist eine Zusammenstellung von Funktionen, welche zusammengehören.
Im Modul ``random`` befinden sich zum Beispiel viele Funktionen bei denen es um den Zufall und Wahrscheinlichkeiten geht.

Um ein Modul nutzten zu können muss es, d.h. dessen Quellcode, auf Ihrem System installiert sein.
Manche Module wie beispielsweise ``random`` gehören zur Standardbibliothek von ``Python`` und werden installiert sobald ``Python`` installiert wird.
Ist das Modul installiert, müssen wir es in unseren Code *importieren*.
Wir machen es unserem Code bekannt, sodass wir es auch nutzten können.
Dies geschieht mit dem *Schlüsselwort* ``import``.

```{code-cell} python3
import random
random.random()
```

Mit ``import random`` machen wir das Modul ``random`` unter dem Namen ``random`` bekannt.
In der zweiten Zeile des Codes rufen wir die Funktion ``random`` des Moduls ``random`` auf.
Diese kann ohne Argumente aufgerufen werden.

Was macht diese Funktion?
Wenn Sie die obige Zelle mehrfach ausführen werden Sie feststellen, dass sie uns eine zufällige Fließkommazahl zwischen 0 und 1 zurückliefert.

Funktionen, Module und auch Funktionen von Modulen enthalten oft eine Dokumentation in Form von Kommentaren.
Wir können uns deshalb Informationen zu dem **Was** (und manchmal auch zu dem **Wie**) einer Funktion holen.
Hierzu schreiben wir den Funktionsnamen ohne die runden Klammern und fügen ein ``?`` an.
Oder Sie verwenden die Hilfefunktion ``help`` und übergeben die Funktion: ``help(random.random)``.

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

``random() -> x`` bedeutet, dass ``random()`` den Wert ``x`` zurückgibt, wobei ``x`` im Intervall $[0;1)$ liegt.
In anderen Worten: Die Funktion ``random()`` liefert einen Wert zwischen 0 und 1 zurück, wobei die 1 ausgeschlossen ist.

```{exercise} Hilfe
:label: help-exercise
Nutzten Sie die eingebaute Hilfe und betrachten Sie die Ausgabe von ``help(max)`` bzw. ``max?``.
Beschreiben Sie die möglichen Argumente der Funktion ``max`` und das **Was** jener Funktion.
Sie müssen nicht jedes Wort verstehen aber ziehen Sie ihre Schlüsse.
```

```{solution} help-exercise
:label: help-solution
:class: dropdown

Neben der optionalen Argumente erwartet ``max`` entweder ein iterierbares Argument oder aber mindestens zwei Argumente.
Im ersten Fall gibt ``max`` das größte Element des iterierbaren Arguments zurück.
D.h. ein iterierbares Argument ist wohl so etwas wie eine Sequenz, Liste, Menge an Elementen.

```

## Auswertungsreihenfolge

Ein *Funktionsaufruf* ist ebenfalls ein *Ausdruck* und wie beim Rechnen werden Ausdrücke von innen nach außen *ausgewertet*.
Blicken Sie auf folgenden Ausdruck:

```{code-cell} python3
round(max(abs(-abs(-3)), 3, 5 + 3) - 0.6)
```

Dieser Ausdruck besteht aus mehreren Ausdrücken.
Die Auswertung des gesamten Ausdrucks erfolgt von innen nach außen.
Um ``round`` auszuwerten muss zu aller erst der Ausdruck ``max(abs(-abs(-3)), 3, 5 + 3) - 0.6`` ausgewertet werden.
Deshalb wird ``max(abs(-abs(-3)), 3, 5 + 3)`` ausgewertet.
Um jedoch ``max`` auszuwerten werden alle Argumente berechnet.
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
Durch die folgende Abfolge von Ausdrücken berechnen wir den prozentualen Anteil der Einwohner in Deutschland, die in München wohnen auf zwei Nachkommastellen gerundet: 

```{code-cell} python3
population_munich = 1_553_373
population_germany = 83_121_363
persentage = round(10000 * 1_553_373 / 83_121_363) / 100
persentage
```

## Das Kennenlernen

Programmieren beginnt oft mit der Dokumentation von Modulen und Bibliotheken.
Bevor wir loslegen müssen wir erst in Erfahrung bringen **was** überhaupt möglich ist.
Welche vordefinierten Funktionen und welche Module gibt es bzw. welche dieser Module könnten für meine Zwecke nützlich sein.

Selbst nach Jahren an Programmierkenntnissen hört dieser Lernprozess nie auf.
Ständig werden neue nützliche Module programmiert und auch Sie werden noch irgendwann Ihre eigenen Module implementieren und nutzten.
Einer der wichtigsten Fähigkeiten ist es, Dokumentationen zu finden und richtig zu lesen.

Mit der Erfahrung funktioniert auch das immer besser.
Zum Beispiel würden erfahrene Programmierer*innen richtigerweise vermuten, dass das Modul ``random`` auch eine Funktion bieten wird, welche eine zufällige natürliche Zahl zurückliefert.
Durchforsten wir das Internet nach diesem Modul so stoßen wir möglicherweise auf [diese Seite](https://docs.python.org/3/library/random.html).
Dort finden wir eine Funktion ``random.randint``.

```{exercise} Dokumentation
:label: documentation-exercise
Finden Sie die Dokumentation der Funktion ``random.shuffle`` und beschreiben Sie anhand der Dokumentation das **Was** dieser Funktion.
```

```{solution} documentation-exercise
:label: documentation-solution
:class: dropdown

Diese Funktion mischt eine gegebene Sequenz.
Die übergebene Sequenz ``x`` wird dadurch verändert (durchgemischt).

```