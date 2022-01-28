(history-today)=
# 19. Jahrundert bis heute

1842 entwarf die britische Mathematikerin Ada Lovelace einen Algorithmus, mit welchem Bernoulli-Zahlen mit einer Rechenmaschine (Analytical Engine) berechnet werden konnten.
Die Maschine wurde zu ihrer Lebzeit nie gebaut.
Sie gilt heute als die erste Programmiererin und wurde mit dem Namen der Programmiersprache Ada gewürdigt.
Es sei hier erwähnt, dass Frauen der Zugang zu Bildung und Hochschulausbildung aus verschiedenen Gründen bis ins 20. Jahrhundert verwehrt wurde und sie auf männliche Hilfe angewiesen waren.
Eine große Ausnahme stellt die griechische spätantike Mathematikerin, Astronomin und Philosophin Hypatia dar, welche aus politisch-religösen Gründen ermordet wurde. 

```{figure} ../../figs/ada-lovelace.jpeg
---
height: 150px
name: ada-lovelace
---
Erste bekannte Programmiererin Ada Lovelace.
```

1847 führte der englische Mathematiker und Philosoph Georg Boole in seinem Buch *The Mathematical Analysis of Logic* die sog. boolsche Algebra ein.
Insbesondere die *zweielementige boolsche Algebra* mit den Elementen 0 und 1, welche Anwendungen in der Aussagenlogik hat, sollte sich als Meilenstein der bis dato noch nicht existierenden Informatik herausstellen.
Die *zweielementige boolsche Algebra* ist Teil jeder modernen Programmiersprache.
Zusätzlich beruhen auf ihr alle (auch arithmetische) Operationen des Computers.
Um 1930 beobachtete Claude Shannon, dass sich die Regeln der boolschen Algebra auf elektrische Schaltungen übertragen lassen.
In fast allen digitalen Computern stellen elektrische Schaltungen die physikalische Manifestation boolscher Operationen dar.

Im 19. Jahrhundert konzipierte der Vater des Computers und Ingenieur, Charles Baddage, den ersten mechanischen Computer.
Baddage war seiner Zeit weit voraus.
Programme und Daten seiner Maschine sollten per Lochkarten eingelesen werden.
Die Machine sollte ihre Ergebnisse per Ausdruck ausgeben.
Baddage's mechanischer Computer war bereits *Turing-vollständig* und konnte daher theoretisch all das berechnen, was heutige Computer berechnen können.
Da ihm jedoch zu wenig finanzielle Mittel zur Verfügung standen, sollte es erst seinem Sohn im Jahr 1888 gelingen eine vereinfachte Variante der Machine herzustellen.
Zu jener Zeit war die Entwicklung analoger Computer bereits rückläufig.

Die Theoretiker sollten, nach Baddage's Konzeption, zu den Ingenieuren wieder aufstoßen.
Anstoß dazu gaben David Hilbert und Wilhelm Ackermann, die 1928 das sog. *Entscheidungsproblem* formulierten.
Es ist ein Problem, welche wie kein zweites die Logik und Informatik verbindet:

```{admonition} Das Entscheidungsproblem
:class: hint
Existiert ein Algorithmus der für jedes Element einer vorgegebenen Menge beantworten kann, ob eine vorgegebene Eigenschaft zutrifft oder nicht?
```

Der österreichische Mathematiker Kurt Gödel beantwortet die Frage mit einem *nein* und sowohl Alonzo Church wie auch Alan Turing veröffentlichen unabhängige Beiträge, die zeigen, dass das *Entscheidungsproblem* nicht zu lösen ist, sofern alles was *grundsätzlich berechenbar* ist, sich mit dem deckt, was *Turing-berechenbar* ist.
Diese Annahme wird als *Church-Turing-These* bezeichnet.
Trifft die These zu ist alles was *grundsätzlich berechenbar* ist auch von einem *Turing-vollständigen* Computer (jedem modernen Computer) berechenbar.
Über das *Entscheidungsproblem* konnte Turing die Fragestellung des sog. *Halteproblem* beantworten.

```{admonition} Das Halteproblem
:class: hint
Existiert ein Algorithmus der für einen anderen beliebigen Algorithmus und einer Eingabe bestimmen kann ob dieser Algorithmus je stehen bleibt oder nicht?
```

Auch ein solcher Algorithmus wird niemals existieren.
Für uns als Programmierer\*innen bedeutet dies, dass wir selbst prüfen müssen ob unser Algorithmus das berechnet und vollzieht was vorgesehen ist.
Es gibt keine Software, die uns für einen beliebigen Quellcode sagen kann ob wir eine Endlosschleife programmiert haben.

```{figure} ../../figs/goedel-church-turing.png
---
height: 150px
name: goedel-church-turing
---
Mathematiker Kurt Gödel, Alonzo Church und Alan Turing.
```

Was aus dem theoretischem Diskurs hervorging waren jedoch nicht nur zerstörte Träume, sondern auch neue fruchtbare Theorien, die das Fundament der Informatik und damit auch des künftigen Computational Thinkings prägen sollten.
Alan Turing entwickelte mit seiner *Turingmaschine* ein sehr konkretes Modell für einen Computer, welcher im Stande war all das zu berechnen, was heute moderne Computer berechnen können.
Durch jenes Modell kann man noch heute prüfen ob konkrete Ingenieurskonstruktionen den Ansprüchen der *Turing-Vollständigkeit* genügen.
Seine *universellen Turingmaschine* zeigt schon zu dieser Zeit einen fließenden Übergang zwischen Hard- und Software.
Mit seiner Arbeit beeinflusste Turing imperative Programmiersprachen maßgeblich, wohingegen sein Doktorvater, Alonzo Church, mit dem *Lambda-Kalkül* *funktionale Programmiersprachen* ins Leben rufen sollte.

Aus der Frage der Berechenbarkeit folgte unweigerlich die Frage der Komplexität, also wie *schwer* ein Problem ist und wie dies zu messen ist.
Lassen sich Probleme anhand ihrer *Komplexität* vergleichen?
Was ist einfacher: Sudoku oder Karten sortieren?
Außerdem ergaben sich auch neue philosophische Fragen wie: Ist der menschliche Geist ein Informationsverarbeitungsprozess? Ist gar die Natur ein solcher Prozess oder kann sie zumindest als solcher modelliert werden?
Ähnliche Fragen entstanden als die Mechanik ihren Siegeszug antrat.
Zu dieser Zeit stellte man sich das menschliche Gehirn als eine Art Uhr vor.
Inwieweit sich dieser Computationalismus bestätigt oder widerlegt bleibt abzuwarten.

```{figure} ../../figs/model-of-a-tm.jpeg
---
height: 200px
name: model-of-a-tm
---
Eine konkrete Konstruktion einer Turingmaschine.
```

Von den Ingenieuren wurden diese theoretischen Erfolge zunächst kaum beachtet.
Stattdessen wurde vieles ausprobiert.
Konrad Zuse stellte 1939 einen der ersten auf Relais basierte elektromechanischen Computer her.
Als die Zuverlässigkeit der Relais sichergestellt war, entwickelte Zuse den Z3, welcher mit einer Taktfrequenz von 5-10 Hz Gleitkommazahlen verarbeiten konnte.
Anders als Baddage's machanischer Computer war der Z3 jedoch nicht *Turing-vollständig*.

Während des tobenden zweiten Weltkriegs zwischen 1942 und 1944 wurde die Überlegenheit der Maschinen gegenüber dem menschlichen Computer deutlich.
Um die Kommunikation der deutschen Wehrmacht zu entschlüsseln wurden große Anstrengungen unternommen.
Zu dieser Zeit war die Tätigkeit des Programmierens fast ausschließlich in der Hand von Frauen.
Sie wurde als Bürotätigkeit angesehen, weshalb sie (wegen des damaligen Frauenbildes) an Frauen delegiert wurde.
Zudem fiel die Bezahlung der Frauen deutlich geringer aus und so konnten Kosten gespart werden.
Frauen wurden sehr häufig auch als menschliche Computer eingestellt, ihre Erfolge gingen in der Geschichte leider oft unter.

```{figure} ../../figs/turing-bomb.jpeg
---
height: 150px
name: turing-bomb
---
Die sog. Turing-Bombe, welche für die Entschlüsselung der Enigma verwendet wurde.
```

Zur Zeit des Weltkriegs gelang es den Codeknackern um Alan Turing die Verschlüsselung der Enigma zu schlagen.
Etwas später wurde auch der Code der Lorenz SZ 40/42 durch Max Newman und seiner Gruppe geknackt.
Beide Gruppen konnten diesen Erfolg nur durch die Rechenleistung ihrer Maschinen erzielen.
Daraus ging nicht nur ein wichtiger strategischer Vorteil hervor, sondern auch der erste elektrisch-digitale programmierbare Computer.
Die USA zogen mit einer sehr ähnlichen Konstruktion, der ENIAC, nach.
Beide Maschinen waren *Turing-vollständig*.
Für den Erfolg der ENIAC wurden Kathleen McNulty Mauchly Antonelli, Jean Bartik, Frances Elizabeth Holberton, Marlyn Meltzer, Frances Spence und Ruth Teitelbaum über 50 Jahre nach ihren männlichen Kollegen ausgezeichnet.

```{figure} ../../figs/eniac-programmiererinnen.png
---
height: 150px
name: eniac-programmiererinnen
---
ENIAC-Programmiererinnen Marlyn Wescoff und Ruth Lichterman.
```

Im Jahr 1945 begann Turing mit seiner Arbeit an der Entwicklung eines elektronisch-programmierbaren Computers mit Speicher.
Zur gleichen Zeit notierte der charismatische John von Neumann auf einem 101-seitigen Dokument einen ähnlichen Entwurf.
Dieser ist heute unter dem Namen *von Neumann Architektur* bekannt.
Auf jener Architektur basieren heute nahezu alle modernen Computer und auch zukünftige Maschinen werden seinem Entwurf noch eine Zeit lang folgen.
Weitere konzeptuelle Entwicklungen sollten folgen, doch die grobe Architektur blieb seither nahezu unberührt.

```{figure} ../../figs/von-neumann-architecture.png
---
height: 300px
name: von-neumann-architecture
---
Die von Neumann Architektur.
```

In den darauffolgenden Jahren waren es insbesondere Entwicklungen von neuen Bauteilen, wie Transistoren und integrierten Schaltkreisen, die die Leistungsfähigkeit der Computer immer weiter verbesserten.
Die Bauteile wurden stetig kleiner und die Taktrate der Rechner wurde immer weiter in die Höhe getrieben.
Um 2006 brach der Zusammenhang zwischen höherer Taktfrequenz und gleichbleibendem Stromverbrauch jedoch zusammen.
Transistoren wurden immer kleiner und mehr und mehr Transistoren wurden auf einen Chip verbaut.
Ab einer bestimmten Größe änderte sich die Situation.
Mit steigender Taktfrequenz stieg die Wärmeentwicklung der Chips.
Mehr und mehr Kühlung wurde notwendig, was wiederum den Stromverbrauch in die Höhe trieb.
Verkleinern wir die Transistoren weiter, so dringen wir in die Quantenwelt vor und bekommen es mit Quanteneffekten zu tun.
Elektronen könnten dann selbst durch einen geschlossenen Transistor hindurchdringen -- wir erreichen eine harte physikalische Grenze.
Aus diesen Gründen konzentrieren sich Chiphersteller schon eine Weile auf Mehrkernprozessoren, eine Entwicklung die sich auch auf die Programmiersprachen ausgedehnt hat.
Allerdings können wir die Parallelität nicht überall nutzen und die Verwendung von mehreren Kernen verursacht auch immer einen gewissen Verwaltungsaufwand -- ein Teil jedes Programms wird immer sequenziell ausgeführt.
Abhilfe verspricht man sich durch die *Quantencomputer*.

Schon in den 1940ger Jahren wurde versucht die Informationsverarbeitung am Beispiel des menschlichen Gehirns zu modellieren. 
Dieser Ansatz wurde durch die Hirnforschung inspiriert.
Die Idee war und ist es, eine riesige Anzahl an hochgradig vernetzter aber relativ simpler Neuronen durch Software zu simulieren.
Dieser Ansatz wurde in den 80er Jahren aufgegriffen.
Zu jener Zeit fehlten allerdings die Daten und die Rechenleistung, um derartige *Neuronale Netze* praktisch nutzen zu können.

Etwa zehn Jahre später erklärt John McCarthy:

>[Es sei das Ziel von KI], intelligentes menschliches Verhalten durch Computerprogramme (künstlich) nachzubilden.

Und 1959 entwickelte Arthur L. Samuels ein Programm, welches das Spiel *Dame* erlernen konnte.
Heute ist die *künstliche Intelligenz (KI)* ein breites und interdisziplinäres Feld der Forschung und Entwicklung.

Durch die Integration der Technik in unser alltägliches Leben, bekannt unter dem Schlagwort *Internet der Dinge* (engl. Internet of Things (IoT)), in Kombination mit der damit verbundenen Datensammlung, hocken wir heute auf einer immens großen Menge an Daten.
Gleichzeitig haben wir die Rechenkapazität um die Algorithmen aus den 80ger Jahren auf jene Daten loszulassen.
Diese Algorithmen sind im Stande Strukturen in jenen Daten zu finden.
Wir verbinden damit die Schlagwörter *BigData* und *maschinelles Lernen*.

Tom Mitchell definiert *maschinelles Lernen* wie folgt:

>A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$.

Der wesentliche Unterschied zwischen einem klassischen Algorithmus und dem *maschinellen Lernen* ist somit in seinen Augen, dass sich der Algorithmus anhand der Daten, die er verarbeitet, selbständig anpasst -- er lernt von seinen Erfahrungen.
Ein sehr einfaches Beispiel ist der sog. *Spamfilter*.
Ein Spamfilter befolgt keine fest eingebrannten Regeln, sondern *lernt* was Spam und was kein Spam ist, indem wir E-Mails als Spam markieren.
Er benötigt *Trainingsdaten* und kann dann neue Daten selbständig *klassifizieren*.

Diese Entwicklung wird sich fortsetzten.
Das maschinelle Lernen wird sich auf alle Bereiche ausbreiten für die wir große Datenmengen gesammelt haben oder sammeln können.
Anbieter können so ihre Produkte optimieren -- was auch immer das im einzelnen bedeutet.
Deshalb sind Daten heute ein echtes Wirtschaftsgut.

Uns allen sollte bewusst sein, dass diese immense, oft undurchsichtige Datensammlung auch ihre Schattenseiten hat.
Insbesondere wenn *personenbezogene Daten* gesammelt werden, müssen wir kritisch hinterfragen was mit diesen Daten gemacht wird und ob wir mit dieser Entwicklung einverstanden sind.
Auch hängt die Qualität der Entscheidung eines lernenden Algorithmus von dessen Erfahrungen, d.h., Daten ab.
Diskriminierungen, welche sich in den Daten finden, werden auch lernende Algorithmen durch die Reproduktion von Stereotypen übernehmen.
