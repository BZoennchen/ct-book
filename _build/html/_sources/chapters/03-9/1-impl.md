(sec-cpython-impl)=
# Implementierungen

Welche Befehle Ihre Maschine genau ausführt, hängt mit den Interpretationen zusammen, die Ihr Programm in Maschinencode überführen.
Die Sprache selbst legt zwar die Semantik fest, jedoch nur im Kontext der Sprache selbst.
Durch welche Maschinenbefehle eine Addition oder Multiplikation auf Ihrer konkreten Maschine realisiert wird, legt die Sprache ``Python`` nicht fest.
Das ist die Aufgabe des Zusammenschlusses an Interpretationen, die wir als *Implementierung* von ``Python`` bezeichnen.

```{admonition} Python Implementierung
:name: def-python-implementation
:class: definition

Als ``Python``-*Implementierung* bezeichnen wir das was die Semantik der Sprache auf einer Maschine realisiert. 

```

Streng genommen gibt es unterschiedliche Implementierungen von ``Python``.
Zum Beispiel:

+ [CPython](https://github.com/python/cpython) ([Referenzimplementierung](def-reference-implementation) von ``Python``)
+ [IronPython](https://ironpython.net/) (``Python`` realisiert durch die .NET-Platform)
+ [Jython](https://www.jython.org/) (``Python`` realisiert durch die Java Virtual Maschine (JVM))
+ [PyPy](https://www.pypy.org/) (Eine performantere ``Python``-Implementierung mit einem Just-In-Time-[Übersetzer](def-compiler) (JIT), wird allerdings von nur wenigen Modulen unterstützt)
+ [Stacklass Python](https://github.com/stackless-dev/stackless/wiki/) (Äbgeändertes CPython, welches die Funktionsweise des ``C``-Call-Stacks abändert und Microthreads unterstützt, jedoch weiterhin durch den [Global Interpreter Lock]() behindert wird)
+ [MicroPython](https://micropython.org/) (``Python`` was auf Microcontrollern läuft)
+ ...

Wenn wir aber im allgemeinen von **der** ``Python``-Implementierung sprechen meinen wir die bekannteste von allen Implementierungen und das ist [CPython](https://github.com/python/cpython).
Auch wir haben und werden ausschließlich diese Implementierung in diesem Kurs verwenden.