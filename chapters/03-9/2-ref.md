(sec-cpython-ref)=
# Referenzimplementierung

CPython ist eine sog. *Referenzimplementierung* von ``Python`` und wurde vom Erfinder der Sprache selbst (Guido van Rossum) initiiert. 

```{admonition} Referenzimplementierung
:name: def-reference-implementation
:class: definition

Als *Referenzimplementierung* bezeichnen wir eine *Implementierung* die einen Standard oder De-facto-Standard darstellt und damit für alle anderen *Implementierungen* vorgibt, wie sich diese zu verhalten haben und welche Standards diese erfüllen sollten.

```

Wie der Name andeutet, ist CPython in ``C`` (und ``Python`` selbst) geschrieben.
Das mag verwirrend klingen.

>Wenn eine Sprache wie ``Python`` eine Implementierung wie *CPython* benötigt, die wiederum in einer anderen Sprache wie ``C`` geschrieben ist, wie kann es dann jemals ausführbaren Code geben?

Wie im Abschnitt [Interpretation](sec-interpretation) beschrieben, kann eine Interpretation (CPython-[Interpreter](def-interpreter)) den Repräsentaten (``Python``-Code) in dessen Bedeutung (*Maschinencode*) umwandeln.
Die Interpretation kann dabei sogar aus einer Komposition von mehreren Interpretationen bestehen.
Die Realisierung der Intreptation ist im Fall von CPython ein [Interpreter](def-interpreter) (ein Programm) der wiederum in der Programmiersprache ``C`` geschrieben ist.

Die [(C)Python Standard Library](https://docs.python.org/3/library/) besteht aus den built-in Modulen die in ``C`` geschrieben sind und Modulen, die wiederum in ``Python`` selbst geschrieben sind.
Der ``C``-Code liegt in übersetzer Form (*Maschinencode*) vor.