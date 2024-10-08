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

(sec-dict)=
# Wörterbücher - dict

Die letzte *built-in* Datenstruktur, welche wir besprechen, sind die sogenannten Wörterbücher (engl. [Dictionary](https://docs.python.org/3/library/stdtypes.html#dict)) ``dict``.
In anderen Programmiersprachen, wie z.B. ``Java`` spricht man stattdessen auch von *Hashtables* oder *Hashmaps*.
Sie sind neben den [Listen](sec-list) ``list`` die zweitwichtigste Datenstruktur in ``Python``.
Zwar ist ihr Anwendungsgebiet ein anderes doch sind sie ähnlich wie [Mengen](sec-set) ``set`` realisiert.

Wörterbücher sind **veränderlich** (engl. mutable).
Wir können sie uns als zweispaltige Tabelle vorstellen.
Eine Spalte beinhaltet die **eindeutigen** sog. **Schlüssel** ``key``s und die andere Spalte enthält die sog. **Werte**  ``value``s.
Jede Zeile ist ein Tupel ``tuple`` aus ``key`` und ``value``.

Da die Schlüssel im Sinne der [Gleichheit](def-identity) eindeutig sind, kann die Spalte aus ``key``s als Menge ``set`` an **Schlüsseln** angesehen werden.
Die **Werte** müssen hingegen nicht eindeutig sein.
Sind Sie wie ich ein Freund der Mathematik, so realisiert ein Wörterbücher ``dict`` eine [(mathematische) Funktion](sec-math-function):

$$f : K \rightarrow V,$$

wobei $K$ die endliche Menge der Schlüssel ist.
Es kann durchaus zwei **Schlüssel** geben, die auf den gleichen **Wert** ``value`` verweisen, doch müssen die Schlüssel eindeutig sein!

Wie bei den Mengen, gilt für die **Schlüssel**, dass diese aus **unveränderlichen** Datentypen bestehen müssen.
Das hat die gleichen Gründe wie in Abschnitt [Mengen](sec-set) angesprochen.
Deshalb eigenen sich zum Beispiel [Zahlen](sec-int), [Zeichenketten](sec-string), [Fließkommazahlen](sec-float) oder [Tupel](sec-tuple) -- die **unveränderliche** Datentypen enthalten -- als Schlüssel.

Identisch zu Mengen, können wir extrem schnell testen ob es einen bestimmten Eintrag im Wörterbücher für einen bestimmten Schlüssel gibt.
Das folgt aus der Eigenschaft der [Mengen](sec-set).
Doch anders als bei Mengen ``set``, identifizieren wir damit nicht nur den Schlüssel ``key`` der Menge $K$, sondern auch dessen Wert ``value`` aus $V$.
Wir nutzten die schnelle Adressierung bzw. den schnellen Zugriff um auf **veränderliche** Werte zugreifen zu können.

## Erstellung

Ein Wörterbuch ``dict`` erzeugen Sie ebenfalls durch den Einsatz der geschweiften Klammern, doch besteht jeder Eintrag aus einem Tupel ``(key, value)`` geschrieben als: ``key: value``.
Zum Beispiel könnten wir ein Wörterbuch ``students`` erstellen für welches die eindeutige Matrikelnummer die Schlüssel $K$ und die Nachnamen die Werte $V$ sind.

```{code-cell} python3
students = {123451: 'Huber', 123451: 'Langer', 213131: 'Schmidt', 4131129: 'Langer'}
students
```

Wir können ein Wörterbuch durch die Funktion ``dict()`` aus einer Liste von Tupeln konstruieren:

```{code-cell} python3
students = dict([(123451, 'Huber'), (123451, 'Langer'), (213131, 'Schmidt'), (4131129, 'Langer')])
students
```

Sofern Ihre Schlüssel Zeichenketten ``str`` sind, erlaubt uns ``Python`` auch die *Argumentschreibweise* zu verwenden:

```{code-cell} python3
rectangle = dict(shape='rectangle', x=0.0, y=1.0, width=10, height=20)
print(rectangle)
```

## Zugriff

Im Unterschied zu Mengen können wir auf die **Werte** ``value`` eines Wörterbuchs durch den passenden **Schlüssel** ``key`` zugreifen.
Auch hierzu verwenden wir die eckigen Klammern.
``dictionary[key]`` ergibt den ``value`` für den Schlüssel ``key`` des Wörterbuchs.

```{code-cell} python3
students = {123451: 'Huber', 123451: 'Langer', 213131: 'Schmidt', 4131129: 'Langer'}
print(f' key = {123451}, value = {students[123451]}')
print(f' key = {4131129}, value = {students[4131129]}')
print(f' key = {213131}, value = {students[213131]}')
```

Gibt es den Schlüssel nicht im Wörterbuch, so erhalten wir einen Fehler beim Zugriff.

```{code-cell} python3
---
tags: [raises-exception]
---
print(f' key = {00000}, value = {students[00000]}')
```

## Veränderung

Folgender Ausdruck hat eine von zwei möglichen Bedeutungen.

```{code-cell} python3
students = dict([(123451, 'Huber'), (123451, 'Langer'), (213131, 'Schmidt'), (4131129, 'Langer')])
students[123133] = 'Fischer'
students
```

In unserem Fall, fügen wir in das Wörterbuch ``students`` ein neues Tupel ``(123133, 'Fischer')`` ein.
Existiert der Schlüssen, hier ``123133``, so verändern wir den damit identifizierten Eintrag:

```{code-cell} python3
students[123133] = 'Alberto'
students
```

In den meisten Fällen möchte man genau das, einen Eintrag verändern oder neu einfügen wenn er noch nicht existiert.
Möchten Sie jedoch einen Eintrag nur verändern und nicht einfügen falls er nicht existiert, so müssen Sie zuvor testen ob er existiert:

```{code-cell} python3
# no insertion but a change
if 123133 in students:
  students[123133] = 'Hamilton'
print(students)

# no insertion and no change
if -131331 in students:
  students[-131331] = 'Hamilton'
print(students)
```

Wir testen in diesem Code ob der Schlüssel sich im Wörterbuch befindet.
Um zu testen ob ein Tupel ``(key, value)`` sich im Wörterbuch befindet müssen Sie

1. testen ob sich ``key`` im Wörterbuch befindet und
2. ob ``dictionary[key] == value`` gilt.


```{code-cell} python3
# no insertion but a change
print(123133 in students and students[123133] == 'Hamilton')
print(123133 in students and students[123133] == 'Schmidt')
print(-111111 in students and students[-111111] == 'Schmidt')
```

Um ein Tupel aus dem Wörterbuch zu löschen verwenden wir erneut die *built-in*-Operation ``del``:

```{code-cell} python3
# no insertion but a change
print(123133 in students and students[123133] == 'Hamilton')
del students[123133]
print(123133 in students and students[123133] == 'Hamilton')
```

## Ansichten

Wir könne uns auch alle Schlüssel und Werte eines Wörterbuchs holen.
Durch ``dictionary.keys()`` erhalten wir die Schlüssel, durch ``dictionary.values()`` die Werte, und durch ``dictionary.items()`` beide Spalten (als Liste von Tupeln):

```{code-cell} python3
students = dict([(123451, 'Huber'), (123451, 'Langer'), (213131, 'Schmidt'), (4131129, 'Langer')])
print(f'dictionary: {students}\n')
print(f'key: {students.keys()}')
print(f'values: {students.values()}')
print(f'items: {students.items()}')
```

Es scheint so als wären dies alles Listen ``list``, doch das ist nicht korrekt.
Zwar werden Sie wie Listen ausgegeben, doch sind sie **unveränderlich**.

```{code-cell} python3
---
tags: [raises-exception]
---
students = dict([(123451, 'Huber'), (123451, 'Langer'), (213131, 'Schmidt'), (4131129, 'Langer')])

values = students.values()
values[0] = 'Test'
```

Sie werden als sog. Ansichten (engl. [View Objects](https://docs.python.org/3/library/stdtypes.html#dict-views)) bezeichnet.
Das bedeutet kurz gesagt: Änderungen am Wörterbuch werden in diesen Datenstrukturen übernommen, doch können wir *Ansichten* nicht direkt ändern.
``students.values()`` gibt uns eine *Ansicht* auf die Werte des Wörterbuchs ``students``.

```{code-cell} python3
students = dict([(123451, 'Huber'), (123451, 'Langer'), (213131, 'Schmidt'), (4131129, 'Langer')])

values = students.values()

print(values)
students[123451] = 'Müller'
print(values)
```

In diesem Beispiel ist die letzte Zeile interessant.
Obwohl wir ``values`` nicht verändern, wird es durch unsere Änderungen am Wörterbuch ``students`` verändert.
Dies ist ein sog. *erwünschter Seiteneffekt*.

## Wörterbücher und der Speicher

Wie Wörterbücher im Speicher realisiert werden erläutern wir ansatzweise im Abschnitt [Mengen](sec-set) und tiefgreifender im Kapitel [Namensregister](sec-name-register) im Abschnitt [Hashing und das Dictionary](sec-hashing).