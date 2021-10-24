(sec-primitive-data-types-in-python)=
# Primitive Datentypen in Python?

Jetzt kommen wir zu einer Besonderheit in ``Python``, welche Sie als Anfänger erst einmal ignorieren können.
Dennoch möchten wir Sie Ihnen nicht vorenthalten und auch kein Halbwissen vermitteln!

Sie vermuten wohl zurecht, dass ``byte``, ``int``, ``long``, ``float``, ``bool`` [primitive Datentypen](def-primitive-datatypes) sind und Sie lägen bei vielen anderen Programmiersprachen richtig, doch in ``Python`` gibt es gar keine primitiven Datentypen.
Das ist für Anfänger verwirrend!
Wie kann es keine primitive Datentypen geben?
Irgendwann muss sich doch ein Datentyp nicht mehr weiter zerlegen lassen?
Und weshalb ist eine ganze Zahl ``int`` kein *primitiver Datentyp*?

```{admonition} Datentypen in Python
:name: alert-datatypes-python
:class: warning
Es gibt in ``Python`` keine primitiven Datentypen!
```

``Python`` kapselt die primitiven Datentypen für uns Programmierer*innen.
Zu unserem eigenen Schutz können wir auf diese nicht direkt zugreifen und mit ihnen nicht direkt arbeiten.
Hinter dem Datentyp ``int`` verbirgt sich ein zusammengesetzter Datentyp, der es uns leichter macht mit ganzen Zahlen umzugehen.
Implementiert ist dieser Datentyp in der Programmiersprache ``C++`` und ``Python`` ruft am Ende des Tages ``C++``-Code auf.
Die Implementierung von ``int`` findet sich in den folgenden Dateien (**bitte lassen Sie sich davon nicht abschrecken, Sie müssen diesen Code nicht verstehen!**)

+ [longobject.c](https://github.com/python/cpython/blob/main/Objects/longobject.c)
+ [longintrepr.h](https://github.com/python/cpython/blob/main/Include/longintrepr.h)
+ [longobject.h](https://github.com/python/cpython/blob/main/Include/longobject.h)

In ``Python`` benötigt eine ganze Zahl ``int`` nicht immer den gleichen Speicherbereich!
Deshalb ist es, anders als in vielen anderen Sprachen, in ``Python`` möglich mit sehr großen ganzen Zahlen zu rechnen.
Wäre ``int`` ein primitiver Datentyp, wie etwa in ``Java``, ``C/C++``, so würde ein ``int`` Wert immer gleich viel Speicherplatz belegen.
Ob im Speicher eine ``5`` oder eine ``1000`` steht ist für den Speicherplatz den diese Werte verbrauchen egal.


Wie alle Datentypen in ``Python`` ist auch ``str`` ein zusammengesetzter Datentyp.
Anders als in vielen anderen Sprachen gibt es in ``Python`` keinen Datentyp für ein einzelnes Zeichen ``char``.
Ein einzelnes Zeichen ist in ``Python`` eine Zeichenkette der Länge 1.
Dennoch ist ``str`` kein primitiver Datentyp.