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

# Operationen

## Betrag

Die Betragsfunktion $|\cdot| : \mathbb{R} \rightarrow \mathbb{R}^+$ wandelt eine negative Zahl in eine positive Zahl um.

```{admonition} Betragsfunktion
:name: def-math-abs
:class: definition

Sei $x \in \mathbb{R}$ eine reelle Zahl, so ist ihr *Betrag* definiert als

$$|x| = \begin{cases} -x, & \text{ falls } x < 0 \\ x, & \text{ sonst.} \end{cases}$$
```

```{code-cell} python3
abs(-10)
```

## Max- und Minimum

```{admonition} Maximum
:name: def-math-max
:class: definition

Für eine nicht leere Menge $M \subset \mathbb{R}$ ist das *Maximum* $\max M$ definiert als

$$\max M = x \text{ sodass } x \in M \text{ und } \forall y \in M : x \geq y$$
```

```{code-cell} python3
M = {1,2,3,4,5}
max(M)
```

```{admonition} Maximum
:name: def-math-min
:class: definition

Für eine nicht leere Menge $M \subset \mathbb{R}$ ist das *Minimum* $\min M$ definiert als

$$\min M = x \text{ sodass } x \in M \text{ und } \forall y \in M : x \leq y.$$
```

```{code-cell} python3
M = {1,2,3,4,5}
min(M)
```

## Ab- und Aufrunden

Bei der Entwicklung Ihrer Algorithmen werden sie das *Abrunden* sehr oft einsetzten.
Es wird in allen gängigen Programmiersprachen implizit durchgeführt, wenn Sie eine Gleitkommazahl in eine ganze Zahl umwandeln.

```{code-cell} python3
import math
print(int(1.49))
print(math.floor(1.49))
```

Diese Abrundungsfunktion $\left \lfloor{\cdot}\right \rfloor : \mathbb{R} \rightarrow \mathbb{Z}$ rundet Zahlen zur nächst größeren ganzen Zahl auf. 

```{admonition} Maximum
:name: def-math-floor
:class: definition

Sei $x \in \mathbb{R}$ so ist $x$ aufgerundet gleich

$$\left \lfloor{x}\right \rfloor = \max\{k \in \mathbb{Z} : k \leq x \}.$$
```

Diese Aufrundungsfunktion $\left \lceil{\cdot}\right \rceil : \mathbb{R} \rightarrow \mathbb{Z}$ rundet Zahlen zur nächst kleineren ganzen Zahl ab. 

```{admonition} Maximum
:name: def-math-ceil
:class: definition

Sei $x \in \mathbb{R}$ so ist $x$ abgerundet gleich

$$\left \lceil{x}\right \rceil = \min\{k \in \mathbb{Z} : k \geq x \}.$$
```

```{code-cell} python3
import math
print(math.ceil(1.49))
print(math.ceil(-1.49))
```

## Die Restwertdivision

```{admonition} Restwert
:name: def-euclid-division
:class: definition

Für zwei ganze Zahlen $n, m \in \mathbb{Z}$, $m \neq 0$ gibt es zwei eindeutige ganze Zahlen $a, r \in \mathbb{Z}$, sodass

$$
n = m \cdot a + r, \quad 0 \leq r < |m|.
$$

Wir nennen $r$ den *Rest*.
```

Seien $n, m$ gegeben so lassen sich $a$ durch die Division und das Abrunden ermitteln.

$$a = \left \lfloor{ n / m}\right \rfloor$$

und damit lässt sich der *Rest* $r$ bestimmen

$$r = n - a \cdot m.$$

Zum Beispiel gilt für $n = 13$, $m = 5$: 

\begin{gather*} 
a = \left \lfloor{13/5}\right \rfloor = 2\\
r = 13 - 2 \cdot 5 = 3.
\end{gather*}


Die *Restwertdivision* wird von allem gängigen Programmiersprachen durch den ``%`` Operator unterstützt und ist für Computer relativ günstig zu berechnen.
Mithilfe dieser Operation können wir zum Beispiel feststellen ob eine ganze Zahl gerade oder ungerade ist.
Das ist genau dann der Fall wenn der Rest $r$ der Restwertdivision mit 2 gleich null ist.

```{code-cell} python3
print(5 % 2 == 0)
print(13 % 5)
```