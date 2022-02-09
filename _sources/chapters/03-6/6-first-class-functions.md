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

(sec-first-class-functions)=
# First-Class-Funktion

Wie in ``JavaScript``, so sind Funktionen in ``Python`` ebenfalls First-Class-Funktionen (Funktionen erster Klasse).
Das bedeutet im Wesentlichen, dass es keinen Unterschied mit dem Umgang zwischen Funktionen und Daten gibt.

```{code-cell} python3
def f(x, y):
    return 2*x + y
```

Wir können einer Variable eine Zahl wie auch eine Funktion zuweisen.

```{code-cell} python3
variable = f
variable(3, 2)
```

Wir können Funktionen in *Datenstrukturen* packen.

```{code-cell} python3
functions = [f, f, max, min]
for func in functions:
    print(func(5, -6))
```

Wir können Funktionen als Argumente übergeben und als Funktionswerte zurückgeben.

```{code-cell} python3
def h(x, func):
    return func(3, x) + x

h(10, f)
```

Doch richtig fällt uns der Unterschied erst auf, wenn wir eine Sprache betrachten, für die Funktionen keine *First-Class-Funktionen* sind.
Beispiele wären ``Java``, ``C/C++``, und viele mehr.
Es hat sich gezeigt, dass *First-Class-Funktionen* eine wertvolle Spracheigenschaft ist und Sprachen wie ``Java`` versuchen diese durch syntaktische Tricks zu simulieren.

In ``Java`` können wir mittlerweile Funktionen ähnlich wie *First-Class-Funktionen* behandeln.
Ein Beispiel:

```java
Function<Integer> func = (x) -> x * x;
func(5);
```

Hierbei ist

```java
(x) -> x * x
```

eine [anonymen Funktion](sec-anonymous-function) die wir scheinbar einer Variablen ``func`` zuweisen.
Doch im Hintergrund wird ein ganzes Objekt (Daten + Funktionen) erstellt, welches keine Daten und nur eine Funktion enthält.

Sind Funktionen First-Class-Funktionen, so ist man als Programmierer\*in eher dazu ermuntert mehr in Funktionen als in Objekten und Methoden zu denken.