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

(sec-name-register)=
# Namensregister

Sie kennen womöglich gar keinen ausgedruckten Namensregister mehr.
Vor langer langer Zeit in einer weit entfernten Galaxie gab es noch so etwas wie Telefonbücher und zwar als wirkliches reales Buch!
In einem solchen Buch standen die Telefonnummern der Menschen, welche in einem bestimmten Ort wohnen.

```{admonition} Lernziel
:class: learngoals

In der Übung [Speicher - alles ist eine Liste](sec-memory) hatten wir uns angesehen, wie eine [Liste](sec-list) im Arbeitsspeicher realisiert wird.
In dieser Übung lernen Sie wie aus dieser Liste mittels einer Hashfunktion die zweite wichtige Datenstruktur, das [Wörterbuch / Dictionary](sec-dict) entsteht.
Sie werden Ihr eigenes Wörterbuch Schritt für Schritt entwickeln.
```

Ein Telefonbuch liefert Ihnen für einen gegebenen Namen die zugehörige Telefonnummer der Familie oder Person.
Falls es keine zwei Personen mit dem gleichen Haushalt gibt, so können wir das Telefonbuch als mathematische Funktion interpretieren.
Der Definitionsbereich sind die Namen der Haushalte und der Wertebereich ist die Menge zugehörigen Telefonnummern.

Warum ist ein Buch voller Namen und Telefonnummern nützlich?
Welche wesentliche Eigenschaft des Telefonbuchs macht es nützlich?

```{exercise} Eigenschaft des Telefonbuch
:label: telefonnr-property-exercise
Aufgrund welcher Eigenschaft finden wir im Telefonbuch eine Telefonnummer recht schnell?
```

```{solution} telefonnr-property-exercise
:label: telefonnr-property-solution
:class: dropdown

Das Telefonbuch ist eine nach Namen **sortierte Liste** von Einträgen!

```

## Binäre Suche im Telefonbuch

### Informelle Beschreibung

Wenn wir in einer solchen **sortierten Liste** nach einem Eintrag suchen gehen wir intuitiv anders vor als wenn die Liste unsortiert wäre.
Im Fall der unsortierten Liste bleibt uns nichts anderes übrig als die Liste von vorne bis hinten zu durchsuchen ([lineare Suche](def-linear-search)).

```{exercise} Suchen im Telefonbuch
:label: telefonnr-search-exercise
Beschreiben Sie informell, wie Sie nach der Telefonnummer von Fr. ``Reichel`` suchen.
```

```{solution} telefonnr-search-exercise
:label: telefonnr-search-solution
:class: dropdown

Wir schätzen erst ab wo die Namen mit dem Buchstaben ``R`` beginnen.
Wir schlagen das Buch recht weit hinten auf und betrachten den ersten und letzten Namen der Seite.
Ist der erste Name lexikographisch kleiner und der letzte lexikographisch größer als ``Reichel``, so suchen wir den Namen auf der Seite.

Ist der erste Name lexikographisch größer als ``Reichel``, finden wir den Namen im vorderen Teil des Buches.
Ist der letzte Name lexikographisch kleiner als ``Reichel``, finden wir den Namen im hinteren Teil des Buches.

Wir nehmen den entsprechenden Teil und schlagen die Seite in der Mitte dieses Teils auf.
Den anderen Teil werden wir nie wieder betrachten.

Diesen Prozess wiederholen wir bis wir die entsprechende Seite gefunden haben.
Dann können wir entweder den Namen auf der Seite mit einer [linearen Suche](def-linear-search) auffinden oder die gleiche [binäre Suche](def-binary-search) mit den Namen auf der Seite vollziehen.
```

Im Abschnitt [Sprechen in der Taucherglocke](sec-dive-bell) haben wir unter [Suchalgorithmen](sec-dive-bell-binary-search) bereits diese sogenannte [binäre Suche](def-binary-search) angewendet.
Wir möchten an dieser Stelle ein wenig Formalismus einbringen um eine eindeutigere Beschreibung der [binäre Suche](def-binary-search) zu erhalten.
Wie jede neue Sprache kann der Formalismus abschreckend wirken, doch bietet er ähnlich wie die Programmiersprachen eine Möglichkeit sich unmissverständlich auszudrücken.

### Formale Beschreibung

Bei dieser Gelegenheit stellen wir Ihnen ein häufig verwendetes Konstrukt, den sog. **Komperator**, vor.
Sei also $E$ eine Menge von möglichen Einträgen.
Sei $\mathcal{L} = (e_0, \ldots, e_n), e_i \in E$ ein (geordnetes) Tupel.
Sei 

```{math}
:label: name-register-eq-1
f_E : E \times E \rightarrow \{-1,0,1 \}
```

eine (Komparator-)Funktion (Comparator) oder kurz **Komparator** bezüglich $E$.
Dieser vergleicht zwei Elemente $e_i, e_j \in E$ sodass

```{math}
:label: name-register-eq-2
f_E(e_i, e_j) = 
\begin{cases}
-1, & \quad \text{falls } e_i < e_j\\
+1, & \quad \text{falls } e_i > e_j\\
+0, & \quad \text{sonst}.
\end{cases}
```

Aus $f_E$ lassen sich die Vergleichsoperatoren rekonstruieren:

\begin{gather}
e_i < e_j \iff f(e_i, e_j) = -1 \\
e_i = e_j \iff f(e_i, e_j) = +0 \\
e_i > e_j \iff f(e_i, e_j) = +1.
\end{gather}

Für das Tupel nehmen wir an dass

```{math}
:label: name-register-eq-3
i < j \Rightarrow f_E(e_i, e_j) \leq 0 ,
```

das heißt, das Tupel ist sortiert. 

Wir suchen nun ein Element $e \in E$.
Schrittweise zerteilen wir die Liste oder das Tupel $\mathcal{L}$ in zwei gleiche Hälften und wählen eine davon.
Dabei passen wir das Intervall $I = [a;b]$ der Listenindices an, welche diese Hälften definieren.

Wir beginnen mit $a_0 = 0, b_0 = |\mathcal{L}|-1$ und berechnen ein Pivotindex 

$$k_0 = a_0 + \left \lfloor{(b_0 - a_0) / 2}\right \rfloor$$

Dabei ist $\left \lfloor{\cdot}\right \rfloor$ das Abrunden.
Falls das Pivotelement $e_{k_0}$ gleich dem gesuchten Element $e$ ist also

$$f_E(e, e_{k_0}) = 0,$$ 

sind wir fertig. Ansonsten passen wir das Suchintervall $I_0 = [a_0;b_0]$ wie folgt an:

$$
a_1 = \begin{cases}
k_0+1, & \quad \text{falls } f_E(e, e_{k_0}) = 1\\
a_0, & \quad \text{sonst}
\end{cases}
$$

$$
b_1 = \begin{cases}
k_0-1, & \quad \text{falls } f_E(e, e_{k_0}) = -1\\
b_0, & \quad \text{sonst}
\end{cases}
$$

Wir haben ein neues Intervall $I_1 = [a_1;b_1]$ und wiederholen die Schritte für die Intervallanpassung bis für irgendeine Iteration $j$

$$e_{k_j} = e$$

oder 

$$a_j < b_j$$ 

gilt.

```{figure} ../../figs/name-register/binary-search.png
---
width: 600px
name: fig-binary-search
---
Binäre Suche nach dem Element $e = 8$ in einer sortierten Liste $\mathcal{L}$ aus Zahlen.
```

```{admonition} Zuweisung (Notation)
:class: remark dropdown

Falls wir uns der mathematischen Schreibweise bedienen vermeiden wir die Zuweisung über das $=$ Zeichen.
$a = 2$ bedeutet, dass $a$ gleich $2$ ist.
Der Ausdruck 

$$a = a + 2$$ 

ist eine falsche Aussage.
Oben haben wir stattdessen viele Variablen verwendet also

$$a_1 = a_0 + 2.$$

Stattdessen können wir auch einen anderen Operator verwenden.
Üblich ist

$$a \leftarrow a + 2.$$
```

Lassen Sie uns ein Beispiel durchgehen.
Angenommen wir haben eine Liste mit $100$ Zahlen und wir suchen die Zahl $e_i$ mit dem Index $i = 66$.
So ist folgende Sequenz die Sequenz der Intervalle:

$$[0;99], [50;99], [50;73], [62;73], [62;66], [65;66], [66;66]$$

```{exercise} Binäre Suchen - Intervalle
:label: binary-search-interval-exercise
Bestimmen Sie die Sequenz der Intervalle für eine Liste mit $150$ Elementen und $i = 48$.
```

```{solution} binary-search-interval-exercise
:label: binary-search-interval-solution
:class: dropdown

$$[0;149], [0;73], [37;73], [37;54], [46;54], [46;49], [48;49]$$

```

### Algorithmische Beschreibung

Die wesentliche Eigenschaft welche die [binäre Suche](def-binary-search) ausnutzt sind in Gleichungen {eq}`name-register-eq-1`, {eq}`name-register-eq-2` und {eq}`name-register-eq-3` zusammengefasst.
Wir benötigen eine [Ordnung](def-math-order), sodass es einen Komparator $f_E$ gibt.
Das Tupel bzw. unsere Liste muss sortiert sein {eq}`name-register-eq-3`.

Der Komparator $f_E$ wird passend zur Menge der möglichen Listenelemente $E$ definiert, d.h. je nachdem welche Art von Liste (Namensliste, Telefonbucheinträge, Zahlen, Klausuren) wir vorfinden, müssen wir ein geeignetes $f_E$ konstruieren. 

Zum Beispiel ist für die Klausuren $f_E(e_i, e_j)$ gleich $-1$ wenn der Name des Studierenden der Klausur $e_i$ lexikographisch kleiner ist als der Name des Studierenden der Klausur $e_j$.
$f_E$ **abstrahiert** alle unwichtigen Eigenschaften der Elemente der gegebenen Liste $\mathcal{L}$.

Wie das passende $f_E$ definiert ist, wissen wir als Entwickler\*innen des Suchalgorithmus nicht und müssen es auch nicht wissen.
Durch $f_E$ haben wir das Problem in zwei Teilprobleme zerlegt:

1. Die Definition des **Komparators** $f_E$, der zur Sortierung der Elemente passt und
2. die Suche unter der Annahme eines wohldefinierten **Komparators**.

Wir lösen lediglich das zweite **Teilproblem**.
Um ersteres müssen sich die Anwender\*innen unseres Suchalgorithmus kümmern.
Durch diese **Abstraktion** schaffen wir es einen Suchalgorithmus zu entwickeln, der **jede beliebige sortierte Liste** durchsuchen kann!

Wir haben aber noch ein Problem!
Nach was wollen wir denn eigentlich Suchen.
In der formalen Beschreibung vergleichen wir die Elemente in der Liste mit dem gesuchten Element.
Doch dieses gesuchte Element wollen wir ja gerade finden!
Wir kennen es nicht aber wir kennen etwas mit dem wir es identifizieren können.
Im Fall des Telefonbuchs, kennen wir den Nachnamen des Eintrags (Elements).
Der Nachname ist ein sogenannter Schlüssel, der ein Element eindeutig identifiziert.

Erneut können wir diesen Schlüssel heraus**abstrahieren**. Erneut erfolgt dies durch eine Funktion

$$g: E \rightarrow \mathcal{K},$$

wobei $\mathcal{K}$ die Menge der Schlüssel ist.
Da wir demnach Schlüssel vergleichen ändern wir den **Komperator** $f_E$ zu

$$f_\mathcal{K}: \mathcal{K} \times \mathcal{K} \rightarrow \{-1,0,1 \}$$


```{exercise} Binäre Suche mit Komperator
:label: binary-search-register-exercise
Transformieren Sie die formale Beschreibung (erneut) in eine ``Python`` Funktion ``binary_search(key, mylist, f, g)``, welche Ihnen das Element mit dem Schlüssel ``key`` zurückgibt.

**Hinweis:** In ``Python`` ist es möglich Funktionen einer anderen Funktion als Argument zu übergeben.
```

````{admonition} Ganzahlendivision (Python)
:name: python-int-division
:class: python
Teilen wir in ``Python`` zwei ganze Zahlen mit ``/`` so erhalten wir eine Fließkommazahl selbst wenn die Division eine Ganzzahl ergeben würde!

```python
print(3/2)
print(type(3/2))
print(4/2)
print(type(4/2))
```

``Python`` bietet aber auch die Ganzzahlendivision ``//`` an bei der das Ergebnis immer eine Ganzzahl ist.
Es wird dabei stets auf die nächst liegende ganze Zahl [abgerundet](def-math-floor).

```python
print(3//2)
print(type(3//2))
print(4//2)
print(type(4//2))
```

````

```{code-cell} python3
def binary_search(key, mylist, f, g = lambda x : x):
    a = 0
    b = len(mylist)-1
    k = (b-a) // 2
    while b-a >= 0:
        if f(key, g(mylist[k])) == 0:
            return mylist[k]
        elif f(key, g(mylist[k])) == -1:
            b = k-1
        else:
            a = k+1
        k = a + (b-a) // 2
    return None
```

In unserer Lösung belegen wir ``g`` mit der Identität als Standardargument.
Das heißt, wenn die Anwender\*innen kein ``g`` spezifizieren, gehen wir davon aus, dass 

$$\mathcal{K} = E$$

gilt.

```{exercise} Binäre Suche von Zahlen mit Komperator
:label: binary-search-register-numbers-exercise
Definieren Sie einen passenden **Komparator** ``cmp_numbers(number1, number2)`` für eine Liste von ganzen Zahlen, d.h. $E = \mathbb{Z}$ und testen Sie diesen und ``binary_search``.
```

```{code-cell} python3
def cmp_numbers(number1, number2):
    if number1 < number2:
        return -1
    elif number1 > number2:
        return 1
    return 0

print(binary_search(1, [1,2,3,4,5], cmp_numbers))
print(binary_search(7, [1,2,3,4,5], cmp_numbers))
print(binary_search(-7, [1,2,3,4,5], cmp_numbers))
```


Lassen Sie uns noch das Telefonbuchbeispiel testen.
Folgender Code generiert Ihnen durch den Aufruf der Funktion ``random_phone_book(n)`` ein zufälliges Telefonbuch mit ``100`` Einträgen (unser Telefonbuch hat keine Seiten sondern nur Einträge).

```{code-cell} python3
import names
import functools as func
import numpy as np

def random_phone_number():
    pre = "0"+func.reduce(lambda a, b : str(a) + str(b), np.random.randint(10, size=3), "")
    post = func.reduce(lambda a, b : str(a) + str(b), np.random.randint(10, size=7), "")
    return pre + "-" + post

def random_phone_book(n):
    telbook = [
        {'name': names.get_last_name(), 'phone_number': random_phone_number()} for _ in range(n)
    ]
    telbook = sorted(telbook, key=lambda x: x['name'])
    return telbook

telbook = random_phone_book(100)
```

Sie müssen den Code nicht verstehen.
Für die Generierung eines zufälligen Namens bedienen wir uns eines Paketes ``names``.
Und auch für die zufällige Telefonnummer setzten wir auf das ``numpy`` Paket.
Jeder Eintrag ist ein [Dictionary](def-python-dictionary) der Form

```python
{'name': name, 'phone_number': telnr}
```

```{exercise} Binäre Suche
:label: binary-search-telbook-exercise

Generieren Sie sich ein zufälliges Telefonbuch und benutzten Sie die Funktion ``binary_search(key, mylist, f, g)`` um einen existierenden Namen ``key`` im Telefonbuch zu finden.
Sie müssen ein geeignetes ``f`` und ``g`` definieren.

**Tipp:** Finden Sie heraus wie ``Python`` Zeichenketten vergleicht.
```

```{code-cell} python3
index = 66
key = telbook[index]['name']
g = lambda entry : entry['name']

def cmp_strings(name1, name2):
    if name1 < name2:
        return -1
    elif name1 > name2:
        return 1
    return 0
    

print(binary_search(key, telbook, cmp_strings, g))
```

````{admonition} Zeichenkettenvergleich (Python)
:class: python
:name: python-string-concat
In ``Python`` werden Zeichenketten lexikographisch verglichen. Zum Beispiel ergibt

```python
"Abraham" < "Anna"
``` 

``True``. 
Jedoch müssen sie auf die Klein- und Großschreibung achten.
So ergibt

```python
"abraham" < "Anna"
``` 

``False``. 
Kleinbuchstaben sind also lexikographisch größer als Großbuchstaben.

````

## Fächer und Markierungen

An Telefonbüchern finden sich häufig *Markierungen*, welche die Suche weiter beschleunigen.
Für jeden Buchstaben finden wir oft eine Markierung, sodass wir genau wissen wo wir Namen mit dem Anfangsbuchstaben, z.B. ``C``, finden.
Anstatt die [binäre Suche](def-binary-search) über alle Einträge durchzuführen, müssen wir lediglich alle Einträge, die mit ``C`` starten betrachten.

```{exercise} Unterstützte binäre Suche
:label: binary-search-supported-exercise

Angenommen jeder Buchstabe kommt als Anfangsbuchstabe gleich häufig vor.
Wie viele Schritte (Intervallanpassungen) sparen Sie sich durch die Markierungen, wenn ihr Telefonbuch 20 000 Einträge enthält?

```

```{solution} binary-search-supported-exercise
:label: binary-search-supported-solution
:class: dropdown

Wir starten mit $20 000 / 26 \approx 769$.

$$20 000 \cdot 2^{-5} < 769 < 20 000 \cdot 2^{-4}$$

Damit sparen wir uns $5$ Schritte.

```

Eine weitere Variante Dinge zu Ordnen ist diese in unterschiedliche leicht identifizierbare *Fächer* zu packen.
Wir könnten zum Beispiel für jeden Anfangsbuchstaben ein Fach eröffnen und alle Seiten des Telefonbuchs in das jeweilige Fach packen.
Dafür müssten wir das Buch natürlich zerschneiden.

Diese zwei Varianten möchten wir uns ansehen 

1. **Fächer:** Eine zweidimensionale Liste.
2. **Markierungen:** Eine eindimensionale Liste unterstützt durch eine Liste aus Markierungen.

Dazu werden wir zunächst Namen aus einer Datei einlesen und doppelte Einträge löschen.

### Eine CSV Datei lesen

Lassen Sie uns diese Markierungen nutzten.
Wir werden dafür eine Liste der beliebtesten 1000 Mädchen- und Jungen-Namen von 1880 bis 2009 in den USA verwenden.
Die Datei ist eine CSV (Comma Seperated Value) Datei.
Eine solche Datei hat meist einen sogenannten *Header* (Kopfzeile) gefolgt von den jeweiligen Daten.
In unserem Fall sieht der Inhalt der Datei wie folgt aus.

```
"year","name","percent","sex"
1880,"John",0.081541,"boy"
1880,"William",0.080511,"boy"
1880,"James",0.050057,"boy"
1880,"Charles",0.045167,"boy"
1880,"George",0.043292,"boy"
...
```

Wir möchten aus dieser Datei lediglich die Namen also die Spalte ``name`` extrahieren.
Mit dem bekannten Modul ``Pandas`` können wir mit solchen Dateien bzw. Daten sehr viel einfacher umgehen.
Doch hier möchten wir selbst Hand anlegen.

Der folgende Code öffnet die Datei ``baby-names.csv`` und ließt diese, sodass nach der Ausführung ``names`` alle Namen von ``baby-names.csv`` enthält (auch doppelte Einträge).
``babynames`` ist eine Sequenz von gelesenen Zeilen der CSV.
Durch ``next(babynames)`` überspringen wir die *Kopfzeile*.
Die ``for``-Schleife iteriert über alle Zeilen.
Jede Zeile ``row`` beinhaltet für jede Spalte einen Eintrag.
``row[0]`` ist das Jahr ``year`` und ``row[0]`` der Name ``name``, den wir extrahieren möchten.

```{code-cell} python3
---
tags: [hide-output]
---
from csv import reader

def read_babynames():
    names = []
    with open('baby-names.csv') as file:
        babynames = reader(file, delimiter=',')
        next(babynames)
        for row in babynames:
            names.append(row[1])
    return names

names = read_babynames()
names
```

### Zählen von doppelten Einträgen

```{exercise} Zählen doppelter Einträge
:label: count-duplicates-exercise
Schreiben Sie eine Funktion ``count(name, names)``, welche die Anzahl der Einträge in ``names``, die gleich ``name`` sind, zurückgibt.
Zählen Sie die Vorkommen von ``John``.
```

```{code-cell} python3
def count(name, names):
    count = 0
    for entry in names:
        if entry == name:
            count +=1 
    return count

count("John", names)
```

Wir möchten nun die Anzahl aller Namen in ``names`` zählen.
Diese Anzahl sagt uns wie oft ein Name von 1880 bis 2008 in den Top 1000 der beliebtesten Namen in den USA war.
Dazu legen wir ein [Dictionary](def-python-dictionary) an, wobei der Schlüssel ``key`` des [Dictionarys](def-python-dictionary) ein Name ist und dessen Wert ``value`` angibt wie oft dieser Name vorkommt.
Zum Beispiel:

```python
countings = {'John': 234, 'Anna': 201, ...}
```

Wir haben die folgenden beiden Funktionen entwickelt:

```{code-cell} python3
def count_all(names):
    countings = {}
    for name in names:
        if name in countings:
            countings[name] = count(name, names)
    return countings
```

und

```{code-cell} python3
def count_all(names):
    countings = {}
    for name in names:
        if name in countings:
            countings[name] += 1
        else:
            countings[name] = 1
    return countings
```

```{exercise} Zählen aller Einträge
:label: count-all-duplicates-exercise
Welche der beiden Varianten ist die bessere? Begründen Sie Ihre Antwort.
```

```{solution} count-all-duplicates-exercise
:label: count-all-duplicates-solution
:class: dropdown

Die zweite Variante ist die bessere, da sie das gleiche Ergebnis in weniger Schritten erzeugt.
``count`` iteriert durch die gesamte Liste ``names`` deshalb benötigen wir in der ersten Variante $n \cdot n$ Schritte und in der zweiten Variante nur $n$ Schritte, wobei $n$ die Länge der Liste ``names`` ist.

```

Dieses Beispiel zeigt, dass es nicht immer von Vorteil ist, ein größeres Problem (``count_all``) durch Teilprobleme (``count``) zu lösen.

Interessanterweise haben wir durch unser Zählen auch gleich alle doppelten Einträge gelöscht, denn wenn wir nun alle Schlüssel des [Dictionary](def-python-dictionary) in eine Liste packen, so beinhaltet diese keine doppelten Einträge mehr.

```{exercise} Einzigartige Einträge
:label: unique-entries-exercise

Sammeln Sie nun alle Schlüssel ein und packen Sie diese in eine Liste.
```

```{code-cell} python3
countings = count_all(names)
unique_names = list(countings.keys())
```

In [Karten sortieren](sec-sort-cards-with-python) haben wir selbst einen Sortieralgorithmus entworfen.
Selbstverständlich hat ``Python`` bereits einen solchen Algorithmus im Angebot.
Diesen haben wir oben beim Generieren des zufälligen Telefonbuchs verwendet.

```{code-cell} python3
sorted?
```

bzw.

```{code-cell} python3
help(sorted)
```

liefert Ihnen Hinweise darüber was die Funktion macht und wie sie zu benutzten ist.


```{exercise} Einzigartige Einträge sortieren
:label: unique-entries-sort-exercise

Verwenden Sie ``sorted`` um ``unique_names``

1. lexikographisch und
2. nach der Anzahl der Einträge in ``names`` (meist vorkommende Name ganz vorne in der Liste)

zu sortieren

```

```{code-cell} python3
unique_names_lex = sorted(unique_names)
unique_names_count = sorted(unique_names, key = lambda entry : countings[entry], reverse=True)
```

### Ordnung durch Fächer 

Mit ``unique_names_lex`` haben wir eine lexikographisch sortierte Liste an beliebten Babynamen in den USA.
Wäre es nicht praktisch sich die Namen, welche mit einem bestimmten Buchstaben beginnen aus der Liste herauszuziehen?
Dies vereinfacht die Suche nach einem bestimmten Namen.
Lassen Sie uns überdenken wie und warum wir Menschen Dinge in *Fächern* (engl. *Buckets*) ordnen.

Wie ordnen wir Menschen ganz alltägliche Dinge?
Zum Beispiel in der Küche oder im Schlafzimmer?
Gläser befinden sich in einem bestimmten Schrank, Teller in einem anderen.
Das Besteck stecken wir in eine Schublade und diese ist oft so aufgeteilt, dass Messer, Löffel und Gabeln sich in je einem separierten Teil befinden.
Hosen trennen wir von anderen Klamotten.
Die Unterwäsche befindet sich an einer ganz bestimmten Stelle im Kleiderschrank.
In einem Ordner sammeln wir Steuerunterlagen in dem anderen Arbeitsverträge oder Zeugnisse.

Warum machen wir das?
Nun damit wir bestimmte Dinge schneller finden.
Anstatt den gesamten Schrank nach einer Hose zu durchsuchen, müssen wir nur einen kleinen Teil durchwühlen.
Diese Ordnung dient natürlich auch der Übersicht.
So sehen wir sehr schnell, wie viele Hosen wir überhaupt besitzen und ob es Zeit wird sich mal wieder eine neue zu besorgen.

Die wesentliche Eigenschaft, die wir diesen Beispielen entziehen können ist, dass wir Dinge *Fächern* zuordnen.
Diese *Fächer* können wir eindeutig und schnell identifizieren bzw. auf diese schnell zugreifen.
So wissen wir in welcher Schublade sich das Besteck befindet und in welchem Unterabteil der Schublade wir zur Gabel greifen.
*Fächer* können sortiert sein, z.B. sind unsere Hemden möglicherweise in einer ganz bestimmten Reihenfolge aufgehängt.
Sie können aber auch unsortiert sein, z.B. sind alle Gabeln durcheinander in einem Schubladenabteil.
Befindet sich eine bestimmte Art von Dingen in einem *Fach* so können wir uns einen Überblick über diese eine Art verschaffen.

Es ist kein Zufall, dass wir Menschen Dinge durch *Fächer* ordnen.
Wir passen uns auch im Alltag den algorithmischen Strukturen an, die uns durch die Natur gegeben sind.
Besonders bei den simpleren Datenstrukturen wird klar, dass es nicht die Informatiker\*innen waren, die diese Strukturen erfunden haben.
Sie haben diese lediglich aus der Natur *abstrahiert*, in ein imaginäres Objekt umgewandelt und schließlich wieder als reales Objekt auf den Computer gebracht.

In der *abstrakten Welt* modellieren wir mehrere *Fächer* meist durch eine einfache Liste.
Jeder Listeneintrag *repräsentiert* ein *Fach*, was wiederum eine Liste aber auch eine andere [Sammlung (Collection)](def-collection) sein kann, siehe untere 
{numref}`Abbildung {number} <fig-buckets>`.

```{figure} ../../figs/name-register/bucket.png
---
width: 600px
name: fig-buckets
---
Fächer als Liste von Listen
```

Da wir eine Liste zur Modellierung verwenden, müssen wir anhand des Listenindex das gewünschte Fach identifizieren können.
In unserem Beispiel brauchen wir eine Funktion ``index_of`` die uns für einen Buchstaben den korrekten Index liefert.

```{code-cell} python3
def index_of(name):
    return ord(name[0]) - ord('A')
```

Wir machen aus ``unique_names_lex`` eine zweidimensionale Liste ``names_by_letter``, sodass

+ ``names_by_letter[0]`` alle Namen die mit ``A`` beginnen enthält, und 
+ ``names_by_letter[1]`` alle Namen die mit ``B`` beginnen enthält, und 
+ ...
+ ``names_by_letter[25]`` alle Namen die mit ``Z`` beginnen enthält. 


```{figure} ../../figs/name-register/babynames.png
---
width: 300px
name: fig-babynames-buckets
---
Babynamen in Fächern
```

```{exercise} Babynamen in Fächern
:label: babynames-buckets-exercise

Schreiben Sie eine Funktion ``to_lex_buckets(unique_names_lex)`` welche Ihnen die [Sammlung](def-collection) aus {numref}`Abbildung {number} <fig-babynames-buckets>` erzeugt.

```

```{code-cell} python3
def to_lex_buckets(unique_names_lex):
    names_by_letter = [[]]
    letter = 'A'

    for name in unique_names_lex:
        while name[0] != letter:
            letter = chr(ord(letter)+1)
            names_by_letter.append([])     
        names_by_letter[index_of(letter)].append(name)
    return names_by_letter

names_by_letter = to_lex_buckets(unique_names_lex)
```

Beachten Sie, dass wir statt einer ``if``-Kondition, eine ``while``-Schleife verwenden.
Warum?
Nun es könnte sein, dass es einen Buchstaben gibt, für den gar kein Name in der Liste ist.

Um mit unserer neuen Datenstruktur zurecht zu kommen, können wir uns weitere Hilfsfunktionen basteln.
Zum Beispiel wäre es praktisch auf ein bestimmtes *Fach* nicht über den Index 0,1,..., 25, sondern über den entsprechenden Buchstaben ``A``,``B``,...,``Z`` zuzugreifen.

```{exercise} Zugriff eines Fachs
:label: access-with-buckets

Schreiben Sie eine Funktion ``get_names(char, names_by_letter)``, die Ihnen für einen Buchstaben ``char`` die Liste mit allen Babynamen, welche mit ``char`` beginnen (der soeben erzeugen Datenstruktur ``names_by_letter``) zurückliefert.

```

```{code-cell} python3
---
tags: [output_scroll]
---
def get_names(char, names_by_letter):
    return names_by_letter[index_of(char)]

get_names('C', names_by_letter)
```

### Ordnung durch Markierungen

Wenn wir ein Telefonbuch genauer betrachten werden wir feststellen, dass es mit gut sichtbaren *Markierungen* versehen ist.
Zum Beispiel finden wir häufig für jeden Anfangsbuchstaben eine solche Markierung.
Wir können diese *Markierungen* auch als *Fächer* interpretieren, denn mithilfe von zwei aufeinanderfolgenden *Markierungen* beschreiben wir ein *Fach*.
Nehmen wir zum Beispiel die Markierung für ``C`` und ``D``, so können wir das *Fach* ``C`` bzw. mit dem Index 2 identifizieren.

Diese Gemeinsamkeit ist ersichtlich doch worin unterscheiden sich *Markierungen* von *Fächern*?
Anders gefragt: Worin unterscheidet sich Ihr Kleiderschrank von einem Telefonbuch im wesentlichen?

```{exercise} Kleiderschrank und Telefonbücher
:label: buckets-vs-marks-exercise

Welche wesentliche Eigenschaft unterscheidet einen Kleiderschrank (*Fächer*) von einem Telefonbuch (*Markierungen*)?

**Hinweis:** Es geht uns um eine Eigenschaft, die sich auf die Implementierung auswirken wird.

```

```{solution} buckets-vs-marks-exercise
:label: buckets-vs-marks-solution
:class: dropdown

Einen Kleiderschrank können wir jederzeit befüllen und leeren, er ist *veränderlich* (engl. *mutable*)!
Wir legen neue Kleider hinein und holen Kleider heraus.

Ein Telefonbuch ist in der Regel *unveränderlich* (engl. *immutable*).
```

Wenn Sie sich unsere Implementierung der *Fächer* ansehen, wird klar, dass wir sehr einfach neue Namen hinzufügen können.
Falls uns doppelte Elemente und die Sortierung innerhalb eines *Fachs* gleichgültig sind, reicht es das Element hinten anzuhängen.
Andernfalls müssen wir die richtige Stelle identifizieren an der wir ein neues Element einfügen wollen.
Wir müssen in jedem Fall nichts an der Anordnung der *Fächer* ändern!

Wie realisieren wir *Markierungen*?
Eine *Markierung* zeigt auf eine bestimmte Seite im Telefonbuch.
Im Beispiel mit den Babynamen, zeigt sie auf einen bestimmten Index der Liste aus Babynamen.
Wir verwenden weiterhin ``unique_names_lex``, fügen aber eine weitere unterstützende Liste ``marks`` hinzu, sodass

+ ``marks[0]`` ist der kleinste Index der Indices der Wörter die mit einem ``A`` beginnen,
+ ``marks[1]`` ist der kleinste Index der Indices der Wörter die mit einem ``B`` beginnen,
+ ...
+ ``marks[25]`` ist der kleinste Index der Indices der Wörter die mit einem ``Z`` beginnen,

```{figure} ../../figs/name-register/marks.png
---
width: 250px
name: fig-babynames-marks
---
Babynamen (rechts) mit Markierungen (links)
```

```{exercise} Markierungen erzeugen
:label: babynames-marks-exercise

Schreiben Sie eine Funktion ``generate_marks(names_by_letter)`` die Ihnen die Markierungen ``marks`` aus {numref}`Abbildung {number} <fig-babynames-marks>` erzeugt.

```

```{code-cell} python3
def generate_marks(names_by_letter):
    marks = [0]
    letter = 'A'
    index = 0
    for name in unique_names_lex:
        while name[0] != letter:
            letter = chr(ord(letter)+1)
            marks.append(index)
        index += 1
    return marks

marks = generate_marks(unique_names_lex)
unique_names_lex[marks[1]-1]
```

Wir können nun sehr einfach durch alle Namen iterieren, die mit einem ``C`` starten:

```{code-cell} python3
---
tags: [output_scroll]
---
marks = generate_marks(unique_names_lex)

mark_index = index_of('C')
for i in range(marks[mark_index], marks[mark_index+1]-1, 1):
    print(unique_names_lex[i])
```

Oder wir können uns eine Teilliste kopieren, die nur Namen beinhaltet die mit ``D`` starten:

```{code-cell} python3
---
tags: [output_scroll]
---
mark_index = index_of('D')
unique_names_lex[marks[mark_index]:marks[mark_index+1]]
```

Wir hatten festgehalten, dass sich ein Telefonbuch mit *Markierungen* nicht verändert.
Welches Problem tritt auf wenn wir Elemente in die Liste der sortierten Babynamen einfügen?

```{exercise} Elemente einfügen und Markierungen anpassen
:label: babynames-marks-insert-exercise

Schreiben Sie folgende Hilfsfunktionen:
1. ``add_name(name, unique_names_lex, marks)``: Fügt einen Namen ``name`` **an die korrekte Stelle** in ``unique_names_lex`` ein.
2. ``remove_name_(name, unique_names_lex, marks)``: Löscht einen Namen ``name`` (falls vorhanden).

Beide Funktionen passen ``marks`` entsprechend an!
Die Sortierung soll erhalten bleiben!
Eventuell macht es Sinn eine weitere Hilfsfunktion ``index_of_element(name, unique_names_lex, marks)`` zu schreiben, welche Ihnen den Index ``i`` des Namen ``name`` in ``unique_names_lex`` zurückliefert.

**Tipp:** Verwenden Sie die Methoden der ``Python``-Liste [append](https://www.w3schools.com/python/ref_list_append.asp), [insert](https://www.w3schools.com/python/ref_list_insert.asp) und [pop](https://www.w3schools.com/python/ref_list_pop.asp).
```

```{code-cell} python3
def index_of_element(name, unique_names_lex, marks):
    if name < unique_names_lex[0]:
        return 0
    
    if name > unique_names_lex[len(unique_names_lex)-1]:
        return len(unique_names_lex)
    
    letter = name[0]
    mark_index = ord(letter)-ord("A")
    start = marks[mark_index]
    end = marks[mark_index+1]
    
    for i in range(start, end, 1):
        if unique_names_lex[i] == name:
            return i
        if unique_names_lex[i] > name:
            if unique_names_lex[i-1] < name:
                return i-1
            
def add_element(name, unique_names_lex, marks):
    # 1. compute index
    index = index_of_element(name, unique_names_lex, marks)

    # 2. insert if name is not contained
    if unique_names_lex[index] != name:
        unique_names_lex.insert(index, name)
       
        # 3. adapt marks
        letter = name[0]
        mark_index = ord(letter)-ord("A")
        for i in range(mark_index+1, len(marks), 1):
            marks[i] +=1
        return True
    return False
    
def remove_element(name, unique_names_lex, marks):
    # 1. compute index
    index = index_of_element(name, unique_names_lex, marks)
    
    # 2. delete if name is contained
    if unique_names_lex[index] == name:
        unique_names_lex.pop(index)
        
        # 3. adapt marks
        letter = name[0]
        mark_index = ord(letter)-ord("A")
        for i in range(mark_index+1, len(marks), 1):
            marks[i] -=1
        return True
    return False
        
print(index_of_element(unique_names_lex[88], unique_names_lex, marks) == 88)
print(index_of_element(unique_names_lex[2388], unique_names_lex, marks) == 2388)
name = "Mustermann"
print(len(unique_names_lex))
add_element(name, unique_names_lex, marks)
print(len(unique_names_lex))
remove_element(name, unique_names_lex, marks)
print(len(unique_names_lex))
```

Immer wenn wir die Liste mit sortierten Babynamen ändern, müssen wir auch ``marks`` anpassen.
Je nachdem wie viele *Markierungen* wir haben, kann dies viel Zeit kosten.

(sec-hashing)=
## Hashing und das Dictionary

In [Speicher - alles ist eine Liste](sec-memory) haben wir uns angesehen wie Listen im [Arbeitsspeicher](def-main-memory) realisiert werden.
Erinnern Sie sich!
Im Speicher liegen nur Zahlen und aus diesen Zahlen haben wir uns den Datentyp Liste gebastelt.

Was wir nicht beschrieben haben ist wie die zweite wesentliche Datenstruktur, das [Dictionary](def-python-dictionary) im Speicher realisiert ist.
Wie der Titel dieser Aufgabe betont, ist alles eine Liste.
Der Arbeitsspeicher ist eine Liste durch den wir ``Python``-[Listen](sec-list) erhalten und die Basis des Dictionary ist Liste die im Speicher liegt.

In diesem Abschnitt werden wir uns gemeinsam erarbeiten wie wir von einer Liste zu einem Wörterbuch/Dictionary gelangen.
Der Schlüssel hierfür sind die sogenannten Hashingverfahren.

Datenstrukturen die das *Hashing* verwenden versuchen die Speicheradresse (siehe [Speicher - alles ist eine Liste](sec-memory)) bzw. den Index eines Elements in einer Liste *direkt* durch einfache arithmetische Operationen aus einem Schlüssel ``key`` des Elements zu berechnen.
Genau genommen verwendet unsere obige Fächer-Datenstruktur ein einfache Hashfunktion, denn wir berechnen anhand des Anfangsbuchstaben eines Elements (d.h. seinem ``key``) einen Index.

Mit 'versuchen' meinen wir, dass zwei unterschiedliche Elemente mit unterschiedlichen Schlüsseln durchaus den gleichen Index ergeben können.
Dies bezeichnen wir als *Kollision*.
Diese Kollisionen müssen wir irgendwie auflösen und wir hoffen, dass wir möglichst weniger solcher Kollisionen erzeugen.

```{admonition} Universum, Schlüssel, Liste und Hashfunktion
:name: def-hashing-universe
:class: definition
Für die weitere Diskussion benötigen wir folgende Definitionen:

+ Ein *Universum* $\mathcal{U}$ an möglichen Schlüsseln, zum Beispiel $\mathcal{U} \subseteq \mathbb{N}_0$,
+ eine Menge an *Schlüsseln* $\mathcal{K} \subseteq \mathcal{U}$,
+ eine Liste $\mathcal{L}$ mit $|\mathcal{L}| = n$, oft auch *Hashtabelle* genannt, und
+ eine *Hashfunktion* $h : \mathcal{U} \rightarrow \{0, \ldots, n-1\}$

```

In unserer Fächer-Datenstruktur, lösen wir Kollisionen auf indem wir alle Elemente mit gleichem Index in eine zweite Liste packen.
Ein solches Verfahren heißt *offenes Hashing mit geschlossener Adressierung*.

```{figure} ../../figs/name-register/open-hashing.png
---
width: 530px
name: fig-open-hashing
---
Offenes Hashing realisiert durch Fächer.
```

```{exercise} Offenes Hashing
:label: name-register-open-hashing-exercise

Benennen Sie $\mathcal{U}$, $\mathcal{K}$, $n$ unserer Fächer-Datenstruktur und beschreiben Sie $h$.

```

```{solution} name-register-open-hashing-exercise
:label: name-register-open-hashing-solution
:class: dropdown

+ $\mathcal{U}$ = alle möglichen Zeichenketten
+ $\mathcal{K}$ = alle Zeichenketten in ``unique_names_lex``
+ $n = 26$
+ $h$: Entspricht ``index_of(name)`` und berechnet aus dem ersten Zeichen einer Zeichenkette die Stelle des Buchstabens im Alphabet (beginnend bei Null).

```

Eine weitere Möglichkeit eine *Kollision* aufzulösen ist es nur eine große Liste zu verwenden.
Tritt eine Kollision auf, so wird nach einem anderen freien Platz gesucht.
Für diese Technik muss $\mathcal{L}$ deutlich größer sein.
Sobald die Liste droht voll zu laufen muss sie vergrößert werden.

Ein solches Verfahren heißt *geschlossenes Hashing mit offener Adressierung*.
In {numref}`Abbildung {number} <fig-closed-hashing>` ist dieses mit einer der einfachsten Kollisionsauflösungen skizziert: Falls ein Platz belegt ist suchen wir aufsteigend nach dem nächst liegenden freien Platz.

```{figure} ../../figs/name-register/closed-hashing.png
---
width: 430px
name: fig-closed-hashing
---
Geschlossenes Hashing
```

Egal welche Technik verwendet wird, eine solche [Sammlung](def-collection) enthält **keine doppelten Schlüssel**.
Wir nennen eine solche [Sammlung](def-collection) auch *Hashtable*.
Ziel ist es in konstant vielen Schritten $(\mathcal{O}(1))$ auf ein beliebiges Element einer solchen [Sammlung](def-collection) 

+ zuzugreifen ``search``,
+ ein Element einzufügen ``insert``,
+ oder zu löschen ``delete``.

### Geschlossenes Hashing

Lassen Sie uns anstatt des *offenen Hashings* das *geschlossene Hashing* aus {numref}`Abbildung {number} <fig-closed-hashing>` verwenden.
Wir möchten dabei zunächst unsere bereits bekannte *Hashfunktion* ``index_of(name)`` einsetzten.
Außerdem gehen wir zunächst davon aus, dass die Menge der Schlüssel erneut unsere Babynamen sind.

```{exercise} Indexsuche
:label: name-register-open-hashing-index-search-exercise

Schreiben Sie eine Funktion ``search_index(name, hashtable)``, welche Ihnen den index des Namens ``name`` der Liste ``hashtable`` anhand der Hashfunktion ``index_of(element)`` liefert.
Gehen Sie davon aus, dass ein Platz in der Liste frei ist wenn dieser gleich ``None`` ist.
```

```{code-cell} python3
def search_index(name, hashtable):
    key = name
    index = index_of(key) % len(hashtable)
    for i in range(len(hashtable)):
        j = (index+i) % len(hashtable)
        if hashtable[j] == key:
            return j
        if hashtable[j] == None:
            return j
    
    # there is no free place left
    return None
```

Wir starten die Suche bei Index ``index_of(key) % len(hashtable)`` um sicher zu gehen, dass der Index nicht außerhalb der Liste liegt.
Dann durchlaufen wir die Liste zyklisch bis wir einen freien Platz finden oder aber festellen, dass die Liste voll ist.

````{exercise} Hashtableverwaltung
:label: name-register-open-hashing-management-exercise

Schreiben Sie mithilfe ``search_index(name, hashtable)`` nun folgende Funktionen:

+ ``contains(name, hashtable)``: Liefert ``True`` genau dann wenn ``name`` sich in der Liste ``hashtable`` befindet.
+ ``get_value(name, hashtable)``: Liefert ``name`` zurück falls es in ``hashtable`` enthalten ist, sonst ``None``.
+ ``insert(name, hashtable)``: Fügt ``name`` in ``hashtable`` falls es noch nicht in ``hashtable`` enthalten ist und gibt ``True`` zurück genau dann wenn ``name`` eingefügt wurde.
+ ``new_hash_table(names)``: Erzeugt unter der Verwendung der Funktion ``insert`` eine neue Liste ``hashtable`` welche alle Namen in der Liste ``names`` enthält.

Testen Sie Ihre Funktionen mithilfe einer kleinen Liste an Namen, z.B.

```python
names = ['Berta', 'Hans', 'Thomas']
```

**Hinweis:** Überlegen Sie sich was Sie machen wenn die Liste voll gelaufen ist!
````

Falls ``hashtable`` voll ist fügen wir den einzufügenden Namen hinten an.

```{code-cell} python3
def index_of(name):
    return ord('A')-ord(name[0])

def search_index(name, hashtable):
    key = name
    index = index_of(key) % len(hashtable)
    for i in range(len(hashtable)):
        j = (index+i) % len(hashtable)
        if hashtable[j] == key:
            return j
        if hashtable[j] == None:
            return j
        
    # there is no free place left
    return len(hashtable)

def contains(name, hashtable):
    index = search_index(name, hashtable)
    return index < len(hashtable) and hashtable[index] == name

def get_value(name, hashtable):
    index = search_index(name, hashtable)
    if index < len(hashtable) and hashtable[index] == name:
        return hashtable[index]
    else:
        None

def insert(name, hashtable):
    index = search_index(name, hashtable)
    while index >= len(hashtable):
        hashtable.append(None)
        
    if hashtable[index] == name:
        return False
    else:
        hashtable[index] = name
        return True

def new_hash_table(names):
    hashtable = [None for i in range(2*len(names) + 8)]
    for name in names:
        insert(name, hashtable)
    return hashtable
```

Lassen Sie uns die Funktionen testen:

```{code-cell} python3
names = ['Berta', 'Hans', 'Thomas']
hashtable = new_hash_table(names)
print(f"hashtable = {hashtable}")
print(f"contains('Dieter', hashtable) = {contains('Dieter', hashtable)}") # False
print(f"contains('Berta', hashtable) = {contains('Berta', hashtable)}") # True
print(f"search_index('Dieter', hashtable) = {search_index('Dieter', hashtable)}") # 11
print(f"search_index('Berta', hashtable) = {search_index('Berta', hashtable)}") # 13
print(f"insert('Dieter', hashtable) = {insert('Dieter', hashtable)}") # True
print(f"insert('Dieter', hashtable) = {insert('Dieter', hashtable)}") # False

# fill the list to test if everything works if it is full
for name in unique_names_lex[0:20]:
    insert(name, hashtable)
    
print(f"hashtable = {hashtable}")

all([search_index(name, hashtable) == index for index, name in enumerate(hashtable)])
```

Die letzte Zeile des Codes erzeugt eine Liste aus boolschen Werten und wertet diese durch ``all`` aus.
``all`` ergibt genau dann ``True`` wenn jeder Wert in der Liste ``True`` ist.
Der Wert am Index ``index`` ist ``True`` genau dann wenn der ``search_index(name, hashtable) = index``, wobei ``name`` am Index ``index`` der Liste ``hashtable`` steht.

Was noch fehlt ist das Löschen eines Elements in unserer Hashtable.
Für das offene Hashing ist dies recht einfach: Wir suchen das Fach und löschen das Element aus diesem heraus.
Für das geschlossenes Hashing ist dies jedoch nicht so einfach!
Angenommen wir fügen die Schlüssel ``'Anna'``, ``'Alex'``, ``'Clara'``, ``'Alba'`` und ``'Fabian'`` nacheinander in eine leere Hashtabelle ein.
Und angenommen wir verwenden als Hashfunktion ``index_of`` und eine *lineare Sondierung*.
Dann erhalten wir als Resultat die Liste aus {numref}`Abbildung {number} <fig-closed-hashing-deletion>`.

```{figure} ../../figs/name-register/closed-hashing-deletion.png
---
width: 600px
name: fig-closed-hashing-deletion
---
Löschvorgang beim geschlossenes Hashing mit linearer Sondierung: Es wird der Schlüssel ``'Alex'`` gelöscht.
```

Wenn wir nun ``'Alex'`` einfach löschen und anschließend nach ``'Alba'`` suchen, werden wir beim Index ``1`` stoppen und diesen Namen nicht mehr finden!
Löschen wir ``'Alex'``, so müssen wir alle Namen die einen größeren Index als ``'Alex'`` haben und lückenlos aufeinander folgen, ebenfalls löschen und erneut einfügen.
Beachten Sie, dass sich die Position von ``'Clare'`` in der Liste in {numref}`Abbildung {number} <fig-closed-hashing-deletion>` nicht verändert, da ``index_of('Clare') == 2``.

```{exercise} Schlüssel löschen
:label: name-register-open-hashing-delete-exercise

Implementieren Sie den beschriebenen Algorithmus zum löschen eines Schlüssels in der Hashtabelle, d.h., implementieren Sie die Funktion ``delete(name, hashtable)``.

```

```{code-cell} python3
def delete(name, hashtable):
    index = search_index(name, hashtable)
    if index < len(hashtable) and hashtable[index] == name:
        hashtable[index] = None
        i = 1
        while(hashtable[index+i] != None):
            value = hashtable[index+i]
            hashtable[index+i] = None
            insert(value, hashtable)
            i += 1
        return True
    else:
        return False
```

Lassen Sie uns das Beispiel aus {numref}`Abbildung {number} <fig-closed-hashing-deletion>` testen:

```{code-cell} python3
names = ['Anna', 'Alex', 'Clara', 'Alba', 'Fabian']
hashtable = new_hash_table(names)
print(hashtable)
delete('Alex', hashtable)
print(hashtable)
```

Nun wird es Zeit unsere Hashtabelle mit den Babynamen aus ``unique_names_lex`` zu befüllen.

```{exercise} Hashtable füllen
:label: name-register-open-hashing-fill-exercise

Füllen Sie nun eine neue ``hashtable`` mit den Namen aus ``unique_names_lex``.
Achten Sie auf die Zeit die dieser Vorgang in Anspruch nimmt.
Was fällt Ihnen auf?
Finden Sie eine Erklärung.

```

```{code-cell} python3
hashtable = new_hash_table(unique_names_lex)
```

```{solution} name-register-open-hashing-fill-exercise
:label: name-register-open-hashing-fill-solution
:class: dropdown

Der Vorgang nimmt eine beachtliche Zeit in Anspruch.
``unique_names_lex`` enthält 6782 Namen.
Unsere Hashfunktion liefert jedoch nur Werte zwischen 0 und 25.
Damit iterieren wir für das Einfügen des $m$-ten Elements über mindestens $m-25$ Elemente.
Insgesamt benötigen wir damit in etwa

$$
\sum_{i=1}^n i = \frac{n \cdot (n+1)}{2}
$$

also 

$$
6782 \cdot 6783 / 2 \approx 23 \cdot 10^6,
$$

d.h., circa 23 Millionen Schritte! In anderen Worten wir haben immens viele Kollisionen.
Unsere Hashfunktion ``index_of`` ist keine gute Hashfunktion!

```

### Hashfunktionen

Was genau ist eine Hashfunktion und wozu ist diese gut?

````{admonition} Hashfunktion
:name: def-hash-function
:class: definition

Eine *Hashfunktion* über einem *Universum* $\mathcal{U}$ (zum Beispiel die Menge aller Zeichenketten)

$$h : \mathcal{U} \rightarrow \{0, \ldots, n\}$$ 

erzeugt durch meist einfache arithmetische Berechnungen aus einem Schlüssel $k \in \mathcal{K} \subseteq \mathcal{U}$ eine natürliche Zahl h(k), sodass

```{math}
:label: name-register-hash-eq-1
k_i = k_j \Rightarrow h(k_i) = h(k_j).
```

Den Wert $h(k)$ nennen wir *Hashwert* oder kurz *Hash* von $k$.
````

Sind zwei Schlüssel verschieden muss die Hashfunktion hingegen keine verschiedenen Zahlen zurückliefern!
Die einfachste gültige und zugleich recht nutzlose Hashfunktion ist eine Konstante, z.B., $h(k) = 0$.

Hashfunktionen werden oft verwendet um zu prüfen ob zwei Schlüssel gleich sind.
Aus Gleichung {eq}`name-register-hash-eq-1` folgt:

```{math}
:label: name-register-hash-eq-2
h(k_i) \neq h(k_j) \Rightarrow k_i \neq k_j.
```

Deshalb wertet man erst die Hashfunktion der beiden Schlüssel aus.
Erst wenn die Hashfunktion die gleichen Werte liefert, prüft man genauer weiter.
Da die Hashfunktion oft sehr schnell ausgewertet werden kann, 
insbesondere wenn 

1. die Ungleichheit wahrscheinlich ist und 
2. wir eine gute Hashfunktion besitzen

sind enorme Ersparnisse der Rechenzeit möglich.
Sie können, zum Beispiel, aus einem riesigen Textdokument einen Hashwert generieren und so zwei Textdokumente auf Gleichheit prüfen.

>Was aber ist eine gute Hashfunktion?

Die erste wichtige Eigenschaft einer guten Hashfunktion $h$ ist, dass diese gut *streut*.
D.h., werten wir alle Hashwerte für unsere Schlüssel $\mathcal{K}$ aus, dann wäre es optimal, wenn jeder Hashwert eindeutig ist, d.h. wenn

$$
k_i \neq k_j \Rightarrow h(k_i) \neq h(k_j) 
$$

gilt.
Ist der Hashwert nahezu zufällig gleichverteilt zwischen $0$ und $n-1$ ist dies ebenfalls eine sehr gute Hashfunktion.

Leider ist das *Universum* $\mathcal{U}$ meistens riesig, insbesondere deutlich größer als die Hashtabelle $\mathcal{L}$.
Kennen wir $\mathcal{K}$ im Voraus und ändert sich diese Menge nicht, dann lässt sich oft eine perfekte Hashfunktion berechnen.
Ein Beispiel sind unsere oben besprochenen Markierungen.

Ein Geburtsdatum oder der Fingerabdruck (in einer Zahl codiert) wären Hashwert einer Person aus dem echten Leben.
Das Geburtsdatum wäre jedoch ein schlechter Hashwert, da er für sehr viele Menschen gleich ist.
Der Fingerabdruck hingegen ist ein sehr guter Hashwert.

Die zweite wichtige Eigenschaft einer guten Hashfunktion $h$ ist, dass ihre Auswertung *billig* ist.
Die Auswertung sollte in konstant vielen Schritten vonstatten gehen.
Nur wenn Sie billig ist, lohnt sich der Umweg über eine Hashfunktion.

### Die Build-in Hashfunktion

Bevor wir unsere eigene verbesserte Hashfunktion schreiben, nutzten wir doch einmal was uns ``Python`` bereits bietet.

````{exercise} Pythons Hashfunktion
:label: name-register-hashing-pythons-hash-exercise

1. Lesen Sie die Dokumentation zur ``Python``-Funktion ``hash``. Sie finden diese [hier](https://docs.python.org/3/library/functions.html?highlight=hash#hash).

2. Verwenden Sie ``hash`` als Ihre Hashfunktion. Bauen Sie dafür die Funktionen aus der vorherigen Aufgabe so um, dass sie diesen eine Hashfunktion ``hash_func`` als Argument übergeben können.
3. Führen Sie anschließend
    ```python
    hashtable = new_hash_table(unique_names_lex, hash_func=hash)
    ```
    aus und beobachten Sie wie lange die Funktion arbeitet.
````

```{code-cell} python3
def index_of(name):
    return ord('A')-ord(name[0])

def search_index(name, hashtable, hash_func=hash):
    key = name
    index = hash_func(key) % len(hashtable)
    for i in range(len(hashtable)):
        j = (index+i) % len(hashtable)
        if hashtable[j] == key:
            return j
        if hashtable[j] == None:
            return j
        
    # there is no free place left
    return len(hashtable)

def contains(name, hashtable, hash_func=hash):
    index = search_index(name, hashtable, hash_func)
    return index < len(hashtable) and hashtable[index] == name

def get_value(name, hashtable, hash_func=hash):
    index = search_index(name, hashtable, hash_func)
    if index < len(hashtable) and hashtable[index] == name:
        return hashtable[index]
    else:
        None

def insert(name, hashtable, hash_func=hash):
    index = search_index(name, hashtable, hash_func)
    while index >= len(hashtable):
        hashtable.append(None)
        
    if hashtable[index] == name:
        return False
    else:
        hashtable[index] = name
        return True

def delete(name, hashtable, hash_func=hash):
    index = search_index(name, hashtable, hash_func)
    if index < len(hashtable) and hashtable[index] == name:
        hashtable[index] = None
        i = 1
        while(hashtable[index+i] != None):
            value = hashtable[index+i]
            hashtable[index+i] = None
            insert(value, hashtable, hash_func)
            i += 1
        return True
    else:
        return False

def new_hash_table(names, hash_func=hash):
    hashtable = [None for i in range(2*len(names) + 8)]
    for name in names:
        insert(name, hashtable, hash_func)
    return hashtable
```

Die Berechnungszeit ist deutlich kürzer.
Lassen Sie uns erneut testen ob alles mit rechten Dingen zugeht.

```{code-cell} python3
hashtable = new_hash_table(unique_names_lex, hash_func=hash)
all([search_index(name, hashtable, hash_func=hash) == index 
     for index, name in enumerate(hashtable) 
     if name != None])
```

```{exercise} Kollisionen zählen
:label: name-register-hashing-countcollisions-exercise

Schreiben Sie eine ``Python``-Funktion ``collisions(hashtable, hash_func)``, welche Ihnen für die Listenelemente der Liste ``hashtable`` die Kollisionen, abhängig von der Hashfunktion ``hash_func`` zählt.
In anderen Worten ``collisions(hashtable, hash_func)`` berechnet die Anzahl die Kollisionen die stattgefunden haben um die Elemente in ``hashtable`` einzufügen.

Vergleiche Sie die Hashfunktionen ``index_of`` und ``hash``.
```

```{code-cell} python3
def collisions(hashtable, hash_func=hash):
    collisions = 0
    for index, key in enumerate(hashtable):
        if key != None:
            j = hash_func(key) % len(hashtable)
            collisions += abs(j-index)
    return collisions
```

```{code-cell} python3
print(f'number of elements: {len(unique_names_lex)}')
print(f' collisions with hash: {collisions(new_hash_table(unique_names_lex, hash), hash)}')         # 16914
print(f' collisions with index_of: {collisions(new_hash_table(unique_names_lex, index_of), index_of)}') # 60751108
```

16914 *Kollisionen* für das Einfügen von 6782 ist ein akzeptabler Schnitt.
Das ist ca. 2.5 Kollision pro Element!
``index_of`` verursacht hingegen über 60 Millionen *Kollisionen*!

Im Abschnitt [Python](sec-python) hatten wir erwähnt, dass ``Python`` aufwendige Berechnungen in ``C/C++``-Coder verlagert.
Dies ist auch für die Funktion ``hash`` der Fall.
Im folgenden zeigen wir ihnen den Code der Hashfunktion ``hash`` für Zeichenketten.
Bitte erschrecken Sie nicht.
Sie brauchen den Code nicht verstehen!
Die Berechnung von Hashwerten sieht oft nach viel Voodoo aus.
Hier werden Zahlen mit sogenannten [Bit](def-bit)-Verschiebungen manipuliert.
Man sieht dem Code an, dass er auf Performance und nicht auf Lesbarkeit getrimmt ist.

```c++
static long
string_hash(PyStringObject *a)
{
    register Py_ssize_t len;
    register unsigned char *p;
    register long x;

#ifdef Py_DEBUG
    assert(_Py_HashSecret_Initialized);
#endif
    if (a->ob_shash != -1)
        return a->ob_shash;
    len = Py_SIZE(a);
    /*
      We make the hash of the empty string be 0, rather than using
      (prefix ^ suffix), since this slightly obfuscates the hash secret
    */
    if (len == 0) {
        a->ob_shash = 0;
        return 0;
    }
    p = (unsigned char *) a->ob_sval;
    x = _Py_HashSecret.prefix;
    x ^= *p << 7;
    while (--len >= 0)
        x = (1000003*x) ^ *p++;
    x ^= Py_SIZE(a);
    x ^= _Py_HashSecret.suffix;
    if (x == -1)
        x = -2;
    a->ob_shash = x;
    return x;
}
```

### Eine eigene gute Hashfunktion

Lassen Sie uns nun unsere eigene verbesserte Hashfunktion entwickeln.
Wir suchen nach einer Funktion, welche verschiedene Zeichenketten in verschiedene natürliche Zahlen umwandelt.
Verwenden wir nur ein Zeichen für die Berechnung ist klar, dass wir nicht mehr als 26 verschiedene Zahlen erwarten können.

Lassen Sie uns deshalb mehrere Zeichen für die Berechnung des Hashwerts verwenden.
Eine erste Idee wäre die Summe der codierten Zeichen:

```{code-cell} python3
def hash_func_sum(name):
    hash_value = 0
    for char in name:
        hash_value += ord(char)
    return hash_value

print(collisions(new_hash_table(unique_names_lex, hash_func_sum), hash_func_sum))
```

Immerhin erreichen wir damit nur noch 20 Millionen *Kollisionen*, was jedoch immernoch viel zu viel ist.
Wie sieht es mit der Multiplikation aus?

```{code-cell} python3
def hash_func_mul(name):
    hash_value = 0
    for char in name:
        hash_value *= ord(char)
    return hash_value

print(collisions(new_hash_table(unique_names_lex, hash_func_mul), hash_func_mul))
```

Etwas schlechter fällt hierfür das Ergebnis aus.

```{exercise} Hashfunktion der Addition und Multiplikation
:label: hash-add-mul-hashmap-exercise
Warum sind die beiden Hashfunktion ``hash_func_sum`` und ``hash_func_mul``, keine besonders guten Hashfunktionen?
```

```{solution} hash-add-mul-hashmap-exercise
:label: hash-add-mul-hashmap-solution
:class: dropdown
Sowohl die Addition als auch die Multiplikation ist kommutativ. Deswegen fließt die Reihenfolge der Zeichen nicht in die Berechnung ein.
``Thomas`` und ``hasToh`` haben den gleichen Hashwert.
```

Erinnern wir uns zurück an die Darstellung von Zahlen im Binär- und Dezimalsystem, siehe [Zahlen im Binärsystem](sec-binary-numbers).
Auch hier haben wir aus einer Folge von Zeichen ``0`` und ``1`` eine **eindeutige Zahl** berechnet.
Aus einer Zahl $b_{n-1} \ldots b_2b_1b_0$ in Binärdarstellung haben wir die eindeutige Dezimalzahl

$$
\sum\limits_{i=0}^n b_i \cdot 2^{i} = b_0 \cdot 2^0 + b_1 \cdot 2^1 + \cdots b_{n-1} \cdot 2^{n-1}
$$

berechnet. Dieses **Berechnungsmuster** können wir wiederverwenden!

Angenommen unsere Zeichenkette, interpretiert als Folge von Zahlen (ASCII), ist $s_{n-1} \ldots s_2s_1s_0$ und $p$ ist irgendeine *Basis*, dann ist 

$$
\sum\limits_{i=0}^n s_i \cdot p^{i} = s_0 \cdot p^0 + s_1 \cdot p^1 + \cdots s_{n-1} \cdot p^{n-1}
$$

eine eindeutige Dezimalzahl sofern $p$ eine valide Basis ist.

Wie im Binärsystem als auch im Dezimalsystem muss $p$ größer sein als alle Ziffern des Zahlensystems.
In unserem Fall müsste $p$ größer sein als ``ord("z")``.
Da wir jedoch keine unbedingte Eindeutigkeit benötigen ist ein kleineres $p$ auch gültig.

Unsere Hashfunktion ist durch

```{math}
:label: name-register-good-hash-function-1
h(s_{n-1} \ldots s_2s_1s_0) = \sum\limits_{i=0}^n s_i \cdot p^{i} = s_0 \cdot p^0 + s_1 \cdot p^1 + \cdots s_{n-1} \cdot p^{n-1}
```

gegeben.

```{exercise} Eindeutigkeit
:label: prime-hashmap-exercise
Was für ein kleines $p$ könnte sich besonders gut eignen und warum?
```

```{solution} prime-hashmap-exercise
:label: prime-hashmap-solution
:class: dropdown
Eine Primzahl $p$ eignet sich besonders gut, da dann die Produkte

$$
s_i \cdot p^{i} \text{ und } s_j \cdot p^{j} \text{ mit } i \neq j
$$ 

nur gleich sein können, wenn $p$ in der Faktorisierung von $s_i$ oder $s_j$ vorkommt.
Ist $p$ keine Primzahl gibt es mehr Möglichkeiten für die Gleichheit der beiden Produkte.
```

Sie sehen, wir tauchen ein wenig in die Zahlentheorie ein.
Dieses mathematische Denken ist auch ein Teil des [Computational Thinkings](sec-what-is-ct).

```{exercise} Eine gute Hashfunktion
:label: good-hashfunction-hashmap-exercise
1. Implementieren Sie die Hashfunktion welche durch Gleichung {eq}`name-register-good-hash-function-1` definiert ist. ``83`` eignet sich als Primzahl (nicht zu klein und groß genug).

2. Testen Sie Ihre neue Hashfunktion durch ``collisions``.
```

```{code-cell} python3
def hash_func(name):
    hash_value = 0
    prime = 83
    for char in name:
        hash_value *= prime
        hash_value += ord(char)
    return hash_value

print(collisions(new_hash_table(unique_names_lex, hash_func), hash_func)) # 3432
```

Wir haben es geschafft!!!
Nur noch 3432 Kollisionen!
Damit sind wir für unseren Fall besser als die ``Python``-Funktion ``hash``.

Allerdings hängt die Berechnungszeit noch von der Anzahl der Zeichen eines Namen ``name`` ab.
Wir könnten uns darauf einigen nur die ersten $m$ Zeichen zu berücksichtige.

```{code-cell} python3
def hash_func(name):
    hash_value = 0
    prime = 83
    m = 8
    for i in range(min(m, len(name))):
        hash_value *= prime
        hash_value += ord(name[i])
    return hash_value
print(collisions(new_hash_table(unique_names_lex, hash_func), hash_func))
```

Das Ergebnis ist mit 3692 Kollisionen immernoch sehr gut und die Auswertung benötigt nun eine **konstante Anzahl** von maximal 8 Schritten.

### Unser Dictionary

Bislang können wir in unsere Hashtable Namen einfügen, löschen und abfragen ob sich ein Element in unserer Hashmap befindet:

```{code-cell} python3
insert('Dieter', hashtable, hash_func)
contains('Dieter', hashtable, hash_func)
delete('Dieter', hashtable, hash_func)
```

Die Funktionalität eines [Dictionary](def-python-dictionary) haben wir damit noch nicht erreicht.
Das besondere des [Dictionary](def-python-dictionary) ist, dass es einen Schlüssel ``key`` und einen Wert ``value`` gibt und dass wir den Wert mit dem Schlüssel identifizieren können:

```{code-cell} python3
dictionary = {'Dieter': '1977-05-06', 'Bella': '1999-10-11'}
print(dictionary['Dieter'])
print(dictionary['Bella'])
```

Das ist genau dann sehr nützlich, wenn wir den Schlüssel einfach berechnen und auch hashen können, den Wert jedoch nicht.
In unserer Hashtable sind Namen die Schlüssel, was bisher fehlt ist der Wert.
Um unsere Hashtable um Werte zu erweitern, machen wir aus der Liste ``hashtable`` zwei gleich Lange Listen ``keys`` und ``values``.
Dafür müssen wir selbstverständlich alle bisher implementierten Funktionen anpassen.

```{exercise} Unser Dictionary
:label: our-dictionary-exercise
Machen Sie aus der ``hashtable`` zwei Listen ``keys`` und ``values``, sodass sich in ``keys`` die Schlüssel unseres Dictionary befinden und in ``values`` die Werte.
Passen Sie alle Funktionen entsprechend an. Sie müssen folgenden Funktionen anpassen:

+ ``search_index``
+ ``contains``
+ ``get_value``: Dies Funktion sollte nicht mehr den Schlüssel sondern den Wert zurückliefern!
+ ``insert``: Sollte nur einen neuen Wert einfügen, falls es den entsprechenden Schlüssel noch nicht gibt.
+ ``delete``
+ ``new_hash_table``
+ ``collisions``

Führen Sie zusätzlich eine Funktion ``set_value`` ein.
Diese soll den Wert eines passend zum übergebenen Schlüssel ändert, sofern dieser existiert.

```

```{code-cell} python3
def search_index(key, hashtable, hash_func=hash):
    keys, values = hashtable
    index = hash_func(key) % len(keys)
    for i in range(len(keys)):
        j = (index+i) % len(keys)
        if keys[j] == key:
            return j
        if keys[j] == None:
            return j
        
    # there is no free place left
    return len(keys)

def contains(key, hashtable, hash_func=hash):
    keys, values = hashtable
    index = search_index(key, hashtable, hash_func)
    return index < len(keys) and keys[index] == key

def get_value(key, hashtable, hash_func):
    keys, values = hashtable
    index = search_index(key, hashtable, hash_func)
    if index < len(keys) and keys[index] == key:
        return values[index]
    else:
        None

def set_value(key, value, hashtable, hash_func):
    keys, values = hashtable
    index = search_index(key, hashtable, hash_func)
    if index >= len(keys):
        return False
    
    keys[index] = key
    values[index] = value
    return True

def insert(key, value, hashtable, hash_func=hash):
    keys, values = hashtable
    index = search_index(key, hashtable, hash_func)
    while index >= len(keys):
        keys.append(None)
        values.append(None)
      
    if keys[index] == key:
        return False
    else:
        keys[index] = key
        values[index] = value
        
        return True

def delete(key, hashtable, hash_func=hash):
    keys, values = hashtable
    index = search_index(key, hashtable, hash_func)
    if index < len(keys) and keys[index] == key:
        keys[index] = None
        values[index] = None
        i = 1
        while(keys[index+i] != None):
            next_key = keys[index+i]
            next_value = values[index+i]
            keys[index+i] = None
            values[index+i] = None
            insert(next_key, next_value, hashtable, hash_func)
            i += 1
        return True
    else:
        return False

def new_hash_table(keys, values, hash_func=hash):
    if len(keys) == len(values):
        hash_keys = [None for i in range(2*len(keys) + 8)]
        hash_values = [None for i in range(2*len(values) + 8)]
        hashtable = (hash_keys, hash_values)
        for key, value in zip(keys, values):
            insert(key, value, hashtable, hash_func)
        return hashtable
    return ([],[])

def collisions(hashtable, hash_func=hash):
    keys, values = hashtable
    collisions = 0
    for index, key in enumerate(keys):
        if key != None:
            j = hash_func(key) % len(keys)
            collisions += abs(j-index)
    return collisions
```

Tests:

```{code-cell} python3
keys = ['0', '1', '2']
values = ['Berta', 'Hans', 'Thomas']
hashtable = new_hash_table(keys, values, hash_func)
print(get_value('1', hashtable, hash_func))         # Hans
set_value('1', 'Peter', hashtable, hash_func)
print(get_value('1', hashtable, hash_func))         # Peter
print(insert('2', 'Anna', hashtable, hash_func))    # False
print(get_value('2', hashtable, hash_func))         # Thomas
print(insert('3', 'Anna', hashtable, hash_func))    # True
print(get_value('3', hashtable, hash_func))         # Anna
```

Zusammen mit unseren Funktionen bildet das Paar ``keys``, ``values`` unser eigenes [Dictionary](def-python-dictionary).

### Hashtable Klasse (optional)

Um die Funktionalität besser zu kapseln, können wir die Funktionalität mit samt der zwei Listen in eine Klasse ``Hashtable`` packen.
Wir haben Ihnen diese zusammengestellt.
``new_hash_table`` haben wir durch ``insert_all`` ersetzt.

Zudem gibt es noch drei weitere Funktionen ``size``, ``__has_to_resize`` und ``__resize``.
``size`` liefert die Anzahl der Elemente in der Hashtable zurück.
``__has_to_resize`` ist genau dann wahr, wenn die Hashtable vergrößert oder verkleinert werden muss und ``__resize`` führt diese Anpassung durch.

Wann immer ein Element aus der Hashtable gelöscht oder eingefügt wird, testen wir mit ``__has_to_resize`` ob wir die Hashtable anpassen müssen.
Ist die Hahstable $2/3$ voll, dann wird sie vergrößert und ist sie nur $1/6$ befüllt, wird sie verkleinert.
Wann immer die Größe der Hahstable angepasst wird, wird diese auf $1/4$ befüllt gesetzt.
Alle Elemente werden neu eingefügt.

```{exercise} Größe der Hashtable
:label: our-dictionary-size-exercise
Weshalb sollte die Hashtable nicht zu groß und nicht zu klein sein?
```

```{solution} our-dictionary-size-exercise
:label: our-dictionary-size-solution
:class: dropdown

Ist die Hashtable zu groß verbrauchen wir unnötig viel Speicher.
Ist sie hingegen zu klein gibt es mehr und mehr *Kollisionen* und die Laufzeit der Funktionen der Hashtable erhöht sich!

```

```{code-cell} python3
class Hashtable():
    def __init__(self, hashf=None):
        if hashf == None:
            self.hash_func = self.hashf
        else:
            self.hash_func = hashf
        self.n = 0
        self.min_size = 8
        self.keys = [None for _ in range(self.min_size)]
        self.values = [None for _ in range(self.min_size)]

    def __search_index(self, key):
        index = self.hash_func(key) % len(self.keys)
        for i in range(len(self.keys)):
            j = (index+i) % len(self.keys)
            if self.keys[j] == key:
                return j
            if self.keys[j] == None:
                return j

        # there is no free place left
        return len(self.keys)

    def contains(self, key):
        index = self.__search_index(key)
        return index < len(self.keys) and self.keys[index] == key

    def get_value(self, key):
        index = self.__search_index(key)
        if index < len(self.keys) and self.keys[index] == key:
            return self.values[index]
        else:
            None

    def set_value(self, key, value):
        index = self.__search_index(key)
        if index >= len(self.keys):
            return False

        self.keys[index] = key
        self.values[index] = value
        return True

    def insert(self, key, value):
        index = self.__search_index(key)
        while index >= len(self.keys):
            self.keys.append(None)
            self.values.append(None)

        if self.keys[index] == key:
            return False
        else:
            self.keys[index] = key
            self.values[index] = value
            self.n += 1
            if(self.__has_to_resize()):
                self.__resize()
            return True

    def size(self):
        return self.n

    def __has_to_resize(self):
        if self.n <= self.min_size:
            return False
        else:
            return self.n > 4 / 6 * len(self.keys) or self.n < 1 / 6 * len(self.keys)

    def __resize(self):
        m = self.n * 4  # 1 / 4 filled
        old_keys = self.keys
        old_values = self.values
        self.keys = [None for _ in range(m)]
        self.values = [None for _ in range(m)]
        for key, value in zip(old_keys, old_values):
            if key != None:
                self.insert(key, value)

    def delete(self, key):
        index = self.__search_index(key)
        if index < len(self.keys) and self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
            i = 1
            while(self.keys[index+i] != None):
                next_key = self.keys[index+i]
                next_value = self.values[index+i]
                self.keys[index+i] = None
                self.values[index+i] = None
                self.insert(next_key, next_value)
                i += 1
                if(self.__has_to_resize()):
                    self.__resize()
            return True
        else:
            return False

    def insert_all(self, keys, values):
        if len(keys) == len(values):
            hash_keys = [None for i in range(2*len(keys) + 8)]
            hash_values = [None for i in range(2*len(values) + 8)]
            hashtable = (hash_keys, hash_values)
            for key, value in zip(keys, values):
                self.insert(key, value)
            return hashtable
        return ([], [])

    def collisions(self):
        collisions = 0
        for index, key in enumerate(self.keys):
            if key != None:
                j = self.hash_func(key) % len(self.keys)
                collisions += abs(j-index)
        return collisions

    def hashf(self, name):
        hash_value = 0
        prime = 83
        m = 8
        for i in range(min(m, len(name))):
            hash_value *= prime
            hash_value += ord(name[i])
        return hash_value
```

Folgender Code zeigt die Verwendung der neuen Klasse

```{code-cell} python3
import hashtable
def simple_test():
    keys = ['0', '1', '2']
    values = ['Berta', 'Hans', 'Thomas']

    mydict = hashtable.Hashtable()
    mydict.insert_all(keys, values)

    print(mydict.get_value('1'))
    mydict.set_value('1', 'Peter')
    print(mydict.get_value('1'))
    print(mydict.insert('2', 'Anna'))
    print(mydict.get_value('2'))
    print(mydict.insert('3', 'Anna'))
    print(mydict.get_value('3'))


def insert_and_delete_test():
    n = 1000
    # intentionally bad hash function!
    mydict = hashtable.Hashtable(lambda i: int(i) % 100)
    for i in range(n):
        mydict.insert(str(i), i)

    for i in range(0, n, 10):
        mydict.delete(str(i))

    print(all([mydict.get_value(str(i)) ==
          i for i in range(n) if i % 10 != 0]))

simple_test()
insert_and_delete_test()
```