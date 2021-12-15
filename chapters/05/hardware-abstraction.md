# Abstraktion der Hardware

Bis jetzt haben wir von Informationen im Binärsystem gesprochen, von Registern, Speicheradressen, Befehlszähler und Gattern, doch unser ``Python``-Code beinhaltet nichts von alledem.
Weshalb sieht unser Programmiercode so anders aus?

Ein Programm liegt als Binärcode im Arbeitsspeicher, doch wir Menschen können kein Programm in diesem Format schreiben bzw. lesen.
Wir brauchen erkennbare Strukturen.
Eine reine Folge aus $0$ und $1$ erscheint uns wie ein strukturloses chaotisches Informationsrauschen.
Programmiersprachen abstrahieren die Hardware eines Computers, sodass wir Befehle sehr abstrakt beschreiben können.
Der folgende Code beispielsweise

```python
x = 1 + 2
```

Berechnet $1 + 2$ und speichert das Resultat in der Variable $x$ ab.

Andere Programme sogenannte Interpreter oder Compiler übersetzen diesen Code schlussendlich in eine Folge aus $0$ und $1$, welche der Computer versteht.
Wie die Berechnung genau durch die Hardware realisiert wird (z.B. in welches Register welcher Wert geschrieben wird), können wir kaum beeinflussen.
Doch ist garantiert, dass wir durch ``x`` auf das Ergebnis der Rechnung zugreifen können, d.h. durch ``x`` können wir auf einen Speicherbereich des *Arbeitsspeichers* zugreifen indem der Wert ``3`` liegt.

Wie dies genau realisiert ist (wo der Wert im Speicher zu finden ist) hängt von der Programmiersprache und dem Zustand der Maschine ab.
Unterschiedliche Programmiersprachen bieten unterschiedlich viel Kontrolle über die tatsächliche Realisierung und zugleich unterschiedlich viel Abstraktion.
Hohe Abstraktion bedeutet weniger Kontrolle.

Weshalb lohnt sich der Blick in die Funktionsweise des Computers dennoch?
Um zu verstehen wie ihr Code durch die Maschine realisiert wird, brauchen Sie ein grobes konzeptionelles Verständnis des Computers.
Selbst abstrakte Hochsprachen verwenden Strukturen, die aus der konkreten Hardware hervorgehen.
Zum Beispiel werden Listen oder sog. Arrays oft als zusammenhängender Speicher realisiert.
Verstehen Sie wie ein Computer funktioniert, verstehen Sie oft die Limitierungen verschiedener Sprachen besser.
Sie erkennen auf welcher Abstraktionsebene Sie sich befinden und was auf dieser Ebene möglich sein sollte.
Zum Beispiel können Sie in ``Python`` keinen Speicher direkt adressieren, deshalb könnte Ihnen klar sein, dass Sie sich um die Speicherverwaltung im Allgemeinen kaum kümmern müssen.
In ``C`` oder ``C++`` haben Sie die Möglichkeit mit Speicheradressen direkt zu arbeiten, jedoch müssen Sie in diesen Sprachen Speicher selbst explizit reservieren und vor allem wieder freigeben.

Ein weiterer wesentlicher Punkt ist, dass Hardware in Stein gegossenes *Computational Thinking* ist.
Viele Forscher\*innen und Entwickler\*innen haben Hardware immer weiter optimiert und neue innovative Ideen entwickelt um noch mehr aus den Bauteilen herauszuholen.
Durch den Blick in die Funktionsweise der Hardware können Sie demnach viele nützliche algorithmische Denkmuster studieren.
Von *Branch-Prediction* über *Paging-Strategien* oder dem vollziehen einer Art von Berechnung auf vielen Datensätzen (*Single Instruction Multiple Data*) bis hin zu *Caching-Techniken*, Hardware bietet eine Sammlung wichtiger Algorithmen die ineinander wirken.

Zu guter Letzt möchten wir noch anmerken, dass Sie durch Kenntnisse über die Funktionsweise des Computers den Respekt vor ihm verlieren.
Sie entmystifizieren die magische Box und wagen vielleicht mehr und mehr Experimente, tauchen tiefer und tiefer ein und werden mehr und mehr zum Steuermann oder zur Steuerfrau der Maschine.