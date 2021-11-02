# Wahrheitswerte - bool

Ein Wahrheitswert ([Boolean](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)) ``bool`` kann, genau wie ein [Bit](def-bit), einen von zwei Wahrheitswerten ``True`` (1) oder ``False`` (0) annehmen.
``True`` bedeutet wahr und ``False`` falsch.
``True`` oder ``False`` verwenden wir sehr selten explizit.
Viel häufiger wird ein logischer Ausdruck, nach *Auswertung* entweder ``True`` oder ``False`` ist.

x = 9
is_lesser_than_10 = x < 10
print(is_lesser_than_10)

In diesem Beispiel verwenden wir einen [Vergleichsoperator](sec-python-operator-compare), der den Ausdruck $x < 10$ zu ``True`` auswertet, da $x = 9 < 10$ gilt.
*Boolsche* bzw. *logische Ausdrücke* lassen sich durch [logische Operatoren](sec-logic-expressions) verknüpfen.

*Boolsche Ausdrücke* und damit Wahrheitswerte ``bool`` benötigen wir für die Steuerung unseres Programmablaufs.
*Kontrollstrukturen* führen, je nach Auswertung eines *boolschen Ausdrucks*, unterschiedliche Code-Teile aus.

for x in range(11):
  if x < 10:      # is True if and only if x < 10
    print(f'{x} is less than 10')
  else:
    print(f'{x} not is less than 10')