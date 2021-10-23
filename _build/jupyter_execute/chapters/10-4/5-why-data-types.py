# Existenzberechtigung

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

3 + 'a' # int + str -> Fehler!

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

max(3,'b')

Wir können das an dieser Stelle nicht wissen.
Es kommt darauf an **wie** die Funktion ``max`` implementiert wurde und **was** sie genau macht.
Macht aus Ihrer Sicht ein solcher Aufruf Sinn?

Führen wir den Code aus kommt es zu einem weiteren Fehler: ``'>' not supported between instances of 'str' and 'int'``.
Was soll das nun bedeuten?
Wer hat denn was von größer ``>`` gesagt?
Nun, scheinbar verwendet die Funktion ``max`` den Größer-[Vergleichsoperator](sec-python-operator-compare) und dieser kann mit der Kombination ``str`` und ``int`` nicht umgehen.
Wir erhalten den gleichen Fehler mit

3 > 'b'

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