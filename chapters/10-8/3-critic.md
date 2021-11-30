# OOP als Allheilmittel

Fast zeitgleich mit der Zunahme an Popularität der Programmiersprache ``Java`` nahm auch die Objektorientierte Programmierung an Fahrt auf.
Mit seinem Versprechen

>Write once, run everywhere.

war ``Java`` zu dieser Zeit ein echter Hoffnungsstern am Horizont der Programmiersprachen.
Und ``Java`` setzte stark auf die Objektorientierung.
Seither dominiert OOP sie die industrielle Softwareentwicklung.

Der Glaube, dass die OOP der heilige Gral der Programmierung sei hat sich stark und über viele Jahre gehalten.
Es sei das Mittel um Modularität zu ermöglichen und die wachsende Komplexität von Softwarecode in den Griff zu bekommen.
Heute nach über eineinhalb Jahrzehnten haben wir gelernt, dass die OOP keine Allzweckwaffe ist.
Und es drängen neue wie auch alte Ideen in den Vordergrund.

Es gibt Problemstellung die sich wunderbar durch Objekte abbilden lassen.
Klassen bieten eine mächtige Möglichkeit eigene Datentypen zu erzeugen.
Zudem nutzt OOP die Abstraktion, was wir nur begrüßen können.
Auch die Ästhetik Objektorientierter Software kann oftmals entzücken und auch das kann ein wichtiger Faktor sein.
All das ist jedoch nicht auf die Objektorientierung beschränkt.
Klassen lassen sich auch ohne OOP nutzten.
Von langen **Vererbungskaskaden** hält man sich heute ohnehin schon fern.
Die **Polymorphie** ist ebenfalls in vielen anderen Paradigmen zu Hause.
Das was die OOP also wirklich auszeichnet ist die **Kapselung** und diese kann sofern sie exzessive betrieben wird zu Problemen führen.

Aber noch einmal auf Anfang.
Welches Problem wollen wir mit der OOP überhaupt lösen?
Das Hauptproblem großer Softwarepakete ist die Verwaltung des sich ändernden Zustands, d.h. all die **veränderlichen** Daten die im Speicher stehen und sich über den Programmlauf ändern.
Diese Veränderungen, die weitere Veränderungen auslösen, erreichen irgendwann eine Komplexität die undurchschaubar werden kann.
Möchte etwa Funktionalität erweitern, kann dies derart große Auswirkungen auf die Veränderung des Zustands haben, sodass wir unseren Code an sehr vielen Stellen anpassen müssen.
Im Idealfall sollte eine neue Funktionalität oder das Einbauen von Erweiterungen nur dazu führen das wir einen kleinen Bereich des Codes anpassen müssen.
Es sollte so sein, dass wir als Entwickler\*innen keinerlei Befürchtung haben müssen, dass unserer Änderungen unerwartete Seiteneffekte nach sich ziehen.
Wie versucht man dieses Ideal zu erreichen?
Es gibt verschiedene Ansätze.

Wir beginnen das Programmieren indem wir dem prozeduralen bzw. imperativen Programmierparadigma folgen.
Hier kann der Zustand so ziemlich an jeder beliebigen Stelle verändert werden und wir lösen mögliche Probleme mit Seiteneffekten sobald diese auftreten.
Dies ist sozusagen der Standard auf dem wir aufbauen.
Zuständigkeiten werden kaum oder gar nicht gekapselt.
Daten und Funktionen sind voneinander separiert.
Ältere Programmiersprachen wie ``Fortran``, ``C``, ``COBOL`` und ``Pascal`` folgen diesem Paradigma.

In der prozeduralen funktionalen Programmierung versucht man hingegen den Zustand so klein wie möglich zu halten.
Hier setzt man auf viele **unveränderliche Datentypen** und **reine Funktionen**.
``Haskell``, ``Scheme`` und andere reine funktionale Sprachen folgen diesem Paradigma.

Im objektorientierten imperativen Paradigma versucht man im Gegensatz den Zustand in einzelne kleine und handhabbare Teilzustände aufzusplitten (Kapselung).
Daten und Funktionen werden in Klassen gebündelt.
Jeder dieser Teilzustände (ein *Objekt* einer *Klasse*) soll sich selbst, d.h. seinen eigenen Zustand verwalten.
Hier zählen wir ``Java``, ``C#``, ``C++``, ``JavaScript`` und auch ``Python``, allerdings kann man in all diesen Sprachen auch prozedural und auch (teilweise) funktional Programmieren.

Dann gibt es noch das objektorientierte funktionale Paradigma, was eine Kombination der beiden anderen Paradigmen ist.
Das heißt ein möglichst minimaler **veränderbarer Zustand** kombiniert mit **gekapselten Zuständigkeiten**.
Beispiele für Sprachen die diesem Konzept folgen sind z.B. ``Scala`` oder ``F#``.

Wo liegen die Probleme mit der Objektorientierten Programmierung?
Oder noch spezifischer: Weshalb scheitert die **Kapselung** häufig?
Blicken wir auf ein *Objekt*.
Ein *Objekt* sind *private* Daten versteckt hinter einer *öffentlichen* Schnittstelle bestehend aus *öffentlichen* Methoden.
Der Zustand des Objekts lässt sich lediglich über seine Schnittstelle verändern.
Dazu schicken wir Nachrichten (Methodenaufruf) an das Objekt und dieses ändert sich selbst.
Soweit der Idealfall.
Doch selbstverständlich interagieren mehrere Objekte untereinander indem sie sich gegenseitig Nachrichten schicken.
Zeichnen wir einen Abhängigkeitsgraphen eines Objektorientierten Programms ergibt sich ein wust von Knoten (Objekten) und Kanten (Nachrichten).
Ursprünglich sollten diese Nachrichten lediglich Kopien des Teilzustandes und keine Referenzen auf diese Teile des Zustands versenden.
Der Grund: Die Summe aller *Objekte* bilden den Zustand und diese sollten nicht den Zustand anderer Objekte verändern indem diesen anderen Objekten eine Nachricht geschickt wird.
Nehmen wir diese Regel ernst, so muss jedes Objekt welches ein anderes Objekt verändern möchte eine *private* Referenz auf jenes Objekt halten.
Schlussendlich erhalten wir eine Hierarchie an Abhängigkeiten und wir müssen uns dann die Frage stellen: Können wir wirklich noch von einer funktionierenden **Kapselung** sprechen?

Um **Kapselung** zu erreichen kann es passieren dass wir zu früh uns selbst zu viel Struktur auferlegen.
Wir führen möglicherweise künstliche Barrieren ein sodass der Anschein der Kapselung gewahrt wird -- doch ist es dann oftmals eine Kapselung die nichts erzielt.
Wir zwängen alle möglichen Verhalten (Methoden) in bestimmte Datentypen.
Und für Verhalten, zu denen es keinen offensichtlichen Datentyp gibt führen zu Klassen die eben eigentlich keine Datentypen sind sondern lediglich ein Bündel an Funktionen darstellen.
In diesem Fall erhalten wir Objekte mit tollen Namen wie: ``Manager``, ``Factory``, ``Handler``, ``Processor``, ``Caller``, sog. ``Tu-was``-Klassen.

OOP kann auch zu einer übertriebenen Modellierung führen bei der wir die Realität aus den Augen verlieren.
Wir modellieren um dem objektorientierten Paradigma und nicht um die Realität gut abzubilden.
Wir stellen uns Fragen wie:

+ Sollte ein ``Message``-Objekt sich selbst senden?
+ Oder sollte es ein ``Sender``-Objekt mit einer ``send``-Methode?
+ Oder etwa ein ``Receiver``-Objekt mit einer ``receive``-Methode?
+ Oder sollte es eine ``Connection`` mit einer ``transmit``-Methode geben?

Sobald wir die Modellierung der echten Welt verlassen verlassen

```python
class Cat(Animal):
    ...
```

und in die Modellierung eintauchen, die uns die OOP auferlegt 

```python
class ManagerFactory(Factory):
    ...
```

so müssen wir uns Fragen inwieweit wir das objektorientierte Paradigma durchhalten wollen / sollen oder müssen.

Kapselung führt dazu, dass wir Funktionalität zersplittern und auf viele unterschiedliche Klassen aufteilen.
Um die eine Funktionalität zu begreifen müssen wir uns dann häufig durch eine ganze Reihe an Klassen wühlen.
Nehmen Sie mal eine Anwendung mit einer graphischen Oberfläche die im objektorientierten Paradigma programmiert wurde und finden Sie den Code der die Funktionalität eines bestimmten GUI-Elements realisiert.
Sie werden erstaunt sein, wo sich dieser Code befindet und auf wie viele Klassen er sich womöglich verteilt.



OOP wurde und wird noch immer als ein Kommunikationsmittel zwischen Entwickler\*innen und Nicht-Entwickler\*innen verstanden.
Nach dem Motto: Jeder versteht was ein Objekt ist.

Aber es gibt ebenso Problemstellung für die sich ein prozeduraler oder gar funktionaler Programmierstil besser eignet.
Die Idee der Objektorientierung, dass Objekte ihr eigener Zuständigkeitsbereich sind lässt sich in der Praxis oft nicht durchsetzten.
Und oftmals ist es schwer eine bestimmte Logik auf künstliche Art und Weise in ein Objekt zu pressen.
