(sec-math-relation)=
# Relationen

## Das Kartesisches Produkt

Bevor wir Relationen besprechen können benötigen wir noch die Definition des *kartesischen Produkts*.
Es ist eine Operation, welche aus zwei Mengen $A$ und $B$ eine neue Menge erzeugt.
Dabei wird jedes Element aus $A$ mit jedem Element aus $B$ kombiniert.
Es wird auch als das sog. *Mengenprodukt* bezeichnet.

```{admonition} Kartesische Produkt
:name: def-math-set-product
:class: definition

Das *kartesische Produkt* $A \times B$ zweier *Mengen* $A$ und $B$ ist definiert als die Menge aller (geordneter) Paare (2-Tupel) $(a,b)$, wobei $a$ ein Element aus $A$ und $b$ ein Element aus $B$ ist:

$$A \times B = \{(a,b) : a \in A, b \in B\}.$$
```

+ $\{1,2,3\} \times \{1.2,3.5\} = \{(1,1.2), (1,3.5), (2,1.2), (2,3.5), (3,1.2), (3,3.5)\}$
+ $\mathbb{N} \times \{1,2,3\} = \{(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), \ldots \}$
+ $\{1,2,3\} \times \emptyset = \emptyset$
+ $\{\emptyset\} \times \{1,2,3\} = \{(\emptyset, 1), (\emptyset, 2), (\emptyset, 3)\}$

```{exercise} Anzahl der Elemente
:label: set-products-number-of-elements-exercise

Seien die endlichen Mengen $A$ und $B$ gegeben und sei $|A| = m$ und $|B| = n$.
Wie viele Elemente enthält die Menge $A \times B$?
```

```{solution} set-products-number-of-elements-exercise
:label: set-products-number-of-elements-solution
:class: dropdown
Es gilt $|A \times B| = n \cdot m$.
```

## Die Relation

Eine Relation ist nichts anderes als eine Teilmenge eines kartesischen Produkts.

```{admonition} Relation (Beziehung)
:name: def-math-relation
:class: definition

Eine *Relation* $R \subseteq A \times B$ ist eine Menge aus (geordneten) Paaren $(a, b) \in R$ mit $a \in A$ und $b \in B$, wobei $A$ und $B$ Mengen sind.
```

Stammen die Elemente einer Relation $R$ aus den Mengen $A$ und $B$ so gilt:

$$R \subseteq A \times B.$$

Anstatt $(a,b) \in R$ schreibt man auch $a R b$.

## Die Ordnungsrelation

Eine wichtige Relationen, die uns in der Praxis begegnen wird ist die sog. *Ordnungsrelation*.
Für diese schreibt man anstatt $(a,b) \in R$ auch $a \leq_R b$ oder $a \leq b$, falls aus dem Kontext hervorgeht, welche Relation $R$ gemeint ist.

```{admonition} (Totale) Ordnungsrelation
:name: def-math-order
:class: definition

Eine *Ordnungsrelation* $R \subset M \times M$ auf einer Menge $M$ ist eine Relation mit folgenden Eigenschaften:

1. Reflexivität: $\forall a \in M : a \leq_R a$
2. Antisymmetrie: $\forall a, b \in M : a \leq_R b \land b \leq_R a \Rightarrow a = b$
3. Transitivität: $\forall a, b, c \in M : a \leq_R b \in R \land b \leq_R c \Rightarrow a \leq_R c$

Eine *Ordnungsrelation* ist *total* wenn für alle $a,b \in M$ $a \leq_R b$ oder $b \leq_R a$ gilt.
```

```{admonition} Totale Ordnung
:name: remark-math-order
:class: remark

Die *kleiner-gleich-Relation* $\leq$ auf den natürlichen Zahlen ist eine totale Ordnung.
```

Die *Ordnungsrelation* verallgemeinert / **abstrahiert** das Konzept des Ordnens von numerischen Werten.
Immer dann wenn wir Dinge sortieren wollen, machen wir dies anhand einer Ordnungsrelation (siehe [Karten sortieren](sec-sorting)).