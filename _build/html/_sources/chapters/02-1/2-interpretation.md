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

(sec-interpretation)=
# Interpretation

In diesem Abschnitt unternehmen wir einen Versuch die Begriffe **Interpretation**, **Repräsentation**, **Bedeutung**, **Semantik** und **Syntax** zu erklären.
Dadurch möchten wir ein theoretisches Fundament vorausschicken.
Danach folgen im Abschnitt [Repräsentation](sec-representation) verschiedene wichtige Beispiele, die verdeutlichen wie der Computer Information interpretiert und repräsentiert.
Es mag für viele Leser\*innen sinnvoll sein mit den Beispielen zu starten, um danach die theoretische Diskussion besser nachvollziehen zu können.

(sec-semiotik)=
## Semiotik

Wenn Sie mit einem Bleistift einen Apfel auf ein Blatt Papier zeichnen, was stellt Ihre Zeichnung dar?
Physikalisch betrachtet befindet sich auf dem Blatt eine Menge von kleinen Graphitpartikeln.
Diese sind in einer gewissen Weise angeordnet.
Blicken wir auf das Blatt, erkennen wir jedoch einen Apfel, obwohl sich keinerlei physikalische Bestandteile eines Apfels auf dem Blatt befinden.
Die Zeichnung symbolisiert einen Apfel und dessen Qualität (Obst, süß, rund, wächst auf Bäumen) in unserer Vorstellung (kognitiven Welt) und referenziert einen realen Gegenstand oder Sachverhalt aus der Realwelt, in diesem Fall einen konkreten echten Apfel.
Wir sagen auch, dass die Bedeutung der Zeichnung ein Apfel ist.

Schreiben Sie die Zeichen ``2 + 2 = 4`` auf ein Blatt, so symbolisieren diese Zeichen eine Gleichung.
Gleichzeitig referenziert diese Zeichenfolge einen bzw. viele Sachverhalt(e) aus der Realwelt.
Zum Beispiel, referenziert die Zeichenfolge den Sachverhalt, dass wenn man zwei Äpfel hat und weitere zwei erhält, dies dann vier Äpfel sind.
Dabei bedienen wir uns der **Abstraktion** um überhaupt jene vier Objekte als gleich anzunehmen.
Erneut erlangen die Zeichen (durch uns) eine Bedeutung.

```{admonition} Abstraktion
:name: remark-abstraction
:class: remark
Das Unterschiedliche wird durch Abstraktion ununterscheidbar. 
```

Die Zeichenfolge ``23.10.2022`` interpretieren wir normalerweise als Datum und folgendes Symbol 

```{figure} ../../figs/digital-computer/interpretation/stop-sign.jpeg
---
width: 200px
name: fig-stop-sign
---
```

interpretieren wir als Anweisung beim Autofahren.

In all diesen Fällen gehen wir von einer bestimmten **Interpretation** aus mit der wir einer **Repräsentation** (die Zeichnung und die Zeichen) eine gewisse **Bedeutung** zuordnen.
Die Graphitpartikeln (Repräsentant) interpretieren wir als Apfel (Bedeutung).
Die Zeichenfolge ``2 + 2 = 4`` (Repräsentant) interpretieren wir als mathematisch Gleichung (Bedeutung).
Die Zeichenfolge ``23.10.2022`` interpretieren wir als Datum (Bedeutung) und das Stop-Symbol als Anweisung beim Autofahren.
Dies setzt vorraus, das wir Äpfel, Tage, Gleichungen und den Straßenverkehr kennen.

Die wissenschaftliche Disziplin, welche den Zusammenhang zwischen Repräsentant und seiner Bedeutung untersucht ist die sog. Bedeutungslehre oder auch [Semantik](def-semantik-semiotik).
Sie ist ein Gebiet der Semiotik (Zeichentheorie).
Die Zeichenkette ``23.10.2022`` symbolisiert einen bestimmten Tag und dessen Qualität (24h, Oktober, eher kühl in Europa, ...).
Zudem referenziert die Zeichenfolge einen realen Gegenstand: Den echten 23. Oktober 2022. "23. Oktober 2022" ist wiederum ein Repräsentant!
Wir können den echten Tag nicht niederschreiben, wir können ihn lediglich referenzieren.
Das erschwert unsere Erklärversuche, da wir uns mit Zeichen ausdrücken müssen.

Das Stop-Symbol symbolisiert das Stehenbleiben und dessen Qualität (Abbremsen, Autofahren, Straße, Straßenverkehr, ...).
Es referenziert einen Sachverhalt der Realwelt: Das Stehenbleiben eines konkreten Fahrzeugs.
Zusätzlich hat es auf uns eine bestimmte Wirkung, nämlich dass wir, wenn wir es sehen, stehenbleiben (oder zumindest darüber reflektieren).
Diese Wirkung wird im letzten Gebiet der Semiotik, der sog. *Pragmatik* untersucht.

```{admonition} Semantik (Semiotik)
:name: def-semantik-semiotik
:class: definition
Die *Semantik* (auch Bedeutungslehre) ist eine wissenschaftliches Teilgebiet der Semiotik (auch Zeichentheorie), welche den Zusammenhang zwischen Repräsentant und seiner Bedeutung untersucht.
```

Um die Zeichenfolge oder Symoble als etwas bestimmtes zu erkennen, müssen diese in einer ganz bestimmten Art und Weise niedergeschrieben werden---sie müssen eine gewisse Struktur aufweisen.
Diese Vorschrift oder das Regelsystem zur Kombination elementarer Zeichen zu zusammengesetzten Zeichen in Zeichensystemen nennt man [Syntax](def-syntax).
Die Syntax ist ebenfalls eine der drei Disziplinen der Semiotik.

Die [Syntax](def-syntax-semiotik) des Datums ``23.10.2022`` lautet ``tt.mm.jjjj``, wobei ``tt`` eine Zahl zwischen 1 und 31 sein muss, ``mm`` eine Zahl zwischen 01 und 12, und ``jjjj`` eine vierstellige natürliche Zahl sein muss.
Das Stop-Symbol gibt es in leicht unterschiedlichen Ausführungen (Größe, Farbe) doch bleiben dessen Charakteristiken sehr ähnlich.

```{admonition} Syntax (Semiotik)
:name: def-syntax-semiotik
:class: definition
Unter *Syntax* versteht man allgemein ein Regelsystem zur Kombination elementarer Zeichen zu zusammengesetzten Zeichen in natürlichen oder künstlichen Zeichensystemen.
Die Zusammenfügungsregeln der Syntax stehen hierbei den Interpretationsregeln der [Semantik](def-semantik-semiotik) gegenüber.
```

Repräsentanten können mehrere Interpretationen besitzen.
Ein echter Gegenstand oder Sachverhalt kann auch mehrere Repräsentanten haben.
Zum Beispiel haben folgende Wörter eine doppelte Bedeutung.

+ Flügel (Instrument und Körperteil eines Vogels)
+ Bank (Sitzgelegenheit und Finanzinstitut)
+ Erde (Planet und Material des Bodens)

```{exercise} Syntax und Semantik
:label: syntax-and-semantik-exercise
Erklären Sie die Begriffe Syntax und Semantik in Ihren eigenen Worten anhand des Beispiels eines Briefs.
```

(sec-formal-semiotic)=
## Formale Syntax & Semantik

In der Informatik tritt anstelle der allgemeinen [Semantik](def-semantik-semiotik) die sog. *logische*, *formaler* oder auch *reine* Semantik.
In Abgrenzung zur Semantik im allgemeinen Sinn arbeitet die [(formale) Semantik](def-semantik) in der Informatik mit rein formalen, logisch-mathematischen Methoden.
Damit is gemeint, dass die Bedeutungen nicht länger (gesellschaftlich) untersucht, sondern durch explizite Regeln **unmissverständlich** festgelegt werden.
Die (formale) Semantik beschäftigt sich somit mit der exakten Bedeutung von Termen in (formalen) Sprachen, wie beispielweise Programmiersprachen.

```{admonition} Semantik (Informatik)
:name: def-semantik
:class: definition
Als *Semantik* bezeichnet man ein Teilgebiet der (theoretischen) Informatik, in dem die Bedeutung von Computerprogrammen und Spezifikationen formalisiert wird, um beispielweise den Nachweis der Korrektheit von Computerprogrammen zu erbringen (Verifikation).
Die *Semantik eines Computerprogramms* legt dessen Bedeutung fest.
```

Die formale Semantik hat zum Ziel, die Bedeutung von Computerprogrammen in einer formalen Sprache auszudrücken, sodass über das Anwenden von Ableitungsregeln Aussagen über das Programm gemacht werden können.
In der Informatik möchten wir formal beweisen, dass ein Programm dies oder jenes berechnet.
Dazu brauchen wir einen formalen Rahmen---einen sicheren Hafen.

Das Gegenstück zur (formalen) Semantik ist die [(formale) Syntax](def-syntax).
Bei ihr geht es rein um die Wohlgeformtheit von Zeichenfolgen.
Streng genommen wird die inhaltliche Bedeutung nicht betrachtet.

```{admonition} Syntax (Informatik)
:name: def-syntax
:class: definition
Unter der *(formalen) Syntax* versteht man ein System von Regeln, nach denen wohlgeformte, d.h. *syntaktisch* korrekte, Ausdrücke, Formeln, Programmiertexte oder andere Texte aus einem grundlegenden Zeichenvorrat (dem Alphabet) gebildet werden.
Die *Syntax* definiert auch *syntaktische Ableitungsregeln*, durch die **bedeutungslose** Zeichen in andere **bedeutungslose** Zeichen transformiert werden.
```

Wohldefinierte Programmiersprachen benötigen beides: Eine (formale) Syntax auf der dann eine Semantik definiert wird.
Dabei ist die Semantik meist anhand derselben Operationen, durch die auch die Syntax definiert ist, bestimmt.
Deshalb ergibt sich die Bedeutung eines komplexen Ausdrucks aus der Bedeutung seiner Bestandteile und den syntaktischen Operationen für die Zusammensetzung.
Diese Brücke vereinfacht den Umgang mit Programmiersprachen verschleiert aber auch den Unterschied zwischen [Syntax](def-syntax) und [Semantik](def-semantik).

```{admonition} Syntaktischen Ableitungsregeln
:class: attention
:name: attention-syntax-rules
Die syntaktischen Ableitungsregeln haben nichts mit der mathematischen Ableitung von Funktionen zu tun!
```

Betrachten wir folgendes kurzes, *syntaktisch korrektes* ``Python``-Programm:

```python
3 + 5 * 10
```

```{code-cell} python3
---
tags: 
    - remove-input
---
quiz=[{
    "question": "Wie lautet das Ergebnis?",
    "type": "numeric",
    "precision": 2,
    "answers": [
        {
            "type": "value",
            "value": 53,
            "correct": True,
            "feedback": "Richtig."
        }
    ]
}]

from jupyterquiz import display_quiz
display_quiz(quiz, border_radius=2, lang='de')
```

Vermutlich werden Sie die richtige Antwort sofort gefunden haben.

Interessanterweise kann nach den *syntaktischen Ableitungsregeln* der Ausdruck ``3 + 5 * 10`` nur als Summe, nicht aber als Produkt gelesen werden.
Dies möchten wir im Folgenden kurz näher erleutern.
Die folgenden *syntaktischen Ableitungsregeln* sind ein Ausschnitt für die Programmiersprache ``Python``:

```
E -> T '+' E 
   | T

T -> F '*' T
   | F

F -> '(' E ')'
   | Z

Z -> '0' | '1' | '2' ... 
``` 

Wir können also z.B. ``E`` zu ``T + E`` ableiten.
``E`` steht---durch die Semantik---für einen Ausdruck, ``T`` für einen Term, ``F`` für einen Faktor und ``Z`` für eine Zahl.
Ein Ausdruck wie er in unserem obigen Programm steht, also ``3 + 5 * 10`` kann nach diesen Relgen nur ein Term oder eine (syntaktische) Addition aus Term und Ausdruck sein.
Unser Beispiel entsteht wie folgt:

```
E -> T '+' E -> F '+' E -> Z '+' E -> '3' '+' T -> '3' '+' T 
  -> '3' '+' F '*' T -> '3' '+' Z '*' T -> '3' + '5' '*' T 
  -> '3' '+' '5' '*' F -> '3' + '5' '*' Z -> '3' '+' '5' '*' '10'
```

Diese Ableitung hat nichts mit einer arithmethschen Berechnung zu tun.
Sie ist die stupide Umwandlung von Zeichen in andere Zeichen anhand der oben aufgelisteten Regeln, welche wir auch als *Grammatik* bezeichnen.
Dennoch legen diese Regeln fest, dass ein ``E`` zu einem ``Z * Z`` umgewandelt werden kann, aber ein ``F`` nicht zu einem ``Z + Z`` sondern nur in ein ``'(' Z + Z ')'``.
Dadurch unterstützt die Syntax die *semantische Auswertung*, denn sobald bei dieser Auswertung ein ``F`` auftaucht, kann ``F`` getrennt vom rest ausgewertet werden.
In unserem Beispiel bedeutet dies, dass nach den Ableitungen

```
E -> T + E -> F + E
```

klar ist, dass ``E`` *semenatisch* zu ``5 * 10`` und damit zu ``50`` ausgewertet werden kann und ``T`` zu ``3`` ausgewertet werden kann.
In anderen Worten: Die *semantische* Punkt-vor-Strich-Regel ist bereits durch *syntaktische Ableitungsregeln* strukturell vorgegeben.

Zusammenfassend gibt die Syntax vor, welcher Text ein gültiger Programmiercode ist und die Semantik gibt vor welche Operationen---realisiert durch digitale Schaltungen---der Computer aufgrund des Texts ausführt.

Folgender Text ist kein gültiger ``Python``-Programmiercode, da er *syntaktisch* inkorrekt ist.

```{code-cell} python3
---
tags: [raises-exception]
---
3 + 5 *
```

Die Fehlermeldung weist uns darauf hin.

Folgender Text ist ein gültiger ``Python``-Programmiercode.
Dies bedeutet allerdings nicht, dass es keine *semantischen* Fehler gibt.
Hier teilen wir durch 0, was *semantisch* undefiniert ist.

```{code-cell} python3
---
tags: [raises-exception]
---
3 / 0
```

## Formale Interpretation

Da die Bedeutung durch die formale Semantik durch explizite Regeln **unmissverständlich** festgelegt ist, können wir **Bedeutung**, **Repräsentation** und **Interpretation** formal definieren.
Der Computer und seine Bestandteile (Hard- und Software) "interpretieren" anstelle von Zeichnungen, Folgen von [Bits](def-bit) und [Bytes](def-byte) in einer von uns Menschen vordefinierten Art und Weise.
Wir sollten dieses *formale interpretieren* von dem Begriff des *semiotischen Interpretierens* unterscheiden.
In der Informatik sind **Bedeutung** $B$ und **Repräsentation** $R$ Mengen, wohingegen die **Interpretation** $I$ eine Funktion ist.

````{admonition} Interpretation
:class: definition
:name: def-interpretation
Eine *Interpretation* $I$ ist eine Funktion 

\begin{equation*}
I : R \rightarrow B
\end{equation*}

welche jedem Repräsentanten $r \in R$ seine Bedeutung $I(r) \in B$ zuweist.

````

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
Durch die **Interpretation** $I$ erlangt der **Repräsentant** $r \in R$ seine **Bedeutung** $I(r) \in B$.

Diese Bedeutung kann wiederum ein Repräsentant einer anderen Interpretation sein.
Die auf dem Bildschirm angezeigte Zeichenfolge "Apfel" wird als Zeichenkette ``Apfel`` repräsentiert welche widerum durch die Bitfolge ``00`` repräsentiert wird.
Auch kann ein Repräsentant durch verschiedenen Interpretationen unterschiedliche Bedeutungen annehmen.
In den obigen Beispielen repräsentiert die Bitfolge ``00`` einmal die Zeichenkette ``Apfel`` und einmal die Zahl 0. 

Die Computerhardware kann schlussendlich nur [Bits](def-bit) und [Bytes](def-byte) verarbeiten.
Jede Hardwarekomponente verwendet eine bestimmte Interpretation, welche auf der Repräsentation der [Binärzahlen](sec-binary-system) basiert.
Diese Interpretation wurde den Komponenten von uns Menschen "beigebracht" indem wir festgelegt haben welche Bitfolgen welche Berechnungen auslösen.
In anderen Worten, auf welche Art und Weise Informationen verarbeitet werden.
Ein Monitor interpretiert die Bitfolgen als Pixelintensitäten (wie stark und in welcher Farbe leuchtet der jeweilige Pixel), ein Addierer interpretiert Bitfolgen als Zahlen, ein Mikrofon interpretiert Bitfolgen als Amplitudenwerte.

Die Operationen des Computer können die abstrakte Informationswelt nicht verlassen.
Informationssysteme sind *operational abgeschlossen*.
Sie können Computer untereinander vernetzen aber noch ist es nicht möglich Gedanken in diese Systeme einzuspeisen.
Sie werden auch keinen echten Apfel im Computer finden.
Was aber nicht bedeutet, dass ein Computer einen Apfel nicht erkennen kann.
Auch unsere mentalen Operationen scheinen in sich abgeschlossen---sie werden auch keinen echten Apfel in ihrem Kopf finden und Ihre Gedanken bleiben in Ihrem Kopf.

Software basiert auf dem gleichen Prinzip, denn im Grunde genommen ist Hardware ein Stück Software, welches durch Bauteile realisiert wird (siehe Abschnitt [Berechenbarkeit](sec-computability)).
Es ist z.B. nicht unüblich für Berechnungen, die durch Computerprogramme, d.h. Software, durchgeführt wird, neue Bauteile zu konstruieren, die jene Berechnung schneller vollziehen.
Öffnen Sie ein Bild in einem Texteditor, so sehen Sie die Interpretation des Bildes ihres Texteditors.
Öffnen Sie die gleiche Datei in einem Bildverarbeitungsprogramm, sehen sie eine andere Interpretation der Bits und Bytes.

Schreiben Sie einen Buchstaben $\text{'a'}$ durch einen Tastendruck in einem Textverarbeitungsprogramm, so ist das $\text{'a'}$ ein Element der Bedeutung $B$.
Ihr Textverarbeitungsprogramm berechnet die Bitfolge $b = I^{-1}(\text{'a'})$, durch die ihm bekannte Interpretation $I$ bzw. deren Umkehrfunktion $I^{-1}$.
Die Binärfolge $b$ kann dann auf dem Computer gespeichert werden.
Öffnen Sie die Datei, so berechnet das Textverarbeitungsprogramm $I(b) = \text{'a'}$.
Damit Sie den Buchstaben angezeigt bekommen, erhält der Monitor eine Bitfolge, welche dieser als Pixelintensität interpretiert.
Am Ende der Kette sitzen wir vor dem Rechner und interpretieren diese Pixelintensitäten als den eben getippten Buchstaben.

## Interpreter und Compiler

Wie bereits erwähnt ist Programmcode Text den der Computer als Anweisungen interpretiert.
Dabei realisiert er die [Semantik](def-semantik) des Programmiercodes, der hoffentlich [syntaktisch](def-syntax) korrekt ist.
Wie aber soll das funktionieren, wenn die Hardware nur [Bits](def-bit) und [Bytes](def-byte) verarbeiten kann?

Wie im obigen Beispiel des Textverarbeitungsprogramms, hindert uns niemand Text zu schreiben welcher dann in Binärcode durch eine [Interpretation](def-interpretation) umgewandelt wird.
Diese spezielle Interpretation $I$ macht aus dem Text einen Binärcode der ausführbar ist, d.h., den die Computerhardware "versteht".
Damit ist nicht gemeint, dass der Text zuvor als tatsächlicher Text im Speicher des Computers liegt.
Der Text ist bereits binär codiert, wird aber in eine andere Binärfolge umgewandelt welche nicht mehr lesbaren Programmiercode repräsentiert, sondern Binärcode der durch den Computer direkt ausgeführt werden kann.
Dieser Code hängt zum Beispiel von der Art der Hardware des Computers ab.
Das heißt, obwohl der ``Python``-Programmiercode auf zwei Maschinen identisch ist, können sich die Anweisungen, die von den Bauteilen tatsächlich ausgeführt werden, unterscheiden.
Handelt es sich um ein syntaktisch korrektes Programm, welches keinen undefinierten Code enthält, sollte jedoch die [Semantik](def-semantik) im Gesamten identisch sein.
In anderen Worten, das Endergebnis sollte auf beiden Maschinen gleich sein.

Programme die eine solche [Interpretation](def-interpretation) realisieren, also lesbaren Programmcode als ausführbaren *Maschinencode* interpretieren, bezeichnen wir sehr passend als [Interpreter](def-interpreter) oder [Übersetzer](def-compiler) (engl. Compiler).
Interpreter werten $I$ aus, während der Programmcode ausgeführt wird, d.h. sie interpretieren Programmcodefetzen.
Dagegen werten Übersetzer die Interpretation $I(w)$ für den gesamten Code $w$ aus, bevor dieser ausgeführt wird.

```{admonition} Übersetzer / Compiler
:name: def-compiler
:class: definition
Ein *Übersetzer*  (engl. *Compiler*) ist ein Programm welches ein anderes Programm $\alpha_H$, geschrieben in einer Hochsprache $L_H$, entgegennimmt und in ein Programm $\alpha_M$, geschrieben in einer Maschinensprache $L_M$, ausgibt. $\alpha_M$ realisiert $\alpha_H$ auf einer konkreten Maschine, d. h., $\alpha_M$ steuert die konkrete Maschine, sodass es das berechnet was $\alpha_H$ auf abstrakterer Ebene vorgibt zu berechnen.
```

Übertragen wir dieses Prinzip des [Interpreters](def-interpreter) auf das Beispiel mit dem gezeichneten Apfel, so interpretiert der Bleistift den Druck und den Winkel als Anzahl und Positionierung von Graphitteilchen.
Wir als Zeichner\*innen verlassen die Welt der Graphitteilchen und begeben uns stattdessen in die Welt der Zeichentechniken.
Dieser Kontextwechsel wird durch den [Interpreter](def-interpreter)---den Bleistift---ermöglicht!

```{admonition} Interpreter
:name: def-interpreter
:class: definition

Ein *Interpreter* ist ein Programm, welches Befehle, geschriebenen in einer Hochsprache $L_H$ **direkt** ausführt, indem es die Befehle zur Laufzeit in Maschinencode übersetzt oder durch eine andere Form der Sofortausführung umsetzt.
```

Ein [Übersetzer](def-compiler) wandelt hingegen ein gesamtes Kunstwerk in einem Stück in ein anderes Werk um.
Zum Beispiel eine Folge von Bildern in ein Video.
Der Vorteil dabei ist, dass der Übersetzer Optimierungen durchführen kann, da ihm das gesamte zu übersetzende Werk zur Verfügung steht.
Dafür ist er für die Anwender\*innen weniger flexibel, denn diese müssen ihm immer ein gesamtes Werk übergeben.

Ok, das ist noch nicht die ganze Wahrheit.
In der Praxis wenden Compiler oder Interpreter eine hintereinandergeschaltete Kette an Interpretationen $I_0, \ldots, I_n$ an.
Wir als Programmierer\*innen möchten zum Beispiel zwei Zahlen addieren und schreiben folgenden ``Python``-Code:

```python
x = 4 + 9
```

``Python`` interpretiert dies als das Speichern der Addition der Zahlen ``4`` und ``9`` in der Variable ``x``.
Das verstehen die Hardwarekomponenten des Computer jedoch nicht.
Der Interpreter übersetzt durch die Anwendung einer Kette von Interpretationen diesen Code, sodass er in *Assemblercode* transformiert wird.
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
Jeder Compiler erhält als Eingabe einen Programmcode, geschrieben in einer bestimmten Vorschrift ([Syntax](def-syntax)) und wandelt diesen anhand seiner [Interpretation](def-interpretation) in einen anderen Programmcode einer anderen Vorschrift ([Syntax](def-syntax)), um.
So wird es möglich, dass sich Entwickler\*innen nicht mehr in einer Welt der Bits und Bytes befinden sondern in einer Welt aus Dezimalzahlen, Zeichenketten, Listen, Webservices, Webseiten, Apps und so weiter.
Die [Semantik](def-semantik) der unterschiedlichen Programmcodes sollte (im Gesamten) unverändert bleiben.

```{admonition} Undefiniertes Verhalten
:name: remark-undefined-behavor
:class: remark

Enthält ein Programm semantische Fehler welche zu einem undefiniertes Ergebnis führen kann es---zum Beispiel durch die Optimierung des Codes die vom Übersetzer vorgenommen wird---vorkommen, dass sich die Semantik von einer Interpretation zur anderen verändert.
```

```{exercise} Übersetzer und Interpreter
:label: interpreter-compiler-examples-exercise
Beschreiben Sie informell $R$, $B$ und $I$ für die Tastatur, ein Klavier und einen Sprachübersetzer.
```

## Rechnen und Denken

Es stellt sich die Frage worin der Unterchied zwischen der *semiotischen* und der *formalen* Welt liegt.
In anderen Worten: Worin liegt der Unterschied zwischen der formalen Interpretation eines Bildschirms einer Bitfolge in Pixelwerte und unserer semiotischen Interpretation mit der wir diese Pixelwerte als Apfel interpretieren.
Genau an dieser Stelle kommt es zu einer merkwürdigen Überschreitung des operational geschlossenen Systems der symbolischen Manipulationen und des anderen operational geschlossenen Systems der Gedanken oder mentalen Operationen.
Die beiden Systeme scheinen miteinander zu kommunizieren.

Nochmals sei gesagt, dass die Systeme *operational geschlossen* sind, denn weder bohren sich die Symbole in unseren Kopf noch wandern Gedanken in den Computer.
Im Beispiel moderner ChatBots, die auf großen *Sprachmodelle* basieren, erfolgt diese Mensch-Maschinen-Kommunikation durch das gemeinsame Medium der Sprache.
Und im Fall des Bildes eines Apfels auf dem Bildschirm erfolgt die Kommunikation über das Medium der visuellen Darstellung.
Was aber---um es erneut zu betonen---nicht bedeutet, dass Mensch und Maschine Spache oder visuelle Darstellugn auf die gleiche Weise "verstehen".
Vielmehr operieren beide Systeme komplett unterschiedlich---das eine rechnet, das andere denkt.

Die Semantik eines Programms bestimmt welche digitalen Operationen der Computer ausführt.
Mehr dazu in Abschnitt [Manipulation](sec-manipulation).
Was stellen diese Operationen dar?
Wenn wir auf einem Blatt Papier die Rechnung ``3 + 5 * 10`` ausführen und eine ``53`` auf das Blatt schreiben, können wir behaupten, dass der Computer einen analogen Effekt für die Außenwelt erzielt.
Er ist im Stande diese ``53`` in seinen Speicher zu schreiben indem er z.B. das ``Python``-Programm

```{code-cell} python3
3 + 5 * 10
```

ausführt.
Er ist also im Stande die gleiche [symbolische Manipulation](sec-manipulation) durchzuführen.
Aber auch wenn wir in Bezug auf die formale Semantik von einer Bedeutung sprechen, ist damit nicht gemeint, dass der Computer wirklich "versteht" was eine ``53`` wirklich ist.
Es geht lediglich um die Bedeutung in Form von Anweisungen, die der Computer ausführt, um die symbolische Manipulation zu realisieren---d.h. um das zu tun was wir auf dem Papier vollbracht haben.
Doch anders als wir, denkt der Computer nicht---er manipuliert Symbole, d.h. er rechnet.

Wir Menschen besitzen eine Erfahrung und können beispielsweise zu einer abstrakten Zahl, also einem Symbol, eine tatsächliche Erfahrung referenzieren.
Der Apfel als Bild auf dem Bildschirm hat für uns eine "tatsächliche" Bedeutung.
Und es mag so sein, dass gerade aus der Erfahrung heraus eben jene abstrakten Konzepte, wie etwa Zahlen, entstanden sind. 

Wir sollten uns fragen ob sich die Interpreter einmal in Form des Bleistifts, den wir als Werkzeug verwenden, und in Form des Menschen, der den Apfel erkennt, nicht fundamental unterscheiden.
Der Stift ist lediglich ein verlängerter Arm der Künstler\*innen.
Er denkt nicht, hat keinerlei Intelligenz oder Bewusstsein.
Der Mensch hingegen, der die Graphitteilchen als Apfel interpretiert, ist ein bewusstes, denkendes, historisches, biologisches Wesen.

Andererseits haben formale Interpretationen offensichtlich Auswirkungen auf die echte Welt.
Wenn Algorithmen die Kreditwürdigkeit eines Kunden berechnen und aufgrund dessen---womöglich ohne eines Eingriffs einer menschlichen Instanz---ein Kredit abgelehnt wird, haben symbolisch rechnende Systeme natürlich Effekte auf andere Systeme die Denken oder anderweitig kommunizieren.

Es ergeben sich also spannende Fragen aus dem Bereich der *künstlichen Intelligenz* und der *Philosophie des Geistes*:

>Ist der Computer im wesentlichen ein "besserer" Bleistift ohne Intelligenz und Bewusstsein?

>Kann sich ein Computer eigene Interpretationen seiner digitalen Welt erschließen?

Natürlich könnten wir die Frage auch umkehren und uns dem Menschen zuwenden:

>Ist der Mensch im wesentlichen ein "besserer" Bleistift?

Die Euphorie in den Anfängen der künstlichen Intelligenz war groß.
So schrieb Alan Turing einer der Begründer der Informatik in *Computing Machinery and Intelligence*:

>I believe that at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted. -- {cite}`turing:1950`

Diese Vorhersage hat sich wohl nicht erfüllt auch wenn die These der denkenden Maschine durch die Fortschritte des maschinellen Lernens neu entflammt ist.
Es bestehen berechtigte Zweifel daran, dass Computer jemals eine eigene Interpretation oder eine eigene Intension hervorbringen bzw. entwickeln.
Streng genommen ist es diskussionswürdig, ob Computer überhaupt irgendeine echte Bedeutung ([semiotische Semantik](def-semantik-semiotik)) "kennen".
Sind sie nicht doch nur bloße Transformatoren von Zeichen auf einer rein [syntaktischen](def-syntax) Ebene ganz so wie der Bleistift?
Und wenn dem so ist, können wir und sollten wir versuchen dies zu ändern?

Gegen diese utopisch oder dystopische Hoffnung der Futuristen argumentieren z.B. die Philosophen {cite:t}`gabriel:2018` und {cite:t}`rosengruen:2021`.
Gabriel warnt unter anderem vor einem fehlgeleiteten Sprachgebrauch.

>Ob es überhaupt eine künstliche Intelligenz gibt, kann man nicht dadurch entscheiden, dass man sich schlichtweg dazu entschließt, von nun an so zu reden.
>Indem man bestimmte Vorgänge der Datenspeicherung und -verarbeitung, die mit der Digitalisierung einhergehen, metaphorisch in Analogie zu lebendigen Vollzügen beschreibt, erzeugt man damit noch lange keinen Terminator.
>Allenfalls sind die heute verfügbaren K.I.-Systeme eine Art Golem, das heißt ein dummes stumpfes Stück Materie, das Informationen verarbeitet, ohne dabei die geringste Spur des Bewusstseins aufzuweisen.
>Eine Spezies, die nicht über Jahrmillionen Evolution natürlich entstanden ist, ist nicht dazu geeignet, ein geistiges Innenleben zu führen.
>Es fehlen die notwendigen biologischen Vorraussetzungen. -- {cite}`gabriel:2018` s. 205-206

Die Diskussionen bleiben spannend und offfen.
Sie betreffen nicht nur den Bereich der künstlichen Intelligenz, sondern vielmehr unser Menschenbild.
Im Kapitel [Was ist Information?](sec-information) schließen wir an diese Diskussion an, indem wir den Informationsbegriff aus verschiedenen Richtungen kritisch betrachten.
