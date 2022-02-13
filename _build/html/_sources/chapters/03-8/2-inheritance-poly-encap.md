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

(sec-inheritance)=
# Vererbung, Kapselung und Polymorphie

*Objektorientierte Programmierung OOP* ist ein mächtiges Modellierungswerkzeug bei der wir Daten und Methoden in eine zusammenhängende Struktur bringen.
Es deckt sich mit der 'natürlichen' denkweise von uns Menschen.
Wir denken gerne in Objekten wie Bäume, Häuser, Personen, Rechtecken, und so weiter und so fort.
Deshalb kann die OOP dabei helfen die Komplexität einer Software besser zu begreifen.
Dazu ist es notwendig, dass alle beteiligten Entwickler\*innen dem OOP-Paradigma folgen und die gleiche Sprache sprechen.

Neben dem Strukturieren der Programmierlogik durch Objekte bietet die OOP weitere drei wichtige Konzepte an:

1. **Vererbung**
2. **Kapselung**
3. **Polymorphie**

## Vererbung

Vererbung ist eine Möglichkeit Funktionalität und Attribute einer Eltern-Klasse in eine Kind-Klasse zu übernehmen -- zu *vererben*.
Wir sagen, die Kind-Klasse *erbt* von der *Eltern-Klasse*.
Dabei geht es um Ähnlichkeiten.

Zum Beispiel könnte es Sinn machen eine Eltern-Klasse ``Person`` zu schreiben und unsere Kind-Klasse ``Student`` von dieser *erben* zu lassen.
Ein ``Student`` ist eine *spezielle* ``Person``.
Wir könnten eine weitere *spezielle* ``Person``, beispielsweise den ``Lecturer`` definieren.

Unsere Eltern-Klasse oder auch Basis-Klasse ``Person`` ist eine **Abstraktion** von ``Student`` und ``Lecturer``:

```{code-cell} python3
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'name: {self.name}, age: {self.age}'

    def say_name(self):
        print(f'My name is {self.name}.')

    def report(self):
        self.say_name()
        print(f'My age is: {self.age}')
```

Die beiden Kind-Klassen *erben* von ``Person`` und sind weniger abstrakt bzw. konkretere Dinge oder Subjekte:

```{code-cell} python3
class Student(Person):
    def __init__(self, sid, name, age):
        super().__init__(name, age)
        self.sid = sid
        self.type = 'learning'

    def __str__(self):
        return f'{super().__str__()}, sid: {self.sid}'

    def report(self, score):
        super().report()
        print(f'My id is: {self.sid}')
        print(f'My score is: {score}')
        print(f'I am a student.')

class Lecturer(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def __str__(self):
        return f'{self.title} {self.name}'
```

``Student`` und ``Lecturer`` **erben** von ``Person``, d.h. beide erhalten die *Attribute* ``name`` und ``age`` sowie alle Methoden, die in ``Person`` definiert wurden.
Beide Kind-Klassen werden um die Attribute ``name`` und ``age`` **erweitert**.
Diese Attribute können in den Kind-Klassen durch

```python
self.name
self.age
```

angesprochen werden, was wir in ``__str__(self)`` von ``Lecturer`` demonstrieren.

```{admonition} Vererbte Objektattribute
:class: remark
:name: remark-inherited-attributes
Attribute eines Objekts egal ob *vererbt* oder nicht werden **immer** durch ``self.attributename`` und **niemals** über ``super().attributename`` angesprochen.
```

``Student`` **überschreibt** die Methode ``report`` der Klasse ``Person``, wohingegen ``Lecturer`` diese unberührt lässt.
Damit wird ``Lecturer`` um die Methode ``report`` der Klasse ``Person`` **erweitert**.

Um zwischen diesen beiden gleichnamigen Methoden ``report`` der Klasse ``Person`` und ``Student`` zu unterscheiden, verwenden wir einmal ``self`` und einmal ``super()``.
Mit ``super()`` greifen wir auf die Methoden der Eltern-Klasse zu.
Anstelle von ``super()`` können wir die Eltern-Klasse auch explizit angeben, müssen dann jedoch das ``self`` übergeben.
Aus

```python
...
super().__init__(name, age)
...
```

wird 

```python
...
Person.__init__(self, name, age)
...
```

Lassen Sie uns ein Objekt von jeder Klasse erzeugen und die Methoden testen:

```{code-cell} python3
person = Person('Bene', 25)
print(person)
person.report()
```

```{code-cell} python3
student = Student('3131', 'Anna', 22)
print(student)
student.report(413)
```

```{code-cell} python3
lecturer = Lecturer('Huber', 45, 'Prof.')
print(lecturer)
lecturer.report()
```

``Lecturer`` definiert keine Methode ``report``, doch da ``Person`` eine solche Methode enthält mit diesem Namen definiert, existiert diese auch in ``Lecturer``.
Der folgende Code hätte die gleiche Wirkung:

```{code-cell} python3
class Lecturer(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def __str__(self):
        return f'{super().__str__()}, title: {self.title}'

    def report(self, score):
        super().report()
```

Es wird demnach die ``report`` Methode von ``Person`` aufgerufen!
Alles in allem sparen wir Codezeilen bzw. doppelten Code.
Es ist, zum Beispiel, möglich den Code aus ``Person.__init__()`` zu kopieren und die gesamte Initialisierung zu überschreiben:

```python
class Lecturer(Person):
    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.sid = sid
        self.title = title

    ...
```

Doch wenn wir die Initialisierung einer Person ``Person.__init__()`` ändern und sich diese Änderung auch auf alle Kinder auswirken soll, so müssten wir ``Lecturer.__init__()`` entsprechend anpassen.

```{admonition} Vererbung aber wann?
:class: attention
:name: attention-when-inheritance
Gehen Sie besser sparsam mit der Vererbung um. 
Ruft die ``__init__``-Methode nicht ihre Eltern-``__init__`` auf, so ist die Vererbung an dieser Stelle wahrscheinlich nicht die richtige Wahl der Modellierung.
```

## Vererbung und Komposition

Vererbung ist ein mächtiges Werkzeug, doch sollten Sie damit bedacht und sparsam umgehen.
Tiefe Vererbungshierarchien tendieren dazu unverständlich zu werden.
Die Mehrfachvererbung, welche wir in diesem Kurs nicht besprechen werden, ist in ``Python`` möglich, doch in den allermeisten Fällen nicht sinnvoll.

```{admonition} Vererbung aber wann?
:class: remark
:name: remark-when-inheritance
Ob eine Vererbung sinnvoll ist entscheidet sich durch die Datenstrukturen die Sie bauen wollen und nicht unbedingt durch die Realgegenstände, die diese Strukturen modellieren.
```

So könnte man schnell zu dem Schluss kommen, dass ein Quadrat ein spezielles Rechteck ist und dass es somit eine gute Idee ist Quadrat von Rechteck erben zu lassen.
Doch besitzt ein Quadrat lediglich eine Position und eine Breite wohingegen ein Rechteck noch eine zusätzliche Höhe besitzt.
Vererben wir Rechteck an Quadrat erhält es ein überflüssiges Attribut.
Das ist erst einmal nicht tragisch, wenn wir dem Rechteck jedoch eine Methode verpassen mit dem es seine Höhe verändern kann, geraten wir in Probleme.
Denn damit kann ein Rechteck etwas, was ein Quadrat nicht kann -- die Höhe nicht aber die Breite verändern.
Die Datenstruktur Rechteck ist nicht länger einer Abstraktion von Quadrat.

Oftmals ist es besser die *Komposition* der *Vererbung* vorzuziehen.
*Komposition* bedeutet, dass wir eine Klasse definieren, die als Attribute weitere komplexere Klassen beinhaltet.
So könnten wir uns als Klasse ein Auto vorstellen, welches aus den Attributen Rad, Motor, usw. besteht. 

```python
class Car():
    def __init__(self, wheel, engine):
        self.wheel = wheel
        self.engine = engine
        ...

    ...
```

Rad und Motor könnten Klassen sein, die mit Funktionalität ausgestattet sind.
Diese Funktionalität können wir dann in der Klasse ``Car`` nutzten.
So gelangt Funktionalität nicht über Vererbung sondern durch Komposition in die Klasse und somit in seine Objekte.

## Kapselung

*Kapselung* ist ein weiteres fundamentales, wenn nicht sogar DAS fundamentalste aller Konzept der OOP.
Dabei wird der gesamte, sich ändernden Zustand eines Programms in kleine Zuständigkeiten aka Objekte aufgeteilt.

Jedes Objekt kennt sein Innenleben und schützt dieses vor dem Zugriff von außen.
Nach außen bietet das Objekt eine öffentliche Schnittstelle.
Nur über diese ist es möglich das Innenleben des Objekts zu verändern.
Demnach verändert das Objekt sein Innenleben selbst indem es durch seine öffentlichen Methoden dazu aufgefordert wird.

Die Einschränkung des Zugriffs auf bestimmte *Methoden* und *Attribute* eines *Objekts* ist ein wesentlicher Aspekt und wird durch die *Klasse* eines *Objekts* definiert.
Die Idee dahinter ist es Komplexität vor dem Benutzer der Klasse zu verbergen und das 'Innenleben' eines Objekts vor ungewollter Veränderung zu schützten.
Der Benutzer muss lediglich wissen **WAS** eine Methode bewirkt, **WIE** dies erreicht wird bleibt verborgen und gehört zur Zuständigkeit des *Objekts*.

Angenommen wir konstruieren eine Klasse ``Circle`` mit den Attributen ``radius``, ``center`` und ``diameter``.
Wir fügen noch eine Methode ``dist`` und ``contains`` hinzu.
``dist`` berechnet die Distanz zwischen dem Kreis und einem Punkt.
Die Distanz ist negativ wenn sich der Punkt innerhalb des Kreises befindet.
``contains`` prüft ob sich ein Punkt innerhalb des Kreises befindet.

```{code-cell} python3
class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.__radius = radius
        self.__diameter = 2*radius

    def __str__(self):
        return f'center: {self.center}, radius: {self.__radius}, diameter: {self.__diameter}'

    def contains(self, point):
        return self.dist(point) <= 0
        
    def dist(point):
        dx = self.center[0] - point[0]
        dy = self.center[1] - point[1]
        return (dx*dx + dy*dy)**0.5 - radius

    def set_radius(self, radius):
        self.__radius = radius
        self.__diameter = 2*radius

    def get_radius(self):
        return self.__radius

    def get_diameter(self):
        return self.__diameter
```

Zusätzlich bieten wir eine Methode ``set_radius`` an, welche den ``radius`` des Kreises ändert.
Da der Durchmesser ``diameter`` vom Radius abhängt müssen wir, wann immer wir den Radius anpassen, auch den Durchmesser anpassen.
Deshalb wollen wir dem Benutzer nicht erlauben, den Durchmesser selbst zu ändern.
Damit der Benutzer nicht mehr direkt auf die Attribute ``radius`` und ``diamant`` zugreifen kann, fügen wir vor deren Namen zwei Unterstriche ``__`` an.
Dadurch werden diese Attribute *privat*.

```{code-cell} python3
circle = Circle((0,0), 3)
print(circle)
```

Versuchen wir auf die geschützten Attribute zuzugreifen, erhalten wir einen Fehler:

```{code-cell} python3
---
tags: [raises-exception]
---

circle.center = (6, 6)
print(circle)
print(circle.__radius)
```

Zwar können wir ``center`` verändern, da dies nicht geschützt ist, doch ``__radius`` lässt sich nicht von Außen verändern!
Wir bezeichnen dieses Attribut als *privates* Attribut der Klasse.

In der Klasse finden sich die Methoden ``get_radius`` und ``set_radius`` über die wir den Radius wiederum verändern und auf den Wert des Radius zugreifen können:

```{code-cell} python3
circle.set_radius(10)
print(circle)
print(circle.get_radius())
```

Doch dadurch dass wir eine Methode für die Veränderung verwenden, können wir sicherstellen, dass der Durchmesser ebenfalls korrekt abgeändert wird.

Durch die gleiche Schreibweise können wir auch *Methoden* in private Methoden umwandeln, sodass diese nur innerhalb der Klasse sichtbar und aufrufbar sind.
Dies kann sinnvoll für Hilfsmethoden sein, die als solches, getrennt vom Aufruf anderer Methoden, nicht aufgerufen werden sollten.

Das obige Beispiel ist etwas künstlich, denn eigentlich macht das Attribut ``diameter`` an dieser Stelle keinen rechten Sinn.
Eine bessere Variante bietet folgender Code:

```{code-cell} python3
class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.__radius = radius

    def __str__(self):
        return f'center: {self.center}, radius: {self.get_radius()}, diameter: {self.get_diameter()}'

    def contains(self, point):
        return self.dist(point) <= 0
        
    def dist(point):
        dx = self.center[0] - point[0]
        dy = self.center[1] - point[1]
        return (dx*dx + dy*dy)**0.5 - radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_diameter(self):
        return self.__radius*2
```

## Polymorphie

```{admonition} Polymorphie
:class: definition
:name: def-polymorph
*Polymorphie* ist ein Konzept, welches ermöglicht, dass eine Operation abhängig von ihrer Verwendung Werte/Objekte unterschiedlichen Datentyps verarbeiten kann.
```

Wir haben schon einige Beispiele gesehen in der Polymorphie zum Einsatz kam.
Der ``+``-Operator angewendet auf ganzen Zahlen und Zeichenketten wäre ein solches Beispiel:

```{code-cell} python3
print(3 + 6)
print('3' + '6')
```

Die Schnittstelle ist dabei der ``+``-Operator und die unterschiedlichen Objekte sind einmal vom Typ ``int`` und einmal vom Typ ``str``.

Aber auch unser Beispiel mit den Klassen ``Person``, ``Student``, ``Lecturer`` bietet Polymorphie.
Die gemeinsame Schnittstelle ist die Basisklasse ``Person``.
Ein ``Student`` und ``Lecturer`` sind auch jeweils eine ``Person`` und bieten uns alle Attribute und Methoden die auch eine ``Person`` bietet.
Deren konkrete Implementierung kann sich jedoch unterscheiden.

Wir könnten nun eine Funktion schreiben, die eine ``Person`` erwartet.
Da diese Funktion mit ``Person`` als Typ umgehen kann, kann sie auch mit den Typen ``Lecturer`` und ``Student`` umgehen.

```{code-cell} python3
def printName(person):
    print(person.name)

student = Student('3131', 'Anna', 22)
lecturer = Lecturer('Huber', 45, 'Prof.')

printName(student)
printName(lecturer)
```

An dieser Stelle wissen wir nicht genau welchen Typ die Variable ``person`` hat.
Wir wissen allerdings, dass was auch immer der Typ ist, dessen Basisklasse ``Person`` ist und deshalb ein Attribut ``name`` vorhanden sein muss.

Wundert es uns nicht, dass die Funktion ``print`` jeden Wert von jedwedem Datentyp ausgeben kann?
Wie funktioniert das?
Die Antwort lautet: Polymorphie!
``print(ob)`` geht davon aus, dass das Objekt ``ob`` eine Methode ``__str__()`` besitzt und diese eine Zeichenkette zurückliefert.
Das ist der Grund weshalb auch unsere Objekte in schöner Art und Weise ausgegeben werden!
Wir haben diese Methode ebenfalls definiert.

Funktionen und Methoden, welche andere Objekte verarbeiten erwarten von diesen ein bestimmte Menge an Methoden und Attribute.
Diese Menge bezeichnen wir als Schnittstelle (engl. Interface).

Selbst unsere ``for``-Schleife

```python
for i in sequenz:
    # do something
```

erwartet von der Variablen ``sequenz``, dass es sich um eine ``Sequenz`` handelt.
Das heißt um ein *Objekt* das wir iterieren können.
Es ist der Schleife egal ob es eine Liste, ein Bereich, ein Tupel oder sonst etwas iterierbares ist.
Es muss lediglich die Schnittstelle ``Iterable`` erfüllen.

Es sei angemerkt, dass *Polymorphie* ein Konzept ist, was über die objektorientierte Programmierung hinausreicht.
Auch in der prozeduralen wie auch funktionalen Programmierung nutzten wir die *Polymorphie*.