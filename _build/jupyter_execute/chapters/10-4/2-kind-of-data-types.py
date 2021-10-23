(sec-kind-of-data-types)=
# Arten von Datentypen

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

## Primitive Datentypen

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

## Built-in Datentypen

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

## Zusammengesetzte Datentypen

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