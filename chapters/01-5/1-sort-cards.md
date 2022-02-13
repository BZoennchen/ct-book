(sec-sorting-cards-alg)=
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
2. Notieren Sie den Prozess, sodass ein kleines Kind Ihren Algorithmus nachvollziehen und ausführen kann.
3. Lassen Sie den Prozess anhand ihrer Notizen von einer anderen Person durchführen.
4. Beantworten Sie sich selbst folgende Fragen:
    + Führt Ihr Algorithmus zum erwünschten Ergebnis?
    + Wie oft müssen Sie die Karten bewegen (im schlechtesten und besten Fall)?
    + Welche Hilfsmittel benötigen Sie (zum Beispiel einen Ablageplatz, Hände, Augen)?
    + Welches Wissen setzen Sie voraus um dem Algorithmus folgen zu können?
```

## Kontext und Missverständnisse

Stets befinden wir uns in einem *Kontext*.
Dieser Kontext enthält Wörter denen er eine ganz bestimmte Bedeutung bzw. Abfolge von Wörtern zuweist.
Fragen wir ein kleines Kind ob es zur Schule geht, meinen wir damit nicht ob es gerade jetzt auf dem Weg zur Schule ist, sondern ob es bereits eingeschult ist.
In diesem Fall entsteht ein Missverständnis, falls wir und das Kind nicht den gleichen Kontext benutzten. 

Im Kontext des Kartensortierens gehen wir davon aus, dass der- oder diejenige, die die Karten sortiert, weiß, was eine *Ordnung*, eine *Reihenfolge* und ein *Vergleich* ist.
Wenn wir die Anweisung

```python
Platziere Karte x an die vorderste Stelle
```

geben, gehen wir davon aus, dass aus dem Kontext klar hervorgeht, was genau zu tun ist.
Zum Beispiel, dass wir unsere rechte Hand bewegen, mit den Fingern die Karte greifen und an die Position 0 setzen müssen.
Die genaue *Realisierung* von 

```python
Platziere Karte x an die vorderste Stelle
```
nehmen wir als gegeben an.

Geht aus dem Kontext hervor was genau **Sortiere Karten** bedeutet.
Wäre folgende Lösung bereits ausreichend:

```python
Sortiere Karten
```

Geht dies nicht hervor, müssen wir mit den Mitteln die uns zur Verfügung stehen, d.h., mit dem bestehenden Kontext ausdrücken, **wie** das Kartensortieren realisiert wird.
Der Unterschied zwischen dem **Wie** und dem **Was** ist wichtig zu begreifen.
Der Kontext beschreibt viele verschiedene **Was**. 
Mit diesen beschreiben wir **wie** wir ein anderes **Was** realisieren.
Wir erweitern den Kontext um jenes **Was**, in unserem Fall das Kartensortieren. 

Jede Beschreibung befindet sich auf einem mehr oder weniger abstraktem Level.
Zum Beispiel können wir schreiben:

```python
Lege kleinste Karte, welche sich auf der Hand befindet, auf einen Stapel
Lege kleinste Karte, welche sich auf der Hand befindet, auf einen Stapel
```

Das **Was** der beiden Zeilen ist: Die zwei kleinsten Karten werden von der Hand auf den Stapel gelegt.
Das **Wie** beschreiben die beiden Zeilen: Wir nehmen die kleinste Karte auf der Hand und legen sie ab, dann wiederholen wir dies.
Das **Wie** des einzelnen Schritts, also

```python
Lege kleinste Karte, welche sich auf der Hand befindet, auf einen Stapel
```

ist unklar.

Eine gewisse Unklarheit bezüglich des **Wie** wird immer bestehen bleiben.
Das ist auch nichts ungewöhnliches.
Selbst wenn wir mit einem Stift auf ein Blatt Papier schreiben ist uns nicht vollkommen klar was auf der Atomebene bei diesem Vorgang vor sich geht.
Die Frage lautet daher welche Mittel wir zur Verfügung haben und in welchem Kontext wir uns befinden.
Können wir davon ausgehen, dass aus dem Kontext das **Was** klar hervorgeht?
Ist also klar, wie wir die kleinste Karte auf der Hand überhaupt finden?
In unserem Fall würden wir dies mit einem nein beantworten.

Wie sieht es zum Beispiel mit

```python
Lege dritte Karte von der Hand auf den Stapel
```

Hier würden wir sagen, dass diese Beschreibung für den Kontext genau genug ist.
Wir können davon ausgehen, dass die ausführende Einheit (der oder diejenige) weiß **Wie** dieses **Was** durchzuführen ist.

Wir müssen also festlegen was die ausführende Einheit kann und was nicht -- was sie versteht und was nicht.
Genauso verhält es sich mit dem digitalen Computer und den Programmiersprachen.
Zusammen geben sie uns einen Kontext in dem bestimmte **Was** kein **Wie** benötigen.
Während des Programmierens erweitern wir unseren Kontext und können die von uns entwickelten **Was** benutzten.

## Bewusstes Denken

Selbst wenn Sie schon oft Karten sortiert haben, ist anzunehmen, dass Sie eher heuristisch vorgegangen sind und keinen präzise und unmissverständlichen Anweisungen, d.h. einem [Algorithmus](def-algorithm), gefolgt sind.
Das liegt in der Natur von uns Menschen.
Wir sind darauf trainiert schnelle einigermaßen gute Einschätzungen zu vollziehen.
Wenn wir beispielsweise einen Ball fangen möchten, dann starten wir keine komplizierten Berechnungen und lösen ein System von Differentialgleichungen, sondern folgen der sog. Blickheuristik.

```{admonition} Blickheuristik
:class: remark
:name: remark-looking-heuristics

Ein Fänger, der die Blickheuristik verwendet, beobachtet den Anfangswinkel des Balls und rennt so darauf zu, dass dieser Winkel konstant bleibt.
```

Derartige Heuristiken stoßen jedoch an ihre Grenzen, wenn die Komplexität des Problems steigt.
Sie können eine handvoll Karten oder ein kleines Sudoku noch mit Hilfe von Heuristiken lösen, möchten Sie aber tausende Karten sortieren, werden heuristische Strategien entweder sehr Zeitaufwendig, oder führen nicht zum optimalen Ergebnis.
Und selbst wenn Sie das Problem heuristisch lösen, um Ihre Lösungsstrategie jemandem mitzuteilen, müssen Sie sich ihrer Heuristik bewusst werden!

```{admonition} Heuristische Algorithmen
:class: remark
:name: remark-heuristics

Heuristische Algorithmen folgen einfachen Daumenregeln die oft zu guten aber nicht zwangsläufig den besten Resultaten führen.

**Beispiel:** Nehmen wir an Sie möchten aus einer Menge von Städten jede Stadt nur einmal auf einer Rundreise besuchen und gleichzeitig den zurückgelegten Weg minimieren.
Eine mögliche Heuristik wäre es, immer die gerade naheliegendste noch nicht besuchte Stadt zu wählen.
In den meisten praktischen Fällen führt das zu einem guten Ergebnis, doch das beste Ergebnis erzielt man damit oft nicht.
```

Unsere (menschlichen) Heuristiken bedienen sich unseres Unterbewusstseins und rufen ab was wir verinnerlicht haben.
Davon bekommen wir praktisch nichts mit.
Eine Herausforderung des *Computational Thinking* ist es, sich das Unbewusste bewusst zu machen.
Ein Problem muss im Detail verstanden werden.
Begriffe müssen, bezogen auf Ihren verwendeten Kontext, eindeutig definiert sein.

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
Weil wir in der Vergangenheit Texte in dieser Art gelesen und interpretiert haben.
Und wir gehen davon aus, dass der aktuelle *Kontext* dies ebenfalls so vorgesehen hat.

Weniger offensichtlich ist die Bedeutung der drei Punkte.

```
...
```

Auch hier sagt uns unser Bauchgefühl was damit gemeint ist, nämlich dass

```
Lege kleinste Karte auf der Hand auf einen Stapel. 
```

solange wiederholt wird bis keine Karten mehr auf der Hand sind.
Die drei Punkte sind eine sog. [Kontrollstruktur](sec-control-statements) die uns der *Kontext* zur Verfügung stellt.

Was passiert aber wenn sich auf unserer Hand keine oder nur eine Karte befindet?
Nehmen wir die Beschreibung mit den drei Punkten wörtlich, dann wissen wir nach dem ersten

```
Lege kleinste Karte auf der Hand auf einen Stapel. 
```

nicht mehr was zu tun ist, bzw. die nächste Anweisung ist nicht mehr ausführbar.
Außerdem enthalten die drei Punkte keinerlei Information darüber wie festgestellt wird, wann der Prozess abgeschlossen ist.
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
In der Programmierung heißen diese Namen [Variablen](sec-variables).

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

Solange sich eine Karte rechts von s befindet:
    Sei k gleich die Karte rechts von k
    Falls k kleiner als s:
        Sei s gleich k
Lege s auf S.
```

Wir holen uns also die kleinste Karte auf der Hand indem wir die Hand von links nach rechts durchsuchen.
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
Mit ``Sei x gleich y`` meinen wir in unserem *Kontext*, dass der Name (die Variable) ``x`` der das Objekt ``o1`` (hier eine Karte) identifiziert, nach der Anweisung, das Objekt ``o2`` identifiziert, welches derzeit durch den Namen ``y`` identifiziert wird.

```{figure} ../../figs/find_min.png
---
width: 800px
name: fig-find-min
---
Skizze des Algorithmus zum Finden der kleinsten Karte auf der Hand.
```

Wer unseren *Kontext* nur erahnt könnte es mit einem Vergleich, also sind die Karten (Objekte) mit den Namen ``s`` und ``k`` gleich, verwechseln.
Mit einer anderen [Syntax](def-syntax), können wir solchen Missverständnissen vorbeugen.
Ändern wir nur die Syntax ändert sich die Bedeutung der Ausdrücke ([Semantik](def-semantik)) nicht.
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

```{admonition} Zuweisung und Vergleich
:class: attention
In den allermeisten Programmiersprachen wird eine solche Umbenennung (*Zuweisung*) anstatt durch ``<-`` durch das ``=`` realisiert.
Für den Vergleich verwendet man üblicherweise ``==``.
Das kann anfänglich verwirrend sein, da das ``=`` nicht dem mathematischen $=$ entspricht.
```

## Mathematisches Denken

Das mathematische Denken ist eng mit dem Computational Thinking verknüpft.
In der Mathematik sind alle Objekte und Operationen präzise und unmissverständlich formuliert.
Zugleich verzichtet man auf überflüssige Informationen und versucht Definitionen so allgemein, d.h. abstrakt wie möglich zu halten.

Bei jeder Priorisierung oder Sortierung müssen wir Objekte vergleichen können.
Das Sortieren von Karten können wir intuitiv ohne großartig darüber nachzudenken.
Wir haben bereits ein Verständnis durch unsere Lebenserfahrung erlangt.
Selbst jemand der noch nie Karten sortiert hat, weiß zumindest wie sich vergleichbare Dinge ordnen lassen.
In der Schule sind wir größer oder kleiner als andere Schüler gewesen.
Schon sehr früh können wir Objekte ihrer Größe, Länge oder ihres Gewichts nach ordnen.

Für eine genaue und unmissverständliche Beschreibung können wir von der Mathematik Gebrauch machen.
Sie ist eine internationale äußerst kompakte Sprache mit der wir die Natur beschreiben können.
Zudem ist die Mathematik bereits entwickelt, wir können uns also vieler Konzepte bedienen, die allgemein bekannt sind.
Somit drücken wir uns für all jene verständlich aus, die das nötige mathematische Verständnis mitbringen.

Lassen Sie uns zwei wesentliche Dinge mathematisch betrachten, welche wir beim Sortieren der Karten intuitiv verwenden:

1. Die sog. [Ordnungsrelation](def-math-order) und
2. Objekte in einer Reihenfolge angeordnet.


### Ordnung

Für die Entwicklung eines [Algorithmus](def-algorithm) zum Sortieren von Karten brauchen wir eine präzise Definition einer [Ordnungsrelation](def-math-order) um Karten vergleichen zu können.

Ist unsere Menge $K$ die Menge der Karten, wobei wir zwei Karten mit der gleichen Augenzahl aber unterschiedlicher Farbe als gleich ansehen, dann können wir eine *(totale) Ordnungsrelation* auf den Karten definieren. Ist zum Beispiel $K = \{6,7,8,9,10,\text{Bube},\text{Dame},\text{König},\text{Ass}\}$, so wäre

$$R = \{(6,6),(6,7),(6,8),\ldots,(6,A), (7,7), (7,8), \ldots, (\text{König},\text{Ass}), (\text{Ass},\text{Ass})\}$$

eine *(totale) Ordnungsrelation*.

### Reihenfolge

Die Karten auf der Hand betrachten wir von links nach rechts.
Wir nehmen demnach an, dass es genau eine bestimmte *Reihenfolge* der Karten auf der Hand gibt.
Karten die auf unserer Hand nebeneinander liegen, liegen auch in unserer *Reihenfolge* nebeneinander.

Die Hand mit $n$ Karten lässt sich als sog. $n$-[Tupel](def-math-tuple) mathematisch ausdrücken.
Zum Beispiel,

$$H = (6, 7, \text{Bube}, 8, \text{Bube})$$

Wäre ein $5$-Tupel, welches eine Hand *modelliert*, welche die Karten 6, 7, Bube, 8, Bube von links nach rechts beinhaltet.

Anders als mathematische Mengen sind Tupel geordnet und endlich.
Zugleich können mehrere gleiche Elemente enthalten.

In ``Python`` gibt es zwei Datenstrukturen ([Liste](sec-list), [Tupel](sec-tuple)), welche ein mathematisches endliches Tupel modellieren.