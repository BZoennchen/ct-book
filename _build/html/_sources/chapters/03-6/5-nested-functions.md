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

# Umschlossene Funktionen

Eine *umschlossene Funktion* ist eine Funktion, welche innerhalb einer anderen Funktion definiert wurde.

```{code-cell} python3
def f(x, y):
    z = 5
    def square(x):
        return x * x
    return square(z) + square(x) + 2 * y

f(5, 6)
```

Sie werden vermutlich nur selten in die Verlegenheit kommen eine *umschlossene Funktion* zu verwenden.
Dennoch, in manchen Fällen kann dies sinnvoll sein um zum Beispiel doppelten Code zu reduzieren.

Spezieller wird es, wenn wir diese *umschlossene Funktion* zurückgeben und nach der Abarbeitung der *umschließenden Funktion* weiter verwenden:

```{code-cell} python3
def f(x, y):
    z = 5
    def h(x):
        return x * x * z
    return h

func = f(5, 6)
func(3)
```

Zu beachten ist, dass dabei der sog. [umschließende Namensraum](sec-local-namespace) ins Spiel kommt.
Dieser bleibt auch dann am Leben, wenn die *umschließende Funktion* abgearbeitet wurde.

Im obigen Fall existiert das ``z`` aus der Funktion ``f()`` beim Aufruf ``func(3)`` noch und hat den Wert ``5``.
Der Aufruf ``func(3)`` wird zu ``h(3)`` und dies wird zu ``3 * 3 * 5`` ausgewertet.