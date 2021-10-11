# Erfolgsfaktoren

In den Entwurf von Programmiersprachen ist viel Denkkraft hineingeflossen.
Wie Sie im Beispiel des Kartensortierens gesehen haben, ist es nicht einfach eine saubere gut leserliche und unmissverständliche Sprache zu entwickeln.
Zum Glück können wir von den Vorarbeiten anderer Denker\*innen profitieren und müssen uns über die Entwicklung einer Programmiersprache keine Gedanken machen.
Wir möchten Ihnen dennoch einen Einblick geben, weshalb neue Programmiersprachen entwickelt werden und welche Art von Programmiersprachen es gibt.

```{figure} ../../figs/languages/programming-language-popularity.png
---
width: 700px
name: fig-language-popularity
---
Popularität der Programmiersprachen nach dem [PYPL Index](https://pypl.github.io/PYPL.html) (logarithmische Skala) -- ``Python`` gefolgt von ``Java``, ``JavaScript``, ``C#`` und ``C++``. 
```

Zunächst ist festzuhalten, dass es nicht die eine beste Programmiersprache gibt.
Unterschiedliche Sprachen eigenen sich für unterschiedliche Aufgaben, Anwendungsbereiche und folgen subjektiven Vorlieben.

Die wesentlichen Teile die wir bei einer Sprache beurteilen können sind:
1. ihre **Syntax**
2. ihr **Ökosystem** (vorhandene Bibliotheken, Tutorials, Dokumentationen, Lehrvideos, eine starke offene und diverse Gemeinschaft)
3. ihre **Anwendungsbereiche**
4. ihre **Performance** (Laufzeit des Programmcodes)

Diese vier Säulen stehen in Beziehung.
Eine angenehme gut leserliche Syntax führt zu einer regen Benutzung und damit zu einem starken Ökosystem, was den Anwendungsbereich erweitert.
Ein vielschichtiger Anwendungsbereich stärkt die Diversität des Ökosystems und kann zu neuen syntaktischen Erweiterungen der Sprache führen.
Entwickelt sich die Sprache weiter und wird vielfach verwendet, wird sie oftmals auch hinsichtlich ihrer Performance optimiert.
Diese Rückkoppelung kann deshalb dazu führen, dass eine neue Sprache schnell an Fahrt aufnimmt.

Performance und Lesbarkeit bzw. Entwicklungszeit stehen aber auch im Konflikt.
Um feinste Optimierungen durchzuführen muss die Sprache über Mittel verfügen, die die Entwicklungszeit erhöht und die Lesbarkeit des Codes erschwert.
Hohe Lesbarkeit und eine hohe Performance sind gleichzeitig schwer zu erreichen.
``Python`` hat hier einen Weg gefunden (siehe [Python](sec-python)).

Neue Programmiersprachen haben es natürlich erst einmal schwer, denn etablierte Sprachen werden in vielen Systemen bereits eingesetzt.
Niemand schreibt diese Systeme erneut, es sei denn es lohnt sich wirklich.
Zudem gibt es für etablierte Sprachen eine über die Jahre entwickelte Ansammlung an Bibliotheken, Tools, Tutorials und Dokumentationen - sie besitzten bereits ein gutes **Ökosystem**.

Es gibt Sprachen, wie zum Beispiel ``CUDA``, die einen sehr engen Anwendungsbereich haben: die Programmierung von Nvidea Grafikkarten.
Für den Erfolg der Sprache kann das von Vorteil sein, sofern es schwer ist in dem Anwendungsbereich Fuß zu fassen oder dieser keine breite Anwender\*innen- oder Entwickler\*innenbasis besitzt.
Da GPUs fundamental anders funktionieren als CPUs, bedurfte es neuer Sprachen um die Programmierung dieser Geräte zu vereinfachen.
Im Fall von Nvidea schützt der Hardwarehersteller sein geistiges Eigentum und macht es für andere Entwickler schwierig neue Sprache für Nvidea GPUs zu entwickeln.
Der offene Standard ``OpenCL`` wird nicht mehr von Nvidea weiterentwickelt und so können ``OpenCL`` Programmierer\*innen wichtige Features der Grafikkarten nicht nutzen.
Solche Monopole können eine Sprache auch vorran bringen, sind aber heute unserer Ansicht nach nicht mehr Zeitgemäß, da sie die Innovation tendenziell verlangsamen.

Folgender ``OpenCL``-Code addiert zwei große Vektoren (zwei große Listen).
Die Operation wird auf tausenden kleinen Prozessoren parallel ausgeführt.
``id`` ist die eindeutige Nummer des jeweiligen Prozessors.

```c
__kernel void vecAdd(__global double *a, __global double *b, __global double *c, const unsigned int n) {                                                                             
    int id = get_global_id(0);                                
    if (id < n) {                                      
        c[id] = a[id] + b[id];      
    }                           
}
```

Viele Sprachen werden einmalig in Forschungsprojekten für ganz spezielle Zwecke von ihrem Erfinder benutzt und versinken dann wieder in der Versenkung.
Von diesen haben und werden wir nie etwas mitbekommen.
Sehr wenige davon treffen jedoch ins Schwarze.

Ob sich eine Programmiersprache etabliert hängt meist davon ab ob sie verwendet wird.
Diese Tatsache ist in der heutigen global vernetzten Welt noch ausschlaggebender als in der Vergangenheit.
Erfolgreiche Sprachen treffen den Nerv der Zeit, haben oft einflussreiche Unterstützer, oder bringen wichtige neue Konzepte in die Gemeinschaft.

Für den langfristige Erfolg einer Sprache müssen wir noch genauer hinsehen.
Ist eine Sprache zu schnell zu erfolgreich, kann das ihren langfristigen Erfolg bedrohen.
Sie wächst zu schnell.
Überhastet werden Neuerungen eingebracht, die sich später als Fehler herausstellen.
Befinden sich erst einmal bestimmte Konzepte in einer Sprache, kann man diese nur sehr schwer wieder herausbringen, da bereits viele Software-Systeme auf die Konzepte angewiesen sind.
So wird die Vorhersage ob sich eine Sprache durchsetzen wird zu einer eher chaotischen Wettervorhersage.
Es gibt viele unsicherer Variablen inklusive der zukünftigen technischen Entwicklung.

``Haskell`` ist eine Sprache die sehr gemächlich an Erfolg gewonnen hat.
Sie war nie die Nummer eins und ist noch immer eher eine Nischensprache, doch ist sie auch nicht verschwunden.
Das war jedoch nur möglich, da sie von einer kleinen Gruppe am Leben gehalten wurde.

Eine weitere wichtige Ursache für den Erfolg einer Sprache ist deren Leserlichkeit aber auch deren allgemeiner Zugang.
Wird die Sprache oder Bibliotheken kommerzialisiert?
Gibt es eine starke Open-Source oder Free-Source Gemeinschaft?
Wird die Sprache von großen Unternehmen unterstützt?
Gibt es freie Programmierwerkzeuge?

Im Bereich des High Performance Computation (HPC) spielt die Geschwindigkeit des Programmiercodes der Sprache eine zentrale Rolle.
Dieses Feld ist immernoch stark von ``C`` und ``C++`` geprägt, da auch HPC-Bibliotheken wie OpenM und MPI auf diesen Sprachen basieren.
Leserlichkeit ist in diesem Bereich weniger wichtig als optimaler Code.
Hier wird jede Methode bis aufs kleinste Detail optimiert.
Das geht soweit, dass man sich darüber Gedanken macht in welcher Reihenfolge man bestimmte Rechnung wie

```c
x = y - z + a + u;
```

durchführt.

Möchte ich hingegen eine kürzere Entwicklungszeit und weniger Fehlerquellen in meinem Code, mache ich womöglich bei der Geschwindigkeit kleinere Abstriche und wähle stattdessen leichter zu erlernende Sprache wie ``Python``, ``Java`` oder ``C#``.

Für die Anwendung der linearen Algebra ist es sinnvoll der Programmiererin oder dem Programmierer die Möglichkeit zu geben, Matrizen zu multiplizieren.
Im folgenden sehen Sie wie dies in ``MATLAB`` syntaktisch möglich ist.

```matlab
A = [1 3 5; 2 4 7];
B = [-5 8 11; 3 9 21; 4 0 8];
C = A * B
```

Um Webseiten clientseitig zu steuern (d.h. der Code wird lokal auf Ihrem Rechner ausgeführt) bieten Internetbrowser eine eigene Programmiersprache namens ``JavaScript`` an.
Diese Sprache hat sich auch im Bereich Design ausgebreitet.
Sie hat sich so weit verbreitet, dass sie heute auch für andere Zwecke wie die clientseitige Webprogrammierung genutzt wird.
Ein Beispiel ist das Projekt [Node.js](https://en.wikipedia.org/wiki/Node.js).

Unterschiedliche Sprachen folgen unterschiedlichen Philosophien.
In ``Python`` gibt es oft nur den einen richtigen Weg um etwas auszudrücken.
In Sprachen wie ``JavaScript`` gibt es hingegen viele ausdrucksweisen (syntaktische Unterschiede) für die gleiche Semantik.
Im Falle von ``Python`` hat es den Vorteil, dass fremder Code leichter zu lesen ist.
Sind hingegen mehrere Programmierstile valide, dann treffen möglicherweise zwei verschiedene Stile aufeinander was wiederum die Zusammenarbeit behindert.
Andererseits kann mehr Freiheit in der Ausdrucksweise auch zu innovativem Code führen, der sich dann als *Best-Practice* herausstellt und zum neuen Standard wird.

Es gibt Sprachen die kompakt sind dafür aber impliziert Dinge annehmen und Sprachen die viel Text erfordern, dafür aber wenig implizieren.
Kompakte Sprachen integrieren oft etablierte Praktiken bzw. immer wiederkehrende Codestrukturen (**Muster**).
Für den Einstieg sind kompakte Sprachen oder kompakter Code oft ein Hindernis.
Doch je erfahrener man mit der Sprache wird, desto lästiger wird das immer gleiche Getippe.
Nach meiner Erfahrung nimmt die Kompaktheit mit der Lebensdauer einer Sprache zu.

````{exercise} Kompaktheit
:label: compact-code-exercise
Welchen der beiden Codeteile würden Sie als kompakt bezeichnen?
Welcher ist Ihrer Meinung nach lesbarer?

```python
numbers = [i for i in range(100)]
```

```python
numbers = []
for i in range(100):
    numbers.append(i)
```

(Das Resultat ist identisch)
````

Hat jede Sprache Vor- und Nachteile?
Zu bestimmten Zeiten sicherlich.
Doch kann es auch passieren, dass eine Sprache ganz von der Bildfläche verschwindet, da sie gegenüber neuen Sprachen keine Vorteile mehr mit sich bringt.
Irgendwann kann die Zeit kommen die Logik eines alten Programmiercodes, der immernoch erweitert wird, in einer neuen Sprache umzusetzen.
Kaum noch jemand schreibt heute ``Perl``-Skripte oder beginnt ein neues Projekt mit ``Fortran``.