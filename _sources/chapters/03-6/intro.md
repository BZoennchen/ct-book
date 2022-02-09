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

(sec-functions)=
# Funktionen

Der Schlüssel zur Berechnung von Lösungen bzw. der Verarbeitung von Information ist die [Wiederholung](sec-repetition-and-recursion).
Wo es uns [Schleifen](sec-loops) erlauben eine bestimmte Folge von Arbeitsschritte *lokal* mehrfach auszuführen, erlauben es uns Funktionen eine Folge von Arbeitsschritte *global* auszuführen.
In beiden Fällen ändern wir den Verlauf der Codeausführung, sodass dieser nicht mehr der Befehlsfolge (gelesen von oben nach unten) entspricht.

Funktionen bündeln eine Folge von Arbeitsschritten / Befehle.
Es können Parameter definiert werden, sodass wir der Funktion Argumente als Eingabe übergeben.
Wir sind im Stande dieses Bündel irgendwo in unserem Code auszuführen (ohne es noch einmal niederzuschreiben).
Wird die Funktion im Code aufgerufen, springen wir, bzw. die CPU durch ihren [Befehlszähler](def-program-counter), an die Stelle der Funktion, das Bündel an Anweisungen wird ausgeführt und schlussendlich springen wir wieder an jene Stelle zurück, von der wir hergekommen sind.

Durch wiederholtes und verschachteltes Aufrufen einer Funktion erzeugen wir eine Art von Wiederholung.
Zum Beispiel:

```{code-cell} python3
def successor(n):
  return n + 1

successor(successor(successor(1)))
```

Ruft sich eine Funktion, bis zu einer bestimmten Abbruchbedingung selbst auf, so sprechen wir von einer sog. [Rekursion](sec-recursion) oder [rekursiven Funktion](sec-recursive-functions).
Zum Beispiel:

```{code-cell} python3
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)

fib(13)
```

Viele sog. *built-in* (eingebaute) ``Python``-Funktionen haben wir bereits verwendet.
Sie werden uns mit der ``Python``-Standard Bibliothek mitgeliefert.
Zum Beispiel ist ``type()`` oder auch ``len()`` eine solche Funktion.

```{code-cell} python3
type(len)
```

``roboworld`` ist beispielsweise ein Modul, d.h. eine Ansammlung von Funktionalität, welches wir nutzten können.
Deutlich bekannter ist das Modul ``numpy``, welches für numerische Berechnungen verwendet wird.
Um eine Funktion eines Moduls aufzurufen stellen wir den Modulnamen, z.B. ``numpy`` und einen Punkt ``.`` vorne an. Zuvor müssen wir das Modul geladen haben:

```{code-cell} python3
import numpy
numpy.linspace(0, 1, 100)
```

```{code-cell} python3
type(numpy.linspace)
```

Funktionen sind ein Mittel um Codewiederholungen zu verhindern und auch ein Mittel um Code zu strukturieren und bestimmte Funktionalität zu kapseln.
Stellen Sie sich vor wir müssten jedes Mal wenn wir etwas ausgeben wollen den Code der Funktion ``print()`` niederschreiben.
Schnell würden unsere Programme lange und auch langweilig und unübersichtlich werden.

Gute Funktionen zu schreiben kann sehr befriedigend für uns Computational Thinker\*innen sein.
Wir lösen damit oft ein Teilproblem und kommen der gesamten Lösung näher.
Mit ein wenig Erfahrung können wir sogar Probleme lösen indem wir davon ausgehen, ein Teilproblem hätten wir bereits gelöst -- auch wenn dies noch nicht der Fall ist.

Wie ist das gemeint?
Nun, wir wollen zum Beispiel eine Funktion schreiben, welche uns die ersten ``n`` Primzahlen berechnet und in eine Liste packt.
Wir gehen einfach davon aus es gäbe eine Funktion ``is_prime(k)`` die prüft ob ``k`` eine Primzahl ist oder nicht.
Unter dieser Annahme schreiben wir unsere Funktion ``prime_list(n)``:

```{code-cell} python3
def is_prime(k):
  pass

def prime_list(n):
  primelist = []
  k = 1
  while len(primelist) < n:
    if is_prime(k):
      primelist.append(k)
    k += 1
  return primelist
```

Nachdem wir uns um die Generierung der Liste gekümmert haben, widmen wir uns der Funktion ``is_prime(k)``.
Oder andere Entwickler\*innen, die sich besser mit dem Problem auskennen, lösen es.

```{code-cell} python3
def is_prime(k):
  # a really stupid prime check
  if k == 1:
    return False
  elif k == 2:
    return True
  else:
    for i in range(2,k-1,1):
      if k % i == 0:
        return False
  return True

def prime_list(n):
  primelist = []
  k = 1
  while len(primelist) < n:
    if is_prime(k):
      primelist.append(k)
    k += 1
  return primelist

prime_list(20)
```