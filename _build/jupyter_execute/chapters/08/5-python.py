(sec-python)=
# Python

Wie ``Java``, ``C++``, ``C#``, ``Scala`` und viele mehr, zählt ``Python`` zu den Universalsprachen (General Purpose Languages) und ist damit *Turing-vollständig*. 
Das heißt ``Python`` ist in sehr vielen Bereichen anwendbar und ist im Stande all die Probleme zu lösen, die im Allgemeinen als lösbar angesehen werden.
Der Name stammt von der Comedy-Gruppe Monty Python was möglichweise darauf hindeuten soll, dass die Sprache Spaß verbreiten soll!

Was unterscheidet aber ``Python`` von den anderen oben genannten Sprachen? 
``Python`` ist heute eine der weit verbreitesten Sprachen und sie scheint sich weiter und weiter auszubreiten.
Einer der Hauptgründe hierfür ist der einfache Zugang.
``Python`` ist einfach zu lesen und zu erlernen.
Als *interpretierte* Sprache mit guter Toolunterstützung kann jeder in wenigen Klicks einfach loslegen.
Sie installieren ``Python`` (auf vielen Systemen ist es vorinstalliert), öffnen Ihre Konsole, tippen ``python`` und los gehts.

Auch lässt sich in nur wenigen Zeilen ein kleines ``Python``-Skript schreiben und ausführen.
Erstellen wir eine neue Datei ``sum-squares.py`` und fügen folgenden ``Python``-Code ein.

import sys
n = int(sys.argv[1])
squares = sum([(i+1)**2 for i in range(n)])
print(squares)

Führen wir dann das Programm durch den Konsolenbefehl

```
python sum-squares.py 5
```

aus, erhalten wir als Ausgabe die Summe der Quadratzahlen von $1$ bis $5$.
So schnell geht's!

Der einfache Zugang erklärt den anfänglichen Erfolg.
Dieser Erfolg führte zur Unterstützung durch große IT-Unternehmen wie Google und Facebook aber auch der Universitäten, was wiederum die Entwicklung vieler Pakete insbesondere auch im wissenschaftlichen Umfeld antrieb.
Paketen wie ``Numpy``, ``SciPy``, ``Pandas`` und ``Matplotlib`` ist es zu verdanken, dass ``Python`` im wissenschaftlichen Bereich derart verbreitet ist.
Im Unterschied zu ``MATLAB`` und ``Mathematica``, gegen die sich ``Python`` behaupten musste, ist ``Python`` frei zugänglich, was schlussendlich zu einer höheren Codequalität wie auch einer schnelleren Weiterentwicklung geführt hat.

Wissenschaftler\*innen sind keine Programmierexpert\*innen, legen besonders viel Wert auf die Reproduzierbarkeit und haben oft auch noch hohe Ansprüche an die Geschwindigkeit.
Sie entwickeln keine großen Business-Anwendungen aber durchaus effiziente Algorithmen.
Die Möglichkeit sehr schnell gut leserliche Scripte zu schreiben, die auch noch performant laufen (dazu gleich mehr), brachte ``Python`` in der Wissenschaft schnell voran.
Und da heute die Methoden des wissenschaftlichen Rechnens, Big Data Analysis und des Machine Learnings auch in der Wirtschaft immer wichtiger werden, überträgt sich dieser Erfolg auf die Wirtschaft.

Mit den ``Jupyter``-Notebooks haben Wissenschaftler\*innen eine Möglichkeit erhalten, ihre Ergebnisse samt Code anderen in aufbereiteter Weise zur Verfügung zu stellen.
Das beschleunigt den wissenschaftlichen Austausch und verbessert die Transparenz.
Auch dieses Konzept gab es bereits durch ``Mathematica`` doch ist diese Sprache viel schwerer zu lesen und deren Lizenzen sind teuer.

Gute Scripte zu schreiben ist zudem nicht für Wissenschaftler\*innen sondern auch für Systemadministrator\*innen und DevOps wichtig.
Auch in diesem Bereich trat ``Python`` deshalb einen Siegeszug an.

Da ``Python`` einen so schnellen und einfachen Zugang bietet, begannen mehr und mehr Anfänger die Sprache zu nutzen.
Das brachte eine große Menge neue potenzieller Entwickler\*innen auf den Arbeitsmarkt.
Um dieses Potenzial nutzen zu können wurden die Bibliotheken um weitere Pakete für die Webentwicklung (``Django``, ``Flask``), graphische Benutzeroberflächen (``PyQt5``, ``Tkinter``, ``Kivy``) und mehr ergänzt.
Das **Ökosystem** passte sich diesem Potenzial an, ganz nach dem Motto:

>Wollen die Entwickler\*innen nicht zum passenden **Ökosystem** kommen, muss das **Ökosystem** zu ihnen kommen.

Dieses **Ökosystem** ist heute ``Python``s größte Stärke.
Sie bekommen einen unglaublichen Schatz geschenkt!
Das können Sie sich gar nicht vorstellen.
Was Sie nicht kostenfrei bekommen sind die riesigen Rechnerressourcen die in großen Rechenzentren schlummern.


Wir hatten Eingangs erwähnt, dass man sich oft zwischen Performance und Lesbarkeit bzw. Entwicklungszeit entscheiden muss.
``Python`` trifft hier einen ganz bestimmten Sweetspot: die Sprache ist **maschinenenfern**, sehr **leserlich**, man bekommt schnell viel zustande und dennoch ist sie **Leistungsstark**, sofern wir das **Ökosystem** gut nutzen.
Pakte verlagern aufwendige Berechnungen in ``C/C++``-Programmen, eine **maschinennahen** und **leistungsstarken** Spache.
Wie dies funktioniert, soll uns an dieser Stelle noch nicht kümmern.
Durch dieses Zusammenspiel bekommen wir beides: die **Leistung** durch ``C/C++`` und **Abstraktion** und **Lesbarkeit** durch ``Python``!

``Python`` hat aber auch seine Tücken.
Als dynamisch getypte sehr flexible Sprache kann es schwer sein Garantien für den geschriebenen Code sicherzustellen.
Software oder auch Entwickler\*innen, die Quellcode analysieren und auf Korrektheit prüfen, können es schwer haben.

def sum_squares(n):
    return sum([(i+1)**2 for i in range(n)])

Blicken wir nur auf die Argumente der Funktion ``sum_squares`` wissen wir nicht ob die Funktion eine Ganzzahl, eine Fließkommazahl oder eine Zeichenkette, oder irgendetwas anderes erwartet.
Wir müssen deshalb mit Kommentaren kennzeichnen um was es sich handelt, um anderen Entwickler\*innen die Fehlersuche zu erleichtern.
Rufen wir die Methode mit einer Zeichenkette auf z.B. ``sum_square('a')`` wird uns niemand daran hindern und wir bemerken unseren Fehler erst, wenn das Programm abstürzt.

Eine recht neue Möglichkeit ist es den Typ direkt im Code anzugeben, es bleibt aber reine Dokumentation und hat keine Wirkung auf die Ausführung:

```python
def sum_squares(n: int) -> int:
    return sum([(i+1)**2 for i in range(n)])
```

In statisch getypten Sprachen wie ``Java``, ``C++`` oder ``Haskell`` (siehe oben), ist dies durch die Definition der Funktion festgelegt.
Hier würde bereits vor dem Start des Programms ein Fehler entstehen, falls wir ``sum_square('a')`` ausführen.
Gerade bei sicherheitsrelevanter Software wie der Flugzeugsteuerung, Finanzsystemen oder großen Businessanwendungen kann dies zum Problem werden.

Ein zweiter Aspekt den man gut oder schlecht finden kann ist, dass es ``Python`` den Entwickler\*innen erschwert ihren Code als geistiges Eigentum zu schützen. 

Heute ist ``Python`` eine der populärsten Sprachen mit dem Potenzial immer weiter an Fahrt aufzunehmen.
Sie hat eine sehr leserliche **Syntax**, ein herausragendes **Ökosystem**, ist in sehr vielen **Anwendungsbereichen** anzutreffen (Tendenz steigend) und bietet bei richtiger Verwendung auch gute **Performance**.
Deshalb ist ``Python`` eine ausgezeichnete Wahl.