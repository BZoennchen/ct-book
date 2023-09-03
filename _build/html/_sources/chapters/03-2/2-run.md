# Python ausführen

In diesem Kurs verwenden wir Jupyter Notebooks, welche wir im gleichnamigen [Abschnitt](sec-jupyter-notebooks) genauer Besprechen.
Diese Notebooks gibt es noch nicht so lange und sie eigenen sich auch nur für bestimmte Zwecke.

Die wohl gängigste Technik ``Python``-Anwendungen zu entwickeln ist es den Code in Dateien abzulegen und dieses Datei dann [interpretieren](def-interpreter) zu lassen, d.h., auszuführen.
Insbesondere für die Entwicklung großer Anwendungen (z.B. auch Webseiten) oder Pakete, wie etwa [roboworld](https://github.com/BZoennchen/robo-world), und Skripte, ist diese Methode geeignet.
Notebooks eigenen sich hingegen für kleine Probleme bei denen wir Pakete bzw. Module lediglich Nutzung aber nicht selbst entwickeln.

Manchmal möchten wir aber auch nur ein paar Zeilen Code ausprobieren und zwar ohne irgendeine größere Entwicklungsumgebung zu starten.
Wir haben vielleicht vergessen wie ``Python`` den ``+``-Operator für zwei Listen realisiert und möchten das schnell ausprobieren.
Hierzu kann man durch die sog. *Read, Evaluate, Print, Loop* (REPL) zu Deutsch *Lese-Auswerte-Ausgabe-Schleife* oder auch IPython-shell, direkt mit dem ``Python``-Interpreter interagieren.

## REPL

### Python

Öffnen Sie Ihre Konsole und rufen

```sh
python
```

auf.
Jetzt können Sie den ``Python``-Code direkt eintippen.
Es wird das Ergebnis des letzten Befehl ausgegeben.
Zum Beispiel können wir

```python
x = 3 + 6
x + 6
```

rechnen.
Wir können auch Mehrzeilige Befehle abfeuern.
Lassen Sie uns z.B. eine Funktion ``add(x, y)`` definieren:

```python
def add(x, y):
    return x + y

add(9, 5)
```

```{figure} ../../figs/python-tutorial/environment/repl.png
---
width: 800px
name: fig-repl
---
Ausgabe die auf der Konsole durch die oben angegeben Befehle erzeugt wird.
```

Mit ``quit()`` oder ``ctrl + D`` bzw. ``Strg + D`` beenden Sie den Kommandozeileninterpreter.

### IPython

Mit dem Befehl ``ipython`` starten Sie einen anderen Kommandozeileninterpreter zum interaktiven Arbeiten.
Auf diesem basieren die Jupyter Notebooks und Sie müssen das ``jupyterlab`` Modul dazu installiert haben.

```sh
ipython
```

Wir können den selben Code ausführen:

```{figure} ../../figs/python-tutorial/environment/ipython.png
---
width: 800px
name: fig-ipython
---
Ausgabe die auf der Konsole durch die oben angegeben Befehle erzeugt wird.
```

## Script / Datei

Die nächste Möglichkeit besteht darin den Code in eine ``Python``-Datei zu packen.
Wir öffnen unseren Texteditor unserer Wahl und tippen folgenden Code ein:

```python
import sys

n = int(sys.argv[1])
square_sum = 0

for i in range(n):
    square_sum += (i+1)**2

print(square_sum)
```

Dieser Berechnet uns die Summe der Quadratzahlen von 1 bis ``n``, wobei ``n`` das 1. Argument des Programmaufrufs ist.
Das 0. Argument ist immer der Name der Datei in der das ``Python``-Script steht.
Wir speichern die Datei unter dem Namen ``square_sum.py`` im aktuellen Verzeichnis ab und rufen

```sh
python square_square.py 100
```

und erhalten als Ausgabe die Summe aller Quadratzahlen von 1 bis einschließlich 100.

Damit Ihr Code nicht ausgeführt wird, wenn Sie Ihn als Modul importieren, sondern nur wenn Sie Ihn direkt aufrufen, verwendet man eine Bedingung der folgenden Form:

```python
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    ...
```

und es ist gute Praxis anstatt des obigen Codes, folgendes zu schreiben:

```python
import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    square_sum = 0

    for i in range(n):
        square_sum += (i+1)**2

    print(square_sum)
```

Der Aufruf 

```sh
python square_square.py 100
```

funktioniert nach wie vor!

## Jupyter Notebook

Jupyter Notebooks sind die letzte Möglichkeit ``Python``-Code zu entwickeln und auszuführen.
Diese besprechen wir noch im Detail in Abschnitt [Jupyter Notebooks](sec-jupyter-notebooks).
Hier sei nur erwähnt, dass Sie mit

```sh
jupyter lab [path/to/notebook/file]
```

ein bestimmtes Notebook starten und mit 

```sh
jupyter lab
```

die Jupyter-Lab-Umgebung im aktuellen Verzeichnis starten.
Dazu muss das ``jupyterlab`` Modul auf Ihrem System installiert und auffindbar sein.