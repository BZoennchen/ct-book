# Datentypen (Grundlagen)

Wie in Abschnitt [Repräsentation](sec-representation) beschrieben, befinden sich im Speicher des (digitalen) Computers ausschließlich [Bits](def-bit).
Sie können sich den Speicher als eine lange lange Liste von Bits vorstellen.
Diese können nur einen von zwei Zuständen (0 und 1) annehmen.
Dennoch verarbeiten Computer Zahlen, Text, Bilder und mehr.

Die 'Magie' dahinter geschieht durch die Wahl und Implementierung einer [Interpretation](sec-interpretation).
Unterschiedliche Interpretationen ermöglichen es, Bits und [Byte](def-byte) als Zahlen, Text, Bilder usw. zu verarbeiten.

Im Abschnitt [Variablen](sec-variables) haben wir von einer *Variable* als Tupel von **Wert** und **Speicheradresse** gesprochen.
Die *Variable* 'kennt' die Speicheradresse an der der Wert im Speicher steht.
Soweit so gut, woher aber weiß der Interpreter ob es sich bei der Folge von Bits um eine Zahl oder um etwas anderes handelt?

Weisen wir der Variablen ``char`` den Wert ``'a'`` zu

char = 'a'
char

so wird im Speicher irgendwo der **Wert** als binärer ASCII-Code stehen:

$$01100001_2$$

Würde man diese Bitfolge als ganze Zahl interpretieren wäre dies gleich

$$2^0 + 2^5 + 2^6 = 97_{10}$$

Warum gibt uns der Interpreter aber ``'a'`` und nicht ``97`` aus?
Und weshalb kommt es bei folgender Addition

x = 3
char = 'a'
x + char

zu einem Fehler?
Die kurze Antwort lautet: Wegen der Datentypen der Variablen ``x`` bzw. ``char``.

print(f'type of x: {type(x)}')
print(f'type of char: {type(char)}')

Der Datentyp der Variablen ``char`` ist ``str`` (Zeichenkette).
Diese Information bekommt der Interpreter und interpretiert deshalb die Bitfolge im Speicher als Zeichenkette.
Und die ``+``-Operation ist für Kombination von Datentypen ``int`` und ``str`` nicht definiert.
Das ist allerdings eine unbefriedigende Antwort, denn wir wissen noch nicht wie Datentypen realisiert werden.
Wie ist der Zusammenhang zwischen den Programmiersprachen, welche alle auf Datentypen basieren, und den [Übersetzern](def-compiler) oder [Interpretern](def-interpreter) und der Computerhardware?

In diesem Kapitel und nächstem Kapitel unternehmen wir den Versuch Ihnen das Konzept der Datentypen zu vermitteln.
Dies beinhaltet Theorie und Praxis.
Um in ``Python`` mit den Datentypen praktisch umgehen zu können reicht Ihnen dieses Kapitel.
Im nächsten Kapitel [Datentypen (Fortsetzung)](sec-data-types-advanced) werden wir hingegen genauer untersuchen weshalb es Datentypen gibt und welchen Einfluss diese im Detail haben.
Möchten Sie jedoch ein tieferes Verständnis davon bekommen wie Datentypen mit dem Ablauf eines Programms und der Computerhardware zusammenhängen, lohnt sich der Blick in das nächste Kapitel [Datentypen (Fortsetzung)](sec-data-types-advanced).

Wir versuchen folgende Fragen zu beantworten:

1. Grundlagen
   1. Was kann ich in **Python** mit einer Variable eines bestimmten Typs anfangen? Abschnitt 4.1 bis 4.9.
   2. Welche Typisierung verwendet **Python**? Abschnitt [4.2 Pythons Typisierung](sec-typing-in-python).

2. Fortsetzung
   1. Was ist der Unterschied zwischen statischer und dynamischer Typisierung? Abschnitt [5.1 Dynamische und statische Typisierung](sec-type-systems).
   2. Weshalb gibt es überhaupt Datentypen? Abschnitt [5.2 Existenzberechtigung](sec-why-data-types).
   3. Was passiert bei einer Änderung des Datentyps einer Variablen? Abschnitt [5.3 Interpretationswechsel](sec-change-of-data-types).
   4. Welche Datentypen gibt es? Abschnitt [5.4 Arten von Datentypen](sec-kind-of-data-types).
   5. Warum gibt es in Python keine primitiven Datentypen? Abschnitt [5.5 Primitive Datentypen in Python?](sec-primitive-data-types-in-python)).