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

(sec-imperativ-and-functional)=
# Imperativ und funktional

Funktionale Programmiersprachen bieten hohe Sicherheit indem sie sogenannte *Seiteneffekte* nicht erlauben und anstatt Variablen (abänderbar/mutable) nur Konstanten (unabänderlich/immutable) zulassen.

```{admonition} Seiteneffekt
:name: def-side-effect
:class: definition
Übergeben Sie eine Variable oder eine Datenstruktur einer Funktion und verändert diese Funktion jene Variable oder Datenstruktur, dann sprechen wir von einem *Seiteneffekt*.
```

In imperativen Programmiersprachen (``Python``, ``Java``, ``C#``, ``C++``, ``C``, ``JavaScript``, ...) sind *Seiteneffekte* manchmal erwünscht und auch notwendig.
Folgender Code zeigt einen Seiteneffekt in ``Python``.

```{code-cell} python3
y = []
def sideeffect(x):
    x += [1,2,3]
    return x

print(y)
print(sideeffect(y))
print(y)
```

Die Liste ``y`` (Datenstruktur) wird durch die Funktion ``sideeffect`` befüllt.

Dies ist in der funktionalen Programmiersprache ``Haskell`` nicht möglich!
Wir können den obigen *Seiteneffekt* in ``Python`` wie folgt auflösen.

```{code-cell} python3
y = [-10]
def no_sideeffect(x):
    x = x + [1,2,3]
    return x

print(y)
print(no_sideeffect(y))
print(y)
```

In diesem Fall bleibt ``y`` unberührt, stattdessen wird eine neue Liste (eine Kopie) von ``y``) befüllt.

Funktionale Sprachen umgehen *Seiteneffekte* indem sie keine Datenstrukturen ändern, sondern stattdessen neu erzeugen.
Fügt man ein neues Element in eine Liste an, entsteht eine komplett neue Liste.
Funktionale Sprachen verzichten auf Variablen und realisieren Operationen durch Konstanten und sog. *Pure Functions* (mathematische Funktionen).

```{admonition} Reine Funktion (pure Function)
:name: def-pure-function
:class: definition

Eine Funktion nennen wir *reine Funktion* wenn
1. Der Rückgabewert der Funktion für die gleiche Funktionsargumente stets identisch ist.
2. Wenn die Funktion keine *Seiteneffekte* hat.
```

*Reine Funktionen* verhalten sich deshalb wie mathematische Funktionen.
Die folgende Funktion ist eine *reine Funktion*.

```{code-cell} python3
def f(x):
    return x + 1

print(f(2))
```

Folgende Funktion ist keine *reine Funktion*.

```{code-cell} python3
y = 2
def f(x):
    if y == 2:
        return x + 1
    else:
        return x

print(f(2))
y = 1
print(f(2))
```

````{admonition} Reine Funktion und Python
:class: remark
:name: remark-python-pure-functions
``Python`` macht es uns schwer keine *reine Funktion* zu konstruieren.
Zum Beispiel würde folgender Code zu einem Fehler führen:

```python
y = 0
def f(x):
    y = y + 1
    return x + y

print(f(2))
print(f(2))
```

````

```{exercise} Seiteneffekte
:label: sideeffect-exercise
Weshalb könnte es Sinn machen *Seiteneffekte* zuzulassen?
Weshalb macht es zugleich Sinn sie so gut es geht zu vermeiden?
```

```{solution} sideeffect-exercise
:label: sideeffect-solution
:class: dropdown
Immer wieder Kopien anzulegen kann viel Speicherplatz und Rechenzeit kosten.
Zudem ist jede Eingabe durch ein Eingabegerät schlussendlich ein *Seiteneffekt*.
Die Ein- und Ausgabe kann ohne *Seiteneffekte* nicht realisiert werden.

Code der auf Funktionen ohne Seiteneffekte basiert, lässt sich leichter lesen, analysieren und kombinieren.
Besonders wenn die Reihenfolge, in der die Funktionen aufgerufen werden, nicht mehr eindeutig ist (Parallelität), kann eine Fehlersuche unglaublich schwierig sein, sofern *Seiteneffekte* vorhanden sind.
```

Wir besprechen reine Funktionen in ``Python`` im Abschnitt [Reinheit](sec-purity).

Funktionale Sprachen wie ``Haskell`` waren anfänglich rein akademische Sprachen mit denen sich in der Praxis nichts wirklich anfangen ließ.
Nichtsdestotrotz haben diese Sprachen interessante Konzepte zutage gebracht.
Von "extrem sicher aber unbrauchbar" wandern funktionale Sprachen Schritt für Schritt in Richtung "extrem sicher und brauchbar".

Imperative Sprachen hingegen wandern tendenziell von "sehr brauchbar aber unsicher", zu "sehr brauchbar und sicher".
Beide Lager lernen voneinander.
So existieren in ``Python`` und allen anderen sehr nützlichen Sprachen wie ``Java``, ``C#``, ``C++`` Konstrukte, die von funktionalen Sprachen inspiriert sind.
Zum Beispiel erzeugt

```{code-cell} python3
def square(x):
    return x * x

list(map(square, [1,2,3]))
```

eine neue Liste mit den quadrierten Zahlen der Ursprungsliste.
Das besondere dabei ist, dass wir die Funktion ``square`` einer anderen Funktion ``map`` übergeben.
Funktionen als Übergabeparameter (sog. [Funktion erster Klasse](sec-first-class-functions)) ist ein Konzept der funktionalen Sprachen.
In ``Haskell`` sieht das ganze wie folgt aus:

```haskell
square :: Int -> Int
square x = x * x
map square [1, 2, 3]
```