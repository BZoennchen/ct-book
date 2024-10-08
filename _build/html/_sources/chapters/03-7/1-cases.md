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

(sec-cases)=
# Fallunterscheidungen

Für eine Fallunterscheidung können wir für jeden Fall $i$ einen bestimmten Codeblock $B_i$ definieren.
Dieser wird genau dann ausgeführt sofern ein logischer Ausdruck $P_i$ wahr, d.h. ``True`` ergibt und kein anderer logischer Ausdruck $P_j$ für $j < i$ bereits ``True`` ergeben hat.
In anderen Worten, der Fall $i$ trifft zu und kein Fall davor ist bereits eingetreten.

Damit führt eine Fallunterscheidung zur Ausführung von **höchstens** einer der Codeblöcke $B_0, \ldots, B_n$.
Trifft keiner der Fälle zu, d.h. kein $P_i$ ergibt ``True`` und es ist kein Alternativfall (``else``) definiert, so wird keiner der Codeblöcke ausgeführt.
Eine Fallunterscheidung beginnt immer mit dem ``if``-Signalwort!

## ``if``

Die einfachste Form der Fallunterscheidung prüft ob ein logischer Ausdruck $P_0$ eingetreten.
Nur wenn dies zutrifft, wird der Codeblock $B_0$ ausgeführt:

```python
if P0:
    B0
```

```{code-cell} python3
x = 2

if x <= 2:
    x += 1
    print(f'x: {x}')
```

## ``if``-``else``

In der nächsten Variante wird ein Codeblock $B_0$ nur dann ausgeführt, sofern ein logischer Ausdruck $P_0$ ``True`` ergibt.
Ist dies nicht der Fall, so wird ein Alternativblock (``else``) $B_1$ ausgeführt.

```python
if P0:
    B0
else:
    B1
```

```{code-cell} python3
x = 2

if x <= 2:
    x += 1
    print(f'x: {x}')
else:
    print(f'x > 2')
print(x)
```

## ``if``-``elif``

In der nächsten Variante wird höchstens ein Codeblock $B_i$ nur dann ausgeführt, sofern ein logischer Ausdruck $P_i$ ``True`` ergibt.
Gibt es mehr als einen logischen Ausdruck $P_i$ welcher ``True`` ergibt, so wird der erste Codeblock (der mit dem kleinsten $i$) ausgeführt.

```python
if P0:
    B0
elif P1:
    B1
elif P2
    B2
...
```

```{code-cell} python3
x = 2

if x <= 2:
    print(f'x <= 2')
    x += 1
elif x <= 5:
    print(f'x <= 5')
    x += 2
elif x <= 6:
    print(f'x <= 4')
    x += 6
print(x)
```

## ``if``-``elif``-``else``

In der nächsten Variante wird genau ein Codeblock $B_i$ nur dann ausgeführt, sofern ein logischer Ausdruck $P_i$ ``True`` ergibt. Gibt es mehr als einen logischen Ausdruck $P_i$ welcher ``True`` ergibt, so wird der erste Codeblock (der mit dem kleinsten $i$) ausgeführt.
Trifft kein Fall zu, wird der Alternativblock $B_n$ ausgeführt.

```python
if P0:
    B0
elif P1:
    B1
elif P2
    B2
...
else:
    Bn
```

```{code-cell} python3
x = 2

if x <= 2:
    print(f'x <= 2')
    x += 1
elif x <= 5:
    print(f'x <= 5')
    x += 2
elif x <= 7:
    print(f'x <= 7')
    x += 10
else:
    print(f'x > 2 and x > 5 and x > 7')
    x = 2   
print(x)
```

## ``if``-``if``-``else``

Aufeinanderfolgende ``if``-Statements sind nicht eine sondern mehrere Fallunterscheidungen, denn jedes ``if``-Statement leitet eine neue Fallunterscheidung ein!

```{code-cell} python3
x = 2

if x <= 2:
    print(f'x <= 2')
    x += 1
if x <= 5:
    print(f'x <= 5')
    x += 2
if x <= 7:
    print(f'x <= 7')
    x += 10
else:
    print(f'x > 2 and x > 5 and x > 7')
    x = 2   
print(x)
```

```{admonition} Aufeinander folgende Fallunterscheidungen
:class: remark
:name: remark-multi-cases
Es ist zu empfehlen aufeinanderfolgende ``if``-Statements durch eine Leerzeile zu trennen.
```

```{code-cell} python3
x = 2

if x <= 2:
    print(f'x <= 2')
    x += 1
    
if x <= 5:
    print(f'x <= 5')
    x += 2
    
if x <= 7:
    print(f'x <= 7')
    x += 10
else:
    print(f'x > 2 and x > 5 and x > 7')
    x = 2   
print(x)
```

## Verschachtelung

Selbstverständlich kann ein Codeblock $B_i$ erneut eine oder mehrere Fallunterscheidungen enthalten.
Und selbstverständlich können wir Fallunterscheidungen in Funktionen einbauen.

```{code-cell} python3
def nested_branching(x, y):
    if x > 2:
        if y < 2:
            out = x + y
        else:
            out = x - y
    else:
        if y > 2:
            out = x * y
        else:
            out = 0
    return out

print(nested_branching(3, 1))
print(nested_branching(3, 2))
print(nested_branching(1, 3))
print(nested_branching(1, 1))
```

Wir können häufig verschachtelte Fallunterscheidungen auflösen. Zum Beispiel können wir die Funktion auch wie folgt definieren:

```{code-cell} python3
def nested_branching(x, y):
    if x > 2 and y < 2:
        out = x + y
    elif x > 2:
        out = x - y
    elif x <= 2 and y > 2:
        out = x * y
    else:
        out = 0
    return out

print(nested_branching(3, 1))
print(nested_branching(3, 2))
print(nested_branching(1, 3))
print(nested_branching(1, 1))
```

Es ist eine Frage der **Lesbarkeit**, welche Variante besser ist. 
In der zweiten Version haben wir zwar eine niedrigere Verschachtellung, allerdings sehen wir nicht sofort, dass die ersten Fälle 

```python
if x > 2 and y < 2:
        out = x + y
elif x > 2:
    out = x - y
...
```

und die beiden letzten Teile

```python
...
elif x <= 2 and y > 2:
    out = x * y
else:
    out = 0
```

eine Entweder-Oder-Beziehung besitzen. 
Zudem haben wir zweimal den logischen Ausdruck ``x > 2``.

Einen Block der Art:

```python
if P0:
    if P1:
        if P2:
            if P3:
                ...
```

lässt sich immer in 

```python
if P0 and P1 and P2 and P3 ...:
```

umwandeln.

## Schnellschreibweise

``Python`` erlaubt es uns einen Ausdruck der Form

```python
if P0:
    x = A0
else:
    x = A1
```

als 

```python
x = A0 if P0 else A1
````

zu schreiben.

```{code-cell} python3
y = 12
x = 0 if y % 2 == 0 else 1
x
```

Diese Schreibweise lässt sich gut mit sog. [Comprehension](sec-comprehension) verbinden:

```{code-cell} python3
numbers = list(range(10))
even = [True if x % 2 == 0 else False for x in numbers]
print(f'numbers: {numbers}')
print(f'even: {even}')
```

## Beispiel (quadratische Gleichungen)

Sei $f(x) = ax^2 + bx + c$ mit konstanten Zahlen $a, b, c \in \mathbb{R}$. Wir wissen, dass $f(x) = 0$ für

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

sofern $b^2 - 4ac >= 0$.
Lassen Sie uns eine Funktion ``solve_quadratic(a, b, c)`` entwerfen, welche uns alle $x_{1,2}$ berechnet. 
Es gibt eine, zwei oder keine Lösung.

Lassen Sie uns als erstes eine Funktion entwerfen, die testet ob eine Fließkommazahl annähernd gleich null ist.
Beachten Sie: [Fließkommazahlen](sec-float) sind lediglich eine Annäherung des echten Wertes und damit ist der exakte Vergleich ``==`` ungeeignet.
Stattdessen ist unsere Fließkommazahl ``x`` gleich null, falls sie annähernd gleich null ist.

```{code-cell} python3
def is_zero(x):
    epsilon = 1.0e-12
    return -epsilon < x < 1.0e-12
```

Lassen Sie uns nun die quadratische Gleichung lösen.
Dazu müssen wir lediglich die Formel für $x_{1,2}$ implementieren:

```{code-cell} python3
def solve_quadratic(a, b, c):    
    disc = b**2 - (4*a*c)
            
    # disc < 0 => no solution
    if disc < 0:
        return ()
    
    # disc == 0? => one solution
    if is_zero(disc):
        return -b / (2*a),
    
    # default case => 2 solutions
    return (-b + disc**0.5) / (2*a), (-b - disc**0.5) / (2*a)
```

Der Code scheint zur richtigen Lösung zu führen:

```{code-cell} python3
print(f'solution for x^2 -4x + 1 = 0: {solve_quadratic(1, -4, 1)}')
print(f'solution for x^2 + x = 0: {solve_quadratic(1, 1, 0)}')
print(f'solution for x^2 = 0: {solve_quadratic(1, 0, 0)}')
```

Was passiert allerdings wenn ``a==0`` ist?

```{code-cell} python3
---
tags: [raises-exception]
---
print(f'solution for -4x + 1 = 0: {solve_quadratic(0, -4, 1)}')
```

In diesem Fall teilen wir durch null und erhalten (zum Glück) einen Fehler.
Sofern ``a==0`` gilt müssen wir die lineare Gleichung 

$$bx + c = 0 \Rightarrow x = c/b$$

lösen.
Hier wartet ein weiterer Sonderfall für ``b==0``!
In diesem Fall gibt es kein Ergebnis sofern ``c != 0``, andernfalls gibt es unendlich viele Lösungen.
Nutzen wir die Fallunterscheidung um all diese Sonderfälle abzudecken:

```{code-cell} python3
def solve_quadratic(a, b, c):
    """"
    solves the quadratic equation ax^2 + bx + c = 0.
    a == b == c == 0 is not allowed!
    """
    
    disc = b**2 - (4*a*c)
    epsilon = 1.0e-12
    
    # a == 0? => line => one or none solution
    if is_zero(a):
        # b == 0? 
        if is_zero(b):
            # c == 0 => infinitely many solutions
            if is_zero(c):
                raise AttributeError('Invalid arguments a == b == c == 0! This quadratic equation has infinitely many solutions.')
            else:
                return ()
        else:
            return -c/b,
        
    # disc < 0 => no solution
    if disc < 0:
        return ()
    
    # disc == 0? => one solution
    if is_zero(disc):
        return -b / (2*a),
    
    # default case => 2 solutions
    return (-b + disc**0.5) / (2*a), (-b - disc**0.5) / (2*a)
```

```{code-cell} python3
print(f'solution for x^2 -4x + 1 = 0: {solve_quadratic(1, -4, 1)}')
print(f'solution for x^2 + x = 0: {solve_quadratic(1, 1, 0)}')
print(f'solution for x^2 = 0: {solve_quadratic(1, 0, 0)}')
print(f'solution for -4x + 1 = 0: {solve_quadratic(0, -4, 1)}')
print(f'solution for 1 = 0: {solve_quadratic(0, 0, 1)}')
```

Gilt ``a == b == c == 0`` wird unsere Funktion zu $f(x) = 0$ und demnach gilt für jedes $x_0 \in \mathbb{R}$ dass es eine Nullstelle ist.
Das wären unendlich viele Zahlen, deshalb werfen wir (``raise``) in diesem Fall einen Fehler.

```{code-cell} python3
---
tags: [raises-exception]
---
print(f'solution for 0 = 0: {solve_quadratic(0, 0, 0)}')
```

