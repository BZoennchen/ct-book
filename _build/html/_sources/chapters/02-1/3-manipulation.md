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

(sec-manipulation)=
# Manipulation

Eingabegeräte transformieren Information, wie etwa einen Tastendruck oder die Aufnahmen einer Videokamera, in elektrische Signale.
Sie realisieren eine bestimmte [Interpretation](def-interpretation) $I$.
Die Tastatur interpretiert unseren Tastendruck einer bestimmten Taste und gibt ihre Bedeutung an die anderen Bauteile des Computers weiter.
Die elektrischen Signale (**Strom aus** und **Strom an**) gelangen über mikroskopisch kleine Leitungen in sogenannte Schaltkreise.
Dort werden die Signale, d. h. die [Bits](def-bit) und [Byte](def-byte) weiterverarbeiten.

*Logikgatter* oder kurz *Gatter* sind konzeptionelle Anordnungen von elektrischen Schaltungen, welche boolsche Operationen durchführen.

```{admonition} Gatter und Bauteile
:class: remark
:name: remark-gates

Gatter beschreiben die Funktionsweise.
Elektrische Schaltkreise und Transistoren sind eine mögliche Realisierung.
Gatter sind **konzeptionelle Bauteile** wohingegen elektrische Schaltkreise, Transistoren, Leitungen und Flip-Flops (später mehr dazu) **physikalische Bauteile** sind.
```

Ein oder zwei Signale gelangen in ein Gatter und, je nachdem um welches Gatter es sich handelt, wird ein bestimmtes Ausgabesignal ausgegeben.
Das Ausgabesignal hängt von den ein oder zwei Eingabesignalen und dessen Typ des Gatters ab.
Jedes Gatter realisiert eine [(mathematische) Funktion](def-math-function).

(sec-gates)=
## Basis Gatter

Das einfachste **Not**-Gatter nimmt als Eingabe ein Signal und gibt dessen *Negation* davon aus.
Aus 0 wird 1 und aus 1 wird 0.

```{code-cell} python3
def lnot(bit):
    return int(not bit)
    
print(lnot(0))
print(lnot(1))
```

```{figure} ../../figs/digital-computer/manipulation/gatter-not.png
---
width: 300px
name: fig-not
---
Das Symbol für das **Not**-Gatter (links) und seine Ein- und Ausgabewerte (rechts).
```

Ein weiteres sehr einfaches Gatter ist das sogenannte **AND**-Gatter.
Es kombiniert zwei Signale und gibt genau dann 1 aus, wenn beide Eingabesignale gleich 1 sind.

```{code-cell} python3
def land(in1, in2):
    return in1 and in2
    
print(land(0,0)) 
print(land(0,1))
print(land(1,0))
print(land(1,1))
```

```{figure} ../../figs/digital-computer/manipulation/gatter-and.png
---
width: 340px
name: fig-and
---
Das Symbol für das **AND**-Gatter (links) und seine Ein- und Ausgabewerte (rechts).
```

Zu guter Letzt fehlt noch das **OR**-Gatter.
Es kombiniert zwei Signale und gibt 1 aus genau dann wenn eines oder beide der Eingabesignale gleich 1 sind.

```{code-cell} python3
def lor(in1, in2):
    return in1 or in2
    
print(lor(0,0)) 
print(lor(0,1))
print(lor(1,0))
print(lor(1,1))
```

```{figure} ../../figs/digital-computer/manipulation/gatter-or.png
---
width: 340px
name: fig-or
---
Das Symbol für das **OR**-Gatter (links) und seine Ein- und Ausgabewerte (rechts).
```

```{exercise} OR-Gatter
:label: or-gate-exercise
Das Symbol für das OR-Gatter enthält das größer gleich Zeichen $\geq$.
Was könnte das für einen Grund haben?
Schreiben Sie eine Python Funktion ``lor(in1, in2)`` die sich diesen Grund zunutze macht.

**Tipp**: Denken Sie an die Addition.
```

````{solution} or-gate-exercise
:label: or-gate-solution
:class: dropdown
Der Grund dafür ist, dass das Gatter genau dann 1 ist wenn

$$x + y \geq 1$$

gilt.

```python
def lor(in1, in2):
    return int(in1 + in2 >= 1)

print(lor(0,0)) 
print(lor(0,1))
print(lor(1,0))
print(lor(1,1))
```

````

Jedes Gatter können wir auch als [Interpretation](sec-interpretation) $I$ beschreiben.
Zum Beispiel wäre die Interpretation des **AND**-Gatters durch folgende Mengen gegeben:

+ Bedeutung $B_{\text{AND}} = \left\{0, 1\right\}$
+ Repräsentation $R_{\text{AND}} = \left\{ 00, 01, 10, 11 \right\}$
+ Interpretation $I_{\text{AND}} = \left\{ (00, 0), (01, 0), (10, 0), (11, 1) \right\}$.

Nun gut, diese Operationen scheinen lächerlich einfach zu sein, aber kombinieren wir mehrere Gatter können wir mehr und mehr komplexe Operationen durchführen.
Im Endeffekt **basieren alle Berechnungen des Computers auf diesen sehr primitiven Gattern/Operationen**.
Die Logikgatter implementieren die sog. *boolsche Algebra*.

Obwohl sehr viele kleine Operationen notwendig sind, lassen sich diese Operationen sehr schnell durchführen.
Signale breiten sich mit annähernd Lichtgeschwindigkeit aus und so sind gigantische Mengen an primitiven Operationen in sehr kurzer Zeit durchführbar.
Je kleiner die Chips, desto kleiner ist die Distanz, welche die Signale überwinden müssen und desto schneller ist der Computer.

## Komplement

In Abschnitt [Ganze Zahlen](sec-integers) haben wir besprochen wie diese durch das zweier Komplement repräsentiert werden.
Um aus eine Binärzahl $k = b_{n-1}\ldots b_0$ ihr Negativ zu bilden, also $-k$, bilden wir das Komplement und addieren eins:

$$-k = \overline{b_{n-1}\ldots b_0} + 1$$

Wie würden wir das Komplement $\overline{b_{n-1}\ldots b_0}$ mit Gattern realisieren?
Jedes Signal $b_i$ muss durch ein Not-Gatter negiert werden.
Somit könnten wir die Signale der Binärzahl durch $n$ Not-Gatter hindurch schicken und würden ihr Komplement erhalten:

```{code-cell} python3
def complement(b3, b2, b1, b0):
    return lnot(b3), lnot(b2), lnot(b1), lnot(b0)

print(complement(0,0,0,0)) 
print(complement(1,0,1,1)) 
```

(sec-addierer)=
## Addierer

Betrachten Sie einmal ``land`` und ``lor``.
Welche mathematische Funktion realisieren diese einfachen Gatter?
Nun ja, wenn wir die beiden Eingabesignale als Zahlen interpretieren, dann ist ``land`` gleich dem Minimum ``min`` und ``lor`` gleich dem ``max`` der beiden Signale:

```{code-cell} python3
def lor(in1, in2):
    return max(in1, in2)

def land(in1, in2):
    return min(in1, in2)   

print(lor(0,0)) 
print(lor(0,1))
print(lor(1,0))
print(lor(1,1))

print(land(0,0)) 
print(land(0,1))
print(land(1,0))
print(land(1,1))
```

Diese Operation ist sehr simpel.
Dennoch berechnen wir mit nur einem Gatter bereits etwas.

Im folgenden wollen wir Ihnen durch den Bau eines $n$-Bit Addierers zeigen, wie wir durch *Komposition* aus einfachen Berechnungen/Bauteilen komplexe Berechnungen/Bauteilen realisieren können.

### 1-Bit-Addierer

Bauen wir aus den gegebenen Gattern einen Addierer der zwei Zahlen $a, b \in \{0,1\}$ addiert.
Der Addierer erhält zwei Eingabesignale $a, b$ und gibt zwei Signale $c = c_0, c_1$ aus.
Sei $c = c_1c_0$ das Ergebnis der Addition.
Lassen Sie uns alle Möglichkeiten notieren:

\begin{equation*}
\begin{split}
    b\ + a\ &= c_1c_0\\ \hline
    0_2 + 0_2 &= 00_2 \\
    0_2 + 1_2 &= 01_2 \\
    1_2 + 0_2 &= 01_2 \\
    1_2 + 1_2 &= 10_2
\end{split}
\end{equation*}

Wir erhalten $c_1 = 1$, d.h. einen *Übertrag* von $1$ genau dann wenn $a$ und $b$ gleich $1$ sind.
Hingegen ist $c_0$ genau dann $1$ wenn entweder $a$ oder $b$, nicht aber beide, gleich $1$ sind. 
Daraus ergeben sich folgende boolsche Operationen:

$$
\begin{split}
    c_1 &= a \land b \\
    c_0 &= \neg (a \land b) \land (a \lor b) = \neg c_1 \land (a \lor b)
\end{split}
$$

Wir haben diese Operationen als ``Python`` Funktion implementiert.

```{code-cell} python3
def ladd(in1, in0):

    # c1 = a and b
    out1 = land(in1,in0)

    # c0 = (not c1) and (a or b)
    out0 = land(lnot(out1), lor(in0, in1))

    #return c1c2
    return [out1, out0]

ladd(1,1)
```

Als Gatter-Bauplan sieht das ganze wie folgt aus.

```{figure} ../../figs/digital-computer/manipulation/adder.png
---
width: 600px
name: fig-adder
---
Skizze eines 1-Bit-Addierers. Der Zusammenschluss der Gatter (links) und das Symbol für unseren Addierer (rechts).
```
### Erweiterter 1-Bit-Addierer

Durch vier Gatter lassen sich also zwei 1-Bit Zahlen addieren.
Was passiert wenn wir die Anzahl der Bits erhöhen?
Immerhin ist das Addieren von 1-Bit Zahlen doch sehr einschränkend.
Addieren wir größere Zahlen, so stellen wir fest, dass sich diese Operation auf den 1-Bit-Addierer zurückführen lässt.
Wenn Sie, zum Beispiel,

$$1101_2 + 1001_2$$

berechnen, so betrachten Sie in jedem Berechnungsschritt lediglich 3 Bits:
1. das Bit an der $i$-ten Stelle der ersten Zahl
2. das Bit an der $i$-ten Stelle der zweiten Zahl
3. und den Übertrag der letzten ($i-1$-ten) 1-Bit-Addition!

So lautet die erste Rechnung $1+1+0 = 0$ und der Übertrag ist gleich $1$.
Die zweite Rechnung lautet $0+0+1 = 1$ und der Übertrag ist gleich $0$.
Die dritte lautet $0+1+0 = 1$ und der Übertrag ist gleich $0$.
Die vierte und letzte lautet $1+1+0 = 0$ und der Übertrag ist $1$.
Daraus ergibt sich:

$$1101_2 + 1001_2 = 10110_2$$

binär, was 

$$(2^3 \cdot 1 + 2^2 \cdot 1 + 2^1 \cdot 0 + 2^0 \cdot 1) + (2^3 \cdot 1 + 2^2 \cdot 0 + 2^1 \cdot 0 + 2^0 \cdot 1) = 13_{10} + 9_{10} = 22_{10}$$

im Dezimalsystem ergibt.

Wir addieren also je drei 1-Bit Zahlen!
Unser Addierer von oben addiert jedoch nur zwei 1-Bit Zahlen.
Lassen Sie uns also einen 1-Bit-Addierer der drei Zahlen addieren kann konstruieren.
Dieser dient dann der Konstruktion des $n$-Bit-Addierers.
Wir benötigen einen 1-Bit-Addierer mit drei Eingabesignale $u, a, b$ und weiterhin zwei Ausgabesignalen $c_0, c_1$, jedoch interpretieren wir diesmal $u$ als Übertrag für den nächsten Addierer!

Lassen Sie uns erneut alle Möglichkeiten notieren:

\begin{equation*}
\begin{split}
    b\ + a\ + u\ &= c_1c_0\\ \hline
    0_2 + 0_2 + 0_2 &= 00_2 \\
    0_2 + 0_2 + 1_2 &= 01_2 \\
    0_2 + 1_2 + 0_2 &= 01_2 \\
    0_2 + 1_2 + 1_2 &= 10_2 \\
    1_2 + 0_2 + 0_2 &= 01_2 \\
    1_2 + 0_2 + 1_2 &= 10_2 \\
    1_2 + 1_2 + 0_2 &= 10_2 \\
    1_2 + 1_2 + 1_2 &= 11_2
\end{split}
\end{equation*}

Betrachten Sie nun $c_0$.
Fragen wir uns: wann wird $c_0$ gleich $1$?
$c_0$ wird genau dann $1$, wenn genau eines der drei Eingabesignale $1$ ist, d.h., wenn

$$(u \land \neg a \land \neg b) \lor (a \land \neg b \land \neg u) \lor (b \land \neg u \land \neg a).$$

**oder** alle drei Eingabesignale gleich $1$ sind, d.h., wenn

$$(u \land a \land b).$$

Zusammengefasst ergibt sich

$$c_0 = (u \land \neg a \land \neg b) \lor (a \land \neg b \land \neg u) \lor (b \land \neg u \land \neg a) \lor (u \land a \land b).$$

Das scheint sehr ausschweifend, jedoch nur weil wir auf sehr primitive Operationen zurückgreifen können.
Wie sieht es mit $c_1$, also unserem Übertrag aus?
$a_1$ ist genau dann $1$ wenn mehr als 1-Bit der Eingabe gleich $1$ ist, d.h. 

$$c_1 = (u \land a) \lor (a \land b) \lor (b \land u)$$

Kennen wir $c_1$ dann können wir $c_0$ etwas kürzer schreiben.
Denn anstatt zu sagen es muss genau eines der drei Eingabesignale $1$ sein, können wir auch sagen: es gibt keinen Übertrag ($c_1 = 0$) und irgendein Eingabesignal ist $1$.
Aus

$$(u \land \neg a \land \neg b) \lor (a \land \neg b \land \neg u) \lor (b \land \neg u \land \neg a)$$

wird

$$\neg c_0 \land (u \lor a \lor b)$$

und wir erhalten insgesamt:

$$c_0 = (u \land a \land b) \lor (\neg c_1 \land (u \lor a \lor b)).$$

```{code-cell} python3
def ladd(in2, in1, in0):

    # u and a
    and01 = land(in1,in0)
    
    # a and b
    and12 = land(in1,in2)

    # u and b
    and02 = land(in0,in2)

    # u or a or b
    or_all = lor(lor(in0, in1), in2)

    # u and b1 and b
    and_all = land(and01, in2)

    # (u and b1) or (b1 and b) or (u and b)
    out1 = lor(lor(and01, and12), and02)

    # (u and a and b) or ((not c1) and (u or a or b))
    out0 = lor(and_all, land(lnot(out1), or_all))
    return [out1, out0]

print(ladd(0,0,0))
print(ladd(0,0,1))
print(ladd(0,1,0))
print(ladd(0,1,1))
print(ladd(1,0,0))
print(ladd(1,0,1))
print(ladd(1,1,0))
print(ladd(1,1,1))
```

### $n$-Bit-Addierer

Für einen $n$-Bit-Addierer brauchen wir $n$ hintereinander geschaltene 1-Bit-Addierer, welche alle (bis auf den ersten) drei Signale aufnehmen.
Wie oben erwähnt addiert der $i$-te 1-Bit-Addierer das $i$-te Bit der beiden Eingabezahlen und den Übertrag des $(i-1)$-ten 1-Bit-Addierers.
Für den ersten Addierer ist der Übertrag $u$ gleich $0$.

```{figure} ../../figs/digital-computer/manipulation/4-bit-adder.png
---
width: 400px
name: fig-4-bit-adder
---
Skizze eines 4-Bit-Addierers, der $a + b = c$ berechnet. Dabei sind $a, b$ 4-Bit Zahlen und $c$ eine 5-Bit Zahl: $c_4c_3c_2c_1c_0 = a_3a_2a_1a_0 + b_3b_2b_1b_0$
```

Hier sehen Sie den ``Python`` Code eines $4$-Bit-Addierers (wir lesen die Bits von rechts nach links, d.h. das Bit an der Stelle 0 in der liste ist das höchste Bit!):

```{code-cell} python3
def ladd4(a, b):
    # a[3] und b[3] sind die erste Eingabesignale (niedrigsten Bits)
    u1, c0 = ladd(a[3], b[3], 0)
    u2, c1 = ladd(a[2], b[2], u1)
    u3, c2 = ladd(a[1], b[1], u2)
    c4, c3 = ladd(a[0], b[0], u3)
    return [c4, c3, c2, c1, c0]

ladd4([0,0,1,1], [1,0,0,1])
```

Hängt man nun Addierer aneinander so kann man einen Multiplizierer und andere Recheneinheiten wie Fließkommaddierer und mehr bauen.

```{exercise} $n$-Bit-Addierer
:label: n-bit-adder-exercise
Definieren Sie eine ``Python``-Funktion ``laddn(a, b)``, die unter Verwendung von ``ladd(in1, in2, in3)`` Bits variabler länge addiert.
Gehen Sie davon aus, dass die Listen ``a`` und ``b`` die gleiche Länge haben.

**Hinweis:** Studieren Sie den obigen Code, d.h. ``ladd4``. Was wiederholt sich immer wieder und lässt sich somit automatisieren?
```

````{solution} n-bit-adder-exercise
:label: n-bit-adder-solution
:class: dropdown

```python
def laddn(a, b):
    u = 0
    n = len(a)
    result = []
    for i in range(n):
        u, c = ladd(a[n-1-i], b[n-1-i], u)
        result = [c] + result 
    result = [u] + result
    return result

laddn([1,1,1,1], [1,0,0,1])
```
````

```{admonition} Modellierung der Gatter und Addierer
:class: remark
:name: remark-adder-gates
Unser ``Python`` Code modelliert den Addierer als Gatterzusammenschluss.
Natürlich können wir in ``Python`` deutlich einfacher zwei Zahlen addieren.
```

Es gibt auch noch andere Gatter als **AND**, **NOT** und **OR** z.B. **NAND**, **XOR** oder **NOR**, aber all diese Gatter lassen sich durch die drei fundamentalen Gatter ausdrücken.

```{admonition} Anzahl, Größe und Geschwindigkeit
:class: remark
:name: remark-gate-speed
Gatter beschreiben die Funktionsweise, realisiert durch Transistoren, sind unvorstellbar klein und können unvorstellbar oft angesteuert werden.
Transistoren sind dünner als wenige Nanometer (etwa 4000 mal dünner als ein Haar) und lassen sich hunderte Milliarden Mal in der Sekunde ansteuern.
Zum Beispiel befinden sich auf dem Intel i7 4770K Prozessor ca. 1.4 Milliarden Transistoren auf einer Fläche von 177 Quadratmillimeter.
```