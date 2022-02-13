(sec-information-flow)=
# Der Informationskreislauf

Sie kennen nun die vier grundlegenden Aufgaben eines Computers und wissen wie er aus den zwei Zuständen **Strom aus** und **Strom an** Informationen der unterschiedlichsten Art repräsentieren kann.
Zudem haben wir uns angesehen, wie aus primitiven boolschen Operationen, welche über Gatter/Schaltungen realisiert werden, komplexe Berechnungen entstehen.

Bereits an dieser Stelle wird deutlich, dass Abstraktion und Komposition eine zentrale Rolle in der Informatik spielen.
Das konkrete Rasterbild ist auf der abstrakten Ebene nichts anderes als eine Folge von $0$ und $1$.
Durch die Komposition und Hintereinanderschaltung/Wiederholung einfacher Gatter, entstehen aus primitiven Operationen komplexe Berechnungen.

Ein einfacher $n$-Bit-Addierer gleicht einem Taschenrechner, doch ist ein Taschenrechner noch kein vollwertiger Computer.
Manche Taschenrechner lassen sich zwar Programmieren, doch sind sie nicht im Stande all das zu berechnen, was wir als berechenbar wahrnehmen.
Anders als ein Taschenrechner, ist ein Computer *Turing-vollständig*.
Weshalb ist er das?
Wie wird aus Gattern, elektrischen Leitungen und dem Speicher ein vollwertiger (digitaler) Computer der alle vier grundlegenden Aspekte der *Informationsverarbeitung*

1. Informationen **einlesen**
2. Informationen **speichern**
3. Informationen **verarbeiten**
4. Informationen **ausgeben**
   
realisiert?

(sec-von-neumann)=
## Die Von-Neumann-Architektur

Bevor wir diese Frage klären brauchen wir ein konzeptionelles Verständnis der wesentlichen Bauteile und deren grundsätzlichen Interaktion.
Zusammengenommen bilden sie den *digitalen Computer*.
Eine solche Beschreibung bezeichnen wir als *Hardware-Architektur*.
Sie kann selbstverständlich unterschiedlich detailliert ausfallen.
So gibt es auch Beschreibungen einzelner Bauteile die wiederum die Interaktion ihrer Einzelkomponenten beschreiben.

Wie der Bauplan eines Hauses, in dem festgelegt ist wie Küche und Bad miteinander verbunden sind und wie die Bewohner das Gebäude nutzen können, legt eine Architektur fest über welche Leitungen beispielsweise der Speicher mit den Recheneinheiten interagiert.

```{figure} ../../figs/von-neumann-architecture.png
---
height: 300px
name: von-neumann-architecture-2
---
Die Von-Neumann-Architektur auch bekannt als Princeton Architektur.
```

Die *Von-Neumann-Architektur* ist wohl die bekannteste und zugleich meist verwendete Hardware-Architektur bzw. *Rechnerarchitektur* die den Aufbau der Computer beschreibt.
Jeder Rechner den Sie je benutzt haben basiert höchstwahrscheinlich auf dieser Architektur.

```{admonition} Arbeitsspeicher
:name: def-main-memory
:class: definition
Der *Arbeitsspeicher* oder *Hauptspeicher* oder *RAM (Random Access Memory)* eines Computers ist jener Speicher der die gerade auszuführenden **Programme** oder **Programmteile** und die dabei benötigten **Daten** enthält.
```

Die erste wichtige Komponente ist der sogenannten *Hauptspeicher*, auch *Arbeitsspeicher* genannt.
Im Bild oben haben wir *Hauptspeicher* und *Festplattenspeicher* mit Speicher zusammengefasst.
Was der unterschied dieser beiden Speicherkomponenten ist besprechen wir weiter unten.
Im *Speicher* befinden sich die Anweisungen der Informationsmanipulation, d.h. das **auszuführende Programm** als auch alle zu verarbeitenden **Daten**, welche vom Programm verarbeitet werden.

```{admonition} Bus
:name: def-bus
:class: definition
Elektrische Leitungen, über welche die [Bits](def-bit) und [Bytes](def-byte) von verschiedenen Einheiten übermittelt werden nennen wir den *Bus*.
```

Wir sprechen häufig von unterschiedlichen *Bus-Teilen*, zum Beispiel ist die Grafikkarte über den sogenannten PCI-Express Bus mit dem Rest des Computers verbunden.
Der *interne Bus* auch *Speicher-Bus* oder *System-Bus* genannt, verbindet alle internen Komponenten eines Computers mit der *Hauptplatine* (Motherboard/Mainboard).
Es gibt aber auch *Bus-Systeme* die unterschiedliche Computer oder andere Geräte (z.B. externen Speicher) miteinander verbinden.

Die *Hauptplatine* ist jenes Bauteil auf dem die CPU-nahen Komponenten (CPU, Hauptspeicher, Grafikkarte, interne Bus-Systeme) montiert werden.

Die *Kontrolleinheit* besteht aus einer Komposition von Gattern, einem *Instruktionsregister* sowie einem [Befehlszeiger](def-program-counter).
Sie fungiert als Programminterpreter oder 'Mastermind' und delegiert Aufgaben an die jeweils dafür geeigneten Recheneinheiten weiter.
Sie ließt die Programmanweisungen aus dem Hauptspeicher und realisiert diese indem sie die *arithmetische/logische Einheit* mit Instruktionen und den notwendigen, aus dem Hauptspeicher geladenen Daten versorgt.
Fließkommaoperationen delegiert die Kontrolleinheit häufig an eine spezielle (hier nicht eingezeichnete) *Fließkomma-Recheneinheit*.
Der *Befehlszeiger* beinhaltet eine Hauptspeicheradresse, die auf den aktuelle auszuführenden Befehl im Hauptspeicher zeigt. 
Der Befehl $\text{ADD}$ steht zum Beispiel für die Addition von zwei ganzen Zahlen.
Er wird allerdings im Hauptspeicher als Binärfolge abgespeichert!
Ein solcher Befehl wird aus dem Hauptspeicher ins Instruktionsregister geladen.
Die Zahlen, die addiert werden sollen, werden ebenfalls von der Kontrolleinheit aus dem Hauptspeicher in Register der arithmetische/logische Einheit geladen.
Dann wird die arithmetische/logische Einheit aktiviert.
Diese berechnet das Ergebnis und schreibt es in ein weiteres [Register](def-register).
Die Kontrolleinheit schreibt das Ergebnis an die vom Programm definierte Stelle (Adresse) im Hauptspeicher.

Die Recheneinheiten (arithmetische/logische Einheit und Fließkomma-Recheneinheit) sind ebenfalls nichts weiter als Kompositionen von Gattern (das was rechnet) kombiniert mit Registern (das was kleine Informationseinheiten enthält) die mit anderen Einheiten über den [Bus](def-bus) (das was Daten von einer Einheit zur anderen transportiert) verbunden sind.

```{admonition} Central Processing Unit (CPU)
:name: def-cpu
:class: definition
Der *Hauptprozessor* oder *Central Processing Unit (CPU)* besteht aus Leitungen (Bus), Registern, der Kontrolleinheit, der arithmetische/logische Einheit und möglicherweise spezielle Einheiten für bestimmte Berechnungen wie etwa die Fließkomma-Recheneinheit.
```

*Register* sind die kleinsten aber auch schnellsten *flüchtigen* (engl. volatile) Speichereinheiten.
Sie sind dafür gedacht die Variablen einer Operation zu halten.
Addieren wir zum Beispiel zwei Zahlen $x$ und $y$ so werden die Werte aus zwei Registern gelesen, die Gatter verrichten ihre Arbeit und legen das Ergebnis in einem neuen Register ab.
Der Programmcode hierfür könnte wie folgt aussehen:

$$\text{ADD } \text{Reg}_1 \text{ Reg}_2 \text{ Reg}_3$$

Was soviel heißt wie: Addiere Zahl in Register 1 mit Zahl in Register 2 und speicher das Ergebnis in Register 3.
Register wie auch der Hauptspeicher werden aus den gleichen elektrischen Grundbauteilen wie Gatter konstruiert.
Sogenannte *Flip-Flops* können, anders als reine Logikgatter, elektrische Einheiten stabil halten und freigeben.
Konzeptionell sind sie eine Kombination aus rückgekoppelten Logikgatter.
Für die Speicherung von Bits benötigen sie allerdings eine Stromversorgung.
Deshalb sind Register wie auch der Hauptspeicher *flüchtig* - sie verlieren alle Daten sobald die Stromverbindung unterbrochen wird.

```{admonition} Register
:name: def-register
:class: definition
*Register*, sind extrem schnelle kleine flüchtige Speichereinheiten, welche die CPU für viele Operationen verwendet.
```

Deshalb werden Programme und viele Daten als Binärcode oder in anderen Formaten auf einem *persistenten* (*nicht flüchtigen* / engl. *non-volatile*) Speicher wie einer Festplatte *persistent* gespeichert.
Sie werden vor ihrer Ausführung in den Hauptspeicher geladen.
Wie und von wem?
Das sehen wir gleich.
Die *Flüchtigkeit* der Speicher verleiht ihnen Geschwindigkeit, d.h. es ist möglich in sehr kurzer Zeit Daten von einen *flüchtigen* Speicher zu lesen und in ihn zu schreiben.
Der Geschwindigkeitsunterschied ist enorm.
Anstatt in die nächst gelegene Stadt zu reisen (Hauptspeicher), fliegen wir zum Mond (Festplattenspeicher).

```{figure} ../../figs/memory-cache-register.png
---
width: 450px
name: fig-memory-cache-register
---
Zusammenhang zwischen Größe und Geschwindigkeit der verschiedenen *flüchtigen* Speicher des Computers.
```

```{admonition} Cache
:name: def-cache
:class: definition
Ein *Cache* dient als (kleiner) Puffer.
Er enthält einen (kleinen) Teil der Daten die zeitlich gesehen gerade verwendet werden.
Er dient dazu wiederholte Zugriffe auf ein langsames Hintergrundmedium (wie den Hauptspeicher) zu vermeiden.
```

Zwischen Hauptspeicher und Register liegen weitere sehr schneller Speicher, die wir als *Cache* bezeichnen.
Für unser Verständnis der Funktionsweise können wir sie ignorieren.
Caches sind deutlich kleiner als der Hauptspeicher.
Sie beinhalten die Daten die zuletzt von der CPU verwendet wurden.
Fordert die CPU diese Daten erneut an, so ist der Zugriff über den Cache noch einmal viel schneller als über den Hauptspeicher.
Dieses Konzept wird verallgemeinert und so gibt es mehrere Caches die hintereinandergeschaltet sind.
Auch der Cache ist natürlich *flüchtig*.

```{admonition} Von-Neumann vs. Harvard-Architektur
:class: remark
:name: remark-neumann-vs-harvard

Eine weitere beachtenswerte Architektur ist die sog. *Harvard-Architektur*.
Im Unterschied zur *Von-Neumann-Architektur* hat sie zwei unterschiedliche und separierte Speicher, einen für den Programmcode und einen für die zu verarbeitenden Daten.
Das verkompliziert die Architektur und erfordert mehr Bauteile, jedoch kann die CPU **gleichzeitig** Programmcode laden als auch in den [Hauptspeicher](def-main-memory) schreiben oder aus ihm lesen.

```

Wie spielen die verschiedenen Einheiten der Architektur nun zusammen?
Folgende Beschreibung liefert eine vereinfachte konzeptionelle Antwort:

*Eingabegeräte* wandeln die eingelesenen Informationen ins Binärsystem um.
Die [CPU (Central Processing Unit)](def-cpu) manipuliert Informationen, wobei sie durch den *Speicher*, d.h. einen Zustand, unterstützt wird.
Am Ende des Informationskreislaufs wandeln *Ausgabegeräte* die verarbeiteten Informationen in Bild, Ton und andere Formate um.
Die *Ausgabe* des Computers muss nicht zum Konsum für uns Menschen gedacht sein.
Sie kann auch als *Eingabe* für andere Computer oder Maschinen dienen.

Damit die [Bits](def-bit) und [Byte](def-byte) nicht durcheinander gelesen, manipuliert und geschrieben werden ist die CPU *getaktet*.
Es gibt eine (global) tickende Uhr, die vorgibt wann die Komponenten aktiv werden können.
Bei jedem Tick oder anders gesagt, in jedem *CPU-Zyklus*, können die jeweiligen Komponenten aktiv werden.
Eine CPU die mit 3 Gigahertz (GHz) getaktet ist, führt 3 Milliarden Zyklen in der Sekunde durch.
Nicht jede Berechnung oder jeder Speichertransfer benötigt die gleiche Anzahl an Zyklen.
Zum Beispiel ist benötigt die Division zweier Zahlen deutlich mehr Zyklen als die Addition.

## Das Betriebssystem

Soweit so gut.
Wie funktioniert das aber im Detail?
Was passiert zum Beispiel, wenn ich in meinem Textverarbeitungsprogramm die Taste ``A`` drücke.
Auf dem Bildschirm erscheint ein ``A``-Zeichen, wie ist diese Magie zu erklären?
Nun bevor wir dazu kommen, müssen wir überlegen was hierzu nötig ist:

1. Der Computer muss hochgefahren sein und
2. das Textverarbeitungsprogramm muss gestartet sein.

Wie aber startet der Computer?
Wie führt er nicht nur einzelne Operationen sondern ein ganzes Programm aus?
Und wie ist es möglich, dass scheinbar gleichzeitig viele verschiedene Programme auf einem Computer laufen?
Antworten finden wir wenn wir uns das 'Masterprogramm' eines Computers ansehen: Das *Betriebssystem*.

```{admonition} Betriebssystem
:name: def-operating-system
:class: definition
Das *Betriebssystem* eines Computers ist ein spezielles Hauptprogramm, welches alle anderen Programme und die Rechnerressourcen des Computers verwaltet.
```

Das *Betriebssystem* (z.B. Ubuntu, Windows 10, Mac OS) bestimmt wann welches Programm welche Hardware nutzen darf und auf welchen Speicherbereich das jeweilige Programm und der jeweilige Benutzer zugreifen darf.
Hat ein Computer nur eine CPU (mit nur einen Kern), so erscheint es nur so als würden viele Programme gleichzeitig laufen.
In der Realität wechselt das Betriebssystem die aktiven Programme fortwährend durch.

Das *Betriebssystem* wird beim Start des Computers geladen.
Diesen Vorgang nennen wir *Booten*.
Aber wie soll das funktionieren?
Braucht es nicht ein Programm um das Betriebssystem zu laden und braucht dieses Programm nicht wieder ein Programm um es zu laden?
Befinden wir uns nicht in einem Henne-Ei-Problem?

```{admonition} Bootvorgang
:name: def-booting
:class: definition
Das Betriebssystem wird beim Start des Computers geladen.
Diesen Vorgang nennen wir *Bootenvorgang* oder kurz das *Booten*.
```

Der Schlüssel hierzu ist ein kleineres Programm was auf dem sog. *Festwertspeicher (ROM)* liegt.
Dieses Programm wird von der Hardware selbst geladen wird.
Die Logik um das erste Programm vom *Festwertspeicher* zu laden ist also in den Bauteilen selbst fest verdrahtet (Software in Hardware gegossen).
Der Festwertspeicher kann nur gelesen werden und ist nicht flüchtig.
Das heißt, das Programm auf dem Festwertspeicher bleibt auch nach dem Ausschalten des Computers vorhanden.
Der Computer zieht sich quasi wie Münchhausen an den Haaren selbst aus dem Sumpf.

(sec-run-program)=
## Programme ausführen

Starten Sie ein Programm, sagen Sie eigentlich dem Betriebssystem Sie möchten dieses oder jenes Programm ausführen.
Das *Betriebssystem* sorgt dafür, dass es in den Hauptspeicher geladen wird und teilt ihm entsprechende Ressourcen zu.
Erinnern Sie sich an die *Von-Neumann-Architektur*!
Laut dieser liegen die **Daten** als auch die **Programme** im gleichen (flüchtigen) *Hauptspeicher* bzw. *Arbeitsspeicher* (siehe {ref}`Von-Neumann-Architektur <von-neumann-architecture-2>`).
Das Programm ist nichts anderes als eine zusammenhängende Folge von $0$ und $1$, welche Befehle repräsentieren.
Zum Beispiel bedeutet 

$$\text{ADD} \ \$5 \ \$6 \ \$7,$$

dass die Zahl welche in Register $\$5$ steht mit der Zahl die in Register $\$6$ steht addiert wird und das Ergebnis in den Register $\$7$ geschrieben wird.
Andere Befehle wie etwa

$$\text{LOAD} \ \#15 \ \$5 $$

oder

$$\text{STORE} \ \$7 \ \#16 $$

laden ($\text{LOAD}$) Daten aus dem Hauptspeicher an der Adresse (Stelle) $\#15$ ins Register $\$5$ bzw. speichern ($\text{STORE}$) die Daten von Register $\$7$ im Hauptspeicher an Adresse $\#16$.

Da Informationen mit einer unvorstellbaren Geschwindigkeit durch den Computer rasen, spielt die Distanz der Bauteile zueinander eine große Rolle.
Register sind nicht nur deutlich schneller als der *Hauptspeicher* sie befinden sich auch viel näher an den Recheneinheiten.

Wenn ein benötigter Wert noch im Register liegt (eventuell von einer zuvor ausgeführten Berechnung) wird dieser nicht erneut vom [Hauptspeicher](def-main-memory) geladen.
Stattdessen benutzt die CPU den Wert im Register und gewinnt dadurch an Berechnungsgeschwindigkeit.
Sie spart sich einige Zyklen die nötig wären um die Daten aus dem Speicher in den Register zu laden.

```{figure} ../../figs/program-run.png
---
width: 700px
name: fig-program-run
---
Zusammenspiel zwischen Kontrolleinheit und arithmetische/logische Einheit, Register, Befehlszeiger (CPU) und Arbeitsspeicher.
```

Innerhalb der *Kontrolleinheit* befindet sich ein spezielles *Register*, welches die *Arbeitsspeicheradresse* des nächsten auszuführenden Befehls enthält.
Dieses Register nennen wir *Befehlszähler* oder *Befehlszeiger*.
Ist der Befehl an der angegebenen Adresse ein *Sprungbefehl* ändert sich der Wert des *Befehlszeigers* entsprechend.
Andernfalls wird der Befehl (z.B. $\text{ADD } \text{Reg}_1 \text{ Reg}_2 \text{ Reg}_3$) von der CPU ausgeführt und der *Befehlszeiger* wird um $1$ erhöht.

```{admonition} Befehlszeiger
:name: def-program-counter
:class: definition
Der *Befehlszeiger* ist ein spezielles [Register](def-register) der *Kontrolleinheit* welches die *Arbeitsspeicheradresse* des nächsten auszuführenden Befehls enthält.
```

Wenn das Betriebssystem entscheidet, dass ein anderes Programm an der Reihe ist, wird der aktuelle Zustand des laufenden Programms gesichert.
Z.B. wird der *Befehlszeiger* in den Arbeitsspeicher oder auf die Festplatte geschrieben.
Sobald das Programm wieder aktiv wird, werden alle notwendigen Daten wieder in den Hauptspeicher und die Register geladen.

```{exercise} CPU-Workflow
:label: cpu-workflow-exercise
Betrachten Sie das obige Bild {ref}`CPU-Workflow <fig-program-run>`.
Welche Befehle hat die CPU zuletzt ausgeführt und was wird der nächste Befehl bezwecken?
```

```{solution} cpu-workflow-exercise
:label: cpu-workflow-solution
:class: dropdown
Die Kontrolleinheit hat zum einen den Befehl $\text{ADD}$ inklusive der Registeradressen in Register geladen.
Dann hat sie die Werte 17 und 5, welche addiert werden sollen in Register der arithmetischen Einheit geladen.
Sie hat die arithmetischen Einheit instruiert die Addition durchzuführen und das Ergebnis in Register $\$7$ abzulegen.

Im nächsten Schritt wird die Kontrolleinheit den Wert (22) dieses Registers ($\$7$) in den Hauptspeicher an die Adresse $\#16$ schreiben und somit den Wert 5 überschreiben.
```

## Der EVA-Kreislauf

Haben wir (1) den Computer *gebootet* und (2) das Textverarbeitungsprogramm gestartet und drücken dann ``A``, was passiert dann?
Das Eingabegerät (die Tastatur) sendet eine Unterbrechungsanforderung (Interrupt Request (IRQ)) an die CPU.
Nach der Anforderung führt die CPU eine Unterbrechungsroutine aus, diese leitet das ``A`` an das Textverarbeitungsprogramm weiter.

```{admonition} Interrupt Request (IRQ)
:name: def-irq
:class: definition
Ein sog. *Interrupt* zu Deutsch *Unterbrechung* (welcher gewöhnlich von Eingabegeräten ausgelöst wird) erzeugt einen sog. *Interrupt Request (IRQ)* zu Deutsch *eine Unterbrechungsanforderung*, welche den aktuelle Programmablauf unterbricht und eine spezielle Befehlsfolge ausführt um Programme über den *Interrupt* zu informieren.
```

Das Textverarbeitungsprogramm hat sich hierfür über eine *Arbeitsspeicheradresse* für einen solchen IRQ registriert.
Das heißt, es wird der Programmcode der an dieser Adresse beginnt ausgeführt.

Über viele tausende Operationen berechnet das Textverarbeitungsprogramm wie das ``A`` dargestellt werden soll (in welcher Schriftart, und welcher Position und so weiter).
Die Darstellung besteht aus vielen Pixeln welche das Programm an den Monitor weiterleitet.
Dieser wandelt die Folge aus $0$ und $1$ in viele unterschiedlich gefärbte Pixel um.