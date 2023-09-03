(sec-programming-languages)=
# Programmiersprachen

Ein [Algorithmus](def-algorithm) ist eine endliche Folge von Anweisung um für eine bestimmte Eingabe eine bestimmte Ausgabe zu erzeugen.
Durch Programmiersprachen können wir Algorithmen so niederschreiben, dass der Computer diese abarbeiten kann.

```{admonition} Lernziel
:class: learngoals

In diesem Abschnitt möchten wir Ihnen aufzeigen was Programmiersprachen eigentlich sind, wozu sie gebraucht werden, weshalb es verschiedene Sprachen gibt und welche unterschiedlichen Eigenschaften diese Sprachen haben können.
```

Analog zu einer natürlichen Sprache, ist eine Programmiersprache eine Vorschrift, auf die man sich zur Verständigung geeinigt hat.
Sie ist Teil unseres *Kontexts*, welchen wir kennenlernen müssen um Programme zu schreiben.
Anders als natürliche Sprachen, sind Programmiersprachen *unmissverständlich* bzw. *eindeutig*.
Das soll nicht heißen, dass es einfach ist einen Programmiercode zu verstehen, doch gibt es nur eine eindeutige [Interpretation](sec-interpretation).

Als Theoretiker\*innen betrachten wir Programmiersprachen oft als [universelle Turingmaschinen](sec-utm).
Doch sei gesagt, dass es viele Programmierer\*innen und auch Entwickler\*innen von Programmiersprachen gibt, die sich mit [Turingmaschinen](info-turingmaschine) nicht beschäftigt haben.
Wir raten Ihnen dennoch sich mit dem Konzept der Turingmaschine zu befassen.

Die Klarheit von Programmiersprachen hat ihren ganz eigenen Reiz.
Irgendwann werden Sie vielleicht diese Klarheit auch in Texten oder Diskussionen aus ihrem Alltag suchen und werden feststellen, wie schwammig und manchmal diffus so manche Argumentation ist.

Eine Programmiersprache ist durch eine sog. *Grammatik* definiert.
Diese Grammatik legt die [Syntax](def-syntax) einer Programmiersprache fest.
Wir sprechen bei der Syntax auch von einer Beziehung der Symbole zueinander.
In anderen Worten, die Grammatik $G$ einer Programmiersprache $L$ legt fest, welche Zeichenfolge ein syntaktisch korrektes Programm darstellen.
In anderen Worten: Ob eine Programmcode $w$ in der Sprache $L$ liegt, die durch eine Grammatik $G$ definiert ist.
Ist dies der Fall, schreiben wir

$$w \in L(G).$$

Dabei muss dieses Programm $w$ noch lange nicht zum gewünschten Ergebnis führen.
Quellcode bzw. ein Programm bzw. ein Algorithmus $w$ ist in einer bestimmten Programmiersprache $L$ geschrieben.
Die Syntax von ``Python`` legt zum Beispiel fest, dass nach dem Wort ``def`` und einem Leerzeichen, ein Name folgen muss.

```python
def function():
    ...
```

Welche [Bedeutung/Semantik](def-semantik) die Aneinanderreihung von Symbole besitzt, wird ebenfalls von der Programmiersprache festgelegt.
So definieren wir durch die obige Zeichenfolge eine neue [Funktion](sec-functions) mit dem Namen ``function``.
Beachten Sie, dass wir hier einen informatischen Begriff der Semantik verwenden.
Diesen haben wir auch im Abschnitt [Interpretation](sec-interpretation) kennengelernt.
Ein Computer kennt eigentlich keine Bedeutung im menschlichen Sinne. 
Er kann lediglich Symbole manipulieren.

Um die Sprache nutzten zu können, müssen wir sowohl Ihre [Syntax](def-syntax) als auch ihre [Semantik](def-semantik) erlernen.
