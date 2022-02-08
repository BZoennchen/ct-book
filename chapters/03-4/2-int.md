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

(sec-int)=
# Ganze Zahlen - int

Der Datentyp, welcher ganze Zahlen repräsentiert ``int`` (engl. [Integer](https://docs.python.org/3/library/functions.html#int)) ist ein [atomarer Datentyp](def-atomare-data-types) und verhält sich so wie wir es erwarten.

Falls Sie jedoch bereits Programmierkenntnisse besitzen, so gibt es für Sie in ``Python`` eine Besonderheit:

```{admonition} Fehlender Überlauf
:name: remark-int-overflow
:class: remark

In ``Python`` gibt es **keinen** Überlauf für ganze Zahlen ``int``.
```

Anders als Fließkommazahlen benötigen ganze Zahlen ``int`` in ``Python`` eine variable Anzahl an Bits.
Anders ausgedrückt: Nicht jede Zahl benötigt die gleiche Anzahl an Bits im Speicher!
Solange Ihr Speicher nicht komplett belegt ist, können Sie in ``Python`` somit mit sehr großen ganzen Zahlen rechnen.

```{code-cell} python3
large_number = 10**100 
print(type(large_number))
print(large_number)
```

Da wir bei mathematischen Operationen wie ``+``, ``-``, ``*``, ``/``, ``//`` und ``**`` ganze Zahlen ``int`` und Fließkommazahlen ``float`` vermischen können, müssen wir darauf achten welcher Datentyp am Ende herauskommt.
Sobald eine Fließkommazahl ein Teil der Berechnung ist, ist das Ergebnis vom Typ ``float``.

```{code-cell} python3
x = 3 * 1.0     # int * float -> float   
print(type(x))
print(x)
```

```{code-cell} python3
large_number = 10.0**100     # float ** int -> float  
print(type(large_number))
print(large_number)
```

Auch für die ganzzahligen Division ``//`` erhalten wir als Datentyp eine Fließkommazahl sofern eine Fließkommazahl bei der Operation teilnimmt:

```{code-cell} python3
x = 3.0 // 2     # float // int -> float   
print(type(x))
print(x)
```

```{code-cell} python3
x = 3 // 2.0     # int // float -> float   
print(type(x))
print(x)
```

```{code-cell} python3
x = 3 // 2     # int // int -> int   
print(type(x))
print(x)
```