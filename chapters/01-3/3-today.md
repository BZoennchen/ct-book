(sec-history-today)=
# 19. Jahrhundert bis heute

1842 entwarf die britische Mathematikerin Ada Lovelace einen Algorithmus, mit welchem Bernoulli-Zahlen mit einer Rechenmaschine (Analytical Engine) berechnet werden konnten.
Die Maschine wurde zu ihrer Lebzeit nie gebaut.
Ada Lovelace gilt heute als die erste Programmiererin und wurde mit dem Namen der Programmiersprache ``Ada`` gewürdigt.

Es sei an dieser Stelle erwähnt, dass Frauen der Zugang zu Bildung und einer Hochschulausbildung aus verschiedenen Gründen bis ins 20. Jahrhundert verwehrt wurde und sie auf männliche Hilfe angewiesen waren.
Eine große Ausnahme stellt die griechische spätantike Mathematikerin, Astronomin und Philosophin Hypatia dar, welche aus politisch-religösen Gründen in Alexandria ermordet wurde. 

```{figure} ../../figs/history/ada-lovelace.jpeg
---
height: 150px
name: ada-lovelace
---
Erste bekannte Programmiererin Ada Lovelace.
```

1847 führte der englische Mathematiker und Philosoph Georg Boole in seinem Buch *The Mathematical Analysis of Logic* die sog. boolsche Algebra ein.
Insbesondere die *zweielementige boolsche Algebra* mit den Elementen 0 und 1, welche Anwendung in der Aussagenlogik hat, sollte sich als Meilenstein der bis dato noch nicht existierenden Informatik herausstellen.
Die *zweielementige boolsche Algebra* ist Teil jeder modernen Programmiersprache.
Zusätzlich beruhen auf ihr alle (auch arithmetische) Operationen des Computers.

Um 1930 beobachtete Claude Shannon, dass sich die Regeln der boolschen Algebra auf elektrische Schaltungen übertragen lassen.
In fast allen digitalen Computern stellen elektrische Schaltungen die physikalische Manifestation boolscher Operationen dar.

Im 19. Jahrhundert konzipierte der Vater des Computers und Ingenieur, Charles Baddage, den ersten mechanischen Computer.
Baddage war seiner Zeit weit voraus.
Programme und Daten seiner Maschine sollten per Lochkarten eingelesen werden.
Die Machine sollte ihre Ergebnisse per Ausdruck ausgeben.
Baddage's mechanischer Computer war bereits [Turing-vollständig](def-turing-complete) und konnte daher theoretisch all das berechnen, was heutige Computer berechnen können.
Da ihm jedoch zu wenig finanzielle Mittel zur Verfügung standen, sollte es erst seinem Sohn im Jahr 1888 gelingen, eine vereinfachte Variante der Machine herzustellen.
Zu jener Zeit war die Entwicklung analoger Computer bereits rückläufig.

Die Theoretiker sollten, nach Baddage's Konzeption, zu den Ingenieuren wieder aufstoßen.
Anstoß dazu gaben David Hilbert und Wilhelm Ackermann, die 1928 das sog. *Entscheidungsproblem* formulierten.
Es ist ein Problem, welche wie kein zweites die Logik und Informatik verbindet:

```{admonition} Das Entscheidungsproblem
:class: definition
:name: def-decision-problem
Das Entscheidungsproblem verlangt nach der Beantwortung der Frage ob ein Algorithmus existiert, der für jedes Element einer vorgegebenen Menge beantworten kann, ob eine vorgegebene Eigenschaft zutrifft oder nicht?
```

Der österreichische Mathematiker Kurt Gödel beantwortet die Frage mit einem *nein* und sowohl Alonzo Church wie auch Alan Turing veröffentlichen unabhängige Beiträge, die zeigen, dass das *Entscheidungsproblem* nicht zu lösen ist, sofern alles was *[grundsätzlich berechenbar](def-computable)* ist, sich mit dem deckt, was *[Turing-berechenbar](def-turing-computable)* ist.
Diese Annahme wird als *[Church-Turing-These](def-church-these)* bezeichnet.
Trifft die These zu, kann alles was *grundsätzlich berechenbar* ist auch von einem *[Turing-vollständigen](def-turing-complete)* Computer (jedem modernen Computer) berechnet werden.

Über das *Entscheidungsproblem* konnte Turing die Fragestellung des sog. [Halteproblem](def-halting-problem) beantworten.
Es wird demnach keinen Algorithmus geben können, der für jedes beliebige Programm mit beliebiger Eingabewerte festellen kann ob dieses Programm jemals hält oder nicht.
Für uns als Programmierer\*innen bedeutet dies, dass wir selbst prüfen müssen ob unser Algorithmus das berechnet und vollzieht was vorgesehen ist.
Es gibt keine Software, die uns für einen beliebigen Quellcode sagen kann ob wir eine Endlosschleife programmiert haben.

```{figure} ../../figs/history/goedel-church-turing.png
---
height: 150px
name: goedel-church-turing
---
Mathematiker Kurt Gödel, Alonzo Church und Alan Turing, Quellen: [1](https://commons.wikimedia.org/wiki/File:1925_kurt_g%C3%B6del.png), [2](https://en.wikipedia.org/wiki/File:Alonzo_Church.jpg), [3](https://commons.wikimedia.org/wiki/File:Alan_Turing_Aged_16.jpg).
```

Was aus dem theoretischen Diskurs hervorging waren jedoch nicht nur zerstörte Träume, sondern auch neue fruchtbare Theorien, die das Fundament der Informatik und damit auch des künftigen Computational Thinkings prägen sollten.
Alan Turing entwickelte mit seiner *[Turingmaschine](info-turingmaschine)* ein sehr konkretes Modell für einen Computer, welcher im Stande war all das zu berechnen, was heute moderne Computer berechnen können.
Durch jenes Modell kann man noch heute prüfen ob konkrete Ingenieurskonstruktionen den Ansprüchen der *Turing-Vollständigkeit* genügen.
Schon zu dieser Zeit belegt seine *universellen Turingmaschine* den fließenden Übergang zwischen Hard- und Software.
Mit seiner Arbeit beeinflusste Turing imperative Programmiersprachen maßgeblich, wohingegen sein Doktorvater, Alonzo Church, mit dem *Lambda-Kalkül* *funktionale Programmiersprachen* ins Leben rufen sollte.

Aus der Frage der Berechenbarkeit folgte unweigerlich die Frage der Komplexität, also wie *schwer* ein Problem ist und wie dies zu messen ist.
Lassen sich Probleme anhand ihrer *Komplexität* vergleichen?
Was ist einfacher: Sudoku oder Karten sortieren?
Außerdem ergaben sich auch neue philosophische Fragen wie: Ist der menschliche Geist ein Informationsverarbeitungsprozess? Ist gar die Natur ein solcher Prozess oder kann sie zumindest als solcher modelliert werden?
Ähnliche Fragen entstanden als die Mechanik ihren Siegeszug antrat.
Zu dieser Zeit stellte man sich das menschliche Gehirn als eine Art Uhr vor.
Inwieweit sich dieser Computationalismus bestätigt oder widerlegt bleibt abzuwarten.

```{figure} ../../figs/history/model-of-a-tm.jpeg
---
height: 200px
name: model-of-a-tm
---
Eine konkrete Konstruktion einer Turingmaschine, [Quelle](https://de.wikipedia.org/wiki/Turingmaschine#/media/Datei:Model_of_a_Turing_machine.jpg).
```

Von den Ingenieuren wurden diese theoretischen Erfolge zunächst kaum beachtet.
Stattdessen wurde vieles ausprobiert.
Konrad Zuse stellte 1939 einen der ersten auf Relais basierte elektromechanischen Computer her.
Als die Zuverlässigkeit der Relais sichergestellt war, entwickelte Zuse den Z3, welcher mit einer Taktfrequenz von 5-10 Hz Gleitkommazahlen verarbeiten konnte.
Anders als Baddage's machanischer Computer war der Z3 jedoch nicht *Turing-vollständig*.

Zwischen 1942 und 1944, während des tobenden zweiten Weltkriegs, wurde die Überlegenheit der Maschinen gegenüber dem menschlichen Computer deutlich.
Um die Kommunikation der deutschen Wehrmacht zu entschlüsseln wurden große Anstrengungen unternommen.
Zu dieser Zeit war die Tätigkeit des Programmierens fast ausschließlich in der Hand von Frauen.
Sie wurde als Bürotätigkeit angesehen, weshalb sie (wegen des damaligen Frauenbildes) an Frauen delegiert wurde.
Zudem fiel die Bezahlung der Frauen deutlich geringer aus und so konnten Kosten gespart werden.
Frauen wurden sehr häufig auch als menschliche Computer eingestellt, ihre Erfolge gingen in der Geschichte leider oft unter.

```{figure} ../../figs/history/turing-bomb.jpeg
---
height: 150px
name: turing-bomb
---
Die sog. Turing-Bombe, welche für die Entschlüsselung der Enigma verwendet wurde, [Quelle](https://commons.wikimedia.org/wiki/File:Wartime_picture_of_a_Bletchley_Park_Bombe.jpg).
```

Zur Zeit des Weltkriegs gelang es den Codeknackern um Alan Turing die Verschlüsselung der Enigma zu schlagen.
Etwas später wurde auch der Code der Lorenz SZ 40/42 durch Max Newman und seiner Gruppe geknackt.
Beide Gruppen konnten diesen Erfolg nur durch die Rechenleistung ihrer Maschinen erzielen.
Daraus ging nicht nur ein wichtiger strategischer Vorteil hervor, sondern auch der erste elektrisch-digitale programmierbare Computer.
Die USA zogen mit einer sehr ähnlichen Konstruktion, der ENIAC, nach.
Beide Maschinen waren *Turing-vollständig*.
Für den Erfolg der ENIAC wurden Kathleen McNulty Mauchly Antonelli, Jean Bartik, Frances Elizabeth Holberton, Marlyn Meltzer, Frances Spence und Ruth Teitelbaum über 50 Jahre nach ihren männlichen Kollegen ausgezeichnet.

```{figure} ../../figs/history/eniac-programmiererinnen.png
---
height: 150px
name: eniac-programmiererinnen
---
ENIAC-Programmiererinnen Marlyn Wescoff und Ruth Lichterman, [Quelle](https://commons.wikimedia.org/wiki/File:Reprogramming_ENIAC.png).
```

Im Jahr 1945 begann Turing mit seiner Arbeit an der Entwicklung eines elektronisch-programmierbaren Computers mit Speicher.
Zur gleichen Zeit notierte der charismatische John von Neumann auf einem 101-seitigen Dokument einen ähnlichen Entwurf.
Dieser ist heute unter dem Namen *[von Neumann Architektur](sec-von-neumann)* bekannt.
Auf jener Architektur basieren heute nahezu alle modernen Computer und auch zukünftige Maschinen werden seinem Entwurf noch eine Zeit lang folgen.
Weitere konzeptuelle Entwicklungen sollten folgen, doch die grobe Architektur blieb seither nahezu unberührt.

```{figure} ../../figs/digital-computer/informationcycle/von-neumann-architecture.png
---
height: 300px
name: von-neumann-architecture
---
Die Von-Neumann-Architektur.
```

In den darauffolgenden Jahren waren es insbesondere Entwicklungen von neuen Bauteilen, wie Transistoren und integrierten Schaltkreisen, die die Leistungsfähigkeit der Computer immer weiter verbesserten.
Die Bauteile wurden stetig kleiner und die Taktrate der Rechner wurde immer weiter in die Höhe getrieben.
Kleinere Bauteile verbrauchen weniger Energie und so explodierte der Energieverbrauch trotz der immer besseren Rechenkapazität bzw. Rechengeschwindigkeit nicht.

Um 2006 brach der Zusammenhang zwischen höherer Taktfrequenz und gleichbleibendem Stromverbrauch jedoch zusammen.
Dies bezeichnete man als den Zusammenbruch der sog. *Dennard Skalierung*.
Dennard bemerkte 1974, dass die notwendige Spannung und der nötige Strom sich proportional zur linearen Dimension der Transistoren verhielt.
In anderen Worten, die notwendige Leistung sollte proportional zur Fläche des Transistors sein.
Ist diese kleiner, bedarf es auch weniger Leistung.
Diese Annahme stellte sich ab einer bestimmten Größe jedoch als falsch heraus.
Die Wärmeentwicklung der dicht bepackten Chips stieg mit steigender Taktfrequenz an.
Mehr und mehr Kühlung wurde notwendig, was wiederum den Stromverbrauch in die Höhe trieb.
Faktisch ist die Taktrate der Prozessoren auf ca. 4 GHz limitiert.

Dennoch werden noch heute die Transistoren immer kleiner, d.h. das *Mooresche Gesetz* gilt (teilweise) noch immer, doch erzielen wir eine bessere Rechengeschwindigkeit durch andere Effekte, wie etwa die Parallelität oder bessere Cachverfahren.
Aus diesen Gründen konzentrieren sich Chiphersteller schon eine Weile auf Mehrkernprozessoren, eine Entwicklung die sich auch auf die Programmiersprachen ausgedehnt hat.
Allerdings können wir die Parallelität nicht überall nutzen und die Verwendung von mehreren Kernen verursacht auch immer einen gewissen Verwaltungsaufwand -- ein Teil jedes Programms wird immer sequenziell ausgeführt.

Es wird erwartet, dass irgendwann auch das *Mooresche Gesetz* zusammenbricht.
Anzeichen sind bereits klar erkennbar, denn die Rate, in welcher sich die Leistung der Rechner verdoppelt beginnt zu sinken.
Dies könnte zu einem rapiden Anstieg des Energiebedarfs der Prozessoren führen.
Im Hinblick auf die Klimakrise könnte dies zu einer starken Verringerung der ansteigenden Rechnerleistung führen.
Abhilfe verspricht man sich durch die *Quantencomputer*.

Algorithmisch gab es unzählige Entwicklungen.
Was aber heute in aller Munde ist, stammt aus dem Bereich des *maschinellen Lernens*.
Schon in den 1940er Jahren wurde versucht die Informationsverarbeitung am Beispiel des menschlichen Gehirns zu modellieren. 
Dieser Ansatz wurde durch die Hirnforschung inspiriert.
Die Idee war und ist es, eine riesige Anzahl an hochgradig vernetzten aber relativ simplen Neuronen durch Software zu simulieren.
Die Idee der *künstlichen neuronalen Netze* (engl. *artificial neuronal network (ANN)*) war geboren.

```{figure} ../../figs/history/ann.png
---
width: 300px
name: fig-ann
---
Skizze eines künstliches neuronalen Netzes.
```

Um 1960 wurde eine wichtige Erweiterung der *neuronalen Netze*, die sog. *tiefen neuronalen Netze* (engl. *deep neural networks (DNN)*), vorgeschlagen.
Anders als herkömmliche neuronale Netze (siehe {numref}`Abbildung {number} <fig-ann>` ) bestehen diese aus mehrere *verschteckten Schichten*.
Zu jener Zeit fehlten allerdings die Daten und die Rechenleistung, um derartige *DNNs* praktisch nutzen zu können.
Erst in den 80er Jahren wurden erste *künstliche neuronalen Netze* entwickelt (*LeNet* 2011, {cite}`lecun:1989`).
*ANNs* bilden eine Teilmenge der Algorithmen des *maschinelles Lernen*.
Tom Mitchell definiert *maschinelles Lernen* wie folgt:

Ein Computerprogramm lernt von der Erfahrung $E$ in Bezug auf eine Klasse von Aufgaben $T$ und einer Bewertungsmetrik $P$, wenn dessen Fähigkeit die Aufgaben $T$ zu lösen, sich in Bezug auf die Bewertungsmetrik $P$, mit der Erfahrung $E$, verbessert. -- Tom Mitchell, 1997

Der wesentliche Unterschied zwischen einem klassischen Algorithmus und dem *maschinellen Lernen* ist somit in seinen Augen, dass sich der Algorithmus anhand der Daten, die er verarbeitet, selbständig anpasst -- er lernt von seinen Erfahrungen.
Ein sehr einfaches Beispiel ist der sog. *Spamfilter*.
Ein Spamfilter befolgt keine fest eingebrannten Regeln, sondern *lernt* was Spam und was kein Spam ist, indem wir E-Mails als Spam markieren.
Er benötigt *Trainingsdaten* und kann dann neue Daten selbständig *klassifizieren*.

Insbesondere *tiefen neuronalen Netze (DNNs)* konnten erfolgreich für Aufgaben eingesetzt werden, die zuvor als unlösbar galten.
Zu nennen ist die Sprach- (*Microsoft* 2011) und Bilderkennung (*AlexNet* 2012, {cite}`ciresan:2012`).
Der Erfolg ist auf drei Faktoren zurückzuführen: 
Zu nennen ist die hohe Datenmenge.
*Facebook* sammelt täglich etwa 350 Millionen Bilder und *YouTube* ca. 300 Stunden Videomaterial pro Minute.
Durch die Integration der Technik in unser alltägliches Leben, bekannt unter dem Schlagwort *Internet der Dinge* (engl. *Internet of Things* (IoT)), können und werden weitere Daten von einem anderen Typ bzw. von einer anderen Qualität gesammelt.
Der zweite Faktor ist die hohe Rechenleistung, die uns in den letzten Jahren zur Verfügung stand.
Sie erlaubt es uns die Algorithmen aus den 80er Jahren auf jene Daten loszulassen.
Diese Algorithmen sind im Stande Strukturen in jenen Daten zu finden.
Der dritte wesentliche Faktor stellt die anfängliche Erfolgsgeschichte dar.
Keiner wusste so recht, ob diese Netze tatsächlich nützlich sind.
Die überraschend guten Resultate führten zu einer Flut an Entwicklungen neuer [Algorithmen](def-algorithm) und Open-Source-Bibliotheken.
Insbesondere das ``Python``-Ökosystem wurde befüllt.

```{figure} ../../figs/history/ai-context.png
---
width: 300px
name: fig-ai-context
---
```

Das *maschinelle Lernen* ist wiederum eine Unterkategorie der *künstlichen Intelligenz (KI)* (engl. *artificial intelligence (AI)*).
Der Begriff wurde 1956 von *John McCarthy* eingeführt.

[Es sei das Ziel von künstlicher Intelligenz], intelligentes menschliches Verhalten durch Computerprogramme (künstlich) nachzubilden. -- John McCarthy

Die Themen *KI* im Allgemeinen und *maschinelles Lernen* im Besonderen werden uns auch in Zukunft noch beschäftigen.
Die bisherigen Erfolge sind vielversprechend und möglicherweise können uns diese Algorithmen in vielen Bereichen eine echte Stütze sein.
Dabei sollten wir einen gesunden Umgang mit KI-Systemen entwickeln.
Fragen der Ethik, Ökologie und sozialer Gerechtigkeit müssen in diesem Zuge ihren Platz im Diskurs finden.
Das *maschinelle Lernen* wird sich auf all jene Bereiche ausbreiten für die wir große Datenmengen gesammelt haben oder sammeln können.
Anbieter können so ihre Produkte optimieren -- was auch immer das im Einzelnen bedeuten mag.
KI kann uns möglicherweise Helfen die Erderwärmung zu reduzieren, gleichzeitig benötigen diese daten- und energiehungrigen Algorithmen viele Ressourcen.
Diese Spannung zwischen Nutzen und Kosten müssen wir beleuchten.

Daten sind heute ein echtes Wirtschaftsgut.
Uns allen sollte bewusst sein, dass diese immense, oft undurchsichtige Datensammlung auch ihre Schattenseiten hat.
Insbesondere wenn *personenbezogene Daten* gesammelt werden, müssen wir kritisch hinterfragen was mit diesen Daten gemacht wird und ob wir mit dieser Entwicklung einverstanden sind.
Auch hängt die Qualität der Entscheidung eines lernenden Algorithmus von dessen Erfahrungen, d.h., den (Trainings-)Daten ab.
Diskriminierungen, welche sich in den Daten finden, werden auch lernende Algorithmen durch die Reproduktion von Stereotypen übernehmen.