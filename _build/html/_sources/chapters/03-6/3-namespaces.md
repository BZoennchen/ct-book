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

(sec-namespaces)=
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

```{code-cell} python3
---
tags: [output_scroll]
---
dir(__builtins__)
```

Sobald er startet, legt der ``Python``-[Interpreter](def-interpreter) den *built-in Namensraum* an.
Die *Lebensdauer* des Namensraums endet sobald der Interpreter beendet wird.

(sec-global-namespace)=
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
Das haben wir bis hierher noch nie gemacht, sehen wir uns also ein Beispiel an.
Der folgende extra kompliziert gestaltete Code veranschaulicht mehrere Konzepte zugleich:

```{code-cell} python3
def f(y):
    print('start f()')
    x = 5
    t = 99

    def g():
        t = 0
        print('start g()')
        print(f'x from the enclosing namespace {x}')
        print(f'y from the enclosing namespace {y}')
        print(f'z from the enclosing namespace {z}')
        print(f't from the local namespace {t}')
        print('end g()')
        return
    
    z = 42
    print('end f()')
    return g

func = f(-20)
func()
```

``Python`` erzeugt während des Ablauf dieses Codes zwei Namensräume.

1. einen lokalen Namensraum für den Aufruf von ``g()``
2. einen umschließenden Namensraum für ``f()`` 

Der nachdem der Funktionsaufruf ``f(-20)`` zurückspringt, kann die Funktion ``g`` noch immer auf ``x``, ``y`` und ``z`` zugreifen!
Das funktioniert nur weil ``x``, ``y`` und ``z`` sich im *umschließenden Namensraum* von ``f(-20)`` befindet.

In der letzten Zeile rufen wir dieses ``g()`` durch ``func()`` auf.
Dabei wird ein lokaler Namensraum für den Aufruf erzeugt zugleich existiert der umschließende Namensraum.
In beiden gibt es die Variable ``t``.
Es wird jedoch die des lokalen Namensraums bevorzugt!

Nachdem wir wieder aus der Funktion ``func()`` zurückspringen wird der lokale Namensraum von ``func()`` gelöscht.
Der umschließende Namensraum bleibt hingegen solange besteht, solange es noch eine Referenz auf ``func`` gibt.

Bei jedem Aufruf von ``f(y)`` wird ein neuer umschließender Namensraum erzeugt.

Beachten Sie, dass wir ``z`` in der Funktionsdefinition von ``g`` verwenden obwohl es unterhalb der Definition steht.
Zur Laufzeit, d.h., wenn wir ``g()`` aufrufen existiert es jedoch.

Im Gegensatz dazu kracht es bei folgendem Code, da wir ``g()`` aufrufen bevor ``z`` initialisiert wurde:

```{code-cell} python3
---
tags: [raises-exception]
---
def f():
    def g():
        t = 0
        print(f'z from the enclosing namespace {z}')
        return
    g()
    z = 42
    return

f()
```

## Sichtbarkeit

Es gibt also mehrere *Namensräume* und wie in einem Wörterbuch müssen die Schlüssel, d.h. die Namen innerhalb eines Namensraums eindeutig sein.
Allerdings kann es den gleichen Namen in verschiedenen Namensräumen geben und dieser kann auf unterschiedliche Objekte verweisen.

Existiert ein Name nun in mehreren Namensräumen, woher wissen wir welcher Namensraum von ``Python`` verwendet wird?
Der Namensraum den ``Python`` wählt, legt fest welches Objekt (im Speicher) wir schlussendlich adressieren!

Die *Sichtbarkeit* bzw. der *Scope* entscheidet darüber!
Der *Scope* eines Namens ist der Bereich eines Programms in dem der Name eine Bedeutung hat.
Der [Interpreter](def-interpreter) bestimmt dies zur Laufzeit.
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

```{code-cell} python3
---
tags: [raises-exception]
---
def printY():
    y = 2
    print(y)

printY()
y
```

Ein weiteres Beispiel:

```{code-cell} python3
x = 2
def printX():
    print(x)

printX()
```

Innerhalb der Funktion sucht der Interpreter das ``x`` erst im lokalen Namensraum und findet es nicht.
Den umschließenden Namensraum gibt es nicht.
Dann findet er schließlich ``x`` im globalen Namensraum.

Was passiert im folgenden Code?

```{code-cell} python3
z = 5
def printZ():
    z = 42
    print(z)

printZ()
z
```

Innerhalb der Funktion findet der Interpreter das ``z`` im lokalen Namensraum und es hat den Wert ``42``.
Nachdem die Funktion beendet wird, existiert dieser Namensraum nicht mehr und das ``z`` in der letzten Zeile stammt aus dem globalen Namensraum!

Es wird immer die **lokale** Variable, d.h. die Variable des **lokalen Namensraums** bevorzugt!
Die eine Variable liegt im globalen Namensraum ``global.z``, die andere im lokalen Namensraum der Funktion ``global.printZ.z``.

Sie können das Verhalten auch sehr gut mit der *built-in*-Funktion ``id()`` untersuchen:

```{code-cell} python3
z = 5
print(f'global z id: {id(z)}')
def printZ():
    z = 42
    print(f'lokal z id (after lokal z is defined): {id(z)}')
    print(z)

printZ()
z
```

```{admonition} Mehrere Namensräume?
:class: remark
:name: remark-duplicated-namespaces

Eine Variable kann innerhalb einer Funktion einem der vier Namensräume stammen.
Niemals jedoch an der einen Stelle aus dem einen und an der anderen Stelle aus dem anderen Namensraum!
```

Der ``Python``-Interpreter schützt uns vor möglichen und äußerst undurchsichtigen Verwendungen zweier Variablen mit dem scheinbar gleichen Namen.
Folgender Code führt zum Glück zu einem Fehler:

```{code-cell} python3
---
tags: [raises-exception]
---
z = 5
print(f'global z id: {id(z)}')
def printZ():
    print(f'lokal z id (before lokal z is defined): {id(z)}')
    z = 42
    print(f'lokal z id (after lokal z is defined): {id(z)}')
    print(z)

printZ()
z
```

Der Interpreter ließt ``z = 42`` innerhalb der Funktion und weiß deshalb, dass ``z`` im *lokalen Namensraum* liegen muss.
Dann wirft er den Fehler in der ersten Zeile der Funktion, da ``z`` angesprochen aber noch nicht definiert wurde.
Er lehnt es ab, stattdessen das *globale* ``z`` zu verwenden.

Blicken wir auf ein etwas komplizierteres Beispiel und überlegen uns was genau vor sich geht:

```{code-cell} python3
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
```

Vor dem Funktionsaufruf gibt es den Namen ``z`` im *globalen Namensraum*.
Der Wert auf den dieser verweist ist gleich ``5``.
Dann rufen wir ``printZ(z)`` auf.
Damit wandert ``z`` in den *lokalen Namensraum* der Funktion ``printZ()``.
Dieses *lokale* ``z`` zeigt (noch) auf den gleichen Speicherbereich wie das *globale* ``z``.
Dann werden Adresse und Wert des *lokalen* ``z`` durch ``z = 42`` geändert.
Beim zweiten Funktionsaufruf wird diese Änderung nicht durchgeführt, da ``z == 42``.

Lassen Sie uns zum Abschluss noch ein Beispiel mit einem *umschließenden Namensraum* betrachten.
Dabei werden wir erneut eine Funktion als Rückgabewert verwenden.
Wir werden dies noch ausführlicher besprechen, nehmen Sie es also als kleinen Ausblick.

````{exercise} Umschließender Namensraum
:label: closure-exercise

Geben Sie an was folgender Code ausgibt.
In welchem Namensraum liegen ``x`` und ``printX``?

```python
def magic(x):
    def printX():
        print(x)
    return printX

func = magic(42)
func()
func()
func()
```
````

````{solution} closure-exercise
:label: closure--solution
:class: dropdown

Es wird dreimal ``42`` ausgeben.
``x`` und ``printX`` liegen im umschließenden Namensraum von ``magic(42)``.
````

Das Konzept der *umschließenden Namensräume* keine Eigenheit von ``Python`` sondern allgemein unter dem Begriff [Closure](https://de.wikipedia.org/wiki/Closure_(Funktion)) bekannt.