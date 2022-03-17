(sec-cpython-interpreter)=
# Interpreter und Compiler

Wir müssen ein Geheimnis an dieser Stelle lüften!
``Python`` in seiner CPython Implementierung wird sowohl interpretiert als auch compiliert.

```{admonition} Übersetzt und interpretiert?
:name: attention-python-interpretation-and-compilation
:class: attention

``Python`` in seiner CPython Implementierung wird sowohl [interpretiert](def-interpreter) als auch [compiliert](def-compiler).

```

Legen wir eine neue Datei ``hello.py`` mit folgendem Code an

```python
print('hello')
```

und rufen den in ``C`` geschriebenen CPython-Interpreter durch

```
python hello.py
```

auf unserer Konsole auf, was passiert dann genau?

Der ``Python``-Quellcode durchläuft 3 Phase bis er schließlich tatsächlich auf Ihrer Maschine ausgeführt werden kann:

1. **Aufbereitung**: Der Code wird durch den Interpreter zur Übersetzung aufbereitet (Lexing, Parsing).
2. **Übersetzung**: Innerhalb des Interpreters wird ein [Compiler](def-compiler) gestartet, welcher den aufbereiteten Code in *Bytecode* (Intermediate Language Code ILC) umwandelt (``hello.pyc``).
3. **Interpretation**: Dieser Code wird von der *Virtuellen Maschine (PVM)* des Interpreters interpretiert und dadurch als Maschinencode ausgedrückt. Bereits in *Masachinencode* übersetzte ``C``-Module werden nicht in *Bytecode* überführt sondern im *Bytecode* direkt aufgerufen.

Erst durch die Interpretation wird aus dem *Bytecode* (in kombination des vorkompilierten ``C``-Codes) ausführbarer *Maschinencode*.
*Bytecode* ist immernoch nicht speziell auf Ihre Maschine angepasst, stattdessen ist der Code immernoch zu abstrakt.
Durch die Interpretation werden die Spezifika Ihrer Maschine beachtet.

Folgende Abbildung verdeutlicht den Ablauf bei der Ausführung eines ``Python``-Programms.

```{figure} ../../figs/python-tutorial/cpython/cpython-interpreter.png
---
width: 800px
name: fig-cpython-interpreter
---
Schematisch dargestellte Arbeitsweise des CPython-Interpreters.
```

Es wird nun klar weshalb ``Python`` (in seiner *Referenzimplementierung*) zu den langsamen Sprachen zählt.
Der [Übersetzer](def-compiler) ist Teil des [Interpreters](def-interpreter).
Wann immer Code durch den Interpreter ausgeführt wird, kommt es zu einer Übersetzung des ``Python``-Codes in *Bytecode*.
Das heißt, dass **während des Programmlaufs** der Übersetzer aktiv wird.
Diese Übersetzung kostet Zeit.

Im Gegensatz dazu wird ``C``-Code durch einen [Übersetzer](def-compiler) vor dem Programmstart in *Maschinencode* übersetzt.
Starten wir das ``C``-Programm bedarf es weder eines Interpreters noch eines Übersetzers.
Der Code kann direkt ausgeführt werden.

``Java`` basiert auf einem ähnlichen Konzept wie ``Python``.
``Java``-Code wird ebenfalls vor der Ausführung in *Bytecode* übersetzt und dann durch die Java Virtual Machine (JVM) interpretiert.
Der Unterschied ist allerdings, dass der ``Java``-Übersetzer nicht Teil des Interpreters ist.
Der ``Java``-Code wird vor dem Programmlauf einmal komplett in *Bytecode* übersetzt.
Starten wir ein ``Java``-Programm wird die JVM aktiv, jedoch bedarf es keiner zusätzlichen Übersetzung von ``Java``-Code in *Bytecode*.