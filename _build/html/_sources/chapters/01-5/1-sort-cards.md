# Karten sortieren

Stellen Sie sich vor, Sie beginnen in einer gemütlichen Runde einen Spielabend.
Sie starten mit einem Kartenspiel.
Sie erhalten eine Hand voll Karten.
Um sich einen besseren Überblick zu verschaffen, möchten Sie die Karten auf Ihrer Hand sortieren.
Wie gehen Sie vor?

```{exercise} Karten sortieren
:label: exercise-sort-cards

Nehmen Sie sich ein paar gemischter Karten auf die Hand und sortieren Sie diese.
1. Überlegen Sie sich wie Sie Schritt für Schritt im kleinsten Detail vorgehen. 
    + Was machen Ihre Hände? 
    + Wo blicken Sie mit den Augen hin? 
    + Was geht Ihnen durch den Kopf?
2. Notieren Sie den Prozess, so dass ein kleines Kind Ihren Algorithmus nachvollziehen und ausführen kann.
3. Lassen Sie den Prozess anhand ihrer Notizen von einer anderen Person (z.B. Kommilitone) durchführen
4. Beantworten Sie sich selbst folgende Fragen:
    + Führt Ihr Algorithmus zum erwünschten Ergebnis?
    + Wie oft müssen Sie die Karten bewegen (Best/Worst-Case)?
    + Welche Hilfsmittel benötigen Sie (zum Beispiel einen Ablageplatz, Hände, Augen)?
    + Welches Wissen setzen Sie vorraus um dem Algorithmus folgen zu können?
```

## Mathematisches Denken

Jeder weiß doch wie man **Karten sortiert**, oder?
Selbst jemand der noch nie Karten sortiert hat, weiß zumindest wie sich vergleichbare Dinge ordnen lassen.
In der Schule sind wir größer oder kleiner als andere Schüler gewesen.
Schon sehr früh können wir Objekte ihrer Größe, Länge oder ihres Gewichts nach ordnen.
Wir gehen davon aus, dass jede Karte einen bestimmten Wert hat und wir die Karten anhand dieser *Ordnungsrelation* sortieren können.

### Ordnung

```{admonition} (totale) Ordnungsrelation
:name: def-order

Eine *Ordnungsrelation* jene Beziehung die sie verwenden, wenn sie Elemente aus einer Menge Ordnen.

Formal ist eine *Ordnungsrelation* $R \subset K \times K$ auf einer Menge $K$ (z.B. Menge der Karten) eine Relation mit ganz bestimmten Eigenschaften (Reflexivität, Antisymmetrie und Transitivität).
Befindet sich ein Element $a \in K$ in Relation mit einem anderen Element $b \in K$ schreibt man häufig anstatt $(a,b) \in R$ 

$$a \leq_R b$$

und geht aus dem Kontext hervor welche Relation gemeint ist schreibt man häufig

$$a \leq b$$

Die Eigenschaften, die eine *Ordnungsrelation* erfüllen muss sind:

1. Reflexivität: $\forall a \in K : a \leq_R a$
2. Antisymmetrie: $\forall a, b \in K : a \leq_R b \land b \leq_R a \Rightarrow a = b$
3. Transitivität: $\forall a, b, c \in K : a \leq_R b \in R \land b \leq_R c \Rightarrow a \leq_R c$

Eine *Ordnungsrelation* ist *total* wenn für alle $a,b \in K$ $a \leq_R b$ oder $b \leq_R a$ gilt.

```
Ist unsere Menge $K$ die Menge der Karten, wobei wir zwei Karten mit der gleichen Augenzahl aber unterschiedlicher Farbe als gleich ansehen, dann können wir eine *(totale) Ordnungsrelation* auf den Karten definieren. Ist zum Beispiel $K = \{6,7,8,9,10,Bube,Dame,Koenig,Ass\}$, so wäre

$$R = \{(6,6),(6,7),(6,8),\ldots,(6,A), (7,7), (7,8), \ldots, (Koenig,Ass), (Ass,Ass)\}$$

eine *(totale) Ordnungsrelation*.

### Reihenfolge

Wir nehmen intuitiv an, dass es genau eine bestimmte *Reihenfolge* der Karten auf der Hand gibt.
Karten die auf unserer Hand nebeneinander liegen, liegen auch in unserer *Reihenfolge* nebeneinander.
Nummerieren wir die Karten von links nach rechts, und starten mit der null so ist: 

$$0, 1, 2, 3, 4, 5, 6, \ldots,$$ 

unsere Reihenfolge.
Allerdings sind auch ganz andere *Reihenfolgen* wie z.B. 

$$0, 2, 4, 6, ..., 1, 3, 5, 7, ... $$

möglich. 
Jedoch kommt eine solche *Reihenfolgen* nicht in unseren Erfahrungen vor und deshalb schließen wir sie von vornherein aus.

## Kontext und Missverständnisse

Stets befinden wir uns in einem *Kontext*.
Dieser *Kontext* enthält Wörter denen er eine ganz bestimmte Bedeutung bzw. Abfolge von Wörtern zuweist.
Fragen wir ein kleines Kind ob es zur Schule geht, meinen wir damit nicht ob es gerade jetzt auf dem Weg zur Schule ist, sondern ob es bereits eingeschult ist.
In diesem Fall entsteht ein Missverständnis, falls wir und das Kind nicht den gleichen *Kontext* benutzten. 
Im *Kontext* des Kartensortierens gehen wir davon aus, dass der- oder diejenige, die die Karten sortiert, weiß, was eine *Ordnung*, eine *Reihenfolge* und ein *Vergleich* ist.
Wenn wir die Anweisung

```python
Platziere Karte x an die vorderste Stelle
```

geben, gehen wir davon aus, dass aus dem *Kontext* klar hervorgeht, was genau zu tun ist.
Zum Beispiel, dass wir unsere rechte Hand bewegen, mit den Fingern die Karte greifen und an die Position $0$ setzen müssen.
Die genaue *Realisierung* von 

```python
Platziere Karte x an die vorderste Stelle
```
nehmen wir als gegeben an.

Ist in diesem Kontext klar was **Sortiere Kareten** bedeuetet (nämlich genau das was wir möchten).
Wäre folgende Lösung bereits aussreichend:

```python
Sortiere Karten
```

## Bewusstes Denken

Selbst wenn Sie schon oft Karten sortiert haben, ist anzunehmen, dass Sie eher heuristisch vorgehen und keinen präzise und unmissverständlichen Anweisungen (= Algorithmus) folgen.
Das liegt in der Natur von uns Menschen.
Wir sind darauf trainiert schnelle einigermaßen gute Einschätzungen zu vollziehen.
Wenn wir beispielsweise einen Ball fangen möchten, dann starten wir keine komplizierten Berechnungen und lösen ein System von Differentialgleichungen, sondern folgen der sog. Blickheuristik.

```{admonition} Blickheuristik
:class: hint

Ein Fänger, der die Blickheuristik verwendet, beobachtet den Anfangswinkel des Balls und rennt so darauf zu, dass dieser Winkel konstant bleibt.
```

Derartige Heuristiken stoßen jedoch an ihre Grenzen, wenn die Komplexität des Problems steigt.
Sie können eine handvoll Karten oder ein kleines Sudoku noch mit Hilfe von Heuristiken lösen, möchten Sie aber tausende Karten sortieren, werden heuristische Strategien entweder sehr Zeitaufwendig oder führen nicht zum optimalen Ergebnis.
Und selbst wenn Sie das Problem heuristisch lösen, um Ihre Lösungsstrategie jemandem mitzuteilen, müssen Sie sich ihrer Heuristik bewusst werden!

```{admonition} Heuristische Algorithmen
:class: hint

Heuristische Algorithmen folgen einfachen Daumenregeln die oft zu guten aber nicht zwangsläufig den besten Resultaten führen.

**Beispiel:** Nehmen wir an Sie möchten aus einer Menge von Städten jede Stadt nur einmal auf einer Rundreise besuchen und gleichzeitig zurückgelegten Weg minimieren.
Eine mögliche Heuristik wäre es immer die nächst naheliegendste noch nicht besuchte Stadt zu wählen.
In den meisten praktischen Fällen führt das zu einem guten Ergebnis, doch das beste Ergebnis erzielt man damit oft nicht.
```

Unsere (menschlichen) Heuristiken bedienen sich unseres Unterbewusstseins und rufen ab was wir verinnerlicht haben.
Davon bekommen wir praktisch nichts mit.
Eine Herausforderung des *Computational Thinking* ist es, sich das Unbewusste bewusst zu machen.
Ein Problem muss im Detail verstanden werden.
Begriffe müssen eindeutig, bezogen auf Ihren verwendeten Kontext, definiert sein.

## Kontrollstrukturen und Variablen

Gehen wir davon aus, dass **Karten sortieren** in Ihrem Kontext nicht definiert ist.
Dann könnte möglicherweise folgender Algorithmus unseren Ansprüchen genügen:

```
Lege kleinste Karte auf der Hand auf einen Stapel. 
Lege kleinste Karte auf der Hand auf einen Stapel. 
...
Lege kleinste Karte auf der Hand auf einen Stapel.
```

Wir nehmen an, dass die obigen Anweisungen von links nach rechts und oben nach unten durchlaufen werden.
Weshalb?
Weil wir in Vergangenheit Texte in dieser Art gelesen und interpretiert haben.
Und wir gehen davon aus, dass der aktuelle *Kontext* dies ebenfalls so vorgesehen hat.

Weniger offensichtlich ist die Bedeutung der drei Punkte.

```
...
```

Auch hier sagt uns unser Bauchgefühl was das damit gemeint ist, nämlich dass

```
Lege kleinste Karte auf der Hand auf einen Stapel. 
```

solange wiederholt wird bis keine Karten mehr auf der Hand sind.
Die drei Punkte sind eine sog. *Kontrollstruktur* die uns der *Kontext* zur Verfügung stellt.

```{admonition} Kontrollstruktur

TODO

```

Was passiert aber wenn sich auf unserer Hand keine oder nur eine Karte befindet?
Nehmen wir die Beschreibung mit den drei Punkten wörtlich, dann wissen wir nach dem ersten

```
Lege kleinste Karte auf der Hand auf einen Stapel. 
```

nicht mehr was zu tun ist, bzw. die nächste Anweisung ist nicht mehr ausführbar.
Außerdem enthalten die drei Punkte keinerlei Information darüber wie festegestellt wird wann der Prozess abgeschlossen ist.
Wie wäre es mit folgender präziseren Variante:

```{code-block}
---
lineno-start: 1
---
Falls noch mindestens eine Karte auf der Hand ist, springe zu Zeile (2), andernfalls springe zu Zeile (4)
Lege kleinste Karte auf der Hand auf den Stapel 
Springe zu Zeile (1)
Ende
````

Sofern die neuen Begriffe wie

```
Springe zu Zeile (4)
``` 

klar definiert sind, ist diese Variante weniger missverständlich.
Was noch zu Verwirrung führen kann ist der unspezifizierte Stapel, d.h.,

```
auf einen Stapel
```

Welcher Stapel ist damit gemeint?
Auf einen bestimmten oder jede Karte auf einen anderen?
Was wir in unserem *Kontext* benötigen sind eindeutige Namen mit denen wir Objekte Identifizieren/Adressieren können.
In der Programmierung heißen diese Namen *Variablen*.

```{admonition} Variable

TODO

```

Die neue Version


```{code-block}
---
lineno-start: 1
---
Sei H unsere Hand mit Karten
Sei S ein leerer Stapel

Falls noch mindestens eine Karte auf der Hand H ist, springe zu Zeile (5), andernfalls springe zu Zeile (7)
Lege kleinste Karte auf der Hand H auf den Stapel S
Springe zu Zeile (3)
Ende
```

kann sich sehen lassen.
Sie ist präziser als all unsere Varianten zuvor, allerdings fällt es der menschlichen Wahrnehmung schwerer in sehr kurzer Zeit zu verstehen was vor sich geht.
Ein anderes, für uns Menschen leserliches Beispiel wäre:

```
Sei H unsere Hand mit Karten
Sei S ein leerer Stapel
Solange noch Karten auf der Hand H sind:
    Lege kleinste Karte auf der Hand H auf den Stapel S 
```

Der Sprung ist hierbei durch ``Solange`` und die Einrückung definiert.

Wir können uns an dieser Stelle fragen weshalb diese Variante leichter zu lesen ist?
Wir sind es gewohnt Texte linear von oben nach unten zu lesen.
Die Wiederholung von Textstellen bricht mit dieser Erfahrung.
In der Variante zuvor, wird dieser Bruch nicht durch einen Bruch im Text hervorgehoben.
Visuell sieht es nicht nach einer Wiederholung aus.
Zudem ist der Teil, der wiederholt wird, nicht hervorgehoben.

## Dekomposition

Soweit so gut.
Wovon wir bis jetzt ausgegangen sind ist, dass

```
Lege kleinste Karte auf der Hand auf S. 
```

von unserem *Kontext* definiert ist.
Falls nicht, müssen wir selbst eine Definition mit den Mittel, die uns der *Kontext* zur Verfügung stellt, notieren.
Zum Beispiel:

```
Sei s erste Karte (von links)
Sei k erste Karte (von links)

Solange sich eine Karte rechts von k befindet:
    Sei k die Karte rechts von k
    Falls k kleiner als s:
        Sei s gleich k
Lege s auf S.
```

Sie werden vielleicht bemerkt haben, dass 

```
Sei s gleich k
```

oder 

```
Sei k die Karte rechts von k
```

und auch 

```
Sei s erste Karte (von links)
Sei k erste Karte (von links)
```

missverständlich sein kann.
Mit ``Sei x y`` meinen wir in unserem *Kontext*, dass der Name (die Variable) ``x`` der das Objekt ``o1`` (hier eine Karte) identifitiert, nach der Anweisung, das Objekt ``o2`` identifiziert, welches derzeit durch den Namen ``y`` identifiziert wird.

```{figure} ../../figs/find_min.png
---
width: 800px
name: fig-find-min
---
Skizze des Algorithmus zum Finden der kleinsten Karte auf der Hand.
```

Wer unseren *Kontext* nur erahnt könnte es zu einem Vergleich, also sind die Karten (Objekte) mit den Namen ``s`` und ``k`` gleich.
Mit einer anderen *Syntax*, können wir solchen Missverständnissen vorbeugen.
Ändern wir nur die *Syntax* ändert sich die Bedeutung der Ausdrücke (*Semantik*) nicht.
Ein Beispiel wäre

```
s <- erste Karte (von links)
k <- erste Karte (von links)

Solange eine sich eine Karte rechts von k befindet:
    k <- die Karte rechts von k.
    Falls k kleiner als s:
        s <- k
Lege s auf S.
```

```{admonition} Syntax

TODO
```

In den allermeisten Programmiersprachen wird eine solche Umbenennung (*Zuweisung*) anstatt durch ``<-`` durch das ``=`` realisiert.
Für den Vergleich verwendet man üblicherweise ``==``.
Das kann anfänglich verwirrend sein, da das ``=`` nicht dem mathematischen $=$ entspricht.
