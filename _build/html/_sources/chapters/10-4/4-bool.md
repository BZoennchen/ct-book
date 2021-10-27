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

# Wahrheitswerte - bool

Ein Wahrheitswert ``bool`` kann, genau wie ein [Bit](def-bit) einen von zwei Wahrheitswerten ``True`` (1) oder ``False`` (0) annehmen.
``True`` bedeutet wahr und ``False`` falsch.
Sehr selten verwenden wir explizit ``True`` oder ``False`` vielmehr wird ein logischer Ausdruck, nach *Auswertung* entweder ``True`` oder ``False`` ist.

```{code-cell} python3
x = 9
is_lesser_than_10 = x < 10
print(is_lesser_than_10)
```

In diesem Beispiel verwenden wir einen [Vergleichsoperator](sec-python-operator-compare), der den Ausdruck $x < 10$ zu ``True`` auswertet, da $x = 9 < 10$ gilt.
*Boolsche* bzw. *logische Ausdrücke* lassen sich durch [logische Operatoren](sec-logic-expressions) verknüpfen.

*Boolsche Ausdrücke* und damit Wahrheitswerte ``bool`` benötigen wir für die Steuerung unseres Programmablaufs.
*Kontrollstrukturen* führen, je nach Auswertung eines *boolschen Ausdrucks*, unterschiedliche Code-Teile aus.

```{code-cell} python3
for x in range(11):
  if x < 10:      # is True if and only if x < 10
    print(f'{x} is less than 10')
  else:
    print(f'{x} not is less than 10')
```
