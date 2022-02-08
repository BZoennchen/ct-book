# Klassen und Objekte

Eine *Klasse* ist die Blaupause seiner *Objekte*.
Sie ist ein *zusammengesetzter Datentyp* welche *Methoden* enthält, die allesamt auf jenen Datentyp angewendet werden sollen.
Eine *Klasse* definiert somit ein Bündel aus **Daten** und **Funktionen** (welche wir *Methoden* nennen).
Und ein *Objekt* ist eine konkrete *Instanz* einer *Klasse*, d.h. eine Variable eines *zusammengesetzte Datentyp* belegt mit bestimmten Werten.

```{admonition} Objekte in Python
:class: important
In ``Python`` ist alles (auch Werte von atomaren Datentypen) ein Objekt.
```

Von einem *Objekt* gibt es nur eine *Klasse*, doch gibt es viele *Objekte* dieser *Klasse*.
Jedes *Objekt* liegt als *Datenbündel* im Speicher.
Jedes Objekt einer bestimmten Klasse beinhaltet andere Werte, jedoch sind die Methoden allesamt die gleichen.

## Klassen

Eine *Klasse* ist eine Definition eines [zusammengesetzten Datentyps](sec-datastructures) angereichert mit *Methoden*, die auf dem Datentyp ausgeführt werden sollen.
Sie ist ein Codeblock der mit dem ``class``-Ausdruck beginnt:

```python
class ClassName(Superclass):
    def __init__(self, arguments):
        # define or assign object attributes

    def other_method(self, arguments):
        # body of the method
```

Ähnlich wie eine Funktion, müssen wir eine Klasse zuerst definieren bevor wir sie nutzten können.
Doch anders als Funktionen, schreibt man Klassennamen (hier ``ClassName``) in [CamelCase/CamelCaps](https://en.wikipedia.org/wiki/Camel_case).
``superclass`` ist optional und ist die Klasse von der ``ClassName`` *erbt*.
Was das bedeutet, werden wir im Abschnitt [Vererbung](sec-inheritance) besprechen.

Methoden der Form ``__method_name__()``, sind spezielle ``Python``-Methoden die eine vordefinierte Bedeutung besitzen.
Die voran- und nachgestellten doppelten Unterstriche deuten an, dass diese Methoden für spezielle Zwecke reserviert sind.
``__init__()`` wird ausgeführt sobald ein Objekt der Klasse instanziiert / erzeugt wurde.
Genau genommen ist ``__init__()`` nicht der Konstruktor](def-constructor), sondern wird direkt nach dem Konstruktor aufgerufen.
In ``Python`` definieren wir den Konstruktor nicht explizit.
``__init__()``  füllt das Objekt mit seinen Daten bevor das Objekt benutzt wird.

```{admonition} Konstruktor
:name: def-constructor
Als *Konstruktor* bezeichnen wir eine spezielle Methode einer Klasse, die beim Erzeugen des Objekts der Klasse aufgerufen wird.
Die Methode erzeugt das Objekt, d.h., diese Methode reserviert Speicher und legt es das Objekt in den Arbeitsspeicher an die entsprechende Speicheradresse.
```

Die Methode ``other_method`` ist eine Funktion des Objekts der Klasse ``ClassName``.
Es wird Ihnen aufgefallen sein, dass jede der Methoden als erstes Argument ``self`` definiert.
Jede Klassenmethode muss dieses Extraargument ``self`` besitzen.
Dieses Argument referenziert das Objekt **selbst**.
Durch dieses ``self`` können wir auf alle Attribute und Methoden des Objektes zugreifen (auch die privaten).
Greifen wir auf Attribute oder Methoden des Objekts zu, so müssen wir den Weg über das ``self``-Argument gehen.

Blicken wir auf ein Beispiel.
Wir definieren eine neue Klasse ``Student`` mit den *Attributen* ``sid`` (id der Studierenden), ``name``, ``type`` und ``age``.
Wir definieren eine Methode ``say_name`` welche uns einen Text über den Studierenden ausgibt.
Alle Attribute bis auf ``type`` werden bei der Objekterzeugung übergeben.

class Student():
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
        self.type = 'learning'
        
    def say_name(self):
        print(f'My name is {self.name}.')

Sie sehen wie wir über ``self.attributename`` auf die *Attribute* des Objekts zugreifen können.
Für Methoden gilt diese Regel ebenso.
Lassen Sie uns das veranschaulichen indem wir unsere Klasse um eine weitere Methode ``report`` erweitern.

class Student():
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
        self.type = 'learning'
        
    def say_name(self):
        print(f'My name is {self.name}.')

    def report(self, score):
        self.say_name()
        print(f'My id is: {self.sid}')
        print(f'My age is: {self.age}')
        print(f'My score is: {score}')

``report`` ruft die Methode ``say_name`` durch ``self.say_name()`` auf.
Beachten Sie, dass wir das ``self`` **nicht** als Argument übergeben müssen!
Der Interpreter wandelt im Grunde ``self.say_name()`` zu ``say_name(self)`` um.

In ``report`` übergeben wir ein weiteres Argument ``score``, welches wir wie gewöhnt durch seinen Namen ansprechen können.

## Objekte

Ein *Objekt* ist eine Instanz einer Klasse.
Die *Klasse* ist der *Datentyp* und das Objekt ist ein *Wert* vom Typ der Klasse angereichert mit den Methoden, die in der Klasse definiert wurden.
Wir können viele verschiedene und auch gleiche *Objekte* einer *Klasse* erzeugen.
Die Klasse können wir als den Bauplan der Objekte verstehen.

Rufen wir Methoden eines Objekts auf, müssen wir das erste spezielle ``self``-Argument nicht angeben.
Eine Methode ``methodname`` des Objekts ``objectname`` rufen wir durch

```python
objectname.methodname(arguments)
```

auf.
Ein solcher Aufruf wird auch als Nachricht, die wir an einen Empfänger schicken, verstanden.
Dabei ist die Nachricht gleich ``methodname(arguments)`` und der Empfänger ist das Objekt ``objectname``.
Diese Analogie wird deutlich wenn wir uns an den Roboter ``robo`` erinnern.
Diesen haben wir mit der Nachricht ``move()`` gesagt, er solle sich bewegen.
Auch im folgenden Beispiel können wir Methodenaufrufe als Anweisungen oder Nachrichten die an das Objekt gesendet werden verstehen:

student1 = Student("001", "Susan", 24)
student2 = Student("002", "Mike", 23)

student1.say_name()
student2.say_name()
print(student1.type)
print(student1.age)
print()
student2.report(331)

Im obigen Beispiel erzeugen wir zwei Instanzen ``student1``, ``student2`` der Klasse ``Student``.
Die Daten der Objekte unterscheiden sich, doch deren Methoden sind identisch.
Rufen wir ``report`` auf, so wird intern (innerhalb des Objekts) die Methode ``say_name`` aufgerufen.

## Klassenattribute

``self.attributename`` sind *Attribute* des *Objekts*.
Diese können für jedes Objekt einen anderen Wert besitzen.
*Klassenattribute* sind hingegen *Attribute* einer Klasse und da es nur eine *Klasse* eines bestimmten *Typs* gibt, teilen sich alle *Objekte* einer *Klasse* deren *Klassenattribute*.

Wir definieren *Klassenattribute* indem wir das ``self`` weglassen und diese außerhalb jedweder Methode niederschreiben.
Um es zu verwenden müssen wir den Klassennamen voranstellen, d.h. ``ClassName.attributename``.
Im folgenden Fall führen wir ein *Klassenattribut* ``n_instances`` ein, welches die Anzahl der erzeugten Objekte der Klasse ``Student`` beinhaltet.

class Student():
    n_instances = 0

    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
        self.type = 'learning'
        Student.n_instances +=1
        
    def say_name(self):
        print(f'My name is {self.name}.')

    def report(self, score):
        self.say_name()
        print(f'My id is: {self.sid}')
        print(f'My age is: {self.age}')
        print(f'My score is: {score}')
    
    def num_instances(self):
        print(f'We have {Student.n_instances}-instance in total')

Lassen Sie uns den Code testen:

student1 = Student("001", "Susan", 23)
student1.num_instances()
student2 = Student("002", "Mike", 25)
student1.num_instances()
student2.num_instances()

Wir erzeugen zwei Objekte, doch lediglich ``sid``, ``name`` und ``age`` gehören zu einem bestimmten Objekt.
``student1.name`` hat den Wert ``"Susan"`` und ``student2.name`` hat den Wert ``"Mike"``.
Doch ``n_instances`` wird **objektübergreifend** geteilt.
Bei der Erzeugung der Klasse wird ``n_instances`` auf den Wert ``0`` gesetzt.
Immer wenn wir ein ``Student``-Objekt erzeugen, erhöht sich das *Klassenattribut* ``n_instances`` um eins.

```{admonition} Klassenattribute
:class: warning
*Klassenattribute* sollten sparsam eingesetzt werden und sollten niemals dazu verwendet werden um das Verhalten eines Objekts zu beeinflussen!
Das *Verhalten* muss sich stets aus der Kombination von Objektattributen und Methoden ergeben.
```