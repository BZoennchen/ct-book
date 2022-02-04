(sec-interpretation)=
# Interpretation

In diesem Abschnitt unternehmen wir einen Versuch die Begriffe **Interpretation**, **Repräsentation**, **Bedeutung**, **Semantik** und **Syntax** zu erklären.
Dadurch möchten wir ein theoretisches Fundament vorausschicken.
Danach folgen im Abschnitt [Repräsentation](sec-representation) verschiedene wichtige Beispiele, die verdeutlichen wie der Computer Information interpretiert und repräsentiert.
Es mag für viele Leser sinnvoll sein mit den Beispielen zu starten, um danach die theoretische Diskussion besser nachvollziehen zu können.

## Der Mensch

Wenn Sie mit einem Bleistift einen Apfel auf ein Blatt Papier zeichnen, was stellt Ihre Zeichnung dar?
Physikalisch betrachtet befindet sich auf dem Blatt eine Menge von kleinen Graphitpartikeln.
Diese sind in einer gewissen Weise angeordnet.

Blicken wir auf das Blatt, erkennen wir jedoch einen Apfel, obwohl sich keinerlei physikalische Bestandteile eines Apfels auf dem Blatt befinden.
Die Zeichnung symbolisiert ([Semantik](def-semantik)) einen Apfel und dessen Qualität (Obst, süß, rund, wächst auf Bäumen) in unserer Vorstellung (kognitiven Welt) und referenziert einen realen Gegenstand oder Sachverhalt aus der Realwelt, in diesem Fall einen konkreten echten Apfel.

Schreiben Sie die Zeichen ``2 + 2 = 4`` auf ein Blatt, so symbolisieren ([Semantik](def-semantik)) diese eine Gleichung.
Gleichzeitig referenziert diese Zeichenfolge einen (bzw. viele) Sachverhalt(e) aus der Realwelt.
Zum Beispiel, referenziert die Zeichenfolge den Sachverhalt, dass wenn man zwei Äpfel hat und weitere zwei erhält, dies dann vier Äpfel sind.

In beiden Fällen gehen wir von einer bestimmten **Interpretation** aus mit der wir einer **Repräsentation** (die Zeichnung und die Zeichen) eine gewisse **Bedeutung** ([Semantik](def-semantik)) zuordnen.
Würden wir keinen Apfel aus der echten Welt kennen oder hätten keinerlei Zahlenverständnis, wäre unsere Interpretation eine andere.

Wir interpretieren fortwährend das was wir wahrnehmen.
Die Zeichenfolge ``23.10.2022`` interpretieren wir als Datum und folgendes Symbol 

```{figure} ../../figs/stop-sign.jpeg
---
width: 200px
name: fig-stop-sign
---
```

interpretieren wir als Anweisung beim Autofahren.

Die Repräsentanten werden in einer ganz bestimmten Art und Weise niedergeschrieben.
Diese Vorschrift bezeichnen wir als [Syntax](def-syntax).
Die [Syntax](def-syntax) des Datums ``23.10.2022`` lautet ``tt.mm.jjjj``, wobei ``tt`` eine Zahl zwischen 1 und 31 sein muss.
Das Stopsymbol gibt es in leicht unterschiedlichen Ausführungen (Größe, Farbe) doch bleiben dessen Charakteristiken sehr ähnlich.

```{exercise} Syntax und Semantik
:label: syntax-and-semantik-exercise
Erklären Sie die Begriffe Syntax und Semantik in Ihren eigenen Worten anhand des Beispiels eines Briefs.
```

Blicken wir nochmals auf die [Semantik](def-semantik).
Die Zeichenkette ``23.10.2022`` symbolisiert einen bestimmten Tag und dessen Qualität (24h, Oktober, eher kühl in Europa, ...).
Zudem referenziert die Zeichenfolge einen realen Gegenstand, den echten ``23. Oktober 2022``.
``23. Oktober 2022`` ist wiederum ein Repräsentant!
Wir können den echten Tag nicht niederschreiben, wir können ihn lediglich referenzieren.

Das Stopsymbol symbolisiert das Stehenbleiben und dessen Qualität (Abbremsen, Autofahren, Straße, Straßenverkehr, ...).
Es referenziert einen Sachverhalt der Realwelt, das Stehenbleiben eines konkreten Fahrzeugs.
Zusätzlich hat es auf uns eine bestimmte Wirkung, nämlich dass wir, wenn wir es sehen, stehenbleiben.

Repräsentanten können mehrere Interpretationen besitzen und ein echter Gegenstand oder Sachverhalt kann mehrere Repräsentanten besitzten.
Zum Beispiel haben folgende Wörter eine doppelte Bedeutung.

+ Flügel (Instrument und Körperteil eines Vogels)
+ Bank (Sitzgelegenheit und Finanzinstitut)
+ Erde (Planet und Material des Bodens)

## Der Computer

Der Computer und seine Bestandteile (Hardware und Software) interpretieren anstelle von Zeichnungen, Folgen von [Bits](def-bit) und [Bytes](def-byte) in einer von uns Menschen vordefinierten Art und Weise.
Im Zusammenhang mit dem Computer sind **Bedeutung** $B$ und **Repräsentation** $R$ Mengen, wohingegen die **Interpretation** $I$ eine Funktion

```{math}
:label: eq:interpretation
I : R \rightarrow B
```

ist.

Ein Beispiel ist die Codierung von Zahlen durch zwei Bits.

+ Bedeutung $B = \left\{ 0, 1, 2, 3 \right\}$
+ Repräsentation $R = \left\{ 00, 01, 10, 11 \right\}$
+ Interpretation $I = \left\{ (00, 0), (01, 1), (10, 2), (11, 3) \right\}$.

Wir werden noch detailliert auf das binäre Zahlensystem eingehen. 
Lassen Sie uns noch ein weiteres Beispiel auflisten.

+ Bedeutung $B = \left\{ \text{'Apfel'}, \text{'Orange'}, \text{'Banane'}, \text{'Traube'} \right\}$
+ Repräsentation $R = \left\{ 00, 01, 10, 11 \right\}$
+ Interpretation $I = \left\{ (00,\text{'Apfel'}), (01, \text{'Orange'}), (10, \text{'Banane'}), (11, \text{'Traube'}) \right\}$.

Mit dieser Interpretation repräsentiert die Bitfolge $00$ die Zeichenkette $I(00) = \text{'Apfel'}$.
Durch die **Interpretation** $I$ erlangt der **Repräsentant** $r \in R$ seine **Bedeutung** ([Semantik](def-semantik)) $I(r) \in B$.

```{admonition} Semantik (Informatik)
:name: def-semantik
:class: definition
Die Bedeutung eines Repräsentanten bezeichnen wir als seine *Semantik*.
```

Diese Bedeutung kann wiederum ein Repräsentant einer anderen Interpretation sein.
So repräsentiert die Zeichenfolge ``Apfel``, welche durch die Bitfolge ``00`` repräsentiert wird, einen Apfel der echten Welt.
Auch kann ein Repräsentant durch verschiedenen Interpretationen unterschiedliche Bedeutungen annehmen.
In den obigen Beispielen repräsentiert die Bitfolge ``00`` einmal die Zeichenkette ``Apfel`` und einmal die Zahl 0. 

```{admonition} Syntax (Informatik)
:name: def-syntax
:class: definition
Die Art und Weise wie ein Repräsentant niedergeschrieben ist nennen wir *Syntax*.
```

Die Computerhardware (alle Bauteile) kann schlussendlich nur [Bits](def-bit) und [Bytes](def-byte) verarbeiten.
Jede Hardwarekomponente verwendet eine bestimmte Interpretation, welche auf der Repräsentation der [Binärzahlen](sec-binary-system) basiert.
Diese Interpretation wurde den Komponenten von uns Menschen 'beigebracht'.

Ein Monitor interpretiert die Bitfolgen als Pixelintensitäten (wie stark und in welcher Farbe leuchtet jeweils der Pixel), ein Addierer interpretiert Bitfolgen als Zahlen, ein Mikrofon interpretiert Bitfolgen als Amplitudenwerte.

Software basiert auf dem gleichen Verständnis, denn Hardware ist Software realisiert durch Bauteile (siehe Abschnitt [Berechenbarkeit](sec-computability)).
Öffnen Sie ein Bild in einem Texteditor, so sehen Sie die Interpretation des Bildes ihres Texteditors.
Öffnen Sie die gleiche Datei in einem Bildverarbeitungsprogramm, sehen sie eine andere Interpretation der Bits und Bytes.

Schreiben Sie einen Buchstaben $\text{'a'}$ durch Tastendruck über ein Textverarbeitungsprogramm, so ist das $\text{'a'}$ ein Element von $B$.
Ihr Textverarbeitungsprogramm berechnet die Bitfolge $b = I^{-1}(\text{'a'})$ durch die ihm bekannte Interpretation $I$ bzw. deren Umkehrfunktion $I^{-1}$.
Die Binärfolge $b$ kann dann auf dem Computer gespeichert werden.
Öffnen Sie die Datei so berechnet das Textverarbeitungsprogramm $I(b) = \text{'a'}$.
Damit Sie den Buchstaben angezeigt bekommen, erhält der Monitor eine Bitfolge, welche dieser als Pixelintensität interpretiert.
Am Ende der Kette sitzen wir vor dem Rechner und interpretieren diese Pixelintensitäten als den eben getippten Buchstaben.

## Interpreter und Compiler

Programmcode ist Text den der Computer als Anweisungen interpretiert.
Wie aber soll das funktionieren, wenn die Hardware doch nur [Bits](def-bit) und [Bytes](def-byte) verarbeiten kann?
Wie im obigen Beispiel des Textverarbeitungsprogramms hindert uns niemand Text zu schreiben, welcher dann in Binärcode durch eine Interpretation umgewandelt wird.
Diese spezielle Interpretation $I$ macht aus dem Text einen Binärcode der ausführbar ist, d.h., den die Computerhardware versteht.
Programme die eine solche Interpretation realisieren bezeichnen wir sehr passend als [Interpreter](def-interpreter) oder [Übersetzer](def-compiler) (engl. Compiler).
Interpreter werten $I$ aus, während der Programmcode ausgeführt wird.
Dahingegen werten Compiler $I$ für den gesamten Code aus, bevor dieser ausgeführt wird.

```{admonition} Übersetzer / Compiler
:name: def-compiler
:class: definition
Ein *Übersetzer*  (engl. *Compiler*) ist ein Programm welches ein anderes Programm $\alpha_H$, geschrieben in einer Hochsprache $L_H$, entgegennimmt und in ein Programm $\alpha_M$, geschrieben in einer Maschinensprache $L_M$, ausgibt. $\alpha_M$ realisiert $\alpha_H$ auf einer konkreten Maschine, d.h., $\alpha_M$ steuert die konkrete Maschine, sodass es das berechnet was $\alpha_H$ auf abstrakterer Ebene vorgibt zu berechnen.
```

Ok, das ist noch nicht die ganze Wahrheit.
In der Praxis wenden Compiler oder Interpreter eine hintereinandergeschaltete eine Kette an Interpretationen $I_0, \ldots, I_n$ an.
Wir als Programmierer möchten zum Beispiel zwei Zahlen addieren und schreiben folgenden ``Python``-Code:

```python
x = 4 + 9
```

``Python`` interpretiert dies als das Speichern der Addition der Zahlen ``4`` und ``9`` in der Variable ``x``.
Das verstehen die Hardwarekomponenten des Computer jedoch nicht.
Der Compiler übersetzt durch die Anwendung einer Kette von Interpretationen diesen Code, sodass er in Assemblercode transformiert wird.
Dieser könnte in etwa folgende Gestalt annehmen:

```
SET 4 #15
SET 9 #14
LOAD #15 $0
LOAD #14 $1
ADD $0 $1 $2
STORE $2 # 16
```

Diese Befehle sprechen direkt bestimmte Hardwarekomponenten an und werden im letzten Schritt in reinen Binärcode übersetzt.
Jeder Compiler erhält als Eingabe einen Programmcode, geschrieben in einer bestimmten Vorschrift ([Syntax](def-syntax)), und wandelt diesen anhand seiner Interpretation in einen anderen Programmcode, einer anderen Vorschrift (Syntax), um.
So wird es möglich, dass sich Entwickler\*innen nicht mehr in einer Welt der Bits und Bytes befinden sondern in einer Welt aus Dezimalzahlen, Zeichenketten, Listen, Webservices, Webseiten, Apps und so weiter.

```{admonition} Interpreter
:name: def-interpreter
:class: definition

Ein *Interpreter* ist ein Programm, welches Befehle, geschriebenen in einer Hochsprache $L_H$ direkt ausführt ohne diese in eine Maschinensprache zu [übersetzen](def-compiler).
Da die Maschine, die Sprache $L_H$ jedoch nicht versteht, **simuliert** der Interpreter die Befehle (siehe [universellen Turingmaschine](sec-utm)).

```

Übertragen wir dies auf das Beispiel mit dem gezeichneten Apfel, so interpretiert der Bleistift den Druck und den Winkel als Anzahl und Positionierung von Graphitteilchen.
Wir als Zeichner\*innen verlassen die Welt der Graphitteilchen und begeben uns stattdessen in die Welt der Zeichentechniken.
Dieser Kontextwechsel wird durch den [Interpreter](def-interpreter) -- den Bleistift -- ermöglicht!

Ein [Übersetzer / Compiler](def-compiler) wandelt hingegen ein gesamtes Kunstwerk in einem Stück in ein anderes Werk um.
Zum Beispiel eine Folge von Bildern in ein Video.
Der Vorteil dabei ist, dass der Übersetzer Optimierungen durchführen kann, da ihm das gesamte zu übersetzende Werk zur Verfügung steht.
Dafür ist er für die Anwender\*innen weniger flexibel, denn diese müssen ihm immer ein gesamtes Werk übergeben.

```{exercise} Übersetzer und Interpreter
:label: interpreter-compiler-examples-exercise
Beschreiben Sie informell $R$, $B$ und $I$ für die Tastatur, ein Klavier und einen Sprachübersetzer.
```

## Der interpretierende Computer?

Unsere hier präsentierten Definitionen für [Semantik](def-semantik) und [Syntax](def-syntax) stammen aus der Informatik und stimmen nicht notwendigerweise mit den Definitionen aus anderen Bereichen der Wissenschaft überein.
Auch müssen wir uns fragen ob sich der Interpreter in Form des Bleistifts, den wir als Werkzeug verwenden, und in Form des Menschen, der den Apfel erkennt, nicht fundamental unterscheiden.
Der Stift ist lediglich ein verlängerter Arm des Zeichners.
Er denkt nicht, hat keinerlei Intelligenz oder Bewusstsein.
Der Mensch hingegen, der die Graphitteilchen als Apfel interpretiert, ist ein denkendes Wesen mit Bewusstsein.
Wir haben auch behauptet, dass Computer ihre Interpretationen von uns Menschen diktiert bekommen.

Es ergeben sich hierbei spannende Fragen aus dem Bereich der künstlichen Intelligenz und Philosophie:

>Ist der Computer im wesentlichen ein 'besserer' Bleistift ohne Intelligenz und Bewusstsein?

>Kann sich ein Computer eigene Interpretationen seiner digitalen Welt erschließen?

Natürlich könnten wir die Frage auch umkehren und uns dem Menschen zuwenden:

>Ist der Mensch im wesentlichen ein 'besserer' Bleistift?

Bisher besteht Zweifel daran, dass Computer jemals eine eigene Interpretation hervorbringen.
Streng genommen ist es diskussionswürdig, ob Computer überhaupt irgendeine Bedeutung ([Semantik](def-semantik)) 'kennen'.
Anders ausgedrückt müssen wir uns fragen ob sie nicht doch nur bloße Transformatoren von Zeichen auf einer rein [syntaktischen](def-syntax) Ebene sind -- ganz so wie der Bleistift.
Und wenn dem so ist, was muss getan werden um dies zu ändern?

Im Kapitel [Was ist Information](sec-information) schließen wir an diese Diskussion an, indem wir den Informationsbegriff aus verschiedenen Richtungen kritisch betrachten.