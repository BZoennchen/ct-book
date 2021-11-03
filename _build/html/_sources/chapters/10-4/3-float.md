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

# Fließkommazahlen - float

Zunächst ist zu sagen, dass Sie für Fließkommazahlen (engl. [Floating Point Number](https://docs.python.org/3/library/functions.html#float)) nicht das Komma ``,`` sondern den englischsprachigen Punkt ``.`` verwenden.

Im Gegensatz zu ganzen Zahlen benötigen Fließkommazahlen immer die gleiche Anzahl an Bits.
Da stellt sich die Frage: Wie ist es unter diesen Bedingungen möglich Zahlen darzustellen, deren absoluter Wert sehr verschieden ist?
Zum Beispiel können wir problemlos die Zahl $0.0000000001$ und die Zahl $10000000.0$ als Fließkommazahl definieren:

```{code-cell} python3
small_float = 0.0000000001
large_float = 10000000.0
print(small_float)
print(large_float)
```

``1e-10`` bedeutet hierbei $1.0 \cdot 10^{-10}$ und diese Darstellung liefert uns bereits Hinweise auf die Antwort.

Physiker\*innen kennen das Problem der Zahlen aus sehr unterschiedlichen Skalen.
Die Lichtgeschwindigkeit in km/h ist eine sehr große Zahl, wohingegen die Ladung eines Elektrons in Coulomb eine sehr kleine Zahl ist.
Physiker\*innen möchten ebenfalls in einem riesigen Zahlenbereich rechnen und dabei Zahlen kompakt notieren können.
Deshalb haben sie die wissenschaftliche Notation eingeführt.
Fließkommazahlen sind aus dieser Notation entstanden.
In dieser Notation schreiben wir $10000000.0$ als $0.1 \cdot 10^8$ und aus $0.0000000001$ wird $0.1 \cdot 10^{-9}$.

Ohne zu sehr ins Detail zu gehen, besteht eine Fließkommazahl ``float`` aus Bits für die einzelnen Teile dieser Schreibweise:

+ das *Vorzeichen*, 
+ die *Mantisse* und 
+ den Exponenten.

Für $0.1 \cdot 10^8$ wäre das *Vorzeichen* gleich +, die *Mantisse* gleich 0.1 und der *Exponent* gleich 8.

Da der Computer jedoch im Binärsystem rechnet, verwendet er als Basis die 2 anstatt die 10.
Nehmen wir die Zahl 

$$0.875_{10} = 8 \cdot 10^{-1} + 7 \cdot 10^{-2} + 5 \cdot 10^{-3}.$$

Binär können wir die Zahl wie folgt ausdrücken:

$$0.111_2 = 1 \cdot 2^{-1} + 1 \cdot 2^{-2} + 1 \cdot 2^{-3}.$$

Soweit so gut.
Was passiert aber wenn jede Ziffer von 0 verschieden ist und sich endlos fortsetzt z.B. $\pi = 3.14159265359 \ldots$ oder auch $1/3 = 0.33333333333 \ldots$?
In diesem Fall wird die Zahl abgeschnitten sobald keine Bits mehr zur Verfügung stehen.
Demnach ist eine Fließkommazahl immer nur eine gute **Annäherung** des echten Werts!!!

Weshalb folgende Rechnung nicht 0.3 ergibt, erklärt sich durch diese **Annäherung** in Kombination mit der Binärdarstellung!

```{code-cell} python3
0.2 + 0.1
```

Denn es gilt:

$$0.1_{10} = 0.0001100110011 \ldots_2.$$

```{admonition} Ungenauigkeit der Fließkommazahlen
:class: important
Fließkommazahlen ``float`` sind eine gute *Annäherung* des echten Werts.
```

Dieses Verhalten kann nicht nur zu kleinen Ungenauigkeiten, sondern zu großen Fehlern führen.
Folgender Code subtrahiert 20 mal $1.0 \cdot 10^{-14}$ von $1.0 \cdot 10^{10}$.
Doch verändern diese Subtraktionen ``x`` nicht.

```{code-cell} python3
x = 1e10
epsilon = 1e-14

print(f'epsilon = {epsilon}')
print(f'x = {x} before subtraction')

for i in range(20):
  x = x - epsilon

print(f'x = {x} after subtraction')
```

Das zeigt, dass der (akkumulierte) Fehler theoretisch unendlich groß werden kann.
Besonders kritisch ist die Subtraktion und Addition von Zahlen die in sehr unterschiedliche Skalen fallen.
Die Multiplikation und Division ist für Fließkommazahlen sehr viel ungefährlicher.

```{code-cell} python3
x = 1e10
epsilon = 1e-14

print(f'epsilon = {epsilon}')
print(f'x = {x} before multiplication')
x = x * epsilon
print(f'x = {x} after multiplication')
```

Obiger Code liefert das korrekte Ergebnis von: 

$$(1.0 \cdot 10^{10}) \cdot (1.0 \cdot 10^{-14}) = 1.0 \cdot 10^{10-14} = 1.0 \cdot 10^{-4} = 0.0001.$$

```{admonition} Ungenauigkeit der Fließkommazahlen
:class: warning
Prüfen Sie Fließkommazahlen niemals auf Gleichheit ``==``.
Verwenden Sie stattdessen immer einen kleinen Bereich in dem die Zahl liegen sollte.
```
