(sec-working-with-data-types)=
# Pythons Datentypen

Beginnen wir mit der Praxis und sehen uns an welche Datentypen uns ``Python`` bietet und was wir mit diesen anfangen können.
Die von ``Python`` vorab definierten Datentypen nennt man *built-in Datentypen*.
Wir werden in diesem Abschnitt nicht alle *built-in Datentypen* besprechen, sondern jene mit denen Sie die meiste Zeit zu tun haben.
Eine vollständige Liste der Datentypen finden Sie im Abschnitt [Built-in Datentypen](sec-built-in-data-types).

Wir können die *built-in Datentypen* in weitere zwei Kategorien zerteilen:

1. *Atomare Datentypen*, also Datentypen die sich auf einen einzelnen Wert beziehen und
2. *Zusammengesetzt Datentypen*

Haben Sie bereits Programmiererfahrung, so werden Sie *atomare Datentypen* als *primitive Datentypen* wahrnehmen, doch streng genommen gibt es in ``Python`` keine primitiven Datentypen.
Dennoch verhalten sich *atomare Datentypen* ähnlich wie *primitive Datentypen*.

*Atomare Datentypen* sind: Ganze Zahlen ``int``, Wahrheitswerte ``bool`` und Fließkommazahlen.
*Zusammengesetzte Datentypen* sind: Zeichenketten ``str``, Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict``.

Den Datentyp einer Variable oder eines Wertes erfragen Sie mit der *built-in* Funktion ``type``.

x = 5
text = 'Hello'
print(type(x))
print(type(text))
print(type(3.1))

## Atomare Datentypen 

Eine wesentlich Eigenschaft von *atomaren Datentypen* ist, dass der **Wert** einer Variable eines *atomaren Datentyps* **unverändert** im Speicher liegt.
Wird der **Wert** von keiner Variablen mehr adressiert, wird er zwar gelöscht, um den Speicher wieder freizugeben, doch kann er nicht verändert werden solange eine Variable den Wert noch adressiert.

Wir haben dieses Phänomen bereits im Abschnitt [Variablen](sec-variables) beobachtet.
Wir hatten festgehalten, dass Veränderungen der einen Variablen keinen Effekt auf die **Adresse** bzw. *Identität* ``id`` anderer Variablen haben.
Für *atomare Datentypen* gilt noch mehr.
Ändern wir den **Wert** einer Variable vom Typ ``int``, ``bool`` oder ``float``, so kann diese Änderung nicht den **Wert** einer anderen Variablen verändern:

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

*Atomare Datentypen* bestehen nur aus einem *atomaren* **Wert**, den wir nicht weiter zerteilen können.

## Zusammengesetzte Datentypen

*Zusammengesetzte Datentypen* oder auch *Datenstrukturen* bestehen hingegen aus mehreren Werten.
Sie strukturieren diese Werte.

Anders als bei *atomaren Datentypen* lässt sich der Wert einer Datenstruktur verändern.
Damit ist gemeint, dass es sich verändern lässt, was die Datenstruktur enthält.

Nehmen wir einmal an, eine Datenstruktur enthält ausschließlich ganze Zahlen ``int``.
Verändern wir nun eine dieser Zahlen, so wird der **Wert** im Speicher, der diese Zahl repräsentiert, nicht verändert -- es ist ja ein *atomarer Datentyp*!
**Aber** es wird ein neuer Wert in den Speicher geschrieben und die Datenstruktur wird so manipuliert, dass Sie nun auf diesen neuen Wert zeigt.

Im Abschnitt [Wie funktioniert eine Liste](sec-list-and-memory) sehen wir uns an was genau im Speicher vor sich geht, wenn wir mit Listen arbeiten.