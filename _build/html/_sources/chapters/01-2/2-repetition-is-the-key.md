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

# Wiederholung als Grundlage

[Computational Thinking](sec-what-is-ct) beginnt normalerweise dort wo alle Denkprozesse beginnen: In den Köpfen der Menschen.
Der Computer ist sekundäres Werkzeug um das Resultat des Denkprozesses niederzuschreiben und schlussendlich auszuführen.
Wir können eine Musikkomposition als jene Niederschrift und dessen Aufführung als Ausführung interpretieren.
Schließlich ist eine Musikkomposition nichts anderes als ein [Algorithmus](def-algorithm), beschrieben durch eine endliche Folge von Noten.
Wie bei einer Niederschrift eines Algorithmus in Form von Quellcode können wir zwischen

1. der Komplexität der Aufführung/Ausführung (wie viele Noten werden gespielt bzw. wie lange dauert das Stück) und 
2. der Komplexität der Beschreibung (wie viele Seiten an Noten beschreiben das Stück)

unterscheiden. Denken Sie nur an die verschiedenen Kinderlieder, die Sie in einer Endlosschleife singen können und dennoch auf wenigen Seiten Papier beschrieben vorfinden.

Was sich mit der Erfindung und fortwährenden Verbesserungen der Computer geändert hat, ist die benötigte Zeit, die einzelne (arithmetische und kombinatorische) Operationen benötigen.
Primzahlen lassen sich ab einer gewissen Größe nicht mehr händisch berechnen, da der Prozess die Lebenszeit eines Menschen überschreitet.
Computer verschieben diese Grenzen nach oben, doch gehen auch Sie selbstverständlich irgendwann in die Knie.

Ähnlich zur Musik und Literatur brauchen wir für die Kommunikation unseres Denkprozesses eine einheitliche Basis, die wir Sprache nennen. 
Ein wesentlicher Unterschied zur Musik und Literatur ist, dass diese [Programmiersprache](sec-programming-languages) auch von Rechenmaschinen verstanden wird.
Egal ob Notenblatt oder Programmiercode, beide Beschreibungen müssen endlich und unmissverständlich sein.
Dies ist eine notwendige Voraussetzung!
Das Notenblatt bedarf der richtigen Interpretation, d.h., Musiker\*innen müssen Noten lesen können.
Genauso verhält es sich beim Programmiercode.
Ob Mensch oder Maschine ist an und für sich unwichtig, es bedarf lediglich der richtigen [Interpretation](sec-interpretation) des Codes.

Solange sich eine Problemlösung (unsere Musikkomposition) durch Wiederholung ausdrücken lässt, kann sie durch endlich viel Programmcode (Noten) beschrieben und damit (theoretisch) gelöst (aufgeführt) werden.
Die Komplexität des Programmcodes (die länge des Stücks) entkoppelt sich von der Komplexität der ausgeführten Berechnung (der Aufführung).
Zum Beispiel beschreibt folgender ``Python``-Code die Berechnung der Summe aller Quadratzahlen von ``1`` bis einschließlich ``n``.

```{code-cell} python3
def sum_sqrt(n):
    sum_sqrt = 0
    for i in range(n):
        sum_sqrt += (i+1) * (i+1)
    return sum_sqrt

sum_sqrt(10)
```

Die Anzahl der auszuführenden Anweisungen steigt linear mit der natürlichen Zahl ``n``, doch der Programmiercode bleibt unverändert.
Hierin liegt die ganze "Magie": **Wiederholung**!