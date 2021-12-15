# Namensräume und Sichtbarkeit

Jeder *Name*, d.h. jede *Variable* in einem Programm hat einen sogenannten 

+ *Scope* (Sichtbarkeitsbereich), 
+ eine *Lebensdauer*,
+ und ist einem *Namensraum* zugeordnet.

Der Scope wird aus den gerade bestehenden Namensräumen bestimmt.

## Namensräume

Ein *Namensraum* ist eine Sammlung von derzeit definierten symbolischen Namen mit der jeweiligen Information welches Objekt (im Speicher) der jeweilige Name referenziert.
Wir können uns einen Namensraum als ein [Wörterbuch](sec-dict) vorstellen, wobei die Schlüssel die Namen sind und die Werte die jeweiligen Objekte.
Jedes Schlüssel-Wert-Paar bildet einen Namen auf sein entsprechendes Objekt ab.

In ``Python`` gibt es vier *Namensräume* (engl. namespaces):

1. *built-in*,
2. *global*
3. *enclosing*
4. *local*

Und alle diese *Namensräume* haben eine unterschiedliche *Lebensdauer*.
``Python`` kümmert sich automatisch um die Erstellung und Löschung der *Namensräume* zur Laufzeit.

### Built-in

Im *built-in Namensraum* befinden sich alle Namen aller ``Python`` *built-in* Objekte.
Zum Beispiel befinden sich die Namen ``len``, ``list``, ``str`` usw. in diesem Namensraum.
Diesen Namensraum sollten wir nicht verändern.
Wir können uns alle Namen des *built-in* Namensraums ausgeben lassen:

dir(__builtins__)

Sobald er startet, legt der ``Python``-[Interpreter](def-interpreter) den *built-in Namensraum* an sobald er startet.
Die *Lebensdauer* des Namensraums endet sobald der Interpreter beendet wird.


### Global

Der *globale Namensraum* beinhaltet alle Namen die auf der Ebene des Hauptprogramms definiert wurden.
``Python`` erzeugt den globalen Namensraum sobald das Hauptprogramm startet.
Der Namensraum existiert ebenfalls solange der Interpreter noch nicht beendet ist.

Genau genommen erzeugt der Interpreter für jedes Modul einen globalen Namensraum, es gibt somit möglicherweise mehrerer.
Jedes Modul was wir mit ``import`` laden, erhält seinen eigenen globalen Namensraum.

(sec-local-namespace)=
### Lokal und umschließend

Wann immer eine Funktion ausgeführt wird, wird ein neuer *lokaler Namensraum* für diesen Funktionsaufruf erzeugt.
Die Lebensdauer des Namensraums endet sobald die Funktion verlassen wird oder die Funktion durch einen Fehler abbricht.

Ein *umschließender Namensraum* wird hingegen erzeugt, wenn wir innerhalb einer Funktion eine weitere Funktion definieren.
Das haben wir bis hierher noch nie gemacht, sehen wir uns also ein Beispiel an:

def f():
    print('start f()')

    def g():
        print('start g()')
        print('end g()')
        return
    
    g()
    print('end f()')
    return

f()

``Python`` erzeugt hierbei zwei Namensräume.
Einen *lokalen Namensraum* für ``g()`` und einen *umschließenden Namensraum* für ``f()``, denn ``f()`` *umschließt* ``g()``.
Beide Namensraume bleiben bestehen bis deren jeweilige Funktion beendet ist.

## Sichtbarkeit

Es gibt also mehrere *Namensräume* und wie in einem Wörterbuch müssen die Schlüssel, d.h. die Namen innerhalb eines Namensraums eindeutig sein.
Allerdings kann es den gleichen Namen in verschiedenen Namensräumen geben und dieser kann auf unterschiedliche Objekte verweisen.

Existiert ein Name nun in mehreren Namensräumen, woher wissen wir welcher Namensraum von ``Python`` verwendet wird?
Der Namensraum den ``Python`` wählt, legt fest welches Objekt (im Speicher) wir schlussendlich adressieren!

Die *Sichtbarkeit* bzw. der *Scope* entscheidet darüber!
Der *Scope* eines Namens ist der Bereich eines Programms in dem der Name eine Bedeutung hat.
Der Interpreter bestimmt dies zur Laufzeit.
Als Basis verwendet er die Information, wo die Namensdefinitionen auftauchen, und wo der Name referenziert wird.

Bezieht sich unser Code auf den Namen ``x``, so sucht ``Python`` den Namen ``x`` in der folgenden Reihenfolge:

1. **Lokal**: Sofern wir ``x`` innerhalb einer Funktion referenzieren, sucht ``Python`` im lokalen Namensraum der Funktion.
2. **Enclosing**: Referenzieren wir ``x`` innerhalb einer umschlossenen Funktion und so sucht der Interpreter als nächstes im umschließenden Namensraum der umschließenden Funktion.
3. **Global**: Schlägt dies auch fehl und er findet ``x`` nicht, sucht der Interpreter im globalen Namensraum.
4. **Built-in**: Wenn selbst das fehlschlägt, sucht der Interpreter als letztes im built-in Namensraum.

## Beispiele

Im folgenden Beispiel, hat die Variable ``y`` einen lokale Sichtbarkeit.
Der Interpreter sucht und findet sie im lokalen Scope innerhalb von ``printY()``.
Außerhalb der Funktion ist ``y`` jedoch nicht definiert (weder im globalen noch im built-in Namensraum).
Deshalb kommt es zu einem Fehler in der letzten Zeile.

def printY():
    y = 2
    print(y)

printY()
y

Ein weiteres Beispiel:

x = 2
def printX():
    print(x)

printX()

Innerhalb der Funktion sucht der Interpreter das ``x`` erst im lokalen Namensraum und findet es nicht.
Den umschließenden Namensraum gibt es nicht.
Dann findet er schließlich ``x`` im globalen Namensraum.

Was passiert im folgenden Code?

z = 5
def printZ():
    z = 42
    print(z)

printZ()
z

Innerhalb der Funktion findet der Interpreter das ``z`` im lokalen Namensraum und es hat den Wert ``42``.
Nachdem die Funktion beendet wird, existiert dieser Namensraum nicht mehr und das ``z`` in der letzten Zeile stammt aus dem globalen Namensraum!

Es wird immer die **lokale** Variable, d.h. die Variable des **lokalen Namensraums** bevorzugt!
Die eine Variable liegt im globalen Namensraum ``global.z``, die andere im lokalen Namensraum der Funktion ``global.printZ.z``.

Sie können das Verhalten auch sehr gut mit der *built-in*-Funktion ``id()`` untersuchen:

z = 5
print(f'global z id: {id(z)}')
def printZ():
    z = 42
    print(f'lokal z id (after lokal z is defined): {id(z)}')
    print(z)

printZ()
z

```{admonition} Doppelte Namensräume?
:class: hint

Eine Variable kann innerhalb einer Funktion entweder aus dem **lokalen** oder **globalen** Namensraum stammen.
Niemals jedoch an der einen Stelle aus dem einen und an der anderen Stelle aus dem anderen Namensraum!
```

Der ``Python``-Interpreter schützt uns vor möglichen und äußerst undurchsichtigen Verwendungen zweier Variablen mit dem scheinbar gleichen Namen.
Folgender Code führt zum Glück zu einem Fehler:

z = 5
print(f'global z id: {id(z)}')
def printZ():
    print(f'lokal z id (before lokal z is defined): {id(z)}')
    z = 42
    print(f'lokal z id (after lokal z is defined): {id(z)}')
    print(z)

printZ()
z

Der Interpreter ließt ``z = 42`` innerhalb der Funktion und weiß deshalb, dass ``z`` im *lokalen Namensraum* liegen muss.
Dann wirft er den Fehler in der ersten Zeile der Funktion, da ``z`` angesprochen aber noch nicht definiert wurde.
Er lehnt es ab, stattdessen das *globale* ``z`` zu verwenden.

Blicken wir auf ein etwas komplizierteres Beispiel und überlegen uns was genau vor sich geht:

def printZ(z):
    if z == 42:
        print(f'global z id: {id(z)}')
        print(z)
    else:
        z = 42
        print(f'lokal z id: {id(z)}')
        print(z)

z = 5
print(f'global z id: {id(z)}')
printZ(z)
print()

z = 42
print(f'global z id: {id(z)}')
printZ(z)

Vor dem Funktionsaufruf gibt es den Namen ``z`` im *globalen Namensraum*.
Der Wert auf den dieser verweist ist gleich ``5``.
Dann rufen wir ``printZ(z)`` auf.
Damit wandert ``z`` in den *lokalen Namensraum* der Funktion ``printZ()``.
Dieses *lokale* ``z`` zeigt (noch) auf den gleichen Speicherbereich wie das *globale* ``z``.
Dann werden Adresse und Wert des *lokalen* ``z`` durch ``z = 42`` geändert.
Beim zweiten Funktionsaufruf wird diese Änderung nicht durchgeführt, da ``z == 42``.

Lassen Sie uns zum Abschluss noch ein Beispiel mit einem *umschließenden Namensraum* betrachten.
Dabei werden wir jedoch eine Funktion als Rückgabewert verwenden.
Wir werden dies noch ausführlicher besprechen, nehmen Sie es also als kleinen Ausblick:

def magic(x):
    def printX():
        print(x)
    return printX

func = magic(42)
func()
func()
func()

Hmm???
Was passiert hier?
Kurz gesagt: Die Funktion ``magic()`` gibt die Funktion ``printX()`` zurück.
Der Name der Funktion befindet sich in ``func`` und wir rufen mit ``func()`` auf.
Der Interpreter sucht im *lokalen Namensraum* von ``func()``, d.h. im *lokalen Namensraum* von ``printX()`` und findet ``x`` nicht.
Dann sucht er im *umschließenden Namensraum* und wird fündig.
Das bedeutet der *umschließenden Namensraum* besteht möglicherweise weiterhin, auch nachdem die *umschließenden Funktion* beendet wurde.

Dieses Konzept bezeichnet man als sog. [Closure](https://de.wikipedia.org/wiki/Closure_(Funktion)).