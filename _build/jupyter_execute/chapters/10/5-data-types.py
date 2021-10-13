(sec-datatypes)=
# Datentypen

Wie in Abschnitt [Repräsentation](sec-representation) beschrieben, befinden sich im Speicher des (digitalen) Computers ausschließlich [Bits](def-bit).
Sie können sich den Speicher als eine lange lange Liste von Bits vorstellen.
Diese können nur einen von zwei Zuständen (0 und 1) annehmen.
Dennoch verarbeiten Computer Zahlen, Text, Bilder und mehr.
Die Magie dahinter geschieht durch die Wahl und Implementierung einer [Interpretation](sec-interpretation).
Unterschiedliche Interpretationen ermöglichen es, Bits und [Byte](def-byte) als Zahlen, Text, Bilder usw. zu verarbeiten.
Dabei werden schlussendlich diese komplexeren **Datentypen** durch Bits und Byte [repräsentiert](sec-representation).

So könnten wir ein Bild im ``PNG`` oder ``JPEG``-Format als *Werte-Datentyp*-Paar ansehen.
Der *Wert* ist durch die Bits die das Bild als solches ausmachen definiert.
Der *Datentyp* ``PNG`` oder ``JPEG`` gibt an wie diese Bits von der Computerhardware wie auch Software interpretiert werden müssen um das Bild auch als Bild verarbeiten zu können.

Wir sprechen bei diesen Dateiendungen jedoch nicht von **Datentypen** sondern von *Dateiformaten*.
Von **Datentypen** sprechen wir hingegen, wenn es um eine [Interpretation](sec-interpretation) im Zuge der Programmierung geht.

```{admonition} Datentypen
:name: def-datatypes

Ein *Datentyp* oder auch kurz *Typ* ist ein Attribut eines Werts, welches der Computerhardware und dem Compiler oder Interpreter angibt wie der Wert zu verwenden bzw. zu interpretieren ist.

```

Um das Konzept um die Datentypen zu durchdringen empfehlen wir zu einem späteren Zeitpunkt die Übung [Speicher - alles ist eine Liste](sec-memory).

## Zahlen und Zeichen

Bevor wir genauer untersuchen warum und welche Datentypen es gibt, wie wir diese unterscheiden können und was es mit der Typisierung auf sich hat, beginnen wir mit der Praxis.
Die Datentypen mit denen Sie wohl am meisten zu tun haben werden sind Zahlen und Zeichen.

### Zahlen

Computer sind gebaut um numerische Berechnungen auszuführen.



### Zeichenketten


## Arten von Datentypen

Der **Datentyp** einer Variablen gibt an, wie die Bits und Bytes interpretiert werden.
Die Bits und Bytes des Speicherbereichs auf welchen die Variable *zeigt* machen den *Wert* der Variablen aus.
Im folgenden definieren und initialisieren wir Variablen mit unterschiedlichen Datentypen: 

+ Ganze Zahl ``int``, 
+ Fließkommazahl ``float``, 
+ Zeichenkette ``str``, 
+ Wahrheitswert ``bool``, 
+ eine Liste ``list``, welche ganze Zahlen ``int`` enthält und
+ ein Tupel ``tuple``, welche Zeichenketten ``str`` enthält.

number = 111
floating_number = 1.3
characters = 'Hello'
boolean = True
mylist = [1,2,3,4]
mytuple = ('A', 'B', 'C')

Beim Datentyp ``list`` und ``tuple`` fällt auf, dass diese Werte eines anderen Datentyps enthalten, hier ``int`` und ``str``.
Solche Datentypen nennen wir auch *zusammengesetzt Datentypen* wohingegen wir Datentypen, welche wir nicht zerlegen können als [primitive Datentypen](def-primitive-datatypes) bezeichnen.
Zudem gibt es Datentypen, welche von der Programmiersprache die Sie verwenden von vornherein definiert sind und solche die Sie selbst definieren.
Erstere nennen wir *built-in Datentypen* und letztere werden durch *Klassen* realisiert.
Wir werden auf *Klassen* erst am Ende des Kurses eingehen.

Zusammenfassend gibt es vier Arten von Datentypen:

1. Primitive Datentypen,
2. zusammengesetzte Datentypen,
3. built-in Datentypen und
4. eigens definierte Datentypen.

Dabei ist ein Datentyp entweder primitiv oder zusammengesetzt und zugleich entweder built-in oder eigens definiert.
Oftmals sind built-in Datentypen zugleich primitive Datentypen (siehe z.B. ``Java``, ``C/C++``) und eigens definierte Datentypen sind immer auch zusammengesetzte Datentypen.

### Primitive Datentypen

```{admonition} Primitive Datentypen
:name: def-primitive-datatypes

*Primitive Datentypen* sind jene Datentypen für die wir einen festen Speicherbereich definieren.
Ein *primitiver Datentyp* besteht aus keiner Komposition anderer Datentypen.
Ebenso besteht eine Variable vom Typ eines primitive Datentypen eben nicht aus einer Komposition anderer Variablen.
```

Ein *Wert* eines *primitiven Datentyps* belegt im Speicher immer die selbe Anzahl an [Bits](def-bit), wohingegen Werte von *zusammengesetzte Datentypen* unterschiedlich viel Speicher verbrauchen können.
Zudem kann ein *primitiver Datentyp* nicht weiter in andere Datentypen zerlegt werden.

Übertragen wir das auf die 'echte' Welt, so könnte man bei einem Brief von einem *zusammengesetzten Datentyp* sprechen.
Dieser enthält einen Briefkopf, ein Datum einen Absender, Empfänger und den Text.
Das Datum ist wiederum ein *zusammengesetzten Datentyp* bestehend aus Tag, Monat und Jahr.
Der Tag ist schließlich ein *primitiver Datentyp* (eine Zahl zwischen 0 und 31).

```{exercise} Der Datentyp Zeichenkette
:label: datatype-str-exercise
Ist ``str``, d.h. die Zeichenkette, ein primitiver oder zusammengesetzter Datentyp?
Begründen Sie Ihre Antwort.
```

```{solution} datatype-str-exercise
:label: datatype-str-solution
:class: dropdown

``str`` ist ein zusammengesetzter Datentyp.
Zeichenketten haben eine variable Länge und so muss auch der Speicherbereich der von ihnen belegt wird variable sein.
Eine Zeichenkette ist eine Liste aus Zeichen.
Wir können den Datentyp Zeichenkette also in den Datentyp Zeichen zerlegen.
```

### Built-in Datentypen

*Built-in* Datentypen sind jene Datentypen, welche die Programmiersprache (ohne weitere Bibliotheken) mitliefert.
Zur Vollständigkeit listen wir hier alle *built-in Datentypen* von ``Python`` auf.
Einige davon werden Sie jedoch in diesem Kurs nicht verwenden.
Die wichtigsten *built-in Datentypen* sind hervorgehobenen:

1. **Das Nichts** ``None``
2. Zahlen (Numbers)
   + **Ganze Zahlen** ``int``
   + **Fließkommazahl (rationale Zahlen)** ``float``
   + Komplexe Zahlen ``complex``
3. Sequenzen (Sequences)
    1. Unveränderlich
       + **Zeichenketten** ``str``
       + **Tupels** ``tuple``
       + Bytes ``bytes``
    2. Veränderlich
       + **Listen** ``list``
       + Byte Arrays ``bytearray``
4. Mengen (Set types)
   + **(normale) Mengen** ``set``
   + (gefrorene Mengen) ``frozenset``
5. Abbildungen (Mappings)
   + **Wörterbuch** ``dict``
6. Aufrufbare Typen (Callable)
   + **Funktionen**
   + Methoden
   + Klassen
7. Module

Diese Datentypen stehen Ihnen zur Verfügung sobald Sie ``Python`` auf Ihrem System oder Ihrer Umgebung installiert haben.

Anders als in vielen anderen Sprachen müssen Sie den (built-in) Datentyp einer Variablen in ``Python`` nicht explizit angeben.
``Python`` schließt von der Schreibweise des Wertes automatisch auf den richtigen Datentyp.
Eine Folge von Ziffern mit einem optional vorangestellten Minuszeichen werden als ganze Zahl ``int`` interpretiert.
Befindet sich in der Folge ein Punkt ``.`` so wird der Wert als Fließkommazahl interpretiert.
Sie können den Datentyp einer Variablen ``x`` oder eines Wertes mit ``type(x)`` abfragen:

type(-3123)

type(1.313)

name = 'Anna'
type(name)

mylist = [1, 2, 3, 4, 'A']
print(f'List Type: {type(mylist)}')
print(f'Element 0 Type: {type(mylist[0])}')
print(f'Element 4 Type: {type(mylist[4])}')

### Zusammengesetzte Datentypen

Zusammengesetzte Datentypen definieren wir durch andere Datentypen, welche bereits definiert wurden.
Diese sind entweder *built-in Datentypen* der Sprache oder eigens definierte zusammengesetzte Datentypen.
Angenommen Sie wollen den Datentyp ``Person`` definieren welcher sich dadurch auszeichnet, dass er sich aus zwei Zeichenketten ``str`` nämlich dem Vor- und Nachnamen zusammensetzt.
Durch *Klassen* können Sie einen solchen Datentyp definieren.
Wie wir dies machen, werden wir auf einen späteren Zeitpunkt verschieben.

Eine Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict`` sind *zusammengesetzter built-in Datentypen* und zugleich enthalten die Werte (Objekte) dieser Datentypen eine
variable Anzahl an Elementen unterschiedlicher Datentypen.
Eine gute Analogie zu diesen sog, [Sammlung / Kollektion (engl. Collections)](def-collection) sind physikalische Ordner, Schließfächer, Listen auf Papier geschrieben, Rücksäcke, Körbe, Tüten und andere physikalischen Objekte die wir im Alltag verwenden um andere physikalische Objekte zu ordnen, strukturieren oder schlicht zu halten.
Auch der Arbeitsspeicher ist in diesem Sinne eine sowohl physikalische wie auch virtuelle Kollektion an Bits.

```{admonition} Sammlung (Collection)
:name: def-collection
Als *Sammlung* bezeichnen wir alle Datentypen (Tupel, [Dictionary](def-python-dictionary), Listen, usw.) die eine **variable Anzahl** an anderen Elementen (normalerweise mehrere) beinhalten.

```

Mit **variabler Anzahl** ist gemeint, dass es Sammlung gibt, welche 5 Elemente enthalten und Sammlung gibt die 1000 Elementen enthalten.
Es kann dennoch sein, dass eine Sammlung die 10 Elemente enthält nicht verändert werden kann, d.h. sie wird auf immer dieser 10 Elemente enthalten.

mylist = [1, 2, 'A', 3, 1.23, [1, 2, 3]]
mylist

mytuple = (mylist, 'D')
mytuple

mydict = {'firstname' : 'Paulina', 'lastname' : 'Schmidt', 'age' : 23 }
mydict

month = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
month

Eine Zeichenkette ``str`` ist ebenfalls eine Kollektion, jedoch sind deren Elemente alle vom gleichen Typ -- dem Zeichen.

### Eigens definierte Datentypen

Dazu später mehr.


## Primitive Datentypen in Python?

Jetzt kommen wir zu einer Besonderheit in ``Python``, welche Sie als Anfänger erst einmal ignorieren können.
Dennoch möchten wir Sie Ihnen nicht vorenthalten und auch kein Halbwissen vermitteln!

Sie vermuten wohl zurecht, dass ``byte``, ``int``, ``long``, ``float``, ``bool`` [primitive Datentypen](def-primitive-datatypes) sind und Sie lägen bei vielen anderen Programmiersprachen richtig, doch in ``Python`` gibt es gar keine primitiven Datentypen.
Das ist für Anfänger verwirrend!
Wie kann es keine primitive Datentypen geben?
Irgendwann muss sich doch ein Datentyp nicht mehr weiter zerlegen lassen?
Und weshalb ist eine ganze Zahl ``int`` kein *primitiver Datentyp*?

```{admonition} Datentypen in Python
:name: alert-datatypes-python
:class: warning
Es gibt in ``Python`` keine primitiven Datentypen!
```

``Python`` kapselt die primitiven Datentypen für uns Programmierer*innen.
Zu unserem eigenen Schutz können wir auf diese nicht direkt zugreifen und mit ihnen nicht direkt arbeiten.
Hinter dem Datentyp ``int`` verbirgt sich ein zusammengesetzter Datentyp, der es uns leichter macht mit ganzen Zahlen umzugehen.
Implementiert ist dieser Datentyp in der Programmiersprache ``C++`` und ``Python`` ruft am Ende des Tages ``C++``-Code auf.
Die Implementierung von ``int`` findet sich in den folgenden Dateien (**bitte lassen Sie sich davon nicht abschrecken, Sie müssen diesen Code nicht verstehen!**)

+ [longobject.c](https://github.com/python/cpython/blob/main/Objects/longobject.c)
+ [longintrepr.h](https://github.com/python/cpython/blob/main/Include/longintrepr.h)
+ [longobject.h](https://github.com/python/cpython/blob/main/Include/longobject.h)

In ``Python`` benötigt eine ganze Zahl ``int`` nicht immer den gleichen Speicherbereich!
Deshalb ist es, anders als in vielen anderen Sprachen, in ``Python`` möglich mit sehr großen ganzen Zahlen zu rechnen.
Wäre ``int`` ein primitiver Datentyp, wie etwa in ``Java``, ``C/C++``, so würde ein ``int`` Wert immer gleich viel Speicherplatz belegen.
Ob im Speicher eine ``5`` oder eine ``1000`` steht ist für den Speicherplatz den diese Werte verbrauchen egal.


Wie alle Datentypen in ``Python`` ist auch ``str`` ein zusammengesetzter Datentyp.
Anders als in vielen anderen Sprachen gibt es in ``Python`` keinen Datentyp für ein einzelnes Zeichen ``char``.
Ein einzelnes Zeichen ist in ``Python`` eine Zeichenkette der Länge 1.
Dennoch ist ``str`` kein primitiver Datentyp.

## Interpretationswechsel

Wir können zum Beispiel eine Variable mit einer Zahl initialisieren und diese Zahl als Zeichen interpretieren.
Dazu brauchen wir jedoch eine geeignete Interpretation:

number = 90
characters = str(number)
print(f'number {number}')
print(f'characters {characters}')
print('str 90')
print(f'int {90}')

Was passiert hier?
Es wird viermal die Zahl ``90`` als Zeichenkette ausgegeben.
Erst weisen wir die Zahl ``90`` der Variablen ``number`` zu.
In der zweiten Zeile weisen wir die Zeichenkette ``'90'`` der Variablen ``characters`` zu.
``str`` ist eine Funktion welche aus ihrem Argument eine Zeichenkette generiert.

Würden wir uns die Bits der Speicherbereiche der Variablen ``number`` und ``characters`` anzeigen, so wären diese Bits nicht identisch.
Die Bits welche die Zahl 90 ergeben, d.h. $90_{10} = 01011010_2$ ergeben in der von ``Python`` gewählten Interpretation (ASCII) nicht die Zeichenkette ``'90'``.
Auch die Datentypen der beiden Variablen sind unterschiedlich.
``characters`` ist eine sogenannte Zeichenkette (String ``str``) und ``number`` eine ganze Zahl (Integer ``int``).

In diesem Beispiel wechseln wir also beides: Die Interpretation als auch den Wert (die Bits und Byte)!
Mit ``str(90)`` sagen wir ``Python``: Bitte mach uns aus der Zahl 90 die Zeichenkette ``'90'``.
Es wird außerdem klar, dass wir eine Zahl in ihrer Gestalt als ``int`` gar nicht ausgeben können!
Stattdessen wird diese immer erst in eine Zeichenkette umgewandelt.
Die Funktion ``print`` sorgt dafür, dass sowohl der Inhalt von ``number`` als auch ``90`` in die Zeichenkette ``'90'`` umgewandelt werden.

Mit Ausnahme der [Bitoperationen](sec-bit-operations) bieten Hochsprachen wie ``Python``, ``Java``, ``JavaScript`` bewusst kaum die Möglichkeit direkt mit den Bits im Speicher zu interagieren.
Wir ändern Zahlen, Text und anderes und die Hochsprachen kümmern sich darum, dass die Werte im Speicher dementsprechend angepasst werden.
Diese Abstraktion schützt Programmierer*innen vor Fehlern und erhöht die Lesbarkeit des Quellcodes.
Es macht keinen Sinn eine Bitfolge die erst als Text interpretiert wird auf einmal als Zahl zu interpretieren.

Eine Dezimalzahl als Binärzahl zu interpretieren kann durchaus Sinn ergeben.
Deshalb stellen die Bitoperationen eine Ausnahme dar.
Der folgende Bitshift manipuliert einen Bereich des Speichers direkt.

5 << 1

Hier werden die Bits, welche die Zahl ``5`` repräsentieren um eins nach links verschieben, was einer Multiplikation mit ``2`` gleich kommt.
Dabei wird die ``5`` für die Operation als Zahl in ihrer ursprünglichen Binärdarstellung interpretiert.

Dies funktioniert jedoch nicht mit einem Zeichen.
``Python`` verbietet den Bitshift für Zeichen obwohl das Zeichen auch als Bitfolge im Speicher liegt.
Folgender Code führt zu einem Fehler, da er kaum einen Sinn oder Nutzten hat:

```python
'a' << 1
```

In anderen Sprachen wie ``C/C++`` würde dies funktionieren und zu unsauberen, unleserlichen und verwirrenden Code führen.
Auch in diesen Sprachen ist es gute Praxis, dies nicht zu tun, obwohl es theoretisch möglich ist.
Hier kann man Diskutieren was besser ist: Alles erlauben um maximale Freiheit zu gewährleisten oder Programmierer*innen einschränken, um sie zu schützen.

Wir können das Zeichen ``'a'`` mit der Funktion ``ord`` in eine Zahl umwandeln.
Das Ergebnis hängt mit der von ``Python`` gewählten Interpretation (ASCII) zusammen.
Daraufhin können wir den Bitshift durchführen und die Zahl mit ``chr`` wieder in ein Zeichen zurück transformieren.

chr(ord('a') << 1)

Wir erhalten ein neues Zeichen: Ein ``'Â'``, können wir das irgendwo gebrauchen?
Das ist zu bezweifeln und selbst wenn, ist dieser Code besser lesbar, da wir explizit die Anweisung zur Umwandlung in eine Zahl angeben.

Ändern wir in einer Hochsprache die Interpretation, so ändert sich meist auch der Wert im Speicher, da es meistens anders keinen Sinn macht und wir genau das erreichen wollen.
Hochsprachen lösen uns von den Bits und Byte, stattdessen betrachten wir Zahlen in der Dezimalschreibweise.
Vergessen wir einmal die Bits im Speicher und achten nur auf die Zahl ``90`` im obigen Beispiel, so können wir sagen dass sich der Wert ``90`` nicht ändern.
Was sich ändert ist die Interpretation: Einmal die ``90`` als Zahl und einmal als Zeichenkette ``'90'``.

## Existenzberechtigung

Kommen wir noch einmal zurück zu unserer Analogie mit den *Dateiformaten*.
Weshalb enden PDF-Dokumente mit ``.pdf`` und Bilder mit z.B. ``.png``?
Ändern wir die Dateiendung oder lassen Sie Weg, so ändert sich der Inhalt der Datei nicht.
Allerdings kann Ihr Programm zum Lesen von PDFs nur PDFs lesen und die Dateiendung ist eine Art Versprechen, dass es sich bei dieser Datei auch wirklich um eine PDF handelt.
Zudem leitet Ihr Betriebssystem das öffnen der Datei an ein Programm weiter, welches diese Verarbeiten kann.
Da das Betriebssystem nicht alle Dateiformate kennen kann (jeden Tag entstehen neue Formate) achtet es auf die Dateiendung.
Wir als Benutzer können dem Betriebssystem mitteilen, welche Datei mit welchem Programm geöffnet werden soll.

Datentypen existieren aus dem gleichen Grund.
Sie sind ein verpflichtendes Versprechen, wie der Speicherbereich (die Bits und Byte) der den Wert ergibt aussieht.
Funktionen und Operationen verlassen sich auf dieses Versprechen.
Nur so können Sie Informationen verarbeiten, indem die [Interpretation](sec-interpretation) bekannt ist und auch eingehalten wird.
Zum Beispiel erwartet die Addition ``+`` zwei Zahlen.
Dabei kann es sich bei jeder der beiden Zahlen entweder um eine ganze Zahl ``int`` oder um eine Fließkommazahl handeln.

3 + 9       # int + int
3 + 8.6     # int + float
-3.6 + 3.4  # float + float
3.1 + 9     # float + int

Der Datentyp des Ergebnisses der Addition hängt von Datentypen der beiden Summanden ab.

print(type(3 + 9))      # int + int -> int
print(type(3 + 8.6))    # int + float -> float
print(type(-3.6 + 3.4)) # float + float -> float
print(type(3.1 + 9))    # float + int -> float

Zudem wird nicht jeder Datentyp von Addition unterstützt:

```python
3 + 'a' # int + str -> Fehler!
```

Der Fehler der durch diesen Code erzeugt wird besagt: ``unsupported operand type(s) for +: 'int' and 'str'``, d.h. diese Kombination aus Datentypen (``int`` und ``str``) wird nicht unterstützt.
Was passiert wenn wir zwei Zeichenketten 'addieren'?

'a' + 'b' # str + str -> str!

Überraschenderweise führt dies nicht zu einem Fehler.
Wir sprechen hierbei nicht mehr von einer Addition, stattdessen handelt es sich um die sog. Konkatenation (Verkettung) von Zeichenketten.
In anderen Worten entscheiden die Datentypen darüber, welche Operation der ``+``-Operator definiert bzw. welche Operation ausgeführt wird!

Betrachten wir ein weiteres Beispiel:

max([1,2,3,4,5])

und

max('a','b')

Wir rufen beide Male die *built-in Funktion* ``max`` auf.
Einmal ist das Argument eine Liste ``list`` und einmal rufen wir ``max`` mit zwei Argumenten, zwei ganzen Zeichenketten ``str`` auf.
Das Ergebnis ist einmal das größte Element der Liste und einmal das lexikographisch größere Element der beiden Argumente.
Der Datentyp der Rückgabewerte ist einmal eine ganze Zahl ``int`` und einmal eine Zeichenkette ``str``.

Wird folgender Code funktionieren?

```python
max(3,'b')
```

Wir können das an dieser Stelle nicht wissen.
Es kommt darauf an **wie** die Funktion ``max`` implementiert wurde und **was** sie genau macht.
Macht aus Ihrer Sicht ein solcher Aufruf Sinn?

Führen wir den Code aus kommt es zu einem weiteren Fehler: ``'>' not supported between instances of 'str' and 'int'``.
Was soll das nun bedeuten?
Wer hat denn was von größer ``>`` gesagt?
Nun, scheinbar verwendet die Funktion ``max`` den Größer-[Vergleichsoperator](sec-python-operator-compare) und dieser kann mit der Kombination ``str`` und ``int`` nicht umgehen.
Wir erhalten den gleichen Fehler mit

```python
3 > 'b'
```

Es ist im allgemeinen unklar wie wir eine Zahl mit einem Buchstaben vergleichen sollen.
Wir können selbstverständlich einen solchen Vergleich selbst definieren.
Wir greifen hier etwas vor:

def get_key(value):
    if type(value) == str:
        return ord(value[0])
    else:
        return value

max(3, 'b', key=get_key)

Was passiert hier?
Wir definieren eine eigene Funktion ``get_key``.
Diese transformiert den Wert, welchen wir vergleichen wollen in einen anderen Wert.
Ist der Wert eine Zeichenkette, so transformieren wir diese in eine ganze Zahl (ihren ASCII-Code).
Andernfalls geben wir den Wert zurück (keine Transformation).

Wir sagen der Funktion ``max`` Sie solle doch bitte vor jedem Vergleich die zu vergleichenden Werte durch unsere Funktion ``get_key`` transformieren.
Was also passiert ist das ``max``

get_key(3) > get_key('b')

ausführt also

3 > ord('b')

und ``ord('b')`` ergibt ``98``.
Der Rückgabewert ist eine Zeichenkette ``str``.
Rufen wir allerdings folgenden Code auf

def get_key(value):
    if type(value) == str:
        return ord(value[0])
    else:
        return value

max(100, 'b', key=get_key)

so ist der Rückgabewert eine ganze Zahl ``int``.
Auch das ist in vielen anderen Sprachen anders.
In ``Java``, ``C/C++`` ist der Rückgabewert einer Funktion immer vom gleichen Datentyp, denn diese Sprachen sind *statisch getypt* wohingegen ``Python`` oder auch ``JavaScript`` *dynamisch getypt* sind.

## Dynamische und statische Typisierung

Für *statisch getypten Sprache* wird der Datentyp von Werten und Variablen geprüft **bevor** der Programmcode ausgeführt wird.
Im Gegenteil dazu wird diese Prüfung für *dynamisch getypte Sprachen* erst zur Laufzeit durchgeführt, also **während** der Code ausgeführt wird.

Führen Sie folgenden Code aus:

```python
number = 5
number = number + 5
print(number)
number = number + 'b'
```

Dieser führt zu einem bekannten Fehler: ``unsupported operand type(s) for +: 'int' and 'str'`` und dennoch wird die ganze Zahl ``number`` ausgegeben.
In anderen Worten der Code läuft solange bis es kracht.

Lassen Sie uns das ganze einmal in ``Java`` transformieren:

```java
int number = 5;
number = number + 5;
System.out.println(number);
number = number + "b";
```

Dieser Code wird gar nicht erst ausgeführt werden.
Stattdessen erhalten wir eine ähnliche Fehlermeldung vor der Ausführung.
In der ersten Zeilen sehen wir jedoch auch, dass wir den Datentyp für ``number`` explizit definieren müssen!
In ``Java`` ist der Datentyp einer Variablen (hier ``number``) auf festgelegt solange die Variable existiert.
Auch folgender Code führt zu einem Fehler:

```java
int number = 5;
number = "b";
```

und auch dieser hier:

```java
int number = 5;
String number = "b";
```

Dadurch, dass bevor der Code ausgeführt wird auf die richtigen Typen geprüft wird, gelten strengere Regeln für diese Typen.
Andernfalls wäre dies nicht möglich.

Im Gegensatz dazu können wir in ``Python`` viel 'freier' mit Typen handtieren.
Der Äquivalente Code wird einwandfrei ausgeführt:

number = 5
number = 'b'

number = 5
number = 'b'

### Was ist besser?

Die einfache Antwort hierauf lautet: nichts von beidem.
Am liebsten hätte man natürlich eine dynamische Typisierung bei der dennoch die Typen auf Korrektheit vor dem Programmlauf überprüft werden.

Die explizite Angabe des Datentyps bei *statisch getypten Sprachen* dient der Dokumentation und macht den Code oft lesbarer ohne zusätzliche Kommentare hinzuzufügen -- der Code ist die Dokumentation. 
Auf der anderen Seite hat eine statische Typisierung weitreichende Auswirkungen auf die Struktur des Codes.
Wir können auf diese nicht im Detail eingehen, doch erfordern statisch getypte Sprachen einen viel strikteren Umgang mit Typen und deren Definition.
Konzepte wie Vererbung und Polymorphie werden unerlässlich.
Im allgemeinen sind statisch getypte Sprachen hungriger, was die Anzahl der Zeichen des geschriebenen Codes angeht.
Mit dynamisch getypte Sprachen erreicht man oft den gleichen Effekt mit deutlich weniger Zeilen Code.
In der Kategorie der Laufzeit des Codes gewinnen statisch getypte Sprachen.
Das macht auch Sinn, denn sind vor der Ausführung alle Typen aller Werte, Variablen usw. bekannt so können Sie sich vorstellen, dass [Übersetzer](def-compiler) den Code besser optimieren können.

### Sowohl als auch?

``Python`` ist dynamisch getypt.
Jedoch ruft ``Python`` intern ``C/C++`` Code auf und ``C/C++`` sind statisch getypte Sprachen!
Wir sind zwar noch immer nicht am Optimum: Typ checks vor der Laufzeit und dynamische Typen, aber wir sind nah dran.
``Python`` ist immer dann schnell wenn der statisch getypte Code aufgerufen wird und immer dann langsam wenn wir lange im ``Python``-Code selbst (der dynamisch getypt ist) verweilen.

### Typ hints mit Python

Mit ``Python`` 3.6 wurde eine Syntax eingeführt mit der wir den Datentyp trotz dynamischer Typisierung direkt im Code angeben können.
Wir werden dies im Kurs nicht verwenden wollen es Ihnen aber auch nicht vorenthalten.
Der angegebene Typ dient der reinen Dokumentation und hat keinerlei Auswirkungen auf die Laufzeit.
Manche Entwicklungsumgebungen wie Visual Studio Code (SVCode) bieten auf Grundlage dieser [Typ hints](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) Warnmeldungen bzw. Fehlermeldungen.

Mit Type hints wird aus

number = 5
number = 'b'

folgender Code

```python
number : int = 5
number = 'b'
```

Dieser wird noch ausgeführt wie zuvor doch Ihre Entwicklungsumgebung wird Sie vermutlich warnen, dass hier der Typ gewechselt wird.
Besonders für Funktionen ist dies hilfreich um die Dokumentation direkt in den Code zu integrieren.
Zum Beispiel wird aus

def add(x, y):
    return x + y

folgender Code

def add(x: int, y: int) -> int:
    return x + y

Wir geben uns und dem- oder derjenigen, welche unseren Code benutzt zu verstehen, dass die Funktion zwei ganze Zahlen erwartet und eine ganze Zahl zurückliefert.