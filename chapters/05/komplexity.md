# O-Notation

TODO

Sie benötigt höchstens so viele Schritte $\mathcal{O}(\log(n))$ aber auch mindestens so viele Schritte $\Omega(\log(n))$.
Nutzen wir hingegen die *lineare Suche*, ob mit oder ohne Häufigkeit, benötigen wir höchstens $\mathcal{O}(n)$ Schritte aber (nur) mindestens $\Omega(1)$ Schritte.
$\mathcal{O}(f(n)), \Omega(f(n))$ sind sogenannte Komplexitätsklassen.
Ein Algorithmus dessen Aufwand durch eine Funktion beschrieben wird. die sich in der Klasse $\mathcal{O}(f(n))$ befindet hat, salopp gesagt, keinen höheren Aufwand als $f(n)$ wobei $n$ die Problemgröße ist (in unserem Fall die größe der Menge).


## Die Foreach-Schleife

Wollen wir einen bestimmten Codeabschnitt ``n`` mal wiederholen, so können wir diese mit der sog. **Foreach**-Schleife ``for`` und einem passenden Bereich ``range`` realisieren:

```{code-cell} python3
n = 5
for i in range(n):
  print(i)        # code to repeat
  print('Hello')  # code to repeat
```

Gelesen bedeutet dies: Für jedes (engl. for each) Element ``i`` im Bereich ``range(n)`` führe den eingerückten Code aus.

In ``Python`` gibt es keine klassische **For**-Schleife wie zum Beispiel in ``Java``, ``C/C++`` oder ``JavaScript``:

```java
// Java, C/C++
int n = 10
for(int i = 0; i < n; i++){
  // do something
}
```

```javascript
// JavaScript
let n = 10
for(var i = 0; i < n; i++){
  // do something
}
```

Wir können beispielsweise einen Bereich ``range(100)`` mit hundert ganzen Zahlen erzeugen.
Iterieren wir durch diesen Bereich mit einer ``for``-Schleifer, so können wir diesen Prozess frühzeitig mit ``break`` abbrechen:

```{code-cell} python3
for i in range(100):
    print(i)
    if i >= 4:
        break
```

Bemerkenswert ist hierbei, dass lediglich die ganzen Zahlen 0, 1, 2, 3, 4 des Bereichs berechnet werden!
Im Vergleich dazu legen wir mit folgendem Code alle 100 Zahlen in den Speicher:

```{code-cell} python3
numbers = list(range(100))
for i in numbers:
    print(i)
    if i >= 4:
        break
```

Aus diesem Grund nennt man den Bereich **faul** (engl. *lazy*).





## Namesraum Wörterbücher

``Python`` implementiert den **lokalen** und **globalen** Namensraum als Wörterbuch, welches wir uns zu jederzeit auch ausgeben lassen können.

```{code-cell} python3
---
tags: [output_scroll]
---
globals()
```

Fügen wir eine neuen Namen hinzu:

```{code-cell} python3
---
tags: [output_scroll]
---
new_name = 'hello!'
globals()
```