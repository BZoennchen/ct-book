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

(sec-anonymous-function)=
# Anonyme Funktionen

*Anonyme Funktionen* sind **namenlose** Funktionen.
Nehmen wir folgende Funktion mit dem Namen ``add``:

```{code-cell} python3
def add(x, y):
    return x + y
```

Diese Funktion können wir über ihren Namen ansprechen:

```{code-cell} python3
add(4, 6)
```

Der Name befindet sich im [globalen Namensraum](sec-global-namespace) und verweist auf den Code der die Funktion realisiert.
Wir können einen Verweis auf die Funktion auch in einer Variablen abspeichern, dazu verwenden wir lediglich den Namen der Funktion:

```{code-cell} python3
func = add
func(4, 6)
```

Eine *anonyme Funktion* erlaubt uns dies ebenfalls.

```{code-cell} python3
func = lambda x, y : x + y
func(4, 6)
```

In ``Python`` sind *anonyme Funktionen* zugleich *kleine Funktionen*.

Mit dem Signalwort ``lambda`` beginnt die Definition einer *anonyme Funktion*.
Nach ``lambda`` folgen die Parameter und nach dem ``:`` der Funktionsrumpf.
Die gesamte Funktionsdefinition muss dabei in eine Zeile passen.
Es darf sich beim Funktionsrumpf nur im **einen** Ausdruck handeln.
Der Rückgabewert ist automatisch der ausgewertete Ausdruck hinter dem ``:``.

Bei dieser enormen Einschränkung stellt sich die Frage, wann verwenden wir *anonyme Funktionen*?
Anonyme Funktionen werden oft benutzt wenn die Logik der Funktion sehr einfach ist und wir Funktionen als Argumente verwenden um das Verhalten anderer Funktionen zu verändern.
Oder aber wenn Funktionen andere Funktionen zurückliefern.

Diese *anonyme Funktionen* können, wenn sie vernünftig eingesetzt werden, unseren Code verkürzen und die Lesbarkeit erhöhen sowie unserer Produktivität steigern.

Nehmen wir eine Liste von ganzen Zahlen.
Und sagen wir, wir wollen eine neue Liste erzeugen, welche die Quadrate all dieser Zahlen enthält.
Die *built-in* Funktion ``map(func, iterable)`` transformiert ``iterable`` indem es die Funktion ``func`` auf jedem Element von ``iterable`` ausführt.

```{code-cell} python3
numbers = list(range(10))
def square(x):
    return x * x

list(map(square, numbers))
```

Nach diesem Aufruf brauchen wir ``square()`` vermutlich nie wieder, zudem ist die Funktion so simpel, dass eine vollwertige Definition übertrieben scheint.
Kürzer geht das ganze mit einer *anonymen Funktion*:

```{code-cell} python3
numbers = list(range(10))
list(map(lambda x: x * x, numbers))
```

Erwartet eine Funktion eine andere Funktion, so ist es oft sinnvoll ein Standardarguments als *anonyme Funktion* festzulegen, da wir ihn nur an dieser Stelle brauchen:

```{code-cell} python3
def apply(mylist, func = lambda e : e):
    return list(map(func, numbers))

numbers = list(range(10))
print(apply(numbers))
print(apply(numbers, lambda x: 2*x+1))
```

Ein weiterer Fall für den sich eine *anonyme Funktion* eignen kann ist, wenn wir bestimmte Parameter fixieren wollen.
Das bedeutet wir haben eine Funktion mit $n$ Parametern und wir möchten daraus eine neue Funktion mit $m < n$ Parametern bauen und dabei $n-m$ Parameter fixieren.
Zum Beispiel:

```{code-cell} python3
def f(a, b, c, d):
    return (2 * a + b**2 - 3*c) / d

# fix a and d
h = lambda b, c: f(4, b, c, 9)

h(3, 1)
```

So können wir aus einer allgemeineren Funktion eine speziellere Funktion mit weniger Freiheitsgraden bauen.