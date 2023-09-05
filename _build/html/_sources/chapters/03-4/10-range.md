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

(sec-range)=
# Zahlenbereich - range

Ein *Zahlenbereich* oder kurz *Bereich* (engl. [Range](https://docs.python.org/3/library/stdtypes.html#typesseq-range)) ``range`` ist eine **unveränderliche** *faule* (engl. *lazy*) [Sequenzen](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) von **ganzen Zahlen**.

In ``Python`` verwenden wir diese *Bereiche*, wenn wir einen bestimmten Programmcode eine bekannte und feste Anzahl an Durchläufen mithilfe der ``for``-Schleife durchlaufen wollen.
*Faul* (engl. *lazy*) bedeutet, dass Werte erst dann erzeugt werden, wenn Sie gebraucht werden.
Der Aufruf ``range(10)`` erzeugt einen *Zahlenbereich*, welcher die Zahlen $0, 1, \ldots 9$ enthält.
Doch anders als eine Liste, liegen die ganzen Zahlen noch nicht im Speicher.
Sie werden beim Zugriff auf den jeweiligen *Zahlenbereich* **berechnet**.

Die Eigenschaft der *Faulheit* wurde mit **Python 3** eingeführt.

## Erstellung

Einen *Zahlenbereich* erstellen wir entweder mit ``range(stop)``, ``range(start, stop)`` oder ``range(start, stop, step)``.
Alle Argumente müssen ganze Zahlen sein. Vergleichen Sie

```{code-cell} python3
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))
```

Auch negative ganze Zahlen sind möglich, hiermit können wir eine absteigende Sequenz erzeugen:

```{code-cell} python3
print(list(range(-10)))     # start = 0 und stop = -10, thus empty range
print(list(range(-10, -5)))
print(list(range(-5, 5, 2)))
```

## Indexierung

*Zahlenbereich* können, wie [Listen](sec-list-index), indexiert werden.

```{code-cell} python3
myrange = range(10)
print(myrange[0])
print(myrange[1])
```

Indexieren wir mehr als einen Wert eines Zahlenbereichs, so wird ein neuer entsprechender Zahlenbereichs erzeugt:

```{code-cell} python3
myrange = range(10)
print(myrange[2::3])
print(myrange[-1:2:-2])
```

Der obige Code erzeugt lediglich neue *lazy* Bereiche, doch die ganzen Zahlen werden nicht in den Speicher gelegt.
Wandeln wir Bereiche in eine Liste um, so werden deren ganze Zahlen in den Speicher abgelegt.

```{code-cell} python3
myrange = range(10)
print(list(myrange[2::3]))
print(list(myrange[-1:2:-2]))
```