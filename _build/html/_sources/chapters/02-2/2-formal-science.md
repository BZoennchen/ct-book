# Strukturwissenschaften

## Nachrichtentechnik 

1948 griff Claude E. Shannon den physikalischen Begriff der *Entropie* auf und übetrug Ihn auf die Nachrichtenübertragung.
Sein Modell prägte die Informatik über viele Jahre und ist heute noch relevant.
Es ist äußerst wichtig zu verstehen, dass es Shannon um die *Informationsübertragung* ging.
Sie ist für sein Modell von zentraler Bedeutung.
So schreibt er in {cite}`shannon:1948`:

> Frequently the messages have meaning; that is they refer to or are correleted according to some system with certain physical or conceptual entities. These **semantic aspects of communication are irrelevant** to the engineering problem. The significant aspect is that the actual message is one selected from a set of possible messages. The system must be designed to operate for each possible selection, not just the one which will actually be chosen since this is unknown at the time of design. -- Claude E. Shannon

Shannon war sich bewusst, dass zur Information auch Ihre Bedeutung (Semantik) gehört doch befand er diese für die *Informationsübertragung* über ein Medium als irrelevant.
Die Übertragung besteht dabei aus mehreren Teilen:

1. Eine (Informations)-**Quelle** versendet eine **Nachricht**.
2. Diese Nachricht wird durch einen **Sender** in ein **Signal** codiert und in einen **Kanal** eingespeist.
3. Der **Kanal** ist das Medium der Übertragung, beispielsweise ein Netzwerkkabel. Bei dieser Übertragung kann es zu einer Störung durch eine **Störquelle** kommen. Unter Umständen ist das **erhaltene Signal** gestört.
4. Ein **Empfänger** empfängt dieses möglicherweise gestörte **erhaltene Signal**, decodiert es und leitet es an das **Ziel** weiter.
5. Die decodierte **Nachricht** kommt bei ihrem Ziel an.

```{figure} ../../figs/information/shannon-messages.png
---
width: 600px
name: fig-shannon-messages
---
Shannon's Schema der Nachrichtenübertragung bzw. Kommunikation.
```

In diesem Modell ist die Nachricht eine *Information* und der *Informationsgehalt* ist umso größer je mehr mögliche Nachrichten es gibt.

> If the number of [possible] messages [...] is finite then this number [...] can be regarded as a measure of the information produced when one message [... from the set of possible messages], all
choices being equally likely -- Claude E. Shannon

Gehen wir zurück zu unserem Einführungsbeispiel in der U-Bahn.
Falls der Wetterbericht Ihnen lediglich mitteilen kann ob es regnet oder nicht, so ist der Informationsgehalt, dass es regnet gering.
Wenn aber der Wetterbericht Ihnen unterschiedliche Arten von Regen oder anderen Wetterlagen berichten kann so trägt eine dieser konkreten Wetterlagen einen großen Informationsgehalt in sich.
Schon an diesem Beispiel sehen wir aber auch eine schwäche dieser Definition: Ob es draußen 25 Grad oder 25.00001 Grad hat, ist Ihnen höchst wahrscheinlich gleichgültig.
Doch ein Wetterbericht der Ihnen die Temperatur auf fünf Nachkommastellen genau berichtet, liefert nach Shannon's Definition einen viel höheren Informationsgehalt als ein Dienst, der bei der ersten Nachkommastelle rundet.
Der Informationsgehalt ist rein **syntaktisch** definiert.

Einer der Vorzüge der (strukturwissenschaftlichen) Definition ist jedoch, dass wir ein Maß für den *Informationsgehalt* definieren können.
Shannon misst den *Informationsgehalt* einer Nachricht über die *Entropie*, welche uns in der Physik schon über den Weg gelaufen ist.
Die Entropie in der Informatik ist ein Maß für den *mittleren Informationsgehalt* einer *Nachricht*.

```{admonition} Entropie (Informatik)

Sei $X$ eine Zufallsvariable einer gedächtnislosen Quelle über einem endlichen, aus Zeichen bestehenden Alphabet $\Sigma = \left\{ \sigma_1, \ldots, \sigma_m \right\}$.
Sei $p_\sigma = P(X = \sigma)$ die Wahrscheinlichkeit, dass die Zufallsvariable $X$ das Zeichen $\sigma$ annimmt.
Dann ist 

$$I(\sigma) = \log_2(1/p_\sigma) = - \log_2(p_\sigma)$$

der **Informationsgehalt des Zeichens** (notwendige Binärbits um $1 / p_\sigma$ Ereignisse zu unterscheiden).

Die **Entropie eines Zeichens** ist definiert als der Erwartungswert des Informationsgehalts:

$$H_1 = E[I] = \sum_{\sigma \in \Sigma} p_\sigma I(\sigma) = - \sum_{\sigma \in \Sigma} p_\sigma \log_2(p_\sigma)$$

Die **Entropie** $H_n$ **für Wörter** $w \in \Sigma^n$ der Länge $n$ ergibt sich durch

$$H_n = - \sum_{w \in \Sigma^n} p_w \log_2(p_w),$$

wobei $p_w = P(X = w)$ die Wahrscheinlichkeit ist, mit der das Wort $w$ auftritt.

Die **Entropie** $H$ ist der Limes $n \rightarrow \infty$

$$H = \lim_{n \rightarrow \infty} \frac{H_n}{n}.$$
```

Lassen Sie sich nicht von den mathematischen Symbolen abschrecken.
Kurz gesagt: je größer die Gewissheit, desto kleiner ist der Informationsgehalt.
Information führt zur Beseitigung von Unsicherheit.
Je mehr Unsicherheit beseitigt wird, desto größer ist der Informationsgehalt!

Das Konzept der *Entropie* wird schnell anhand eines Beispiels klar.
Nehmen wir den Münzwurf mit einer perfekten Münze.
Werfen Sie die Münze einmal so ist der Informationsgehalt $H_1 = 1$.
Die Wahrscheinlichkeit für Kopf oder Zahl liegt bei $0.5$, daraus ergibt sich:

$$H_1 = 0.5 \cdot \log_2(2) + 0.5 \cdot \log_2(2) = 0.5 + 0.5 = 1$$

Die Informationsquelle ist der Münzwurf, die Nachricht das Ergebnis des Wurfes und der Empfänger sind wir, die den Münzwurf beobachten.

```{exercise} Entropie
:label: entropie-exercise
Welche Entropie $H$ hat die Nachricht die von einer Informationsquelle stammt, welche durchgehend nur $1$ sendet?
```

```{solution} entropie-exercise
:label: entropie-solution
:class: dropdown
Da für jedes Wort $w$ die Wahrscheinlichkeit gleich $1$ ist, d.h. $P(X = w) = 1$, folgt $H = 0$.
```

Lassen Sie uns ein weiteres Beispiel betrachten.
Stellen Sie sich vor, Sie hätten eine Informationsquelle die fortwährend die Folge $0,1,0,1,0,1, \ldots$ ausspuckt.
Für $H_1$ ergibt sich $H_1 = 1$, denn wie beim Münzwurf besteht eine Wahrscheinlichkeit von $0.5$ ob wir eine $0$ oder $1$ für ein Zeichen an einer zufälligen Stelle erhalten.
Das ändert sich jedoch nicht wenn wir die Wortlänge auf $2$ erhöhen ($H_2 = 1$), denn mit Wahrscheinlichkeit $0.5$ sehen wir entweder $1,0$ oder $0,1$.
Wäre die Folge rein zufällig wäre $H_2 = 2$, denn mit Wahrscheinlichkeit $0.25$ sähen wir $0,0$ oder $0,1$ oder $1,0$ oder $1,1$.
Es ergibt sich:

$$H_2 = 4 \cdot 0.25 \cdot \log_2(4) = \log_2(4) = 2$$

Für unsere Folge $0,1,0,1,0,1, \ldots$ entscheidet das erste Zeichen über alle weiteren Zeichen egal wie lang das Wort ist welches wir betrachten, somit ist die Entropie $H_n = 1$ und damit

$$H = \lim_{n \rightarrow \infty} \frac{H_n}{n} = \lim_{n \rightarrow \infty} \frac{1}{n} = 0$$

Der Informationsgehalt ist gering und wir könnten mit deutlich weniger Zeichen, die gleiche Information übertragen!
Die rein zufällige Folge aus $0$ und $1$ steht im Gegensatz dazu und enthält sehr viel Information, denn

$$H_n = \log(2^n) = n$$

und damit gilt

$$H = \lim_{n \rightarrow \infty} \frac{H_n}{n} = \lim_{n \rightarrow \infty} \frac{n}{n} = 1.$$

Bei Shannon's Informationsbegriff gehen wir davon aus, dass Information in kleinste Informationsteile (*Bits*) zerlegbar.
Zudem ist die Summe dieser Teilchen die Information selbst.
Beim Zusammensetzen der Einzelteile, also der Kombination von Symbolen, entsteht demnach keine neue Qualität, welche eben nicht auf die einzelnen Symbole reduziert werden kann.

```{admonition} Information (Informatik)
Eine *Information* ist eine übertragene Nachricht und kann als die Summe ihrer Einzelteile betrachtet werden.
```

Shannon's Informationsbegriff ignoriert jedwede Semantik und verdinglicht die Information, dennoch ist er aus technischer Sicht sehr nützlich.
Sie hiflt uns zu bestimmen wie viel Zeichen (Syntax) notwendig sind um etwas auszudrücken.
Eine hohe *Entropie* bedeutet in diesem Zusammenhang, dass wir unsere Zeichen sparsam nutzen.
Außerdem kann die *Entropie* als Informationsgehalt aus Sicht der digitalen Maschine verstanden werden, da sie keinerlei Semantik a priori kennt.
Zwar kann der Computer, zum Beispiel zwei Binärzahlen addieren, doch hat er keinerlei Vorstellung vom Gegenstand der Zahl.
Alle Manipulationen sind syntaktischer Natur, d.h. eine Manipulation von Zeichen.

```{admonition} Formale Methoden
:class: hint
Formale Methoden sind unter anderem eine Anstrengung um wesentliche semantische Aspekte von Sprache und Denken auf regelgeleitete, rein syntaktische Symbolmanipulation zurückzuführen.
```

## Informationstheorie

Ein weiterer äußerst interessanter technischer Informationsbegriff (die Kolmogorow-Komplexität) stammt aus der Theoretischen Informatik.
Wir werden diesen Begriff hier nur am Rande erwähnen.

Wir wechseln die Perspektive von der *Nachricht* zu ihrer *Konstruktion* durch einen Algorithmus.
Wir suchen den 'einfachsten' Algorithmus der eine bestimmte Information erzeugen kann.
Daraufhin analysieren wir nicht die Information selbst, sondern jenen Algorithmus.
Ist dieser einfach, im Sinne der Kolmogorow-Komplexität, so ist der Informationsgehalt gering.
Ist der Algorithmus hingegen komplex, so ist der Informationsgehalt hoch.

Anders ausgedrückt ist der *Informationsgehalt* einer Nachricht gleich der Länge der bestmöglichen eigenständigen Komprimierung jener Nachricht.
Eine solche Komprimierung kann als Programm aufgefasst werden.
Aus dieser Sicht enthält ein $3000$-seitiges Lexikon weniger Informationen als eine gleich lange rein zufällig generierte Zeichenkette, obwohl das Lexikon selbstverständlich viel nützlicher ist.
Wir könnten aus den Wörtern des Lexikons einige Buchstaben löschen und, aufgrund unserer Sprachkenntnisse, das Werk wieder rekonstruieren.
Für die zufällige Folge an Zeichen gilt dies nicht.

Auch dieser Begriff bezieht nur die Syntax einer vorliegenden *Information* ein.
Die Semantik wird erneut ausgeklammert.