# Die Kunst des Programmierens

In den Anfängen der Informatik tauchte immer wieder die Frage auf, ob diese Disziplin eine Wissenschaft oder eine Ingenieurskunst sei.
Der Zweifel an der Wissenschaftlichkeit keimte auf, da sich die Informatik im wesentlichen mit dem Computer, also einer konkreten Konstruktion des Menschen beschäftige und nicht mit dem Wesen der Natur selbst.
Doch bereits in ihren Anfängen stellte die Informatik die Frage nach dem grundsätzlichen Wesen der [Berechenbarkeit](sec-computability).
Diese Frage geht weit über digitale Computer hinaus und mündet in der Frage nach dem Wesen des Universums

>Ist das Universum eine einzige riesige Turingmaschine?

und des Menschen bzw. der künstlichen Intelligenz

>Ist der Mensch im wesentlichen eine Turingmaschine?

Anstatt die Informatik zu sehr mit Computern in Verbindung zu setzten ist es besser sie als Forschungsgebiet der [Information](sec-information) und deren Verarbeitung zu betrachten.
Es ist heute klar, dass vielerlei Informationsprozesse in der Natur am Werke sind.
Sei es der Prozess der Zellteilung, die DNA-Codierung oder der schlichte Lernprozess von bewussten Lebewesen. 
Die Informatik ist zwar keine Naturwissenschaft, beschäftigt sich aber vielleicht mit dem natürlichsten aller Prozesse.

```{admonition} Lernziel
:class: learngoals

Was genau ist ein *Algorithmus*, *Programmcode*, *Pseudocode* und ein *Programm*?
Welche wesentlichen Programmierkonstrukte verwenden wir beim Einsatz von (imperativen) Programmiersprachen?
Und weshalb reichen diese Kenntnisse nicht aus? 
Weshalb braucht es Übung um meisterhaft zu Programmieren?

Diese Fragen können Sie sich hoffentlich nach diesem Kapitel selbst beantworten.

```

Als *Strukturwissenschaft* bezieht sich die Informatik hauptsächlich auf die theoretische Informatik (formale Methoden, Komplexitätstheorie, Berechenbarkeit, Automaten, usw.).
Dort beschäftigen wir uns mit Fragen wie:

+ Was ist überhaupt eine Berechnung?
+ Was bedeutet [Berechenbarkeit](def-turing-computable)?
+ Wie *komplex* ist ein Algorithmus oder wie *schwer* ist das zu lösende Problem?
+ Welche *Komplexitätsklassen* gibt es überhaupt?
+ Mit welchen Strukturen kann ich was ausdrücken?
+ Ist meine Theorie konsistent und/oder vollständig?
+ ...
  
Diese Fragestellungen gehen weit über den Computer hinaus.
Zum Beispiel, stellen wir die Frage der Komplexität zwar im Bezug auf der Anzahl der Schritte, die ein Computer benötigt, doch können wir dies leicht auf den Menschen und andere 'natürliche' Rechenmaschinen übertragen.
Sie würden uns vermutlich zustimmen, wenn wir behaupten, dass Karten sortieren ein weniger *schweres* Problem ist als das Lösen eines Sudokus.

Ihre zweite Wissenschaftsrubrik, die *Ingenieurswissenschaft*, bezieht sich auf die Konstruktion und analyse von Informationsverarbeitungssystemen.
Und genau hier finden wir das was wir als *die Kunst des Programmierens* bezeichnen.
Von Außen betrachtet wirkt das Programmieren als die vielleicht langweiligste Tätigkeit auf diesem Planeten.
Diese Einschätzung ist nach unserer Auffassung natürlich vollkommen falsch.

Programme zu schreiben ist eine äußerst kreative, interaktive, spannende und schöne Erfahrung.
Leider lässt sich dieses Erlebnis nur schwer beschreiben -- man muss es selbst erleben.
Es ist ein wenig wie das Versinken in einem Spiel, allerdings können wir in diesem Spiel unsere eigene Welt mit unseren Regeln bauen.
Wir beginnen oftmals mit elementaren Objekten, die wir Schritt für Schritt in etwas Größeres zusammenführen.
Dabei ist immer ein gewisses Rätsel zu lösen.

Die Vorstellung der Programmierer\*innen, die scheinbar mühelos und in atemberaubender Geschwindigkeit ihren Code heruntertippen ist ein Mythos.
Natürlich gibt es solche Phasen, dann aber haben wir das vor uns liegende Rätsel bereits gelöst!
Programmieren beginnt im Kopf und sehr oft in der Diskussion.
Es ist anstrengend und wie bei der Kreation eines Kunstwerks, ist es ein Ringen mit der eigenen Unfähigkeit.
Doch genau diese Unfähigkeit verringern wir durch jedes gelöste Rätsel.
Deshalb ist Programmieren ein nicht endender Lernprozess.

Bei genauer Betrachtung endet alles bei der simplen Manipulation von Symbolen, die wir als Informationsverarbeitung bezeichnen.
Softwareentwickler\*innen schöpfen, formen und verwenden Informationen.
Sie bauen [Datenstrukturen](sec-data-structures) und [Algorithmen](sec-algorithms) ganz so wie Architekt\*innen Baupläne und Gebäude entwerfen.
Anders als der Baustoff der Architekt\*innen, können Softwareentwickler\*innen ihre Bauwerke der strukturierten Information nicht nur erschaffen sondern verändern, kombinieren, wiederverwenden und erweitern.
Sie steuern eine Maschine die sich ihnen vollständig ergibt.
Dieser immense Grad der Kontrolle hat etwas selbstbestimmtes, etwas das wir in der echten Welt manchmal vermissen.

Enden wollen wir diesen, hoffentlich motivierenden Abschnitt, mit den Worten des Erfinders von Linux, Linus Torvalds.

>[Phyisics and computer science] are about how the world works at a rather fundamental level. The difference, of course, is that while in physics, you are supposed to figure out how the world is made up, in computer science, you create the world. Within the confines of the computer, you are the creator. You get ultimate control over everything that happens. If you are good enough, you can be God on a small scale. -- Linus Torvalds