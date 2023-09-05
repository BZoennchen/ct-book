(sec-math-function)=
# Funktionen

Eine Funktion ist eine Relation für die bestimmte Bedingungen zutreffen müssen.

```{admonition} Funktion
:name: def-math-function
:class: definition

Eine *Funktion* $f : A \rightarrow B$ ist eine Relation (Beziehung) zwischen zwei Mengen $A$, $B$ die **jedem** Element aus $A$ **genau ein** Element aus $B$ zuordnet.
$A$ bezeichnen wir als die *Definitionsmenge* und $B$ als die *Zielmenge* von $f$.
```

Um durch die Notation anzudeuten, dass es sich bei der Relation um eine Funktionen handelt, schreibt man anstatt $f \subseteq A \times B$ auch

$$f : A \rightarrow B.$$

Und aufgrund der eindeutigen Zuordnung schreiben wir für Funktion $f$ anstatt $(x,y) \in f$ gewöhnlich 

$$f(x) = y.$$

Dies Schreibweise ist eindeutig, da falls $(x,y_1) \in f$ und $(x,y_2) \in f$ gilt, unweigerlich $y_1 = y_2$ folgt.

## Begrifflichkeiten

Anstatt *Definitionsmenge* sagen wir auch *Definitionsbereich*, *Urbildmenge* oder kurz *Urbild*.
Die *Zielmenge* wird auch als *Wertemenge* oder *Wertebereich* bezeichnet.
Diejenigen Elemente von $B$, die tatsächlich auch in einem Paar in $f$ auftauchen, d.h. alle Elemente der Menge

$$\{y : f(x) = y, x \in A \}$$

heißen *Funktionswerte*, *Bildelemente* kurz *Bilder*.

## Beispiele

Beispiele für Funktionen mit reellem Definitions- und Wertebereich die Ihnen bekannt vorkommen sollten:

$$f: A \rightarrow B \text{ mit } A, B \subseteq \mathbb{R}$$

+ Gerade: $f(x) = 2x - 7$
+ Quadratische Funktion: $f(x) = -6x^2 + 3x + 4$
+ Polynom: $f(x) = 8x^5 + x^4 - 3x^3 + 2$
+ Rationale Funktion: $f(x) = \frac{2x^3 - 2x}{5x - 10}$
+ Sinus-Funktion: $f(x) = 2\sin(-2x) + 5$
+ Exponentialfunktion: $f(x) = 5^{x-2}-4$
+ Natürliche Exponentialfunktion: $f(x) = e^x$
+ Logarithmusfunktion: $f(x) = 3 \log_2(2x-4) + 3$

Weitere etwas ungewöhnlichere Beispiele sind:

+ Leere Funktion: $f : \emptyset \rightarrow \emptyset$, $f = \emptyset$
+ Diskrete Funktion $f : \{1,2,3\} \rightarrow \{1,2,3\}$, $f = \{(1,2), (2, 1), (3, 2)\}$
+ Dirichlet Funktion $f : \mathbb{R} \rightarrow \mathbb{R}$, 
  $f(x) = \begin{cases}1, & \text{ falls } x \in \mathbb{Q} \\ 0, & \text{ sonst.}\end{cases}$

## Programmierung

Alle gängigen Programmiersprachen realisieren mathematische Funktionen durch Funktionen bzw. Methoden.
Allerdings sei gesagt, dass nicht jede programmierte Funktion auch eine mathematische Funktion ist.

Welche Möglichkeiten Ihnen ``Python`` bietet, erfahren Sie im Abschnitt [Funktionen](sec-functions).