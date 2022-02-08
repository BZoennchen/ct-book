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

(sec-working-with-data-types)=
# Pythons Datentypen

Beginnen wir mit der Praxis und sehen uns an welche Datentypen uns ``Python`` bietet und was wir mit diesen anfangen können.

```{admonition} Built-in Datentypen
:name: def-built-in-data-types
:class: python

Die von ``Python`` vorab definierten Datentypen nennt man *built-in Datentypen*.
```

Wir werden in diesem Kapitel nicht alle *built-in Datentypen* besprechen, sondern jene mit denen Sie die meiste Zeit zu tun haben.
Eine vollständige Liste der Datentypen finden Sie im Abschnitt [Built-in Datentypen](sec-built-in-data-types).

Wir können die *built-in Datentypen* in weitere zwei Kategorien zerteilen:

1. *Atomare Datentypen*, also Datentypen die sich auf einen einzelnen Wert beziehen und
2. *Zusammengesetzt Datentypen*

Haben Sie bereits Programmiererfahrung, so werden Sie *atomare Datentypen* als *primitive Datentypen* wahrnehmen, doch streng genommen gibt es in ``Python`` keine primitiven Datentypen.
Dennoch verhalten sich *atomare Datentypen* ähnlich wie *primitive Datentypen*.

```{admonition} Python und primitive Datentypen
:name: remark-primitive-data-types-in-python
:class: remark

Es gibt in ``Python`` keine primitiven Datentypen.
```

Der Wert eines *atomaren Datentyps* lässt sich nicht sinnvoll weiter in seine Einzelteile zersplittern.

*Zusammengesetzte Datentypen* sind zum Beispiel: Zeichenketten ``str``, Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict``.

Den Datentyp einer Variable oder eines Wertes erfragen Sie mit der *built-in* Funktion ``type``.

```{code-cell} python3
x = 5
text = 'Hello'
print(type(x))
print(type(text))
print(type(3.1))
```

(sec-atom-data-type)=
## Atomare Datentypen 

Eine wesentlich Eigenschaft von *atomaren Datentypen* ist die Unveränderbarkeit ihres des Werts.
Der **Wert** einer Variable eines *atomaren Datentyps* liegt **unverändert** im Speicher.

```{admonition} Atomare Datentypen
:name: def-atomare-data-types
:class: python

*Datentypen* welche sich auf einen einzelnen Wert beziehen, d.h., ganze Zahlen ``int``, Wahrheitswerte ``bool`` und Gleitkommazahlen ``float`` sind *atomare Datentypen*.
```

Wird der **Wert** durch keiner Variablen adressiert, wird er (vom [Garbage Collector](def-garbage-collector)) zwar gelöscht.
In anderen Worten, wird der Speicher von Ihrem laufenden Programm nicht mehr benötigt, kümmert sich der Garbage Collector, den von Ihnen belegten Speicher wieder freizugeben.
Der Speicher der durch einen Wert eines *atomaren Datentyp* belegt ist kann also durchaus verändert werden, allerdings nur dann wenn er nicht mehr gebraucht wird.

```{admonition} Unveränderliche atomare Datentypen
:class: attention
Atomare Datentypen sind *unveränderlich*.
```

Wir haben dieses Phänomen bereits im Abschnitt [Variablen](sec-variables) beobachtet.
Wir hatten festgehalten, dass Veränderungen der einen Variablen keinen Effekt auf die **Adresse** bzw. *Identität* ``id`` anderer Variablen haben.
Für *atomare Datentypen* gilt noch mehr: 

```{admonition} Unveränderliche atomare Datentypen
:class: remark
Ändern wir den **Wert** einer Variable vom Typ ``int``, ``bool`` oder ``float``, so kann diese Änderung nicht den **Wert** einer anderen Variablen verändern.
```

Folgendes Beispiel illustriert diese Tatsache.

```{code-cell} python3
x = 12313
z = x
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
print('change value of x')
x = 11341
print(f'value of x = {x}')
print(f'id of x = {id(x)}')

print(f'value of z = {z}')
print(f'id of z = {id(z)}')
```

(sec-datastructures)=
## Zusammengesetzte Datentypen

*Zusammengesetzte Datentypen* oder auch *Datenstrukturen* bestehen hingegen aus mehreren Werten.
Sie strukturieren diese Werte.

```{admonition} Zusammengesetzt Datentypen 
:name: def-data-structures
:class: python

Datentypen welche Sammlungen von Werten modellieren, bezeichnen wir als *zusammengesetzte Datentypen* oder *Datenstrukturen*.
```

Anders als bei *atomaren Datentypen* lässt sich der **Wert** einer Datenstruktur verändern.
D.h., der Inhalt der Datenstruktur kann in der Regel verändert werden.

Sie können sich eine Datenstruktur wie ein Behältnis aus der Realwelt vorstellen.
Einen Rucksack können wir mit Dingen befüllen, die wir möglicherweise nicht verändern können.
Der Rucksack selbst, lässt sich demnach sehr leicht verändern.
Wir müssen lediglich Elemente hinauswerfen oder einfügen.

Nehmen wir einmal an, eine Datenstruktur enthält ausschließlich ganze Zahlen ``int``.
Verändern wir nun eine dieser Zahlen, so wird der **Wert** im Speicher, der diese Zahl repräsentiert, nicht verändert -- es ist ja ein *atomarer Datentyp*!
**Aber** es wird ein neuer Wert in den Speicher geschrieben und die Datenstruktur wird so manipuliert, dass einer ihrer Einträge nun auf diesen neuen Wert zeigt.

Im Abschnitt [Listen und der Speicher](sec-list-and-memory) sehen wir uns an was genau im Speicher vor sich geht, wenn wir mit Listen arbeiten.
Dies kann auf andere *Datenstrukturen* übertragen werden.