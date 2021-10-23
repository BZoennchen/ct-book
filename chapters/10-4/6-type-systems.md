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

(sec-type-systems)=
# Dynamische und statische Typisierung

Für *statisch getypten Sprache* wird der Datentyp von Werten und Variablen geprüft **bevor** der Programmcode ausgeführt wird.
Im Gegenteil dazu wird diese Prüfung für *dynamisch getypte Sprachen* erst zur Laufzeit durchgeführt, also **während** der Code ausgeführt wird.

Führen Sie folgenden Code aus:

```{code-cell} python3
---
tags: [raises-exception]
---
number = 5
number = number + 5
print(number)
number = number + 'b'
```

Dieser führt zu einem bekannten Fehler: ``unsupported operand type(s) for +: 'int' and 'str'`` und dennoch wird die ganze Zahl ``number`` ausgegeben.
In anderen Worten der Code läuft solange bis es kracht.

Lassen Sie uns das ganze einmal in ``Java`` transformieren:

```java
int number = 5;
number = number + 5;
System.out.println(number);
number = number + "b";
```

Dieser Code wird gar nicht erst ausgeführt werden.
Stattdessen erhalten wir eine ähnliche Fehlermeldung vor der Ausführung.
In der ersten Zeilen sehen wir jedoch auch, dass wir den Datentyp für ``number`` explizit definieren müssen!
In ``Java`` ist der Datentyp einer Variablen (hier ``number``) auf festgelegt solange die Variable existiert.
Auch folgender Code führt zu einem Fehler:

```java
int number = 5;
number = "b";
```

und auch dieser hier:

```java
int number = 5;
String number = "b";
```

Dadurch, dass bevor der Code ausgeführt wird auf die richtigen Typen geprüft wird, gelten strengere Regeln für diese Typen.
Andernfalls wäre dies nicht möglich.

Im Gegensatz dazu können wir in ``Python`` viel 'freier' mit Typen handtieren.
Der Äquivalente Code wird einwandfrei ausgeführt:

```{code-cell} python3
number = 5
number = 'b'
```

```{code-cell} python3
number = 5
number = 'b'
```

## Was ist besser?

Die einfache Antwort hierauf lautet: nichts von beidem.
Am liebsten hätte man natürlich eine dynamische Typisierung bei der dennoch die Typen auf Korrektheit vor dem Programmlauf überprüft werden.

Die explizite Angabe des Datentyps bei *statisch getypten Sprachen* dient der Dokumentation und macht den Code oft lesbarer ohne zusätzliche Kommentare hinzuzufügen -- der Code ist die Dokumentation. 

Auf der anderen Seite hat eine statische Typisierung weitreichende Auswirkungen auf die Struktur des Codes.
Wir können auf diese nicht im Detail eingehen, doch erfordern statisch getypte Sprachen einen viel strikteren Umgang mit Typen und deren Definition.
Konzepte wie Vererbung und Polymorphie werden unerlässlich.

Im allgemeinen sind statisch getypte Sprachen hungriger, was die Anzahl der Zeichen des geschriebenen Codes angeht.
Mit dynamisch getypte Sprachen erreicht man oft den gleichen Effekt mit deutlich weniger Zeilen Code.

In der Kategorie der Laufzeit des Codes gewinnen statisch getypte Sprachen.
Vor der Ausführung sind alle Typen aller Werte, Variablen usw. bekannt.
Somit können Sie sich vorstellen, dass [Übersetzer / Compiler](def-compiler) den Code besser optimieren können.
Zum Beispiel kann die Typinformation während der Ausführung des Codes vergessen werden -- das spart Speicherplatz.

## Sowohl als auch?

``Python`` ist dynamisch getypt.
Jedoch ruft ``Python`` intern ``C/C++`` Code auf und ``C/C++`` sind statisch getypte Sprachen!
Wir sind zwar noch immer nicht am Optimum: Typ checks vor der Laufzeit und dynamische Typen, aber wir sind nah dran.
``Python`` ist immer dann schnell wenn der statisch getypte Code aufgerufen wird und immer dann langsam wenn wir lange im ``Python``-Code selbst (der dynamisch getypt ist) verweilen.

## Typ hints mit Python

Mit ``Python`` 3.6 wurde eine Syntax eingeführt mit der wir den Datentyp trotz dynamischer Typisierung direkt im Code angeben können.
Wir werden dies im Kurs nicht verwenden wollen es Ihnen aber auch nicht vorenthalten.
Der angegebene Typ dient der reinen Dokumentation und hat keinerlei Auswirkungen auf die Laufzeit.
Manche Entwicklungsumgebungen wie Visual Studio Code (SVCode) bieten auf Grundlage dieser [Typ hints](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) Warnmeldungen bzw. Fehlermeldungen.

Mit Type hints wird aus 

```{code-cell} python3
number = 5
number = 'b'
```

folgender Code

```python
number : int = 5
number = 'b'
```

Dieser wird noch ausgeführt wie zuvor doch Ihre Entwicklungsumgebung wird Sie vermutlich warnen, dass hier der Typ gewechselt wird.
Besonders für Funktionen ist dies hilfreich um die Dokumentation direkt in den Code zu integrieren.
Zum Beispiel wird aus

```{code-cell} python3
def add(x, y):
    return x + y
```

folgender Code

```{code-cell} python3
def add(x: int, y: int) -> int:
    return x + y
```

Wir geben uns und dem- oder derjenigen, welche unseren Code benutzt zu verstehen, dass die Funktion zwei ganze Zahlen erwartet und eine ganze Zahl zurückliefert.