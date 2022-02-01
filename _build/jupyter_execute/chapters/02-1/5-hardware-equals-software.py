(sec-computability)=
# Berechenbarkeit

In diesem Abschnitt tauchen wir in die theoretische Informatik ein und widmen uns der Frage was wir überhaupt berechnen können (**Berechenbarkeit**).
In diesem Zusammenhang folgt unweigerlich die Frage: Welche Mittel benötigen wir um eines der berechenbaren Probleme zu berechnen (**Turing-Vollständigkeit**)?
Und was benötigen wir um jedes dieser Probleme berechnen zu können (**universelle Turingmaschine**)?

Beginnen wir mit einer kurzen Untersuchung von Hard- und Software, d.h., Bauteile des Computers und Programmcode.
Stellen Sie sich vor Sie haben einen Addierer als Bauteil, also als *Hardware* zur Verfügung haben.
Und dass der Befehl ``ladd(a,b)`` diesen realisiert, d.h., die beiden Binärzahlen ``a`` und ``b`` durch ein Bauteil addiert.
Wir haben gesehen, wie dies durch ein *Gatterzusammenschluss* (siehe [Manipulation](sec-manipulation)) möglich ist.

Um zwei Zahlen ``a``, ``b`` zu multiplizieren könnten wir aus mehreren Addierern einen Multiplizierer bauen.
Wir können also durch Komposition von bereits existierenden Bauteilen ein neues Bauteil mit einer neuen Funktion konstruieren.
Doch genauso gut können wir durch Programmcode den Addierer mehrfach aufrufen und erhalten so das gleiche Endergebnis.

# Transformation einer Zahl in Decimaldarstellung zu ihrer Binärdarstellung
def to_binary(number):
    binary_number = []
    while number != 0:
        r = number % 2
        number = number // 2
        binary_number = [r] + binary_number
    return binary_number

# Transformation einer Zahl in Binärdarstellung zu ihrer Decimaldarstellung
def to_decimal(binary_number):
    decimal_number = 0
    i = len(binary_number)-1
    for bit in binary_number:
        decimal_number += bit * 2**i
        i += -1
    return decimal_number
# Zahl in Binärdarstellung 111 0100 1111 wird umgewandelt

def ladd(a,b): # Wir nehmen an diese Funktion wird durch Bauteile/Hardware umgesetzt
    return to_binary(to_decimal(a) + to_decimal(b))

def mul(a, b):  # Wir nehmen an diese Funktion durch Code/Software umgesetzt
    result = [0 for i in range(len(a))]
    for _ in range(to_decimal(b)): # Python versteht unser Binärsystem nicht
        result = ladd(result,a)
    return result

print(f'{[0,0,1,1]} * {[1,0,0,1]} = {mul([0,0,1,1], [1,0,0,1])}')
print(f'{to_decimal([0,0,1,1])} * {to_decimal([1,0,0,1])} = {to_decimal(mul([0,0,1,1], [1,0,0,1]))}')

Halten wir also fest: Wir können einen Multiplizierer als Bauteil konstruieren, z.B. indem wir mehrere Addierer hintereinander schalten, oder wir schreiben Programmcode der die Multiplikation durch das mehrfache Aufrufen des Addierers realisiert.
Wo liegt hierbei der Unterschied?

Interessiert uns nur das Ergebnis, so ist es egal welche der beiden Methoden wir verwenden.
Im Endeffekt sparen wir uns bei der zweiten Berechnung ein Bauteil.
In der Praxis spielt es allerdings eine entscheidende Rolle wie lange die Berechnung dauert.
Ein Multiplizierer der als Bauteil vorliegt, wird seine Arbeit deutlich schneller verrichten, als die Summe der Aufrufe des Addierers.
Werden bestimmte Berechnungen sehr häufig benötigt, so ist es sinnvoll darüber nachzudenken ob man für diese nicht extra angefertigte Bauteile anbietet.

Die Grafikkarte (GPU) ist ein solches Beispiel.
Theoretisch kann die [CPU](def-cpu) all das berechnen, was die Grafikkarte berechnen kann.
Allerdings ist die Grafikkarte darauf optimiert eine bestimmte Operation auf eine Vielzahl an Daten parallel anzuwenden (Single Instruction Multiple Data).
Moderne CPUs können das mittlerweile auch, allerdings ist deren Parallelität geringer, d.h., sie besitzen weniger Prozessorkerne.
Auch verwenden viele Grafikkarten eine weniger genaue Darstellung der Fließkommazahlen, da bei der Generierung von Bildern oder Animationen kleine Fehler nicht auffallen.
Moderne Grafikkarten werden wegen ihres hohen Datendurchsatzes heute für das *maschinelle Lernen* eingesetzt.
Sie haben dazu Bauteile mit denen sich die Matrixmultiplikation kleiner Matrizen sehr effizient berechnen lässt.

Software steuert die Hardware an.
Es besteht hier also eine Art Umweg.
Löst ein Bauteil das Problem so ist es mit sehr großer Wahrscheinlichkeit schneller als jede Softwarelösung.

Auf algorithmischer Ebene ähneln sich Hardware und Software sehr.
Sie gleichen sich mit dem feinen Unterschied, dass Software eine bestimmte Hardware benötigt um überhaupt lauffähig zu sein.

## Turingmaschinen

Wir haben gesehen, dass der Unterschied zwischen Hard- uns Software geringer ist als wir vielleicht angenommen hatten.
Klar ist aber auch, dass ein Computer ohne Hardware nicht funktionieren wird.
Wir können nun die zentralen Fragen der Informatik stellen. 
Salopp fragen wir: 

>'Wie viel' Hardware braucht es denn?

Oder genauer gefragt:

>Welche Eigenschaften muss meine Maschine haben, damit ich all das berechnen kann was berechenbar ist?

Und

>Was können wir überhaupt berechnen?

Beide Fragen wollte Alan Turing mit seinem Berechnungsmodell, d.h., mit seiner *Turingmaschine* beantworten.

```{figure} ../../figs/digital-computer/computability/tm.png
---
height: 200px
name: fig-tm
---
Skizze eine Turingmaschine die sich gerade in Zustand $q_4$ befindet.
```

Die [Turingmaschine (TM)](https://de.wikipedia.org/wiki/Turingmaschine) besteht aus gerade einmal so viel Hardware, dass sie all das berechnen kann, was allgemein als berechenbar gilt.

```{admonition} Turingmaschine (informell)
:name: info-turingmaschine
:class: definition

Eine *Turingmaschine* $T$ besteht aus:

1. Einem **unendlich langen Band** (unendlichen Speicher) aus Zellen
2. Einem **Schreib-/Lesekopf**
3. Einer **endlichen Übergangstabelle** $\delta$
4. Einer **endlichen Zustandsmenge** $Q$
5. Eine **endliche Endzustandsmenge** $F \subseteq Q$

Der Schreib-/Lesekopf ließt oder schreibt $0$, $1$ oder $\#$ in jeder Zeiteinheit an seine aktuelle Zelle auf dem Band.
Dabei steht $\#$ für eine unbeschriebene Zelle, also das Leerzeichen.
Der Kopf kann zudem in einer Zeiteinheit eine Zelle nach links oder rechts fahren oder stehenbleiben.

Die Maschine befindet sich in einem von endlich vielen Zuständen.

Gegeben der Zustand $q$ und das beim Schreib-/Lesekopf stehende Zeichen $a \in \{0, 1, \#\}$, gibt die Übergangstabelle an:

1. Den Zustand $p$ den die Maschine einnimmt
2. Das Zeichen was sie aufs Band schreibt
3. Ob sich der Schreib-/Lesekopf nach links $\text{L}$, rechts $\text{R}$, oder gar nicht $\text{N}$ bewegt.

Die Turingmaschine befindet sich zu Beginn in einem Startzustand $q_0$ und die Eingabe befindet sich zu beginn auf dem Band.
Läuft die Turingmaschine irgendwann in einen Endzustand $q_e \in E$, so ist das was auf dem Band steht das berechnete Ergebnis.
Die Turingmaschine $T$ berechnet $T(w)$ für eine Eingabe(wort) $w$.
```

Übertragen auf Software, bilden die endliche Übergangstabelle $\delta$ und die Zustandsmengen $Q$, $F$ ein Programm.
Diese Tabelle fassen wir auch als Funktion 

$$\delta : Q \times \{0, 1, \# \} \rightarrow Q \times \{0, 1, \#\} \times \{\text{L}, \text{R}, \text{N}\}$$

auf, wobei der Definitionsbereich und der Wertebereich endliche Mengen sind.
Befindet sich die Maschine in Zustand $q$ und steht auf der aktuellen Zelle (dort wo der Schreib-/Lesekopf steht) eine 1, so liefert 

$$\delta(q, 1)$$

das was die Maschine zu tun hat, z.B., $(p, 1, \text{N})$, also gehe in Zustand $p$, schreibe eine 1 und bewege deinen Kopf nicht.

Je nachdem was wir berechnen wollen, müssen wir ein entsprechendes Programm formulieren, d.h. eine Zustandsmenge $Q$ und eine Übergangstabelle $\delta$.
Da die Turingmaschine nur sehr simple Operationen erlaubt, ist es nicht einfach ein Programm für sie zu schreiben.
Schon das Addieren von zwei Zahlen ist eine Herausforderung.
Folgende Zustandsmengen $Q = \{q_0, q_e\}, F = \{q_e\}$ und $\delta$:

| $\{0, 1, \# \}$ | $Q$   | $\{0, 1, \# \}$ | $\{\text{L}, \text{R}, \text{N}\}$ |   $Q$ |
| --------------- | :---- | --------------: | ---------------------------------: | ----: |
| 1               | $q_0$ |               0 |                         $\text{R}$ | $q_0$ |
| 0               | $q_0$ |               1 |                         $\text{R}$ | $q_0$ |
| $\#$            | $q_0$ |            $\#$ |                         $\text{R}$ | $q_e$ |

berechnet das Komplement einer Binärzahl.
Dabei gehen wir davon aus, dass der Schreib-/Lesekopf auf das erste Zeichen der Eingabe zeigt (links).
Die Maschine bewegt ihren Kopf einmal von links nach rechts und schreibt eine 0 wenn sie eine 1 ließt und eine 1 wenn sie eine 0 ließt.
Sobald sie ein Leerzeichen $\#$ ließt bleibt geht sie in den Endzustand $q_e$. 

```{admonition} Allgemeine Berechenbarkeit
:name: def-computable
:class: definition

Ein Problem ist *berechenbar*, wenn für jenes Problem eine Lösung berechnet werden kann.

```

Der Schreib-/Lesekopf können wir als CPU und das Band als Speicher interpretieren.
Die Endlichkeit von $Q$, $F$ und $\delta$ garantiert, dass unser Algorithmus durch endlich viel Text niedergeschrieben werden kann.
Die Turingmaschine geht davon aus, dass ihr unendlich viel Speicher zur Verfügung steht.
Das stellt aber kein Problem dar, denn sofern die Maschine stehen bleibt (unser Algorithmus terminiert) kann sie nur endlich viel Zellen auf dem Band abgefahren haben.

```{admonition} Turing-Berechenbarkeit
:name: def-turing-computable
:class: definition

Ein Problem ist genau dann *Turing-berechenbar*, wenn eine Turingmaschine existiert, die bei jeder Eingabe hält und die Lösung bei entsprechender Eingabe berechnet.

```

Die Probleme die wir mit der *Turingmaschine* berechnen können, bilden eine gewisse Problemklasse.
Nach der unbeweisbaren *Turing-Church-These* handelt es sich bei diesen Problemen um all diejenigen die im {prf:ref}`allgemeinen berechenbar <def-computable>` sind.
Das heißt eine *Turingmaschine* kann alles berechnen was wir vermutlich allgemein berechnet können.

```{admonition} Turing-Church-These (unbeweisbar)
:name: def-church-these
:class: conjecture

Ein Problem ist genau dann *berechenbar*, wenn es auch *Turing-berechenbar* ist.

```

Nehmen wir an die *Turing-Church-These* trifft zu, so wissen wir was **berechenbar** ist und wie viel Hardware es braucht!
Wir brauchen soviel Hardware, dass unser Computer all das kann was eine *Turingmaschine* kann.

Alan Turing definierte den Begriff der *Turing-Vollständigkeit*.
Eine Rechenmaschine die *Turing-vollständig* ist, kann all das berechnen was eine Turingmaschine berechnen kann.

```{admonition} Turing-Vollständigkeit
:name: def-turing-complete
:class: definition

Eine Rechenmaschine (oder Programmiersprache) ist *Turing-vollständig* genau dann wenn sie all das berechnen kann was eine Turingmaschine berechnen kann.

```

Wenn Sie also verstehen möchten, 'wie viel Hardware' ein Computer braucht, lohnt sich ein Blick hin zur Turingmaschine.
Uns ist klar, dass es sich dabei um ein sehr theoretisches Konstrukt handelt.
Wir ersparen Ihnen die formale Definition und möchten Sie dennoch bestärken ein intuitives Verständnis über die Turingmaschine während Ihres Studiums aufzubauen.

Die Turingmaschine kommt mit erstaunlich wenig Hardware aus.
Ein pfiffige Bastler\*innen können diese Maschine als Heimwerkerprojekt im Keller bauen.
Es steht ihnen zwar kein unendliches Band zur Verfügung doch falls ein Algorithmus terminiert, kann der Schreib-/Lesekopf nur eine endliche Distanz fahren und somit ist ein endliches Band ausreichend.
Wie lange dies jedoch sein muss ist im Vornhinein unklar.

```{figure} ../../figs/model-of-a-tm.jpeg
---
height: 200px
name: model-of-a-tm-2
---
Eine konkrete Konstruktion einer Turingmaschine.
```

(sec-utm)=
## Die universelle Turingmaschine

Bis heute können wir jedes berechenbare Problem durch eine bestimmte Turingmaschine berechnen.
Natürlich müssen wir eine *Turingmaschine* für das jeweilige Problem konstruieren.
Ein Computer löst aber nicht nur ein bestimmtes Problem, sondern ist im Stande **jedes** Problem, was durch eine Turingmaschine gelöst werden kann zu berechnen.

Ein Computer ist das Pendant zu einer ganz bestimmten Turingmaschine, der *universellen Turingmaschine (UTM)*.
Die universelle Turingmaschine $U$ (Computer) erhält als Eingabe eine Beschreibung einer andere Turingmaschine $\alpha_T$ (Programm) und die Eingabe(wort) $w$ der Turingmaschine $T$.
Sie simuliert $T$ unter der Eingabe $w$

$$U(\alpha_T, w) = T(w)$$

Das heißt die universelle Turingmaschine $U$ berechnet das was die Turingmaschine $T$ berechnen würde, indem Sie diese simuliert.

Da eine Turingmaschine $T$ durch $\delta$, $Q$ und $F$ vollständig beschrieben ist und all diese Mengen endlich sind, ist sichergestellt dass auch $\alpha_T$ endlich ist.
Der Repräsentant von $\alpha_T$ muss ein Binärcode sein, sodass wir ihn auf das Band von $U$ schreiben können.
Wie $U$ genau aussieht werden wir uns nicht ansehen.
Sie können sich denken, dass die Übergangstabelle von $U$ sehr groß ist.

```{admonition} Universelle Turingmaschine (informell)
:name: info-universal-turing-machine
:class: definition

Eine *universelle Turingmaschine* $U$ ist eine Turingmaschine, die eine beliebige Turingmaschine $T$ auf beliebiger Eingabe $w$ simuliert.

```

## Das Halteproblem

Das Halteproblem ist eines der bekanntesten Probleme der Informatik, da es wesentliche Implikationen über die Mächtigkeit von Computern offenlegt.
Wir würden uns als Programmierer\*innen wünschen, dass es Programm gäbe, dass uns für ein anderes beliebiges Programm mit einer bestimmten Eingabe verrät ob dieses auch halten wird oder ob wir in einer Endlosschleife laufen.

```{admonition} Das Halteproblem
:name: def-halting-problem
:class: definition

Gegeben eine Beschreibung $\alpha_T$ einer Turingmaschine $T$ und deren Eingabe $w$, so verlangt das Halteproblem, nach der Antwort der Frage ob $T(w)$ hält oder nicht.

```

Leider hat sich herausgestellt, dass das Halteproblem nicht berechenbar ist.

```{admonition} Unberechenbarkeit des Halteproblems
:name: theorem-halting-problem-theorem
:class: theorem

Das Halteproblem ist nicht berechenbar.
```

Wir können natürlich $T(w)$ ausführen und einfach abwarten ob die Turingmaschine $T$ hält oder nicht.
Wenn sie aber nicht hält, können wir das niemals feststellen -- wir müssten unendlich lange warten.

Das bedeutet: Es wird niemals einen Algorithmus geben (geschrieben in einer Turing-vollständigen Sprache), welcher für beliebige Programme prüfen kann ob diese auch terminieren.
Das bedeutet jedoch nicht, dass wir dies nicht im Einzelfall selbst prüfen können oder das es Programme gibt, die für viele Programme prüfen können ob diese terminieren.
Es gibt also Hoffnung.

(sec-essenz-of-computers-and-languages)=
## Zusammenfassung

Weshalb reiten wir so auf diesen theoretischen Konzepten herum?
Was kümmern uns imaginäre Turingmaschinen?
Diese Maschinen können zwar all das berechnen was ein Computer berechnet, funktionieren aber doch ganz anders.
Insbesondere sind sie extrem langsam.

Computer und Programmiersprachen sind Werkzeuge um unsere Konzepte welche durch [Computational Thinking](sec-what-is-ct) entstehen zu realisieren.
Was aber können wir überhaupt mit diesen Werkzeugen realisieren?
Die Antwort folgt aus der eben besprochenen Turingmaschine, denn jeder Ihnen bekannte Computer und jede Programmiersprache welche Sie erlernen werden ist {prf:ref}`Turing-vollständig <def-turing-complete>`!

Jeder Computer kann genau das berechnen, was eine Turingmaschine berechnen kann.
Selbstverständlich arbeiten Computer mit vollkommen anderen Bauteilen, was sie viel effizienter macht.
Im wesentlichen sind sie dennoch nichts anderes als effiziente Turingmaschinen.
John von Neumann's Prinzip des [speicherprogrammierten Computers](sec-von-neumann) basiert auf Alan Turing's Turingmaschine.

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

1. **Kompilieren**: Da beide Sprachen Turing-vollständig sind, können Sie ein Programm in der Sprache ``B`` schreiben was den Programmcode ``b`` in einen Programmcode ``a`` der Sprache ``A`` überführt, sodass ``a`` das gleiche berechnet wie ``b``. Diesen Vorgang nennen wir *kompilieren*.

2. **Interpretieren**: Wir können auch fortwährend ein Programm ``a`` in ``A`` immer wieder schreiben, welches die nächsten $n$ Befehle von ``b`` simuliert, d.h. den Code in ``b`` Schritt für Schritt ausführt.

```

Man muss sich vor Augen halten, dass Alan Turing bereits 1936 die Grundlagen für alle modernen Computer und Programmiersprachen dieser Welt gelegt hat.

Gehen wir nun zurück zur Frage nach dem Unterschied zwischen Hard-/ und Software.
Der wesentlichen Unterschied zwischen dem Computer (Hardware) und einem Programm (Software) ist die Art und Weise wie die {prf:ref}`Turing-vollständig <def-turing-complete>` realisiert wird -- durch elektrische Bauteile oder einer Programmiersprache.

Programme als auch Computer sind Turingmaschinen und da der Computer Programme, also andere Turingmaschinen, simuliert ist er eine 
{prf:ref}`universelle Turingmaschine <info-universal-turing-machine>`.

```{admonition} Computer sind universelle Turingmaschinen
:name: computer-universal-turing
:class: remark

Ein handelsüblicher Computer ist eine universelle Turingmaschine.

```

Sobald ein Computer Turing-vollständig ist, sind alle weiteren Bauteile ein Bonus.
In der Theorie ist die universelle Turingmaschine ebenso 'schnell' wie ein moderner Computer.
In der Praxis wäre sie allerdings unfassbar langsam.
In der Theorie ist sogar jeder Prozessor 'gleich schnell'.
In der Praxis ist das natürlich nicht der Fall.
Die Turingmaschine hilft uns dabei die Begriffe *schnell*, *schneller* und *langsamer* und *gleich schnell* formal zu definieren.
Wir werden in Abschnitt [Komplexitätstheorie](sec-complexity) sehen, dass diese Komplexitätsklassen uns etwas über die Schwierigkeit eines Problems verraten, doch in der Praxis mit Vorsicht zu genießen sind.

Zusätzliche oder effizientere Hardware dient im wesentlichen der Beschleunigung bestimmter Berechnungen.
Ein Beispiel, was wir oben bereits besprochen haben ist die Grafikkarte (GPU).
In der Theorie ist sie sogar *genauso schnell* wie eine CPU.
Dennoch hat jeder gängige Heim-Computer eine Grafikkarte, da diese für Berechnungen im 3D-Grafikbereich optimiert ist.

Wichtig ist festzuhalten, dass sich Hardware und Software auf konzeptioneller Ebene gleichen.
Hardware ist die Manifestation von Software und Software ist die Manifestation des Computational Thinkings und so entspringt auch Hardware aus dem Computational Thinking!