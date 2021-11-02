# Ganze Zahlen - int

Ganze Zahlen (engl. [Integer](https://docs.python.org/3/library/functions.html#int)) ``int`` ist ein *atomarer Datentyp* und verhält sich so wie wir es erwarten.

Falls Sie bereits Programmierkenntnisse besitzen, so gibt es in ``Python`` jedoch eine Besonderheit: Ganze Zahlen können nicht überlaufen.
Anders als Fließkommazahlen benötigen ganze Zahlen ``int`` in ``Python`` eine variable Anzahl an Bits.
Anders ausgedrückt: Nicht jede Zahl benötigt die gleiche Anzahl an Bits im Speicher!
Solange Ihr Speicher nicht komplett belegt ist, können Sie in ``Python`` somit mit sehr großen ganzen Zahlen rechnen.

large_number = 10**100
print(type(large_number))
print(large_number)

Da wir bei mathematischen Operationen wie ``+``, ``-``, ``*``, ``/``, ``//`` und ``**`` ganze Zahlen ``int`` und Fließkommazahlen ``float`` vermischen können, müssen wir darauf achten welcher Datentyp am Ende herauskommt.
Sobald eine Fließkommazahl teil der Berechnung ist, ist das Ergebnis vom Typ ``float``.

x = 3 * 1.0     # int * float -> float   
print(type(x))
print(x)

large_number = 10.0**100
print(type(large_number))
print(large_number)

Auch bei der ganzzahligen Division ``//`` erhalten wir als Datentyp eine Fließkommazahl sofern eine Fließkommazahl bei der Operation teilnimmt:

x = 3.0 // 2     # float // int -> float   
print(type(x))
print(x)

x = 3 // 2.0     # int // float -> float   
print(type(x))
print(x)

x = 3 // 2     # int // int -> int   
print(type(x))
print(x)