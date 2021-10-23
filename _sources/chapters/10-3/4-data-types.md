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

(sec-datatypes-intro)=
# Datentypen (Einführung)

Wie in Abschnitt [Repräsentation](sec-representation) beschrieben, befinden sich im Speicher des (digitalen) Computers ausschließlich [Bits](def-bit).
Sie können sich den Speicher als eine lange lange Liste von Bits vorstellen.
Diese können nur einen von zwei Zuständen (0 und 1) annehmen.
Dennoch verarbeiten Computer Zahlen, Text, Bilder und mehr.
Die Magie dahinter geschieht durch die Wahl und Implementierung einer [Interpretation](sec-interpretation).
Unterschiedliche Interpretationen ermöglichen es, Bits und [Byte](def-byte) als Zahlen, Text, Bilder usw. zu verarbeiten.
Dabei werden schlussendlich diese komplexeren **Datentypen** durch Bits und Byte [repräsentiert](sec-representation).

So könnten wir ein Bild im ``PNG`` oder ``JPEG``-Format als *Werte-Datentyp*-Paar ansehen.
Der *Wert* ist durch die Bits die das Bild als solches ausmachen definiert.
Der *Datentyp* ``PNG`` oder ``JPEG`` gibt an wie diese Bits von der Computerhardware wie auch Software interpretiert werden müssen um das Bild auch als Bild verarbeiten zu können.

Wir sprechen bei diesen Dateiendungen jedoch nicht von **Datentypen** sondern von *Dateiformaten*.
Von **Datentypen** sprechen wir hingegen, wenn es um eine [Interpretation](sec-interpretation) im Zuge der Programmierung geht.

```{admonition} Datentypen
:name: def-datatypes

Ein *Datentyp* oder auch kurz *Typ* ist ein Attribut eines Werts, welches der Computerhardware und dem Compiler oder Interpreter angibt wie der Wert zu verwenden bzw. zu interpretieren ist.

```

Um das Konzept um die Datentypen zu durchdringen empfehlen wir zu einem späteren Zeitpunkt die Übung [Speicher - alles ist eine Liste](sec-memory).

## Ganze Zahlen - int

TODO

## Wahrheitswerte - bool

TODO

## Fließkommazahlen - float

Computer sind gebaut um numerische Berechnungen auszuführen.

## Zeichenketten - str

TODO

## Listen - list

TODO

## Tupel - tuple

TODO

## Mengen - set

TODO

## Wörterbücher - dict

TODO


