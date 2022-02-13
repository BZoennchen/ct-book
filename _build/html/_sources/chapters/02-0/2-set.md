(sec-math-set)=
# Mengen

Die Menge ist eines der fundamentalsten mathematischen Objekte.
Eine Menge repräsentiert eine Ansammlung von verschiedenen Objekten / Elementen.
Sie kann unendlich oder endlich viele Elemente enthalten.

```{admonition} Menge
:name: def-math-set
:class: definition

Eine *Menge* $M$ ist eine (ungeordnete) Ansammlung von Elementen.
```

Wir schreiben $e \in M$ um auszudrücken, dass das Element $e$ in der Menge $M$ enthalten ist.

## Mengenkonstruktion

Es gibt verschiedene Schreibweisen um eine Menge zu definieren.
Zum Beispiel, können wir die Elemente der Menge einfach auflisten

$$M = \{3, 1.2, 5, 6\}$$

oder ihre Elemente als Bedingung definieren

$$M = \{x : x \text{ ist eine Primzahl}\}.$$

Selbst wenn wir keine Ahnung haben, wie wir Primzahlen berechnen können, können wir die Menge aller Primzahlen einfach hinschreiben.
Für immer wiederkehrende Mengen haben sich Mathematiker\*innen auf ganz bestimmte Symbole geeignet.

## Zahlenmengen

Besonders wichtig sind dabei die Zahlenmengen:

+ Natürlichen Zahlen: $\mathbb{N} = \{1, 2, 3, \ldots \}$
+ Natürlichen Zahl inklusive der Null: $\mathbb{N}_0 = \{0, 1, 2, 3, \ldots \} = \mathbb{N} \cup \{0\}$
+ Ganzen Zahlen: $\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots \}$
+ Rationalen Zahlen: $\mathbb{Q} = \left\{ \frac{a}{b} : a \in \mathbb{Z}, b \in \mathbb{N} \right\}$
+ Reelle Zahlen:  $\mathbb{R} = \{ \ldots, -e, 1.5, \sqrt{2}, \pi, \ldots \}$
+ Binäre Zahlen: $\mathbb{B} = \{0,1\}$

Enthält eine Menge $B$ alle Elemente einer Menge $A$ so drücken wir diesen Sachverhalt mit

$$A \subseteq B.$$

Gilt zudem $b \in B$ und zugleich $b \notin A$, d.h., es gibt ein Element $b$ in $B$ welches nicht in $A$ enthalten ist, so drücken wir dies mit

$$A \subset B$$

aus. Für die Zahlenmengen gilt:

$$\mathbb{N} \subset \mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}.$$

## Mächtigkeit

```{admonition} Mächtigkeit endlicher Mengen
:name: def-math-set-cardinality
:class: definition

Die *Mächtigkeit* oder auch *Kardinalität* $|M|$ einer **endlichen** Menge $M$ ist gleich der Anzahl ihrer Elemente.
```

Die *leere Menge* notieren wir mit $\emptyset = \{\}$.
Sie enthält keine Elemente.

```{admonition} Mächtigkeit unendlicher Mengen
:name: remark-math-set-cardinality-infinity
:class: remark

Die für einen sauberen *Mächtigkeitsbegriff* unendlicher Mengen benötigen wir Mittel, welche wir hier nicht besprechen.
Es sei jedoch erwähnt, dass $|\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}|$ gilt.
Diese Mengen enthalten *abzählbar* viele Elemente, wohingegen $\mathbb{R}$ *überabzählbar* ($|\mathbb{R}| > |\mathbb{N}|$) viele Elemente enthält.
```

## Programmierung

Alle gängigen Programmiersprachen bieten [Datenstrukturen](sec-data-structures) an, welche **endliche** Mengen repräsentieren.
Welche Möglichkeiten die ``Python`` Mengen ``set`` bieten, erfahren Sie in Abschnitt [Mengen - set](sec-set).