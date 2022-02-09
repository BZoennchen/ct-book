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

(sec-comprehension)=
# Comprehensions

Eine Comprehension ist eine Art von ``Python``-[Syntax](def-syntax), die es uns durch eine sehr kompakte Schreibweise erlaubt aus einer Datenstruktur eine andere Datenstruktur zu erstellen.

## List-Comprehensions

Ein Beispiel:

```{code-cell} python3
numbers = list(range(10))
squares = [x*x for x in numbers]

print(f'numbers: {numbers}')
print(f'squares: {squares}')
```

Wir erzeugen erst eine Liste ``numbers`` und transformieren diese in eine neue Liste aus Quadratzahlen.
Dieser Code wird durch den ``Python``-[Interpreter](def-interpreter) in folgenden Code übersetzt:

```{code-cell} python3
numbers = list(range(10))
squares = []

for x in numbers:
    squares.append(x*x)

print(f'numbers: {numbers}')
print(f'squares: {squares}')
```

``x*x`` ist eine [anonyme Funktion](sec-anonymous-function) in Kurzschreibweise.
Wir können dies explizit verdeutlichen:

```{code-cell} python3
def square(x):
    return x*x

numbers = list(range(10))
squares = [square(x) for x in numbers]

print(f'numbers: {numbers}')
print(f'squares: {squares}')
```

Wir können die Liste der Elemente der Ursprungsliste auch durch eine Fallunterscheidung filter:

```{code-cell} python3
def square(x):
    return x*x

numbers = list(range(10))
odd_squares = [square(x) for x in numbers if x % 2 == 1]

print(f'numbers: {numbers}')
print(f'squares: {odd_squares}')
```

Wir können auch mehrere Sequenzen kombinieren.
Folgender Code 

```{code-cell} python3
numbers = [i + j for i in range(5) for j in range(2)]
print(f'numbers: {numbers}')
```

entspricht

```{code-cell} python3
numbers =[]
for i in range(5):
    for j in range(2):
        numbers.append(i + j)
print(f'numbers: {numbers}')
```

Lassen Sie uns damit eine Matrix $A$ mit

$$
A = \begin{pmatrix}
    0+0 & 0+1 & 0+2 & \ldots & 0+(n-1)\\
    1+0 & 1+1 & 1+2 & \ldots & 1+(n-1)\\
    \vdots & \vdots & \vdots & \vdots\\
    (m-1) + 0 & (m-1) + 1 & (m-1) + 2 & \ldots & (m-1)+(n-1)
\end{pmatrix}
$$

als Liste von Listen generieren:

```{code-cell} python3
n = 3
m = 4
A = [[(i+j) for i in range(m)] for j in range(m)]
print(f'Matrix A: {A}')
```

## Dictionary-Comprehensions

Sehr ähnlich lässt sich diese Schreibweise für [Wörterbücher](sec-dict) einsetzten.

```{code-cell} python3
x = {'a': 1, 'b': 2, 'c': 3}

{key:v**3 for (key, v) in x.items()}
```

## Set-Comprehensions

Und auch für [Mengen](sec-set) können wir Comprehensions verwenden.

```{code-cell} python3
numbers = {1,2,3,4}

{x*x for x in numbers}
```