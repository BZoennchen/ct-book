# Algorithmen
Donald Knuth definiert in seiner Bibel der Programmierung (*The Art of Programming*) einen Algorithmus wie folgt:

>Ein \[Computer-\]Algorithmus ist eine endliche Folge von Anweisung um für eine bestimmte Eingabe eine bestimmte Ausgabe zu erzeugen.
Jede Anweisung bzw. jeder Schritt muss so präzise und unmissverständlich beschrieben sein, sodass er von einer Maschine verstanden und schlussendlich ausgeführt werden kann. -- Donald Knuth (1977)

```{admonition} Algorithmus
:name: def-algorithm
Ein Algorithmus ist eine endliche Folge von unmissverständlich beschriebenen ausführbaren Anweisung (z.B. Text/Programmcode) um für eine bestimmte endliche Eingabe in endlich vielen Schritten eine endliche Ausgabe zu erzeugen (wobei zu jeder Zeit der Ausführung nur endlich viel Speicherplatz verwendet wird).
```

Ein Algorithmus hat demnach folgende Eigenschaften:

1. **Endlichkeit**: Er besteht aus einer endlichen Folge von Anweisungen.
2. **Eindeutigkeit**: Jede Anweisung hat eine eindeutige Bedeutung.
3. **Ausführbarkeit**: Jede Anweisung ist ausführbar.
4. **Gebundenheit**: Bei der Ausführung (unabhängig von der endlichen Eingabe) benötigt der Algorithmus zu jeder Zeit endlich viel Speicher
5. **Terminierung**: Der Algorithmus endet nach endlich vielen Schritten
   
oftmals wird zudem erwartet, dass

1. **Determiniertheit**: Der Algorithmus erzeugt bei gleicher Eingabe auch die gleiche Ausgabe.
2. **Deterministisch**: Während der Ausführung definiert der Algorithmus zu jedem Zeitpunkt die nächste Anweisung.

(sec-what-and-how)=
## Das Was und das Wie

Nach unserer Auffassung muss ein Algorithmus nicht zwangsläufig von einer Maschine verstanden werden.
Die Unmissverständlichkeit bezieht sich hingegen auf einen bestimmten *Kontext* und im Falle der von Maschinen ausgeführten Algorithmen gehört die Maschine zu diesem *Kontext*.
So ist ein Kochrezept ein Algorithmus der im *Kontext* der Küche und des Kochens eine (hoffentlich) unmissverständliche endliche Folge von Anweisungen darstellt.
Durch das Ausführen des Kochrezepts können wir mithilfe von bestimmten Kochutensilien (Eingabe) ein bestimmtes Gericht (Ausgabe) zubereiten.

Algorithmen lassen sich auch von der ausführenden Einheit, also der Maschine oder dem Koch loslösen.
Während des entwickeln eines Algorithmus ist uns oft klar was eine bestimmte Anweisung tut, d.h., **was** passiert, doch unklar ist oft **wie** dies realisiert ist.
In der Realwelt sind wir daran gewöhnt.
Wir wissen zwar dass uns der Flieger von München nach Frankfurt bringt, wie das aber im Detail funktioniert ist uns jedoch unklar.
Selbst bei den einfachsten Dingen des Alltags wissen wir sehr oft nicht wie die Dinge genau funktionieren.
Bevor wir uns Gedanken über Hammer und Nagel machen, hauen wir den Hammer in die Wand.

Ein Beispiel aus der Programmiere wäre folgendes: Nehmen wir an ``min`` lieft uns die kleinste und ``max`` die größte Zahl aus einer Liste von Zahlen.
Wir kennen also das **Was**.
**Wie** ``min`` und ``max`` dies realisieren bleibt im folgenden Algorithmus verborgen und selbstverständlich können wir ``min`` btw. ``max`` verwenden ohne das **Wie** zu kennen.

x = [1, 36, 8, 3, 41, -123, 0, 3]
x_min = min(x)
x_max = max(x)
print(x_min)
print(x_max)

Dies ist die Norm.
Ihre Algorithmen werden unmissverständlich sein, was jedoch im Detail auf der ausführenden Einheit passiert, bleibt verborgen.
Je nachdem welche Programmiersprache und welche Bibliotheken/Pakete Sie verwenden, befinden Sie sich näher oder weiter weg von der ausführenden Einheit.
Zusätzlich können Sie sich selbst weiter von ihr entfernen.
Zum Beispiel können wir eine Funktion schreiben, die uns das größte und kleinste Element einer Liste zurückliefert:

def min_and_max(l):
    l_min = min(x)
    l_max = max(x)
    return l_min, l_max

x = [1, 36, 8, 3, 41, -123, 0, 3]
print(min_and_max(x))

Obwohl wir das **Wie** von ``min`` und ``max`` womöglich nicht kennen, wissen wir dass ``min_and_max`` funktioniert, da wir das **Was** von ``min`` und ``max`` kennen.

Je maschinennäher Sie programmieren, desto mehr **Kontrolle** aber auch **Verantwortung** haben Sie über die genaue Umsetzung (das **Wie**).
Die zusätzliche Kontrolle, die Sie dann nicht einfach abgeben können, führt deshalb zu einem höheren **Entwicklungsaufwand**.

```{figure} ../../figs/world-code-computer.png
---
height: 400px
name: fig-world-code-computer
---
Zusammenhang zwischen modellierter Welt, Quellcode und der realen Welt der Computer.
```

Je näher Sie an der Maschine programmieren, desto näher befinden Sie sich in der wirklichen physikalischen Welt der Transistoren und elektrischen Schaltkreise.
Paradoxerweise führt die Nähe zur wirklichen Welt dazu, dass es schwerer wird die wirkliche Welt zu modellieren.
Wir sprechen hier von zwei verschiedenen Welten, der Welt der elektrischen Schaltkreise und beispielsweise der Welt der Planeten oder die Welt des Kartensortierens.

Wie wir uns von der Maschine wegbewegen und so an Abstraktheit gewinnen hat wiederum mit der von uns bereits diskutierten [Interpretation](sec-interpretation) $I$ zu tun.
Die oben beschriebene Funktion ``min_and_max`` führt zu einer neuen Interpretation in welcher ``min_and_max`` ein Repräsentant ist.
Dieser repräsentiert alle notwendigen Anweisungen für die Berechnung und Rückgabe des maximalen und minimalen Elements einer Liste.
``min``, ``max`` ``return l_min, l_max`` können wir als Bedeutungen dieser Interpretation.
Gleichzeitig sind diese Anweisungen wiederum Repräsentanten einer weiteren Interpretation, welche ins Konkretere führt.

Sogenannte Hochsprachen wie ``Python``, ``Java``, ``C#`` abstrahieren die Welt der elektrischen Schaltkreise in eine phantastische Welt aus Datenstrukturen, Variablen, Funktionen, Klassen und Objekte.
Pakete und Bibliotheken reichern diese Welt mit weiteren Algorithmen und Datenstrukturen an.
Diese Pakete und Bibliotheken werden unentwegt von Programmierer\*innen durch *Computational Thinking* erschaffen.
Durch die Abstraktion wird es möglich, dass elektrische Schaltkreise ganze Galaxien simulieren, Fahrzeuge bewegen oder Transaktionen durchführen.
Schlussendlich basiert jedoch alles auf zwei Zuständen, 0 und 1, unvorstellbar vieler winziger elektrischer Bauteile.

## Die Natur eines Algorithmus

Lassen Sie uns noch ein wenig tiefer in die Natur eines Algorithmus einsteigen.
Achtung! Es wird ein wenig philosophisch.

Überlegen Sie sich einmal was die Zahl $2$ eigentlich ist?
Zunächst einmal ist sie ein Zeichen was wir soeben niedergeschrieben haben.
Doch angenommen vor ihnen liegen zwei Äpfel, dann wird die $2$ durch diese zwei Äpfel ausgedrückt.
Wir finden Formen der $2$ an vielen verschiedenen Orden in der realen Welt aber nirgends finden wir DIE eine einzigartige $2$.

Was DIE $2$ wirklich ist, ist ein Problem mit dem sich viele Philosophen schon auseinander gesetzt haben.
Platon ging davon aus, dass es eine echte Welt der Ideen gäbe in der die Idee der $2$ enthalten ist.
Nach seiner Vorstellung tragen alle Repräsentanten der $2$ die Idee der $2$ in sich.
Die Idee der $2$ scheint durch den Repräsentanten hindurch.
Vertreter dieser Strömung (z.b. Gottlob Frege, Kurt Gödel, Hilary Putnam, Penelope Maddy) werden als mathematische Platonisten bezeichnet.

Nominalisten (z.B. Ludwig Wittgenstein, Rudolf Carnap, Harty Field) lehnen diese Ideenwelt ab und definieren die $2$ als Objekt in Raum und Zeit, welches ein Repräsentant aller zwei realen Objekte ist.
So gesehen würde die $2$ aus unserer Welt verschwinden sobald es keine Repräsentanten von ihr mehr gäbe.

Das ist ja alles schön und gut aber was hat das mit den Algorithmen zu tun.
Ein Algorithmus kann auch als ein Repräsentant (oder als eine Idee der Ideenwelt) aufgefasst werden.
Euklid's Algorithmus zum Finden des größten gemeinsamen Teilers ``gcd``, kann in vielen Unterschiedlichen Formen niedergeschrieben werden.
Der Algorithmus kann sogar nur in unserem Kopf existieren.
Ist der ``gcd`` in ``Java`` ein anderer Algorithmus als der in ``Python``?
Ändere ich die Namen meiner Variablen, ist es dann ein anderer Algorithmus?
Darüber lässt sich streiten.
Wir sagen aber gewöhnlich: *Ich habe den ``gcd``-Algorithmus in ``Python`` programmiert* oder *das ist der Pseudocode für den ``gcd``-Algorithmus*.

Ob nun ein Algorithmus ein Re­prä­sen­tant all seiner Realisierungen ist oder ob jede Realisierung ein eigener Algorithmus ist, ist in der Praxis unwichtig.
Dennoch lohnt es sich ein paar Gehirnzellen dieser Fragestellung zu widmen.
Beantworten Sie es für sich selbst.