(sec-change-of-data-types)=
# Interpretationswechsel

Was passiert wenn wir eine Zahl in eine Zeichenkette umwandeln?
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

Würden wir uns die Bits der Speicherbereiche der Variablen ``number`` und ``characters`` anzeigen, so wären diese Bits **nicht** identisch.
Die Bits welche die Zahl 90 ergeben, d.h. $90_{10} = 01011010_2$ ergeben in der von ``Python`` gewählten Interpretation (ASCII) **nicht** die Zeichenkette ``'90'``.
Auch die Datentypen der beiden Variablen sind unterschiedlich.
``characters`` ist eine [Zeichenkette](sec-string) (``str``) und ``number`` eine [ganze Zahl](sec-int) (``int``).

print(f' type of number {type(number)}')
print(f' type of characters {type(characters)}')

In diesem Beispiel wechseln wir nicht nur die [Interpretation](sec-interpretation) von 'interpretiere Bits als Zahl' auf 'interpretiere Bits als Zeichenkette' sondern auch den **Wert** -- die Bits werden ebenfalls verändert.
Mit ``str(90)`` sagen wir ``Python``: Bitte mach uns aus der Zahl 90 die Zeichenkette ``'90'``.

Es wird außerdem klar, dass wir eine Zahl in ihrer Gestalt als ``int`` gar nicht ausgeben können!
Stattdessen wird diese immer erst in eine Zeichenkette umgewandelt.
Die Funktion ``print`` sorgt dafür, dass sowohl der Inhalt von ``number`` als auch ``90`` in die Zeichenkette ``'90'`` umgewandelt werden.

Mit Ausnahme der [Bitoperationen](sec-bit-operations) bieten Hochsprachen wie ``Python``, ``Java``, ``JavaScript`` bewusst kaum die Möglichkeit direkt mit den Bits im Speicher zu interagieren.
Wir ändern Zahlen, Text und anderes und die Hochsprachen kümmern sich darum, dass die Werte im Speicher dementsprechend angepasst werden.
Diese Abstraktion schützt Programmierer\*innen vor Fehlern und erhöht die Lesbarkeit des Quellcodes.
Es macht keinen Sinn eine Bitfolge, die erst als Text interpretiert wird, auf einmal als Zahl zu interpretieren.

Die Art und Weise wie Werte im Speicher bei der Typumwandlung verändert werden ist für uns Menschen gemacht.
Würden wir lieber in der Binärdarstellung unsere Zahlen betrachten, wäre es besser wenn die Zahl ``90`` auch als Binärzahl ausgegeben wird.
Dies ist allerdings im Allgemeinen (noch) nicht der Fall.

Eine Dezimalzahl als Binärzahl zu interpretieren kann dennoch in besonderen Fällen Sinn ergeben.
Einen solchen Fall stellen die Bitoperationen dar.
Die folgende Bitverschiebung manipuliert einen Bereich des Speichers direkt.

5 << 1

Hier werden die Bits, welche die Zahl ``5`` repräsentieren um eins nach links verschoben, was einer Multiplikation mit ``2`` gleichkommt.
Dabei wird die ``5`` für die Operation als Zahl in ihrer ursprünglichen Binärdarstellung interpretiert.

Dies funktioniert jedoch nicht mit einem Zeichen.
``Python`` verbietet die Bitverschiebung für Zeichen obwohl das Zeichen ja auch als Bitfolge im Speicher liegt.
Folgender Code führt zu einem Fehler, da er kaum einen Sinn oder Nutzten hat:

```python
'a' << 1
```

In anderen Sprachen wie ``C/C++`` würde dies funktionieren und zu unsauberen, unleserlichen und verwirrenden Code führen.
Auch in diesen Sprachen ist es gute Praxis, dies nicht zu tun, obwohl es theoretisch möglich ist.
Hier kann man Diskutieren was besser ist: Alles erlauben um maximale Freiheit zu gewährleisten oder Programmierer\*innen einschränken, um sie zu schützen.

Wir können das Zeichen ``'a'`` mit der Funktion ``ord`` in eine Zahl umwandeln.
Das Ergebnis hängt mit der von ``Python`` gewählten [Interpretation](sec-interpretation) (ASCII) zusammen.
Daraufhin können wir die Bitverschiebung durchführen und die Zahl mit ``chr`` wieder in ein Zeichen zurück transformieren.

chr(ord('a') << 1)

Wir erhalten ein neues Zeichen: Ein ``'Â'``, können wir das irgendwo gebrauchen?
Das ist zu bezweifeln und selbst wenn, ist dieser Code besser lesbar, da wir explizit die Anweisung zur Umwandlung in eine Zahl angeben.

Ändern wir in einer Hochsprache die Interpretation, so ändert sich meist auch der Wert im Speicher, da es meistens anders keinen Sinn macht und wir genau das erreichen wollen.
Hochsprachen lösen uns von den [Bits](def-bit) und [Byte](def-byte), stattdessen betrachten wir Zahlen in der Dezimalschreibweise.
Vergessen wir einmal die Bits im Speicher und achten nur auf die Zahl ``90`` im obigen Beispiel, so können wir sagen dass sich der Wert ``90`` nicht ändern.
Was sich ändert ist die Interpretation: Einmal die ``90`` als Zahl und einmal als Zeichenkette ``'90'``.