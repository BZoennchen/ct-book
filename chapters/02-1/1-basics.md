(sec-computer-basics)=
# Grundlagen

Beim Design der Computer kristallisierten sich vier wesentliche Aufgaben heraus.
Alle Computer basieren auf diesen vier grundlegenden Aufgabe:
1. Informationen **einlesen**
2. Informationen **speichern**
3. Informationen **verarbeiten**
4. Informationen **ausgeben**

Sie bilden das Fundament eines jeden Computers.
Die Verarbeitung von [Information](sec-information) wird symbolisch vollzogen, d.h. Computer manipulieren auf Grundlage von bestimmten Regeln die Symbole der Eingabe um die Symbole der Ausgabe zu bestimmen.
Computer haben keine eigene Intension oder agieren aus einer Emotion heraus.
Sie haben auch keinerlei Verständnis von der Eingabe.
Zum Beispiel können Computer Texte in unterschiedlichen Sprachen übersetzen was jedoch nicht bedeutet, dass sie verstehen was sie da übersetzen.
Inwieweit symbolische Manipulationen zu einem "Verstehen" führen könnten, wird derzeit rege im Bereich der *künstlichen Intelligenz* diskutiert.

```{admonition} EVA-Prinzip
:class: remark
:name: remark-eva
Der Computer basiert auf dem sog. *EVA-Prinzip* (**Eingabe**, **Verarbeitung** und **Ausgabe**).
```

Ein Computer erweitert das EVA-Prinzip um den **Speicher** und damit um einen **Zustand**.
Wäre der Computer zustandslos würde er bei gleicher **Eingabe** $x$ auch stets die gleiche **Ausgabe** $y$ erzeugen.
Durch den Speicher kann sich, je nach Eingabe, der Zustand $z$ des Computers verändern und, je nach seinem Zustand, kann dieselbe Eingabe zu unterschiedlichen Ausgaben führen.

```{figure} ../../figs/digital-computer/basics/dfa.png
---
width: 600px
name: fig-dfa
---
Ein Modell eines Computers mit 4 Zuständen. 
Der Computer befindet sich in Zustand $z = z_1$ (rot).
Die Ausgabe $y$ hängt von der Eingabe $x$ als auch vom aktuellen Zustand $z$ (hier $ = z_1$) des Computers ab.
Während der Berechnung der Ausgabe verändert der Computer seinen Zustand auf $g(z, x)$.
$f$ und $g$ sind mathematische Funktionen.
```

Über *Eingabegeräte*, die den Computer mit der Eingabe füttern, ist er mit der Außenwelt verknüpft.
Tastatur und Maus sind beispielsweise Eingabegeräte, die uns Menschen eine unmittelbare Möglichkeit geben, um *Informationen* in den *Computer* zu speisen.
Als weitere Eingabegeräte können wir eine Kamera oder andere Sensoren wie Messgeräte, die den Puls oder Blutzucker messen, anfügen.

Die Eingabe eines Computers kann analog zu unserer eigene Wahrnehmung gesehen werden.
Unsere Sinne nehmen durch Stimulierungen die Welt wahr und unser "menschlicher Prozessor" verarbeitet die aufgenommenen Informationen.
Der Unterschied zwischen unserer Eingabe und der eines Computers, ist die Art mit der Informationen repräsentiert werden.
Wir Menschen übertragen und verarbeiten Informationen (analog) durch Nervenenden und chemische Prozesse.
Die Eingabe eines Computers wird durch das *Eingabegerät* in eine Folge von zwei Zuständen 0, 1 transformiert und in den Speicher des Computers abgelegt.

Der Prozessor eines Computers **ließt** (digitale) Informationen aus dem Speicher, **manipuliert** sie durch eine Abfolge von Symbolmanipulationen, d. h., durch das Abarbeiten eines [Algorithmus](def-algorithm) (eine endliche Folge von Anweisungen) und **schreibt** die **veränderte** Information zurück in den Speicher.

Wenn alle Arbeit getan ist, wird die verarbeitete Information durch die *Ausgabegeräte* **ausgegeben**.
Ausgabegeräte können Monitore, Lautsprecher aber auch andere Geräte, wie zum Beispiel VR-Brillen sein.
Die Ausgabegeräte erhalten als Information eine Folge von 0 und 1.
Sie transformieren diese Information in Bilder, Videos und mehr.

Durch die *Vernetzung* von mehreren Computern, wie zum Beispiel dem Internet, wird die Ausgabe des einen Computers zur Eingabe des anderen.
Kann ein Problem in viele Teilprobleme aufgeteilt werden (*Dekomposition*), können viele Computer im Verbund eine Lösung berechnen.