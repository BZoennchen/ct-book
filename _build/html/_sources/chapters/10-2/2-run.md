# Python ausführen

In diesem Kurs verwenden wir Jupyter Notebooks, welche wir im gleichnamigen [Abschnitt](sec-jupyter-notebooks) genauer Besprechen.
Diese Notebooks gibt es noch nicht so lange und sie eigenen sich auch nur für bestimmte Zwecke.

Die wohl gängigste Form ``Python``-Anwendungen zu entwickeln und ist es den Code in Dateien abzulegen.
Insbesondere für die Entwicklung großer Anwendungen (z.B. auch Webseiten) oder Module wie etwa [roboworld](https://github.com/BZoennchen/robo-world) und Scripte, ist diese Methode geeignet.
Notebooks hingegen eigenen sich für kleine Probleme bei denen wir Module lediglich Nutzung aber nicht selbst entwickeln.

Manchmal möchten wir aber auch nur ein paar Zeilen Code ausprobieren und zwar ohne irgendeine größere Entwicklungsumgebung zu starten.
Wie haben vielleicht vergessen wie ``Python`` den ``+``-Operator für zwei Listen realisiert und möchten das schnell ausprobieren.
Hierzu kann man den sog. ``Python``-shell oder auch IPython-shell, welche dem REPL-Konzept (Read, Evaluate, Print and Loop) folgt, verwenden.

## REPL

### Python

Öffnen Sie Ihre Konsole und rufen

```sh
python
```

auf.
Jetzt können Sie den ``Python``-Code direkt eintippen und es wird immer der letzte Befehl ausgegeben.
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

Mit ``quit()`` beenden Sie den Kommandozeileninterpreter.

### IPython

Mit dem Befehl ``ipython`` starten Sie einen anderen Kommandozeileninterpreter zum interaktiven Arbeiten.
Auf diesem basieren die Jupyter Notebooks und Sie müssen das ``jupyter`` Modul dazu installiert haben.

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

Damit Ihr Code nicht ausgeführt wird, wenn Sie Ihn als Modul importieren sondern nur wenn Sie Ihn direkt aufrufen, verwendet man eine Bedingung der folgenden Form:

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
Diese besprechen wir noch im Detail in Abschnitt [Jupyter Notebooks](sec-jupyter-notebooks)).
Hier sei nur erwähnt, dass Sie mit

```sh
jupyter notebook [path/to/notebook/file]
```

ein bestimmtes Notebook starten und mit 

```sh
jupyter notebook
```

die Jupyter-Umgebung im aktuellen Verzeichnis starten.
Dazu muss das ``jupyter`` Modul auf Ihrem System installiert und auffindbar sein.