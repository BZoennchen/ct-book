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

(sec-oop)=
# Objektorientierte Programmierung

Um zu verstehen was die *objektorientierte Programmierung* ist, ist es äußerst hilfreich sich klar zu machen, was die *objekt-orientierte Programmierung* nicht ist, beziehungsweise woraus die *objektorientierte Programmierung* entstanden ist.

Die *objectorientierte Programmierung* ist ein Programmierparadigma, welches sich in den letzten 15 Jahren in vielen Bereichen der Softwareentwicklung durchgesetzt hat.
Bis hierhin haben wir uns auf die *prozedurale Programmierung* beschränkt.
Auch vor der Einführung der *objekt-orientierte Programmierung* war die *prozedurale Programmierung*, die dominierende Art und Weise zu programmieren.

Im *prozeduralen Programmierparadigma* schreiben wir Funktionen, die bestimmte Daten verarbeiten.
Jede Funktion steht für sich 'separat' neben den Daten und erhält (sofern sie keine globalen Variablen verwendet) alle Daten als Argumente.

Zum Beispiel können wir als Daten ein Rechteck als Wörterbuch definieren:

```{code-cell} python3
rect1 = dict(x=10, y=10, width=100, height=20)
rect2 = dict(x=-10, y=-10, width=100, height=30)
```

Wenn wir nun eine Funktion schreiben wollen, welche tested ob ein Punkt sich in einem Rechteck befindet, würden wir das in der *prozeduralen Programmierung* wie folgt machen:

```{code-cell} python3
def contains(rect, point):
  if point[0] < rect['x'] or point[1] < rect['y']:
    return False
  if point[0] > rect['x'] + rect['width'] or point[1] > rect['y'] + rect['height']:
    return False
  return True

print(contains(rect1, (15, 17)))
print(contains(rect2, (315, 317)))
```

Wir könnten uns weitere Funktionen überlegen, die wir auf ein Rechteck anwenden wollen.
Zum Beispiel eine Funktion um das Rechteck zu verschieben:

```{code-cell} python3
def translate(rect, delta):
  return dict(x=rect['x']+delta[0], y=rect['y']+delta[1], width=rect['width'], height=rect['height'])

print(translate(rect1, (10,-5)))
print(rect1)
```

Da wir in der *prozeduralen Programmierung* bevorzugt [reine Funktionen](sec-purity) verwenden, legt ``translate`` eine Kopie an und liefert diese verschobene Kopie zurück.

```{admonition} Prozedurale Programmierung
:class: definition
:name: def-procedural-programming
Die *prozedurale Programmierung* ist ein *Programmierparadigma*, welches auf *Funktionen / Prozeduren* aufgebaut ist.
Sie gilt als Erweiterung des *imperativen Paradigmas*.
```

Im Gegensatz dazu bündeln wir in der *objektorientierte Programmierung* **Daten** und deren **Operanden**.
Das heißt, Funktionen welche wir auf die Daten anwenden wollen und die Daten selbst werden in ein sog. *Objekt* gepackt.

*Objekte* sind Daten angereichert mit Funktionen, welche wir als *Methoden des Objekts* bezeichnen.
Objekte sind zugleich Werte bzw. Instanzen von einem bestimmten *benutzerdefinierten zusammengesetzten Datentyp*, die wir als *Klasse* bezeichnen.

Lassen Sie uns zuerst einen *zusammengesetzten Datentyp* ``Rectangle`` erzeugen, welcher zugleich die *Methoden* ``contains`` und ``translate`` enthält.

```{code-cell} python3
class Rectangle():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def __str__(self):
    return f'x={self.x}, y={self.y}, width={self.width}, height={self.height}'

  def contains(self, point):
    if point[0] < self.x or point[1] < self.y:
      return False
    if point[0] > self.x + self.width or point[1] > self.y + self.height:
      return False
    return True

  def translate(self, point):
    self.x += point[0]
    self.y += point[1]
```

In dieser Version verändert ``translate(point)`` das *Objekt* anstatt eine Kopie zurückzuliefern.

```{code-cell} python3
rect1 = Rectangle(x=10, y=10, width=100, height=20)
rect2 = Rectangle(-10, -10, 100, 30)

print(rect1.contains((15, 17)))
print(rect2.contains((315, 317)))
print(rect1.translate((10,-5)))
print(rect1)
```

Die Ausgabe der vorletzten Zeile zeigt, dass ``translate`` keinen Rückgabewert hat sondern das *Objekt* ``rect1`` verändert.
Die Ausgabe des Objekts ist jene die wir in der Methode ``__str__()`` definiert haben.
Die Klasse *erbt* die ``__str__()`` Methode von der Klasse ``object`` und diese wird von der Funktion ``print()`` genutzt.
Wir *überschreiben* die Standarddefinition von ``__str__()`` um eine schönere Ausgabe zu erzielen.
Die ``__init__()`` Methode initialisiert das Objekt mit seinen Daten.
Diese Methode wird aufgerufen sobald wir das Objekt durch ``Rectangle(x=10, y=10, width=100, height=20)`` erzeugt haben.

```{admonition} Objektorientierte Programmierung (OOP)
:class: definition
:name: def-oop
Die *objektorientierte Programmierung* ist ein Programmierparadigma, welches auf *Objekten* aufgebaut ist.
Diese *Objekte* beinhalten und kapseln *Daten* und deren dazugehörige *Methoden*.
```