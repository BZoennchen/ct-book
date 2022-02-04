# Notation

Als Notation verstehen wir die [Syntax](def-syntax) und [Semantik](def-semantik) mathematischer Symbole.
Auch wenn in vielen Bereichen der Mathematik die Notation bereits standardisiert ist, steht es schlussendlich den Autor\*innen frei eine individualisierte Notation zu verwenden.
Zum Beispiel verwenden manche Autor\*innen als Symbol für die natürlichen Zahlen in $\mathbb{N}$ mit einem Doppelstrich andere verwenden ein fett gedrucktes $\mathbf{N}$.

## Gleitkommazahlen

In allen Programmiersprachen verwendet man die englische Notation für Gleitkomma- bzw. Fließkommazahlen.
Das heißt anstatt $1,5$ schreibt man $1.5$.
Aus Gründen der Konsistenz werden wir diese Notation auch im Text verwenden, sodass keine Verwirrung zwischen Programmcode und normalem Text entsteht.

## Folgen

Hin und wieder möchten wir eine unendliche oder sehr lange Folge notieren.
Zum Beispiel

$$1, 2, 4, \ldots$$

Die drei Punkte $\ldots$ deuten an, dass diese Folge unendlich lange weiter geht.
Aus den ersten notierten Zahlen der Folge sollte dabei immer klar hervorgehen, wie diese voran schreitet.

Die gleiche Notation werden wir hin und wieder bei endlichen indexierten Folgen, zum Beispiel:

$$a_0, a_1, \ldots, a_n$$

verwenden. 
In diesem Beispiel hat die Folge $n+1$ Elemente.

## Summen

Um Summen ähnlich wie Folgen kompakter zu notieren, verwenden wir das Summensymbol $\sum$, zum Beispiel:

$$1 + 2 + 3 + 4 + 5 + 6 = \sum\limits_{k=1}^6 k$$


Dieses Summe besteht aus 

+ einer Laufvariable (hier $k$), 
+ einem Endwert (hier $6$) 
+ einem Startwert (hier $1$) und 
+ einer Funktion bezüglich der Laufvariable (hier $f(k) = k$).

Der Endwert kann auch den 'Wert' unendlich $\infty$ annehmen:

$$1 + 2 + 3 + 4 + 5 + \ldots = \sum\limits_{k=1}^\infty k$$

Eine weitere Schreibweise deutet an, dass wir über die Elemente einer Menge $M$ iterieren.
So könnten wir die obige Summe auch als

$$1 + 2 + 3 + 4 + 5 + \ldots = \sum\limits_{n \in \mathbb{N}} n$$

schreiben.
Dabei fehlen Start- und der Endwert, und werden durch eine Menge ersetzt, welche alle Werte festlegt.

## Produkte

Analog zu Summen gibt es auch ein Produktsymbol $\prod$, wodurch sich Produkte kompakter schreiben lassen:

$$1 \cdot 2 \cdot  3 \cdot  4 \cdot  5 \cdot  6 = \prod\limits_{k=1}^6 k$$

auch dafür lässt sich ein unendlich größer Endwert festlegen

$$1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot \ldots = \prod\limits_{k=1}^\infty k$$

und wir können ebenfalls über Mengen iterieren

$$1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot  = \prod\limits_{n \in \mathbb{N}} n.$$