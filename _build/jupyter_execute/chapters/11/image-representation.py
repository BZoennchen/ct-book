# Binäres Zeichnen - Struktur ist Information

````{admonition} Lernziel
:class: learngoals

In diesem Abschnitt nutzen wir zwei Zustände **Strom aus**, **Strom an** bzw. $0$ und $1$ um erst ein Schwarz-Weiß-Bild 

```{figure} ../../figs/image-representation/zero-and-one-to-bw-picture.png
---
width: 200px
name: fig-zero-and-one-to-bw-picture
---
```

und schlussendlich ein Video bzw. eine Animation

```{figure} ../../figs/image-representation/flower.gif
---
width: 200px
name: fig-flower
---
```

 zu repräsentieren.

Diese Übung soll verdeutlichen, wie Informationen erst durch einen Interpreter eine bestimmte Bedeutung erlangen.
Sie sollen selbst erfahren, wie durch Strukturen in einer Folge aus $0$ und $1$ Information entsteht.
Sie werden diese Struktur selbst erarbeiten.

In Sachen ``Python``-Programmierung lernen Sie mit mehrdimensionalen Listen und Tupeln umzugehen und wie sie Ihren Code durch Funktionen strukturieren können.

Zudem werden Sie sehen, wie Sie durch ``Python``-Funktionen in eine abstraktere Welt gelangen und in dieser denken können.
Wir werden Probleme in viele Teilprobleme aufteilen (**Dekomposition**), Sie werden Ihre **Mustererkennung** benötigen und auch **mathematisches Denken** trainieren.
````

## Das Bildformat (Informationsrepräsentation)

Wir beginnen mit einem Schwarz-Weiß-Rasterbild.
Ein [Rasterbild](pixel-image) hat eine bestimmte Anzahl $m$ an Pixel in $y$-Richtung (Zeilen) und eine bestimmte Anzahl $n$ an Pixel in $x$-Richtung (Spalten).
Das Bild kann als $m \times n$-Matrix aufgefasst werden.
In unserem Fall des Schwarz-Weiß-Bilds ist jeder Pixel entweder schwarz $0$ oder weiß $1$.

```{exercise} Bits pro Pixel
:label: repraesentation-bw-exercise
Wie viele *Bits* benötigen Sie für jeden Pixel?
```

```{solution} repraesentation-bw-exercise
:label: repraesentation-bw-solution
:class: dropdown
Jeder Pixel kann nur einen von zwei Zuständen annehmen, demnach brauchen wir pro Pixel $1$ *Bit*.
```

Jede Zeile des Bildes repräsentieren wir als Folge von $0$ und $1$.
Da wir unser Bild verändern möchten eignet sich in ``Python`` hierfür die Liste ``list``.

row = [0, 1, 0, 1, 0, 1, 1]

Ein Bild modellieren wir wiederum als eine Liste von Zeilen (Pixelstreifen) oder eben eine Liste von Listen.

picture = [[0, 1, 0, 1, 0, 1, 1], # 1. Zeile
           [1, 1, 0, 1, 0, 1, 1], # 2. Zeile
           [0, 0, 1, 1, 1, 1, 1], # 3. Zeile
           [1, 0, 0, 1, 0, 1, 1]] # 4. Zeile

## Listen in Python
Mit

picture[3][5]

greifen wir auf das Element in der ``4``-ten Zeile und ``6``-ten Spalte zu denn der Index einer Liste beginnt mit ``0``.

Bevor wir weiter fortfahren möchten wir ein wichtiges Merkmal der ``Python``-Liste hervorheben.
Sie könnten dazu geneigt sein folgender Code zu verwenden um ein Bild mit zwei identischen Zeilen zu erzeugen.

row = [0, 1, 0, 1, 0, 1, 1]
picture = [row, row]

Doch hierbei entsteht ein merkwürdiges Phänomen, welches die folgende Aufgabe zum Vorschein bringt.

```{exercise} Kopie einer Liste
:label: copy-list-exercise
Ändern Sie nun ein einzelnen Pixel und lassen Sie sich das Ergebnis anzeigen.
Was stellen Sie fest?
```

````{solution} copy-list-exercise
:label: rcopy-list-solution
:class: dropdown
Ändern wir einen Pixel einer Zeile, z.B. durch

```python
picture[0][0] = 1
```

so ändert wir sowohl ``picture[0][0]`` als auch ``picture[1][0]``.
````

Unser Bild enthält keine zwei identische Zeilen sondern zweimal die gleiche Zeile.
Es wird nicht der Wert also ``[0, 1, 0, 1, 0, 1, 1]`` kopiert sondern die Referenz / der Zeiger welche auf eine Liste zeigt.

Um das gewünschte Ergebnis zu erzielen müssen wir die Liste und nicht ihre Referenz kopieren, hierzu bietet uns ``Python`` die Listen-Methode ``copy()`` an:

row = [0, 1, 0, 1, 0, 1, 1]
picture = [row.copy(), row.copy()]

Da eine Kopie der Liste (des Objekts) gemacht wird, können Sie sicher sein, dass Änderungen der Listenelemente nur jene eine Liste betreffen.
Bedenken Sie jedoch, dass keine sog. *tiefe Kopie* gemacht wird.
Zum Beispiel laufen Sie mit

row = [0, 1, 0, 1, 0, 1, 1]
picture = [row.copy(), row.copy()]
picture2 = picture.copy()
picture2[0][0] = 1

in das gleiche Problem.

Um Listen zu verketten können Sie in ``Python`` den ``+``-Operator verwenden.

[1,2,3,4] + [5,6,7,8]

Das Ergebnis ist eine neue eindimensionale Liste die alle Elemente der beiden Listen in genau jener Reihenfolge enthält.
Allerdings unterscheidet ``Python`` zwischen ``mylist += other_list`` und ``mylist = mylist + other_list``!
Ersteres, also ``+=``, führt eine [veränderbare](def-mutable) (engl. *mutable*) Addition durch, d.h. hier wird ``mylist`` verändert.
Letzteres, also ``mylist + other_list``, führt eine [unveränderbare](def-mutable) (engl. *immutable*) Addition durch, wodurch eine Kopie erzeugt wird. D.h. ``mylist = mylist + other_list`` erzeugt eine völlig neue Liste und ordnet es ``mylist`` zu.

```{admonition} Veränderlich und Un­ver­än­der­lich­keit
:name: def-mutable

Wir nennen ein Objekt, z.B. eine Variable, *veränderlich* (engl. *mutable*) wenn wir dessen Wert verändern können indem wir den Speicherbereich des Objekts verändern können.
Ein Objekt ist dagegen *unveränderlich* (engl. *immutable*) wenn wir dessen Speicherbereich nicht verändern können.
Ist ein Objekt *unveränderlich* so wird dessen Veränderung durch eine Kopie (einen neuen Speicherbereich) realisiert.
Das Ursprungsobjekt bleibt *unverändert*.

Ist eine Operation *unveränderlich* so verändert sie den Speicherbereich der Objekte, auf denen sie ausgeführt wird, nicht
```

Sie mögen nun denken, dass Ergebnis ist doch identisch?
Sehen wir uns folgenden Code an:

def concat_immutable(list1,list2):
    concat = list1 + list2
    return concat

def concat_mutable(list1,list2):
    list1 += list2
    return list1

a = [1,2,3,4]
b = [5,6,7,8]
c = concat_immutable(a,b)
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

c = concat_mutable(a,b)
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

``concat_mutable`` verändert ``list1`` und da es sich nicht um einen [primitiven Datentyp](def-primitive-datatypes) handelt, wird nur die Referenz kopiert und nicht die Liste ``a`` selbst.
Somit wird ``a += b`` ausgeführt und ``a`` wird verändert.
Dies bezeichnen wir als sogenannten *Seiteneffekt* und in diesem Fall ist es ein unerwarteter *Seiteneffekt* den wir vermeiden sollten!
Dennoch ist ``+=`` immer dann sehr sinnvoll wenn Sie eine Liste sukzessive füllen wollen.
Denn jedesmal die gesamte Liste zu kopieren kann zu einer langen Laufzeit führen.


````{exercise} Immutable vs. Mutable
:label: mutable-vs-immutable-concat
Welcher der beiden Funktionen wird bei gleicher Eingabe schneller laufen und warum?
Testen Sie beide Versionen für große ``n`` > 0.

```python
def my_range_mutable(n):
    number = []
    for i in range(n):
        number += [i]
    return number

def my_range_immutable(n):
    number = []
    for i in range(n):
        number = number + [i]
    return number
````

Um über die Elemente einer Liste zu *iterieren*, verwendet man in ``Python`` das [For-Schleife](https://www.python-kurs.eu/python3_for-schleife.php) und wie immer bestimmt die [Einrückung](https://www.python-kurs.eu/python3_bloecke.php) die Strukturierung (``Python`` verzichtet auf Klammern):

for row in picture:
    print(row)

```{exercise} Iteration
:label: iteration-exercise
Schreiben Sie einen Code der jedes Pixel des Bildes einzeln durch ``print()`` ausgibt.
```

for row in picture:
    for pixel in row:
        print(pixel)

(sec-python-function)=
## Funktionen in Python

Funktionen definieren wir mit dem Schlüsselwort ``def`` gefolgt vom Funktionsnamen und den *Argumenten* der Funktion sowie ihrer Logik.
Anstatt *Argumente* sprechen wir auch von *Parametern*.
Falls Sie mit Ihrer Funktion einen Wert, eine Liste, oder ein anderes Objekt zurückgeben möchten nutzen Sie das ``return``-Schlüsselwort.
Variablen der Funktion sind ihre Argumente und alle anderen Variablen die sie innerhalb der Funktion definieren.
Zum Beispiel:

x = 10
c = 100
def add(x, y):
    c = x + y
    return c
add(15, x)

Die Variablen ``x`` und ``c`` außerhalb der Funktion haben nichts mit den Variablen innerhalb oder Argumenten der Funktion zu tun.
Sie bleiben unverändert.
Durch den obigen Aufruf wird erhalt das Argument ``x`` den Wert ``15`` und ``y`` die Referenz zu ``x`` außerhalb der Funktion.
``c`` wird zu ``25`` und wird zurückgegeben.
Falls ``y`` innerhalb der Funktion verändert wird, würde ``Python`` eine neue Kopie anlegen, da es sich um einen *unveränderlichen* (*immutable*) Datentyp handelt.
Alle [primitiven Datentypen](def-primitive-datatypes) wie ``int, float, bool`` aber auch ``str``(Zeichenketten) und ``tuple`` sind unveränderlich.
Listen jedoch nicht!

Eine gute Übung ist es eine Liste zu *flatten*, d.h. aus einer mehrdimensionalen Liste, eine Liste der Dimension $1$ zu machen.
Hierbei soll die Reihenfolge der Elemente erhalten bleiben.


```{exercise} Flatten
:label: flatten-exercise
Schreiben Sie eine Funktion ``flatten(mylist)``, die die $n$-dimensionalen Liste ``mylist`` in eine $n-1$-dimensionale Liste transformiert.
Zum Beispiel soll aus ``[[[1,2], [3,3]], [[1,3], [4,5]]]``, also einer $3$-dimensionalen Liste, ``[[1,2], [3,3], [1,3], [4,5]]``, also eine $2$-dimensionale Liste werden.
```

def flatten(mylist):
    result = []
    for sub_list in mylist:
        for element in sub_list:
            result.append(element)

    return result

flatten([[[1,2], [3,3]], [[1,3], [4,5]]])

In unserer Lösung bewirkt ``result.append(element)`` das gleich wie ``result += [element]`` jedoch ist die erste Version klarer zu lesen denn wir wollen das Element ``element`` anhängen (engl. append).

## Bildgenerierung (Informationserzeugung)

```{exercise} Bild generieren
:label: repraesentation-pic-with-border
Generieren Sie ein weißes $10 \times 10$ Rasterbild mit einem ein Pixel breiten schwarzen Rand.
Nutzen Sie die Programmierung um sich Zeit zu sparen!
```

top = [0 for i in range(10)]
center = [0] + [1 for i in range(8)] + [0]
picture = [top.copy()] + [center.copy() for i in range(8)] + [top.copy()]
picture

Auch hier müssen Sie darauf achten die richtigen Kopien zu machen.
Um sich Code zu sparen kann das sog. *List Comprehension* Ihnen Zeit beim Schreiben sparen.

````{admonition} List Comprehension (Python)
:class: dropdown
Das *List Comprehension* ist eine kurze Syntax um aus einer bestehenden Sequenz/Liste eine neue Liste zu erzeugen.

**Beispiel:**
```python
[0 for i in range(10)]
```

oder

```python
[0 for _ in range(10)]
```

sind Kurformen von
```python
newlist = []
for _ in range(10):
    newlist.append(0)
```

und erzeugen aus der Sequenz ``0,1,2,3,4,5,6,7,8,9`` die Liste ``[0,0,0,0,0,0,0,0,0,0]``.
````

```{exercise} Bild manipulieren
Testen Sie ihr generiertes Bild.
Ändern Sie den Pixel in der $5$-ten Zeile und und $5$-Spalte, sowie einen Pixeln in der ersten Spalte und einen in der ersten Zeile
```

picture[4][4] = 1
picture

picture[4][0] = 1
picture

picture[0][4] = 1
picture

```{exercise} Variables Bild generieren
Schreiben Sie eine Funktion die Ihnen ein weißes Bild mit schwarzem Rand generiert.
Dabei soll die Breite ``width`` und Höhe ``height`` sowie die Randbreite ``border_width`` ein Argument der Funktion sein.
```

def generate_border_picture(width=10, height=10, border_width=1):
    picture = []
    
    yborder = min(border_width,height)
    xborder = min(border_width,width)
    top = [0 for _ in range(width)]
    for _ in range(yborder):
        picture.append(top.copy())
        
    for _ in range(height-2*border_width):
        picture.append(
            [0 for _ in range(xborder)] + 
            [1 for _ in range(width-2*border_width)] + 
            [0 for _ in range(xborder)])
    
    for _ in range(min(border_width,height-yborder)):
        picture.append(top.copy())
    return picture
generate_border_picture(width=5, height=10, border_width=2)

```{exercise} Variable Bildgenerierung testen
Testen Sie Ihre Funktion insbesondere für besondere Werte wie ``border_width > width``.
```

````{exercise} Variable Bildgenerierung testen
Folgende Funktion plottet Ihr Bild.
```python
import matplotlib.pyplot as plt
def plot_picture(picture):
    plt.imshow(picture, cmap='gray', vmin=0, vmax=1)
```
Sehen Sie sich die dazugehörige [Dokumentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) an und nutzen Sie die Funktion.
````

Mit folgendem Code

picture = generate_border_picture(width=5, height=10, border_width=1)
plot_picture(picture)

erzuegen wir

```{figure} ../../figs/image-representation/border-picture.png
---
height: 150px
name: fig-border-picture.
---
```

## Zeichnen (Informationsmanipulation)

Wir haben bereits jetzt ein neues Bildformat geschaffen und ein kleines Programm, welches unser Format interpretieren und als Rasterbild anzeigt.
Jetzt können wir uns austoben und weitere Bilder generieren.
Wie wäre es zum Beispiel mit einem Kreis, Rechteck oder Dreieck?
Diese Objekte direkt als Ansammlung von Pixeln zu beschreiben ist schwierig und unflexibel.
Was uns das Leben deutlich leichter macht ist die Anwendung der **Abstraktion**.
Wir starten mit den geometrischen mathematischen Objekten Kreis, Rechteck und Dreieck und überlegen uns eine Funktion die diese Objekte **digitalisiert**.

```{figure} ../../figs/image-representation/point-to-pixel.png
---
height: 350px
name: fig-point-to-pixel
---
```

Unsere geometrischen Objekte haben reelle Koordinaten z.B. können wir einen Kreis durch seinen Mittelpunkt $c = (x,y)$ und Radius $r$ eindeutig beschreiben.
Um die Koordinaten in Pixelkoordinaten zu transformieren legen wir auf das Rasterbild ein reeles Koordinatensystem. 
Hat unser Bild $n \times n$ Pixelbild und wir möchten den Raum $10 \times 10 \subset \mathbb{R}^2$ durch das Bild abbilden, entspricht die erste Bildzeile dem Raum $10 \times 1$.
Um keine Verzerrung zu erhalten sollten Pixel in $x$ und in $y$ Richtung gleich viel Anteil des Euklidischen Raumes überziehen.
Die Auflösung ``resolution`` gibt an wie viel Raum ein Pixel repräsentiert.
Bei einer ``resolution = 0.1`` repräsentiert ein Pixel den Raum $0.1 \times 0.1$.
Anders ausgedrückt, braucht es $10 \times 10$ Pixel um den Raum $1 \times 1$ im $\mathbb{R}^2$ zu repräsentieren.

Kennen wir die ``resolution``, die Anzahl der Pixel in $x$-Richtung ``cols``, die Anzahl der Pixel in $y$-Richtung ``rows`` und gehen davon aus, dass der Raum $R$ den wir Abbilden möchten in $(0,0)$ beginnt und nur positive Werte enthält also $R = [0;w] \times [0;h]$, dann können wir für einen gegebenen Punkt $p = (x,y) \in \mathbb{R}^2$ den Pixel $(i,j) \in \mathbb{N}^2$ berechnen der $p$ enthält.

```{exercise} Pixel berechnen
Schreiben Sie eine Funktion ``to_pixel(p, resolution)`` die Ihnen den Pixel ``(i,j)`` zurückgibt der den Punkt ``p = (x,y)`` enthält.
Bedenken Sie, dass wir Pixel beginnend mit $0$ zählen.
```

def to_pixel(p, resolution):
    x, y = p
    return int(x / resolution), int(y/ resolution)

to_pixel((0.7, 0), 0.5)

Soweit so gut!
Widmen wir uns nun dem Problem ein Rechteck bzw. Dreieck zu zeichnen.
Wir wenden die **Mustererkennung** an und bemerken, dass sowohl das Dreieck als auch Rechteck aus Segmenten besteht (drei für das Dreieck und 4 für das Rechteck).
Deshalb können wir das Problem in das Zeichnen mehrere Segmente **zerteilen**.

Ein Segment ist definiert durch zwei Punkte $p_1 = (x_1, y_1)$ und $p_2 = (x_2, y_2)$.
Wir könnten aus den Punkten die Geradengleichung $f(x) = mx + t$ berechnen und diese 'abfahren'.
Hier würden wir jedoch auf unangenehme Sonderfälle stoßen.
Zum Beispiel, lässt sich ein Segment was parallel zur $y$-Achse verläuft nicht durch eine Funktion beschreiben.

```{figure} ../../figs/image-representation/midpoint.png
---
width: 300px
name: fig-midpoint
---
```

Was sagt uns folgende Beobachtung:
Ist $p_1, p_2$ gegeben dann ist der Mittelpunkt $m_1 = ((x_1 + x_2)/2, (y_1 + y_2)/2)$ Teil des Segments.
Außerdem erhalten wir neue Segmente $(p_1,m_1)$ und $(m_1,p_2)$.
Wir können dies mit den beiden neuen Segmenten wiederholen und erhalten vier neue Segmente.
Diesen Vorgang können wir solange fortsetzen, bis ein Segment komplett in einem Pixel enthalten ist und eine weitere Verfeinerung keine Wirkung mehr erzeugt.

Wir können diesen Vorgang **rekursiv** realisieren.
Das heißt die Funktion, welche den Mittelpunkt berechnet, wird innerhalb dieser Funktion erneut aufgerufen.
Das kann endlos so weiter gehen und wir müssen uns eine **Abbruchbedingung** überlegen.

```{exercise} Mittelpunkt berechnen
Schreiben Sie eine Funktion ``midpoint(p1, p2)`` die Ihnen den Mittelpunkt ``(mx,my)`` des Segments ``(p1=(x1,y1), p2=(x2, y2))`` zurückgibt.
```

def midpoint(p1, p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2

midpoint((0,0),(3,3))

````{exercise} Mittelpunkt berechnen
Schreiben Sie eine Funktion ``distance(p1,p2)`` die Ihnen den Mittelpunkt die Länge des Segments ``(p1=(x1,y1), p2=(x2, y2))`` zurückgibt.

**Tipp:** Sie können die Funktion ``sqrt`` der ``numpy`` Bibliothek verwenden, d.h.

```python
import numpy as np
...
np.sqrt(...)
...
```

````

``distance()`` können wir als Abbruchbedingung der Rekursion verwenden.
Ist ``distance(p1,p2) <= resolution`` macht es keinen großen Sinn mehr das Segment ``(p1,p2)`` weiter zu verkleinern. 

```{exercise} Segmentpunkte erzeugen
Schreiben Sie eine Funktion ``line(p1, p2, resolution)``, die Ihnen Punkte des Segments ``(p1,p2)`` erzeugt und als Liste zurückgibt.
```

import numpy as np
def distance(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def split(p1, p2, resolution, points):
    if distance(p1,p2) <= resolution:
        return points
    m1 = midpoint(p1, p2)
    points.append(m1)
    split(p1,m1,resolution,points)
    split(m1,p2,resolution,points)
    return points

def line(p1, p2, resolution):
    points = []
    split(p1, p2, resolution, points)
    return points
line((0,0),(3,0),0.1)

Mit ``line`` können nun Punkte eines Segments erzeugen und durch ``to_pixel`` können wir diese Punkte in Pixel umwandeln.
Lassen Sie uns nun einmal ein Bild mit einer Geraden zeichen:

resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
points = line((1,1), (9,9), resolution)
pixels = list(map(lambda point: to_pixel(point, resolution), points))
for pixel in pixels:
    picture[pixel[1]][pixel[0]] = 0
    
plot_picture(picture)

Das sieht schon recht gut aus.
Da der Pixel ``picture[0][0]`` rechts oben ist, ist unser Koordinatensystem an der $x$-Achse gespiegelt und nach oben verschoben, was wir jedoch hier vernachlässigen.

```{exercise} Linie zeichnen
Schreiben Sie eine Funktion ``draw_line(picture, p1, p2, resolution)``, die das Segment ``(p1,p2)`` in das Bild ``picture`` hineinzeichnet.
Behandeln Sie auch den Fall, dass das Segment nicht in das Bild passt (es soll dann kein Fehler kommen sondern der Teil der nicht hinein passt wird abgeschnitten).
```

def contains_pixel(picture, pixel):
    return pixel[0] >= 0 and pixel[0] < len(picture) and pixel[1] >= 0 and pixel[1] < len(picture[0])

def draw_line(picture, p1, p2, resolution):
    points= line(p1, p2, resolution)
    pixels = list(map(lambda point: to_pixel(point, resolution), points))
    for pixel in pixels:
        if contains_pixel(picture, pixel):
            picture[pixel[1]][pixel[0]] = 0

resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_line(picture, (-1,-1), (11,11), resolution)
plot_picture(picture)

Jetzt haben wir alle Teilprobleme gelöst und können das Dreieck bzw. Rechteck zeichnen.

```{exercise} Dreieck zeichnen
Schreiben Sie eine Funktion ``draw_triangle(picture, p1, p2, p3, resolution)`` die das Dreieck ``(p1,p2,p3)`` in das Bild ``picture`` hineinzeichnet.
```

def draw_triangle(picture, p1, p2, p3, resolution):
    draw_line(picture, p1, p2, resolution)
    draw_line(picture, p2, p3, resolution)
    draw_line(picture, p3, p1, resolution)
    
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_triangle(picture, (1,1), (5,9), (9,1), resolution)
plot_picture(picture)

```{exercise} Rechteck zeichnen
Schreiben Sie eine Funktion ``draw_rectangle(picture, p1, p2, p3, p4, resolution)`` die das Rechteck ``(p1,p2,p3,p4)`` in das Bild ``picture`` hineinzeichnet.
```

def draw_rectangle(picture, p1, p2, p3, p4, resolution):
    draw_line(picture, p1, p2, resolution)
    draw_line(picture, p2, p3, resolution)
    draw_line(picture, p3, p4, resolution)
    draw_line(picture, p4, p1, resolution)
    
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_rectangle(picture, (1,1), (1,9), (9,9), (9,1), resolution)
plot_picture(picture)

Wenn wir uns nun die beiden Funktionen ``draw_triangle`` und ``draw_rectangle`` genauer ansehen und unsere **Mustererkennung** aktivieren könnte uns etwas auffallen?
Die Funktionen gleichen sich!
Beide zeichnen eine Sequenz/Liste von zusammenhängenden Segmenten oder anders gesagt: beide zeichnen ein Polygon!

```{exercise} Polygon zeichnen
Schreiben Sie eine Funktion ``draw_polygon(picture, polygon, resolution)`` die das Polygon ``polygon = (p1,p2,p3,p4,p5,...)`` in das Bild ``picture`` hineinzeichnet.
``polygon`` kann eine Liste oder Tupel sein.
```

def draw_polygon(picture, polygon, resolution):
    for i in range(len(polygon)):
        draw_line(picture, polygon[i-1], polygon[i], resolution)
    
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_polygon(picture, ((1,1), (1,9), (9,9), (9,1)), resolution)
plot_picture(picture)

Dreieck und Reckteck hätten wir geschafft.
Für den Kreis $K$ müssen wir zurück in unsere **abstrakte** Welt der geometrischen Objekte, denn einen Kreis nicht mit lauter Segmenten darzustellen macht wenig Sinn.
Die Punkte eines Kreises lassen sich durch eine *Kurve* beschreiben.
Sie der Kreis durch seinen Mittelpunkt $m = (x_m, y_m)$ und den radius $r$ beschrieben dann sind

$$K = \{(x_m + \cos(t) \cdot r, y_m + \sin(t) \cdot r) : t \in [0;2\pi]\}$$

die Punkte des Kreises bzw. der Kreis selbst.
Um den Kreis zu zeichnen unterteilen wir einfach das Intervall $[0;2\pi]$ in $n$ Teile und erhalten so $n$ Punkte.
Wir könnten z.B. $n$ so wählen dass $2\pi / n <$ ``resolution`` ist. 

```{exercise} Kreis zeichnen
Schreiben Sie eine Funktion ``draw_circle(picture, circle, resolution)`` die den Kreis ``circle = (m=(x,y), r)`` in das Bild ``picture`` hineinzeichnet.
Sie können erneut ``numpy`` verwenden, d.h. ``np.sin()``, ``np.cos()``, ``np.pi`` und (optional) ``np.linspace()``.
```

import numpy as np
def draw_circle(picture, circle, resolution):
    center = circle[0]
    radius = circle[1]
    n = int(6 * np.pi / resolution)
    t = np.linspace(start=0.0, stop=2 * np.pi, num=n)
    for dt in t:
        x = center[0] + np.cos(dt) * radius
        y = center[1] + np.sin(dt) * radius
        pixel = to_pixel((x, y), resolution)
        if contains_pixel(picture, pixel):
            picture[pixel[1]][pixel[0]] = 0
    
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_circle(picture, ((5,5), 3), resolution)
plot_picture(picture)

Im Falle des Kreises beschreibt 

$$k(t) = (x_m + \cos(t) \cdot r, y_m + \sin(t) \cdot r)$$

die *Kurve* des Kreises.
Wir können aber auch andere *Kurven* wir zum Beispiel die Funktion $f(x) = x^2$ durch die *Kurve* $k(t) = (t, f(t))$ zeichnen.
Durch wie viele Punkte die Funktion noch gut erkennbar ist, ist jedoch im allgemeinen nicht so einfach zu schätzen.


```{exercise} (mathematische) Funktion zeichnen
Suchen Sie sich irgendeine geeignete Funktion aus und zeichnen Sie diese in einem geeigneten Intervall.
```

import numpy as np
def draw_function(picture, f, start, stop, resolution):
    n = int(3 * (stop - start) / resolution)
    t = np.linspace(start=start, stop=stop, num=n)
    for dt in t:
        pixel = to_pixel((dt, f(dt)), resolution)
        if contains_pixel(picture, pixel):
            picture[pixel[1]][pixel[0]] = 0
            
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_function(picture, lambda t: (t-5)**2, 1, 9, resolution)
plot_picture(picture)

## Daumenkino

Die folgende Methode erwartet eine Liste von Bilder (in Ihrem Format) und generiert daraus eine Animation (eine Folge von Plots) und falls Sie das Argument ``save`` auf ``True`` setzen wird ein GIF (eine Bildfolge/Daumenkino/Minivideo) erzeugt und in der Datei ``'binary-drawing.gif'`` abgespeichert.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
from IPython.display import HTML, display
from IPython.display import HTML

def animate(pictures, interval = 100, save = False, title = '', dpi = 80):
    cmap='gray'
    vmin = 0
    vmax = 1
    fig, ax = plt.subplots()
    plt.title(title)
    im = plt.imshow(pictures[0], animated=True, cmap = cmap, vmin = vmin, vmax = vmax)
    i = {'index': 0} # trick to enforce sideeffect
    def updatefig(*args):
        i['index'] += 1
        if i['index'] == len(pictures):
            i['index'] = 0
        im.set_array(pictures[i['index']])
        return im, 
    ani = animation.FuncAnimation(fig, updatefig, interval=interval, blit=True, save_count=len(pictures))
    if save:
        ani.save('binary-drawing.gif', dpi=dpi, writer="imagemagick")
    plt.close()
    return ani

````{exercise} Einfaches Daumenkino
Generieren Sie folgendes GIF/Daumenkino bzw. Animation:

```{figure} ../../figs/image-representation/daumenkino.gif
---
height: 150px
name: fig-daumenkino
---
```

**Tipp:** Sie benötigen lediglich mehrere Aufrufe von ``generate_border_picture()``.
````

size = 20
increase = [generate_border_picture(width=size, height=size, border_width=i) for i in range(size//2)]
decrease = [generate_border_picture(width=size, height=size, border_width=(size//2)-i) for i in range((size//2)-1)]
border_pictures = increase + decrease
ani = animate(border_pictures, save=True)
HTML(ani.to_jshtml())

Fassen wir noch einmal kurz zusammen was wir bis jetzt geschafft haben:
Wir haben uns ein Format für ein Schwarz-Weiß-Bild ausgedacht und umgesetzt.
Durch ein wenig Hilfe externer Bibliotheken können wir unser Rasterbild anzeigen.
Wir haben Algorithmen implementiert die uns Polygone (inkl. Dreiecke und Rechtecke), Kreise und sogar Funktionen zeichnen.
Und jetzt haben wir sogar die Möglichkeit aus einer Folge von Bildern ein kleines Video zu generieren.
Dieses Video wiederum ist nichts anderes als eine Liste von Listen von Listen von $0$ und $1$.
Wir haben nun die Möglichkeit eine unbegrenzte Menge an Animationen zu erzeugen, von bewegten geometrischen Objekten bis hin zum [Game Of Life](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens) - Ihre Kreativität ist das Limit.

````{exercise} Simulation eines Partikels
Generieren Sie eine Animation ein Partikel (einen Ball) der sich in einer Box bewegt, d.h. der Ball bewegt sich mit konstanter Geschwindigkeit und prallt von der Wand ab.

```{figure} ../../figs/image-representation/daumenkino_ball.gif
---
height: 150px
name: fig-daumenkino-ball
---
```

**Tipps:** Schreiben Sie erst eine Methode die einen *Kreis* ``circle = (m = (x,y), r)`` in einer Box fortbewegt und diese Bewegung als Liste von Kreisen zurückgibt.
Anschließend können Sie mit ``draw_circle()`` diese Liste in eine Liste von Bildern umwandeln. Bedenken Sie, dass sie für jeden Kreis ein neues Bild durch ``generate_border_picture()`` generieren müssen. 
````

def generate_ball_box(width, height, circle, resolution):
    w = int(width/resolution)
    h = int(height/resolution)
    picture = generate_border_picture(width=w, height=h, border_width=1)
    ball = draw_circle(picture, circle, resolution)
    return picture

def animate_ball(nframes):
    resolution = 0.1
    box_width = 10
    box_height = 10
    x = 5
    y = 5
    radius = 1
    velocity = [0.1,0.3]
    
    animation = []
    time = 1
    for i in range(nframes):
        # collision detection
        if x - radius <= 0 or x + radius >= box_width:
            velocity[0] = -velocity[0]
        if y - radius <= 0 or y + radius >= box_height:
            velocity[1] = -velocity[1]
        
        x = x + velocity[0] * time
        y = y + velocity[1] * time
        circle = ((x,y),radius)
        animation.append(generate_ball_box(box_width,box_height,circle,resolution))
    return animation

ani = animate(animate_ball(nframes=100), save=True)
HTML(ani.to_jshtml())

```{exercise} Eigenes Daumenkino
Erzeugen Sie Ihr eigenes Daumenkino. Vielleicht ein bewegtes Dreieck oder eine fortlaufende Sinuswelle oder etwas ganz anderes?
```

## Fourier-Zeichnungen (optional)

Was nun folgt ist ein sich Austoben in der Welt die wir uns geschaffen haben.
Wir möchten Ihnen eine ganz bestimmte Zeichenmethode nicht vorenthalten.
Stellen Sie sich ein Blatt Papier vor.
Auf diesem zeichnen Sie einen Kreis $K_0$.
Anhand dieses Kreises zeichnen Sie einen weiteren Kreis $K_1$ sodass der Mittelpunkt von $K_1$ während Sie zeichnen auf $K_0$ wandert.
Nachdem Sie fertig sind, löschen $K_0$.
Ihr Ergebnis hängt davon ab wie schnell sie auf $K_0$ wandern und wie schnell Sie $K_1$ zeichen, d.h. das Ergebnis hängt von den Frequenzen ab.
Zeichnen Sie beide Kreise mit der gleichen Frequenz und starten beide Kreise bei $y = 0$ so ist $K_1$ ein Kreis wobei dessen Radius die Summe der Radii der beiden Kreise ist.

Angenommen $K_0(t) = (x_0 + \cos(\omega_0 \cdot t) \cdot r_0, y_0 + \sin(\omega_0 \cdot t) \cdot r_0)$ und $K_1(t) = (\cos(\omega_1 \cdot t) \cdot r_1, \sin(\omega_1 \cdot t) \cdot r_1)$ dann gilt für ihre gezeichnete Kurve 

$$K(t) = K_0(t) + K_1(t)$$

Wir können das weiter verallgemeinen und von $n$ Kreisen ausgehen, dann gilt für ihre Zeichnung:

$$K(t) = \sum_{i=0}^{n-1} K_i(t)$$

````{exercise} Fourier-Zeichnungen
Schreiben Sie eine Funktion ``draw_circular(picture, center, frequencies, radii, resolution, start stop)``, die die oben beschriebene Zeichentechnik implementiert.
Dabei soll ``center`` gleich $(x_0, y_0)$, ``frequencies`` eine Liste die alle Frequenzen $\omega_0, \ldots \omega_{n-1}$ und ``radii`` eine Liste die alle Radii $r_0, \ldots, r_{n-1}$ enthält sein.
``start`` und ``stop`` sollen ihr (Zeichen-)Intervall definieren.

Als Motivation hier ein Beispiel:

```python
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_circular(picture, (5,5), [4,15], [3,0.7], resolution, 0.0, 2*np.pi)
plot_picture(picture)
```

ergibt

```{figure} ../../figs/image-representation/fourier-drawing.png
---
height: 150px
name: fig-fourier-drawing
---
```

````

def draw_circular(picture, center, frequencies, radii, resolution, start=0.0, stop=2*np.pi):
    n = int(2*max(frequencies)*(stop-start) / resolution)
    t = np.linspace(start=start, stop=stop, num=n)
    for dt in t:
        x = center[0]
        y = center[1]
        
        for i in range(min(len(frequencies), len(radii))):
            radius = radii[i]
            frequency = frequencies[i]
            x = x + np.cos(frequency*dt) * radius
            y = y + np.sin(frequency*dt) * radius
        
        pixel = to_pixel((x, y), resolution)
        if contains_pixel(picture, pixel):
            picture[pixel[1]][pixel[0]] = 0
            
resolution = 0.1
picture = generate_border_picture(width=100, height=100, border_width=0)
draw_circular(picture, (5,5), [1,5,4], [2,1,0.5], resolution, 0.0, 2*np.pi)
plot_picture(picture)

Es ergeben sich interessante Fragen.
Zum Beispiel, mit welchen Argumenten erhalten Sie ein **harmonisches** (ein eher einfaches) Bild und warum?
Wann erhalten Sie hingegen ein komplexeres Gebilde?
Was hat das mit den **harmonischen** bzw. **unharmonischen** Schwingungen und einem **harmonischen** bzw. **unharmonischen** Ton zu tun?
Können wir durch unsere Zeichenmethode Ton zeichnen?

Falls Sie sich mehr mathematisches Wissen zu diesem Thema aneignen möchten, ist folgendes exzellentes Video von **Grant Sanderson** ein wunderbarer Einstieg:

<div style="display: block;margin-left: auto;margin-right: auto;width: 632px;">
<iframe width="632" height="276" src="https://www.youtube.com/embed/r6sGWTCMz2k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>