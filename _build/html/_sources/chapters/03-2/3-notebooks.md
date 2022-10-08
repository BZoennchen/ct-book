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

(sec-jupyter-notebooks)=
# Jupyter Notebooks

Wie Sie mittlerweile bemerkt haben, verwenden wir für unseren Kurs ``Python`` in Kombination mit den sogenannten *Jupyter Notebooks*.
Weshalb eignet sich diese Kombination für den Einstieg in das [Computational Thinking](sec-what-is-ct)?
Über [Python](sec-python) haben wir bereits gesprochen, was also sind Jupyter-Notebooks und wozu eignen sie sich?

## Motivation

Die folgende [Referenz](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) liefert eine ausführliche Erläuterung darüber was Jupyter Notebooks sind, welche wir hier in unseren Worten zusammenfassen.

Ein Jupyter Notebook war zu Anfang in erster Linie dazu gedacht wissenschaftlichen Code effektiv innerhalb der Wissenschaftsgemeinschaft auszutauschen.
In fast allen Naturwissenschaften kommt das wissenschaftliche Rechnen zum Tragen.
Forscher entwickeln Computermodelle, simulieren mit Hilfe dieser die Realität und versuchen ausgehend von ihren Ergebnissen Rückschlüsse zu ziehen.
Dabei ergibt sich ein großes Problem: Die Reproduzierbarkeit!
Wird der Computercode nicht offengelegt, so ist es bei ansteigender Komplexität nahezu unmöglich die Forschungsergebnisse nachzuvollziehen.
Nicht nur das, es wird ebenso enorm schwierig auf bestehenden Code aufzubauen.

Aufgrund dieses frustrierenden Zustands machte sich [Fernando Pérez](https://en.wikipedia.org/wiki/Fernando_P%C3%A9rez_(software_developer)) an die Entwicklung des ersten Prototyps der Jupyter Notebooks.
Die Technologie entstand demnach aus der Not heraus.
Sie war dazu gedacht den wissenschaftlichen Austausch und die Zusammenarbeit, kurzum den Wissenstransfer zu verbessern.
Das erdachte und verwirklichte Konzept war recht einfach: Code (Computermodell) und Theorie (die Modellbeschreibung) sollten sich vereint in einem **lesbaren** und **ausführbaren** Dokument befinden.
Der Code sollte die Modellbeschreibung und die Modellbeschreibung den Code erklären.

Wir glauben, dass sich Notebooks für den Einstieg eignen, da durch die zellenweise Auswertung (dazu kommen wir gleich) und die Zellenausgabe ein ständiges Feedback während des Lernen des Programmierens gewährleistet werden kann.
Anfänger\*innen können kleinteilig unterschiedliche Befehle ausprobieren und erhalten für jede Zelle eine Ausgabe/Feedback.
Man könnte auch sagen, dass sich Notebooks einfach debuggen lassen.
Notebooks bieten eine hohe Interaktion zwischen Programmierer/*in und Code bzw. der Maschine.
Das verringert die Hürde um einfach mal loszulegen und kann zudem motivieren, Sie möglicherweise zum sog. *Live Programming* zu führen.
(Beim Live Programming schreiben Sie Code in Echtzeit und führen diesen auch gleich aus, während Ihre Kolleg\*innen zusehen.)

## Starten

Zunächst muss das ``jupyterlab`` Paket auf Ihrem System (oder ihrer aktuell aktiven virtuellen Umgebung) installiert und auffindbar sein.
Ist dem so, können Sie mit

```sh
jupyter lab [path/to/notebook/file]
```

ein bestimmtes die Jupyter-Note starten und mit 

```sh
jupyter lab
```

```{figure} ../../figs/python-tutorial/environment/jupyter-lab-start.png
---
width: 800px
name: fig-jupyter-lab-start-2
---
Die Jupyter-Lab-Umgebung: Auf der linken Seite sehen Sie ihr aktuelles Verzeichnis und rechts können Sie unterschiedliche Anwendungen, z.B., ein Notebook starten.
```

die Jupyter-Lab-Umgebung im aktuellen Verzeichnis öffnen.
Anschließend können Sie in Ihrem Browser zu Ihrem Notebook in einem Unterverzeichnis navigieren oder ein neues Notebook erstellen.

Starten Sie ein ``Python``-Notebook, müssen Sie möglicherweise einen sog. *Kernel* auswählen.
Jede mögliche Auswahl bezieht sich auf eine ``Python``-Umgebung, welche sich im Wesentlichen durch eine ``Python``-Version und bestimmten, von Ihnen installierten Paketen, auszeichnet.
Wählen Sie die Umgebung, welche Sie verwenden wollen.

```{figure} ../../figs/python-tutorial/environment/jupyter-lab-select-kernel.png
---
width: 200px
name: fig-jupyter-lab-select-kernel
---
Auswahl eines Kernels: Uns stehen vier Kernels zur Verfügung.
Der oberste in der Liste bezieht sich auf unsere globale ``Python 3.x`` Umgebung.
Die anderen beziehen sich auf von uns angelegte virtuelle ``Python``-Umgebungen.
```

## Zellen

Ein ausführbares Dokument?
Was soll das sein?
Ohne vorerst genaue ins Detail zu gehen bedeutet dies, dass das Dokument ``Python``-Code enthält der tatsächlich ausgeführt werden kann.
Im Hintergrund rechnet der Computer, liefert das Ergebnis zurück und das Notebook zeigt es in einer gewissen Weise an.
Führen wir zum Beispiel folgende Codezeile aus,

```{code-cell} python3
2**4
```

berechnet der Computer $2^4 = 16$, lieft das Ergebnis ans Notebook zurück, welches daraufhin das Ergebnis in gewisser Weise ausgibt.
Die Kommunikation zwischen dem ``Python``-Interpreter und Ihrem Browser übernimmt der ausgewählte *Kernel*.

Prinzipiell bestehen Jupyter Notebooks aus einer geordneten Liste von *Zellen*.
Innerhalb einer Zelle befindet sich eine Art von Inhalt, d.h., entweder Code oder eine Beschreibung (Text, Bilder, Formeln).
Befindet sich der Cursor innerhalb einer Zelle und wir drücken ``Strg``+``Enter`` (Mac ``CMD``+``Enter``), so wird diese Zelle ausgewertet (evaluiert).
Handelt es sich um eine *Code-Zelle* wird der Code von oben nach unten ausgeführt.
Handelt es sich stattdessen um eine *Beschreibungs-Zelle* wird aus dieser ``HTML``-Text erzeugt, welcher durch ihren Browser angezeigt wird.

Um eine Zelle unterhalb einer anderen Zelle einzufügen drücken Sie mit der Maus links neben die Zelle und drücken ``b`` (below).
Um eine Zelle oberhalb einzufügen drücken Sie ``a`` (above).
Um die ausgewählte Zelle zu löschen drücken Sie zweimal schnell hintereinander ``d`` (delete).

Ok, so ganz stimmt das nicht.
Führen wir eine *Code-Zelle* aus, so wird, nachdem deren Code ausgewertet wurde oder die Auswertung aufgrund eines Fehlers abbricht, das Ergebnis oder die Fehlermeldung auch in ``HTML``-Text umgewandelt.

Außerdem wird auch der unausgewertete Code oder die Beschreibung in ``HTML``-Text übersetzt.
Ihr Browser ist im Stande ``HTML`` anzuzeigen, ganz so wie es Microsoft Word möglich ist, Word-Dokumente anzuzeigen.
Alles in allem bietet Ihnen diese Technologie die Möglichkeit Code und dessen Beschreibung direkt in Ihren Browser "hineinzutippen", anzuzeigen, auszuwerten und diese Auswertung ebenfalls anzuzeigen.
Es ist als würde Sie eine Schulaufgabe entwerfen, mit dem Computer lösen und das Ergebnis an der richtigen Stelle einfügen und das alles über ein einziges Dokument.

Jupyter Notebooks bieten die Möglichkeit der Dokumentation durch ``Markdown`` und (Latex), sodass Text, mathematische Formeln, wie auch Bilder oder Plots in das Notebook eingefügt werden können.
Dabei kann sowohl die Dokumentation wie auch der Code über das Dokument hinweg verteilt werden.
Zwischen Code können Texte, Bilder und Formeln eingefügt werden.

### Markdown

Um eine Zelle in eine ``Markdown``-Zelle umzuwandeln, müssen Sie gleich links neben den Zelleninhalt klicken und dann ``m`` drücken.

``Markdown`` ist eine äußerst einfache Beschreibungssprache.
Auf der [offiziellen Webseite](https://www.markdownguide.org/) finden Sie, falls es Sie interessiert, einen guten Einstieg.
Das [cheat-sheet](https://www.markdownguide.org/cheat-sheet/) ist immer wieder hilfreich, falls Sie vorhaben ihr Notebook mit einer Beschreibung zu füllen.
Auch ``HTML`` ist eine solche Sprache, doch sehr viel komplizierter, jedoch wird ``Markdown``-Code in ``HTML``-Code übersetzt.
Das braucht Sie jedoch nicht zu kümmern aber könnte Sie vielleicht zum staunen bringen, dass dieses Dokument mit Ausnahme des Codes, was sie gerade lesen in ``Markdown`` (mit ein paar Erweiterungen) geschrieben wurde.

Eine Testprobe?
Der Abschnitt sieht in ``Markdown`` wie folgt aus:

```markdown
### Markdown

Um eine Zelle in eine ``Markdown``-Zelle umzuwandeln, müssen Sie gleich links neben den Zelleninhalt klicken und dann ``m`` drücken.

``Markdown`` ist eine äußerst einfache Beschreibungssprache.
Auf der [offiziellen Webseite](https://www.markdownguide.org/) finden Sie, falls es Sie interessiert, einen guten Einstieg.
Das [cheat-sheet](https://www.markdownguide.org/cheat-sheet/) ist immer wieder hilfreich, falls Sie vorhaben ihr Notebook mit einer Beschreibung zu füllen.
Auch ``HTML`` ist eine solche Sprache, doch sehr viel komplizierter, jedoch wird ``Markdown``-Code in ``HTML``-Code übersetzt.
Das braucht Sie jedoch nicht zu kümmern aber könnte Sie vielleicht zum staunen bringen, dass dieses Dokument mit Ausnahme des Codes, was sie gerade lesen in ``Markdown`` (mit ein paar Erweiterungen) geschrieben wurde.```
```

### Code

Der zweite und viel wichtigere Typ von Zellen sind die bereits angesprochenen *Code-Zellen*.
Um aus einer Zelle eine *Code-Zelle* zu machen, müssen Sie gleich links neben den Zelleninhalt klicken und dann ``y`` drücken.
Wenn Sie versehentlich aus einer Code-Zelle eine Markdown-Zelle gemacht haben, wird der Code einfach als Text interpretiert.
Anstatt

```{code-cell} python3
x = 5 * 2 + 6
```

sehen Sie

```markdown
x = 5 * 2 + 6
```

Es fehlt die farbliche Hervorhebung, welche Ihnen das Lesen des Codes vereinfacht und Sie können diese Zelle nicht ausführen, sondern nur auswerten.

## Codeevaluierung

Ohne zuvor mit dem Notebook und der Ausführung von ``Python``-Code experimentiert zu haben, wird Ihnen dieser kurze Abschnitt mysteriös vorkommen.
Vielleicht lesen Sie sich diesen Teil bei Zeiten erneut durch.

Wichtig ist festzuhalten: Ein Notebook besteht aus *Code-* und *Beschreibungszellen*.
Für die Auswertung des Codes können wir alle *Beschreibungszellen* ignorieren.
Nun lassen Sie uns die Zellen eines konkreten Notebooks von oben nach unten durchnummerieren.

### Reihenfolge

Da wir Menschen Dokumente von oben nach unten lesen, macht es Sinn die einzelnen Codezellen nacheinander von oben nach unten auszuführen.
Hierfür bietet die Jupyter-Umgebung auch einen Knopf: ``Run -> Run All Cells`` wertet alle Zellen von oben nach unten aus.
Dabei wird die i-te Zelle erst ausgewertet, wenn die i-1-te Zelle erfolgreich ausgewertet werden konnte.
In anderen Worten, der Code wird so ausgewertet als hätten Sie alles in eine einzige Zelle in der gleichen Reihenfolge hineingeschrieben!

```{figure} ../../figs/python-tutorial/environment/jn-all-cell-evaluation-lab.png
---
height: 300px
name: fig-jn-all-cell-evaluation-lab
---
Alle Zellen ausführen: ``Run -> Run All Cells`` evaluiert alle Zellen von oben nach unten.
```

Diese Ausführungsreihenfolge ist jedoch nicht verpflichtend.
Sie können manuell einzelne Zellen auswerten.
Nehmen wir einmal folgende *Code-Zellen* (1,2,3,4):

```python
y = -3      # Zelle 1
```

```python
x = z + y   # Zelle 2
```

```python
z = 5       # Zelle 3
```

```python
y = 20      # Zelle 4
```

Nehmen wir nun an, wir werten Zelle 1 dann 4 dann 3 und dann 2 aus.
Was glauben Sie welchen Wert die Variable ``x`` enthält?
Nun der effektiv können wir das gleiche Ergebnis erzeugen wenn wir den Inhalt entsprechend der Ausführungsreihenfolge in eine Zelle packen:

```{code-cell} python3
y = -3      # Zelle 1
y = 20      # Zelle 4
z = 5       # Zelle 3
x = z + y   # Zelle 2
x
```

Demnach ist ``x = 5 + 20`` und ``y = 20``.
Führen wir daraufhin Zelle 1 dananch 2 aus, erhalten wir für ``x``: ``x = 5 + (-3) = 2``

```{code-cell} python3
y = -3      # Zelle 1
y = 20      # Zelle 4
z = 5       # Zelle 3
x = z + y   # Zelle 2
y = -3      # Zelle 1
x = z + y   # Zelle 2
x
```

```{admonition} Auswertungsreihenfolge (Notebooks)
:name: remark-evaluation-ordering
:class: remark
Sie sollten darauf achten, dass ihr Code das gewünschte Resultat erzeugt indem alle Zellen, nach einem Neustart des Kernels, von oben nach unten ausgeführt werden.
```

### Wenn es kracht

Was passiert wenn Ihr Code einen [syntaktischen](def-syntax) Fehler enthält oder [semantisch](def-semantik) keinen Sinn ergibt?
Sobald Ihr Code während der Ausführung zu einem solchen Fehler führt, wird die Auswertung der Zelle und alle darauffolgenden Zellen abgebrochen.
Zudem wird eine mehr oder weniger hilfreiche Fehlermeldung ausgegeben.

Lassen wir es doch mal krachen.

```{code-cell} python3
---
tags: [raises-exception]
---
# mit Variablen rechnen, die noch nicht definiert ist
x = number + 4
```

Wir erhalten eine Fehlermeldung, welche darauf hindeutet, dass ``number`` noch nicht definiert ist.
Haben Sie keine Angst vor solchen Fehlern.
Im Gegenteil, provozieren Sie diese um zu sehen was passiert.

Fehlermeldungen schützen Sie jedoch nur vor offensichtlichen Fehlern.
Hin und wieder läuft unser Code, produziert jedoch nicht das richtige Ergebnis, da wir etwas falsch programmiert haben oder unsere Überlegungen - unser [Computational Thinking](sec-what-is-ct) -- fehlerhaft ist.

Das kann dazu führen, dass unser Code gar nicht terminiert.
In einem solchen Fall kommt die Auswertung der Zelle nie zum erliegen.
Folgender Code beinhaltet eine sogenannten Endlosschleife.
Wenn Sie ihn ausführen endet diese Auswertung niemals.

```python
x = 1
while True:
    x = x + 1
```

Sie sehen an dem kleinen Sternchen ``*``, dass die Zelle ausgewertet wird.
Erst wenn dieses verschwindet ist die Auswertung abgeschlossen.

```{figure} ../../figs/python-tutorial/environment/endless-loop-kernel-lab.png
---
width: 200px
name: fig-endless-loop-kernel-lab
---
Während der Ausführung sehen wir den Stern ``*``.
```

Um die Auswertung abzubrechen (engl. interrupt) müssen wir den sog. *Kernel* unterbrechen ``Kernel -> Interrupt``.
Stellen Sie sich den *Kernel* vorerst als einen Vermittler zwischen Notebook (bzw. Ihrem Browser) und ``Python`` vor.
Beachten Sie, dass eine Unterbrechung des Kernels nicht bedeutet, dass alles so ist wie als hätten wir die Zelle gar nicht ausgeführt.
Die Zelle wurde solange ausgeführt, bis wir den Vorgang unterbrochen haben.

```{figure} ../../figs/python-tutorial/environment/interrupt-kernel-lab.png
---
height: 300px
name: fig-interrupt-kernel-lab
---
Unterbrechung der Ausführung durch ``Kernel``->``Interrupt``.
```

Führen Sie folgende Zellen nacheinander aus.
Unterbrechen Sie dabei nach der Ausführung der zweiten Zelle diese und führen Sie dann die letzte Zelle aus.
Wenn die zweite und dritte Zelle mehrmals ausführen so erhöht sich ``k`` immer weiter.

```python
k = 1
```

```python
k = k + 1
x = 1
while True:
    x = x + 1
```

```python
print(k)
```