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

(sec-computability)=
# Berechenbarkeit

## Hardware = Software?

Stellen Sie sich vor Sie haben einen Addierer ``ladd`` als Bauteil, also als *Hardware* realisiert.
Wir stellen uns also vor, dass der Befehl ``ladd(a,b)`` die beiden Binärzahlen ``a`` und ``b`` durch ein Bauteil addiert.
Wir haben gesehen, wie dies durch ein **Gatterzusammenschluss** (siehe [Manipulation](sec-manipulation)) möglich ist.

Um zwei Zahlen ``a``, ``b`` zu multiplizieren könnten wir aus mehreren Addierern einen Multiplizierer bauen.
Wir können also durch Komposition von bereits existierenden Bauteilen ein neues Bauteil mit einer neuen Funktion konstruieren.
Doch genauso gut können wir durch Programmcode den Addierer mehrfach aufrufen und erhalten so das gleiche Endergebnis.

```python
def ladd(a,b): # Wir nehmen an diese Funktion wird durch Bauteile/Hardware umgesetzt
    return to_binary(to_decimal(a) + to_decimal(b))

def mul(a, b):  # Wir nehmen an diese Funktion durch Code/Software umgesetzt
    result = a
    for _ in range(to_decimal(b)): # Python versteht unser Binärsystem nicht
        result = ladd(result,a)
    return result

print(f'{[0,0,1,1]} * {[1,0,0,1]} = {mul([0,0,1,1], [1,0,0,1])}')
print(f'{to_decimal([0,0,1,1])} * {to_decimal([1,0,0,1])} = {to_decimal(mul([0,0,1,1], [1,0,0,1]))}')
```

Was ist also der Unterschied zwischen Hardware (den Gattern) und Software (unserem Code)?
Wir müssen zwei Dinge festhalten:

1. Ein Computer ohne Hardware nicht funktioniert.
2. Logik in Hardware gegossen bringt uns Berechnungsgeschwindigkeit.

Wir werden auf beide Punkte nun eingehen.

## Die Turingmaschine

Auch ein menschlicher Computer benötigt seine mentalen Kräfte sowie Stift und Papier um Berechnungen durchzuführen.
Wir können nun eine der zentralen Fragen der Informatik stellen. 
Salopp fragen wir: 'Wie viel' Hardware braucht es denn. 

Das lässt offen was wir mit der Ansammlung an Hardware überhaupt berechnen wollen.
Wir fragen also eigentlich zwei Fragen:

1. Was kann man überhaupt berechnen?
2. Wie viel Hardware braucht es um alles zu berechnen was man berechnen kann?

Beide Fragen wollte Alan Turing mit seinem Berechnungsmodell, d.h. mit seiner *Turingmaschine* beantworten.

```{admonition} Turingmaschine (informell)
:name: info-turingmaschine

Die *Turingmaschine* besitzt als Speicher ein (1-dimensionales) **unendliches Band**.
Sie hat auch einen **Lese-/Schreibkopf** der in einer Zeiteinheit ein an der aktuellen Position des Kopfes lesen oder schreiben kann.
Die Kopf kann zudem in einer Zeiteinheit eine Position nach links oder rechts fahren.
Sie kann nur $0,1$ oder $\#$ schreiben bzw. lesen.
Dabei steht $\#$ für einen unbeschriebenen Platz also das Leerzeichen.

Die Maschine befindet sich in einem von **endlich vielen Zuständen**.
Zusätzlich hat die Maschine eine **endliche Tabelle an Vorschriften**, diese sagen ihr welche Aktion (Lesen, Schreiben, eins nach rechts fahren, eins nach links fahren) für welchen Zustand und welches aktuelle Zeichen sie durchführen soll.

Die *Turingmaschine* fährt auf dem Band hin und her und schreibt währenddessen $0$, $1$ oder $\#$.
Die (endliche) Eingabe der Maschine befindet sich zu Beginn auf dem Band.

```

Die *Turingmaschine* definiert nun eine gewisse Problemklasse, die sie lösen bzw. berechnen kann.
Nach der unbeweisbaren *Turing-Church-These* handelt es sich bei diesen Problemen um all diejenigen die im allgemeinen **berechenbar** sind.
Das heißt eine *Turingmaschine* alles berechnen was wir vermutlich allgemein berechnet können.

```{admonition} Berechenbar
:name: def-computable

Ein Problem ist *berechenbar*, wenn es für die Lösung ein Algorithmus formuliert werden kann.

```

```{admonition} Turing-Berechenbarkeit
:name: def-turing-computable

Ein Problem ist *Turing-berechenbar*, wenn es für die Lösung eine Turingmaschine existiert.

```

```{admonition} Turing-Church-These (unbeweisbar)
:name: def-church-these

Ein Problem ist genau dann *berechenbar*, wenn es auch *Turing-berechenbar* ist.

```

Nehmen wir an die *Turing-Church-These* trifft zu, so wissen wir was **berechenbar** ist und wie viel Hardware es braucht!
Wir brauchen soviel Hardware, dass unser Computer all das kann was eine *Turingmaschine* kann.
Alan Turing definierte den Begriff der *Turing-Vollständigkeit*.
Eine Rechenmaschine die *Turing-vollständig* ist, kann all das berechnen was eine *Turingmaschine* berechnen kann.
Nach der unbeweisbaren *Turing-Church-These* kann eine *Turingmaschine* alles berechnen was wir allgemein berechnet können.

```{admonition} Turing-vollständig
:name: def-turing-complete

Eine Rechenmaschine (oder Programmiersprache) ist *Turing-vollständig* genau dann wenn sie all das berechnen kann was eine *Turingmaschine* berechnen kann.

```

Wenn Sie also verstehen möchten, 'wie viel Hardware' ein Computer braucht, lohnt sich ein Blick hin zur *Turingmaschine*.
Uns ist klar, dass es sich dabei um ein sehr theoretisches Konstrukt handelt.
Wir ersparen Ihnen die formale Definition und möchten Sie dennoch bestärken ein intuitives Verständnis über die *Turingmaschine* während Ihres Studiums aufzubauen.

Die Turingmaschine kommt mit erstaunlich wenig Hardware aus.
Ein pfiffiger Bastler kann diese Maschine als Heimwerkerprojekt in seinem Keller bauen.
Es steht ihm zwar kein unendliches Band zur Verfügung doch falls Ihr Algorithmus terminiert, kann der Schreib-/Lesekopf nur eine endliche Distanz fahren und somit reicht ein endliches Band.
Wie lange dies jedoch sein muss ist im Vornhinein unklar.

```{figure} ../../figs/model-of-a-tm.jpeg
---
height: 200px
name: model-of-a-tm-2
---
Eine konkrete Konstruktion einer Turingmaschine.
```

## Die universelle Turingmaschine

Die *Turingmaschine* löst alle uns bekannten lösbaren Probleme.
Natürlich müssen wir eine *Turingmaschine* für das jeweilige Problem konstruieren.
Wir benötigen die richtigen Zustände, das richtige Alphabet und die richtige Übergangsfunktion.
All diese mathematischen Objekte sind endlich!
Wir können demnach eine Beschreibung einer jeden *Turingmaschine* mit Stift und Papier aufschreiben.
Noch besser!
Wir können diese Beschreibung digitalisieren und als Folge von $0$ und $1$ auf das Band einer *Turingmaschine* schreiben.
Da es für jedes (Turing-)berechenbares Problem eine *Turingmaschine* gibt, so gibt es auch eine *Turingmaschine*, welche die *Turingmaschine* die auf dem Band steht simuliert!
Diese Turingmaschine nennen wir **universelle Turingmaschine**.


```{admonition} Universelle Turingmaschine (informell)
:name: info-universal-turing-machine

Eine *universelle Turingmaschine* ist eine *Turingmaschine*, die eine beliebige *Turingmaschine* auf beliebiger Eingabe simuliert.

```

Das heißt die *universelle Turingmaschine* berechnet das was die *Turingmaschine* berechnen würde, indem Sie diese simuliert.

(sec-essenz-of-computers-and-languages)=
## Essenz der Computer und Programmiersprachen

Weshalb reiten wir so auf diesen theoretischen Konzepten herum?
Was kümmern mich imaginäre *Turingmaschinen*?
Computer und Programmiersprachen sind beidesamt Werkzeuge um *Computational Thinking* zu realisieren.
Was aber können wir überhaupt mit diesen Werkzeugen realisieren?
Die Antwort folgt aus der eben besprochenen *Turingmaschine*, denn jeder Ihnen bekannte Computer und jede Programmiersprache welche Sie erlernen werden ist **Turing-vollständig**!

Jeder Computer kann genau das berechnen, was eine *Turingmaschine* berechnen kann.
Selbstverständlich arbeiten Computer mit vollkommen anderen Bauteilen, was sie viel effizienter macht.
Im wesentlichen sind sie dennoch nichts anderes als effiziente *Turingmaschinen*.
John von Neumann's Prinzip des [speicherprogrammierten Computers](sec-von-neumann) basiert auf Alan Turings *Turingmaschine*

Für alle gängigen Programmiersprachen gilt, dass Sie mit ihnen Algorithmen formulieren können, die eine Lösung berechnen, welche auch von einer *Turingmaschine* berechnet werden kann!

```{exercise} Kompilieren und Interpretieren
:label: programming-languages-turing-exercise
Angenommen Sie haben zwei Turing-vollständige Programmiersprachen ``A`` und ``B``.
Können Sie mit der Sprache ``A`` ein Programm ``a`` schreiben, welches Programmcode ``b`` der Sprache ``B`` für eine beliebige Eingabe simuliert?
```

```{solution} programming-languages-turing-exercise
:label: programming-languages-turing-solution
:class: dropdown
Ja das ist möglich!

1. **Kompilieren**: da beide Sprachen Turing-vollständig sind können ein Programm schreiben was den Programmcode ``b`` in einen Programmcode der Sprache ``A`` überführt, sodass der Code in ``A`` das gleiche berechnet wie ``b``. Diesen Vorgang nennen wir *kompilieren*.

2. **Interpretieren**: wir können auch ein Programm in ``A`` schreiben, welches die Befehle von ``b`` simuliert, d.h. den Code in ``b`` Schritt für Schritt ausführt.

```

Man muss sich vor Augen halten, dass Alan Turing bereits 1936 die grundlagen für alle modernen Computer und Programmiersprachen dieser Welt gelegt hat.

Gehen wir nun zurück zur Frage nach dem Unterschied zwischen Hard-/ und Software.
Der wesentlichen Unterschied zwischen dem Computer (Hardware) und einem Programm (Software) ist die Art und Weise wie die *Turing-Vollständigkeit* realisiert wird -- durch elektrische Bauteile oder einer Programmiersprache.

Programme wie auch Computer sind *Turingmaschinen* und da der Computer Programme also andere *Turingmaschinen* simuliert ist er eine *universelle Turingmaschine*.

```{admonition} Computer sind universelle Turingmaschinen
:name: computer-uinversal-turing
:class: attention

Ein handelsüblicher Computer ist eine universelle Turingmaschine.

```

Programme sind ebenfalls *Turingmaschinen* welche von Computern simuliert werden.
Es gibt auch Programme sogenannte *Interpreter*, welche beliebige Programme die in einer anderen Sprache sind simulieren können.
Diese *Interpreter* sind universelle Turingmaschinen.

Sobald ein Computer *Turing-vollständig* ist, sind alle weiteren Bauteile ein Bonus.
Und da auch die *Turingmaschine* ein theoretisches Konstrukt ist (Software), ist jede Hardware eine Realisierung von Software durch (elektrische) Bauteile.

In der Theorie ist die *universelle Turingmaschine* ebenso 'schnell' wie ein moderner Computer.
In der Praxis wäre sie allerdings unfassbar langsam.
In der Theorie ist sogar jeder Prozessor 'gleich schnell'.
In der Praxis ist das natürlich nicht der Fall.
Wir werden später noch darauf eingehen was *schnell*, *schneller* und *langsamer* und *gleich schnell* in der Theorie bedeutet.

Zusätzliche oder effizientere Hardware dient im wesentlichen der Beschleunigung bestimmter Berechnungen.
Zum Beispiel kann die CPU all das Berechnen was eine Grafikkarte (GPU) berechnen kann.
In der Theorie ist sie sogar *genauso schnell*.
Dennoch hat jeder gängige Heim-Computer eine Grafikkarte, warum?
Nun die CPU ist dazu gebaut um viele unterschiedliche Berechnungen extrem schnell nacheinander abzuarbeiten.
Um aber Bilder und Grafiken zu berechnen braucht man viele tausende unabhängige Fließkommazahlenberechnungen (z.B. Matrix-Vektor-Multiplikationen).
Unabhängig bedeutet, dass die Ergebnisse der einzelnen Berechnungen nicht voneinander abhängen und so lassen sich sehr viele Berechnungen gleichzeitig (parallel) ausführen.
Auch akzeptiert man bei Bildern und Grafiken größere Ungenauigkeiten - kleine Fehler ändern Bilder und Grafiken so minimal, dass es dem Auge nicht auffällt.
Deshalb besteht eine GPU aus vielen tausend primitiven Prozessoren die besonders für weniger genaue Fließkommaberechnungen geeignet sind.

Wichtig ist festzuhalten, dass sich Hardware und Software auf konzeptioneller Ebene gleichen.
Hardware ist die Manifestation von Software und Software ist die Manifestation des *Computational Thinings* und so entspringt auch *Hardware* aus dem *Computational Thinking*!