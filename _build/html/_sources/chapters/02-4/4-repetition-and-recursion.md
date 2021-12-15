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

## Wiederholung und Rekursion

Auf der konzeptionellen Ebene erscheinen Wiederholung und Rekursion grundverschieden.
Es sind unterschiedliche Denkweisen.
Wir können rekursiv oder aber in Wiederholungen denken.

```{admonition} Wiederholung und Rekursion
:class: important
Sofern bei der Wiederholung, die Anzahl der Durchläufe nicht zur Laufzeit vor der Ausführung der Wiederholung bekannt sein muss können wir überraschenderweise jede Rekursion in eine Wiederholung und jede Wiederholung in eine Rekursion umwandeln!
```

### Wiederholung

Das fundamentale Prinzip der *Wiederholung* ist zentraler Bestandteil des Computational Thinkings.
Blicken wir in den Werkzeugkasten der Algorithmen so finden wir die Wiederholung überall.
Sortieralgorithmen, die Berechnung eine Gleichungssystems, das Verarbeiten eines Bildes, die Schaltflächen einer App, überall finden wir Schleifen, die unsere Informationen *iterativ* verarbeiten.

Nach der Definition eines Algorithmus, muss dieser aus endlich vielen Anweisungen bestehen.
Will man jedoch eine variable Menge an Information verarbeiten, so muss ein Algorithmus abhängig von der Eingabegröße unterschiedlich viele Anweisungen ausführen.
Das bedeutet, dass die Länge des Algorithmus unabhängig von der Anzahl der auszuführenden Anweisungen (für eine gegebenen Eingabe) sein können muss!
Nach dem Schubfachprinzip bedeutet dies wiederum, dass in diesem Fall Teile des Algorithmus öfters durchlaufen werden - Wiederholung muss also in irgendeiner Form stattfinden.

Überraschenderweise hat sich herausgestellt, dass *Wiederholung* in Kombination mit der *Fallunterscheidung* ausreicht, um alles berechnen zu können was wir bisher als natürlich berechenbar ansehen.
Nach der unbeweisbaren Church-Turung-These werden wir keine Problem finden, was natürlich berechenbar aber nicht durch einen Computer berechnet werden kann.
Die Fallunterscheidung in Kombination mit der Wiederholung ist scheinbar ausreichend.

Nun haben Sie vielleicht die Hoffnung, Sie müssten nur die *Wiederholung* und die *Fallunterscheidung* beherrschen und können dann jedes Problem lösen.
Leider sind diese beiden Techniken derart grundlegend, dass sie eine notwendige nicht aber ausreichende Bedingung für die Entwicklung von Algorithmen darstellen.
Wir können das mit der Sprache vergleichen.
Nur weil wir laute von uns geben können, heißt das nicht, dass wir uns in jeder Sprache verständigen können.
Ein weiteres Beispiel wären die Naturwissenschaften.
Nur weil wir die kleinsten Teilchen im Universum verstehen, bedeutet dass nicht, dass wir damit das entstehen von Leben oder anderen emergenten Übergängen erklären können.

Wenn Sie jedoch Erfahrung im entwickeln von Algorithmen gesammelt haben und Algorithmen analysiert und verwendet haben, dann werden Sie beginnen in Wiederholungen zu denken.
Sie werden beginnen in Wiederholungen von Wiederholungen von Wiederholungen zu denken.

Nehmen wir zum Beispiel den [Bubblesort Algorithmus](https://en.wikipedia.org/wiki/Bubble_sort).
Wir möchten eine Liste von Zahlen sortieren.
Wir gehen durch die Liste (1. *Wiederholung*) und wann immer zwei nebeneinander liegende Zahlen falsch sortiert sind, vertauschen wir diese.
Wir wiederholen dies (2. *Wiederholung*) solange bis keine Zahl mehr falsch sortiert ist.

```{code-cell} python3
import random as rnd

def bubble_sort(numbers):
    finished = False
    while(not finished):
        finished = True
        for i in range(1,len(numbers)):
            if numbers[i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                finished = False
    
numbers = [1,2,3,4,5,6,7,8,9]
rnd.shuffle(numbers)
print(f'before sorting: {numbers}')
bubble_sort(numbers)
print(f'after sorting: {numbers}')
```

Die beiden Schleifen liefern uns auch einen Hinweis auf die Laufzeit des simplen Sortieralgorithmus.
Nach jedem ausführen der inneren Schleife befindet sich ein neues Element an seiner korrekten Position.
Damit brauchen wir maximal so viele Durchläufe (1. Wiederholung) wie es Elemente sind.
Jeder Durchlauf benötigt ebenfalls maximal so viel Schritte wie es Elemente sind.
Damit hat der Algorithmus im schlechtesten Fall eine quadratische Laufzeit.

### Rekursion

Rekursion scheint dieses unverständliche Konzept, welches Mathematiker\*innen lieben und vor dem Programmierer\*innen anfänglich davonlaufen.
Derweil würden wir behaupten, dass die *rekursive denkweise* uns Menschen näher ist als das Denken in Wiederholungen.
Rekursive Lösungen sind oft eleganter, kürzer, verständlicher aber leider auch langsamer als iterative Lösungen.

Nehmen wir die Berechnung der Fakultät, einmal iterativ

$$\text{fac}_\text{it}(n) = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1 = \prod\limits_{i=1}^n i$$

```{code-cell} python3
def fac_it(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

fac_it(5)
```

und einmal rekursiv

$$n! = $$

```{code-cell} python3
def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n-1)

fac_rec(5)
```

```{admonition} Rekursion
:name: def-recursion
:class: important
Als *Rekursion* wird ein Vorgang bezeichnet, welcher sich selbst als Teil enthält oder mithilfe von sich selbst definierbar ist.
```