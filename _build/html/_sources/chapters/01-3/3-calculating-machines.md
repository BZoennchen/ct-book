# Rechenmaschinen

Eratosthenes (276 v. Chr. - 194 v. Chr.) war ein herausragenden Denker seiner Zeit und zugleich Leiter der Bibliothek in Alexandria.
Eines Tages, so erzählt man sich, machte er eine herausragende Entdeckung:
Er beobachtet, dass zur gleichen Zeit zwei Obelisken an verschiedenen Orten unterschiedlich lange Schatten auf die Erde werfen.
Erstaunlicherweise schloss er daraus auf die Krümmung der Erde.
Und, da die Griechen von der Perfektion des Kreises überzeugt waren, folgerte Eratosthenes, dass die Erde eine Kugel sei.
Er war sogar in der Lage die Erdkrümmung relativ genau zu berechnen und dadurch auf den Umfang der Erde zu schließen.
Um seine Berechnungen durchführen zu können bediente er sich vermutlich eines menschlichen Computers, der ihm die Strecke zwischen Alexandria und Syren (ca. 800 km) ablief und berechnete.

```{figure} ../../figs/history/earth-curvature.png
---
width: 400px
name: fig-earth-curvature
---
Eratosthenes und die Erdkrümmung.
```

Wir finden also bereits zu dieser Zeit erste Beispiele für eine computergestützte Forschung.
Für lästige und primitive Berechnungen begann man Computer zu beauftragen.
Der Begriff *Computer* sollte lange Zeit auf eine Person anstatt auf eine Maschine hindeuten.
So wurden bis Ende des zweiten Weltkrieg menschliche Computer mit Berechnungen beauftragt.
Oftmals wurde diese Aufgabe von schlecht bezahlten Frauen durchgeführt.
Das zeigt zum einen die geringe Wertschätzung der von Frauen verrichteten Arbeit, wie auch den Stellenwert der Computer.

Die Geschichte der Rechenmaschinen beginnt 2700 bis 2400 Jahre vor Christus.
Zu dieser Zeit konstruierten vermutlich die Sumerer das älteste bekannte Rechenhilfsmittel, den [Abakus](https://de.wikipedia.org/wiki/Abakus_(Rechenhilfsmittel)).
Frühe Formen des Abakus finden sich bereits in Babylonien.
Der Abakus war in anderer Form auch in China, Russland und Japan bekannt.
Er unterstützte die Menschen bei der Addition, Subtraktion, Multiplikation und Division ganzer Zahlen.
Ziel war es Rechenfehler bei einfachen Berechnungen zu verhindern.

Nach dem Zusammenbruch des römischen Reichs, der sich über eine lange Zeit erstreckte, dauert es eine Weile bis sich neue Fortschritte zeigen sollten.
Ca. 1200 nach Christus tauchte der Astrolabium, ein scheibenförmiges astronomisches Rechen- und Messinstrument, erneut auf.
Was zu Zeiten von Eratosthenes noch eine Sphärenkonstruktion war, wurde als scheibenförmige Astrolabien im griechisch-römischen Raum entwickelt.
Mit dem Astrolabium konnte man Sternenpositionen berechnen aber auch Landvermessungen und Zeitmessungen durchführen.
Zudem enthielt er oftmals eine portable Sonnenuhr.
Es ist zu vermuten, dass Theon von Alexandria (ca. 330-400 n. Chr.) zusammen mit seiner Tochter Hypatia die erste Schrift zum Astrolab verfasste.

Der iranische Forscher Al-Biruni entwickelte ca. tausend Jahre nach Christus den ersten mechanischen Mond- und Sonnenkalender.
Seine Konstruktion bestand aus Kabeln und Zahnrädern. 
Zu dieser Zeit verwendete man auch das sogenannte Planimeter um beliebige Flächeninhalte in Landkarten oder anderen Zeichnungen anzunähern.
Die zu berechnende Fläche wird dabei in viele kleine Parallelogramme und Dreiecke zerteilt und so angenähert.

```{figure} ../../figs/history/amsler-polarplanimeter.jpeg
---
height: 150px
name: fig-amsler-polarplanimeter
---
Amsler Polarplanimeter, [Quelle](https://en.wikipedia.org/wiki/Planimeter#/media/File:Amsler-Polarplanimeter-2.jpg).
```

1854 wurde das Polarplanimeter vom Ingenieur Jakob Amsler-Laffon erfunden.

Die erste wirkliche Rechenmaschine geht möglicherweise auf Leonardo da Vinco (1452-1519) zurück.
In einer Zeichnung beschreibt er ein Gerät welches eine bestimmte Anzahl an Zahnrädern die andere Zahnräder um eine Position nach zehn Runden bewegen.
Mit diesem Prinzip kann die Addition im Dezimalsystem berechnet werden.
Allerdings ist unklar ob der Apparat tatsächlich eine Rechenmaschine repräsentiert.

Die Mechanisierung einer Berechnung wurde 1617 von schottischen Mathematiker John Napier (1550-1617) beschrieben.
Er entwickelte die sog. [Napiersche Rechenstäbchen](https://de.wikipedia.org/wiki/Napiersche_Rechenst%C3%A4bchen), mit denen Multiplikationen und Divisionen durchgeführt werden können.

Der Astronom Edmund Gunter (1581-1626) erfand zwischen 1620 und 1624 einen Vorläufer des Rechenschiebers, ein so genanntes *Logarithmenlineal*.
Die Geschichte des Rechenschiebers basiert auf der Entwicklung der Logarithmen. 
Obwohl es indische Quellen aus dem 2. Jahrhundert v. Chr. gibt, in welchen bereits Logarithmen zur Basis 2 erwähnt werden, waren es der Schweizer Uhrmacher Jost Bürgi (1558–1632) und der bereits genannte John Napier, die zu Beginn des 17. Jahrhunderts das erste bekannte System zur Logarithmenberechnung unabhängig voneinander entwickelten. 
Die logarithmischen Maßstäbe des Rechenschiebers wurden auf verschiedene Geräte aufgelegt und fanden als Gunter's Line oder in der Seefahrt Gunter's Scale (oder einfach Gunter) Verbreitung.
Sie hatten auf einer Seite eine lineare Einteilung, auf der anderen eine logarithmische. Durch Aneinanderlegen in der Art des Rechenschiebers konnten damit trigonometrische Berechnungen für die Navigation ausgeführt werden.
Der Rechenschieber basiert also auf den zuvor entdeckten oder entwickelten Rechengesetzen des Logarithmus.
Nach diesen uns bekannten Gesetzen lässt sich die Multiplikation als Addition ausdrücken:

$$ \log_{10}(a \cdot b) = \log_{10}(a) + \log_{10}(b) $$

Sofern die Umkehrfunktion $\log_{10}^{-1}$ bekannt ist, lassen sich Zahlen durch Addition ihres Logarithmus multiplizieren.
Oft führte man Tabellen mit sich, welche $\log_{10}^{-1}$ für bestimmte Zahlen auflisteten.
Solche Rechenschieber finden heute noch ihre Anwendung.

1623 baute der deutsche Astronom und Mathematiker Wilhelm Schickard (1592-1635) die erste tatsächliche Rechenmaschine, um astronomische Rechnungen zu erleichtern. 
Die Maschine beherrschte das Addieren und Subtrahieren von bis zu sechsstelligen Zahlen, einen *Speicherüberlauf* signalisierte sie vermutlich durch das Läuten einer Glocke. 
Um komplexere Berechnungen (Multiplikation, Division) zu ermöglichen, waren Napiersche Rechenstäbchen in Form von Zylindern darauf angebracht, die das kleine Einmaleins zur Unterstützung der Multiplikation auf der Addiermaschine enthielten.
Die Konstruktion war bis zum 20. Jahrhundert verloren, und erst 1960 wurde eine funktionierende Replik hergestellt.

Zwischen 1642 und 1645 entwickelte Blaise Pascal die Konstruktionspläne für eine Reihe von Prototypen seiner *Pascaline*.
Die Pascaline ist eine mechanische Rechenmaschine mit Metallwählscheiben, an denen die gewünschten Nummern eingestellt werden konnten.
Die Ergebnisse erschienen in Kästchen über den Wählscheiben.
Der Prototyp hatte nur einige wenige Wählscheiben, spätere Versionen hatten eine größere Anzahl und konnten mit Zahlen bis zu 9.999.999 rechnen. Direkte Subtraktion war mit der Pascaline nicht möglich; es musste die Komplementärmethode verwendet werden.
Pascal begann mit der Arbeit an seiner Rechenmaschine, als er 19 Jahre alt war, und konstruierte sie als Arbeitserleichterung für seinen Vater, der Steuerbeamter war.

Es ist kein Zufall, dass das Leibniz-Rechenzentrum (LRZ) seinen namen von Leibniz geerbt hat, denn neben den zahlreichen Beiträgen in der Philosophie und Mathematik hatte Leibniz bereits die Idee einer alles berechnenden Maschine.
Durch den Fortschritt in der Feinmechanik sah Leibniz die rasche Entwicklung kleiner Automaten zum Anlass einen Prototypen einer Rechenmaschine zu konstruieren.
Leibniz' (1646-1716) Rechenmaschine war ein historischer Meilenstein im Bau von mechanischen Rechenmaschinen.
Das von ihm erfundene Staffelwalzenprinzip, mit dem Multiplikationen auf mechanische Weise realisiert werden konnten, hielt sich über 200 Jahre als unverzichtbare Basistechnik.
Die feinmechanischen Probleme, die es beim Bau einer solchen Maschine zu überwinden galt, waren jedoch so immens, dass berechtigte Zweifel daran bestehen, ob zu Leibniz’ Lebzeiten jemals eine fehlerfrei arbeitende Maschine realisiert werden konnte.
Im weiteren Sinne war Leibniz wegbereitend für die Rechenmaschine im heutigen Sinne, den Computer. 
Er entdeckte, dass sich Rechenprozesse viel einfacher mit einer binären Zahlencodierung durchführen lassen, und ferner, dass sich mittels des binären Zahlencodes die Prinzipien der Arithmetik mit den Prinzipien der Logik verknüpfen lassen.
Die hier erforschten Prinzipien wurden erst 230 Jahre später (z.B. bei Zuse Z1) in der Konstruktion von Rechenmaschinen eingesetzt.
Leibniz hatte beim Bau seiner Rechenmaschine, anders als frühere Erfinder\*innen, eher philosophische Motive.
Mit dem viel bemühten Zitat, 

>Es ist unwürdig, die Zeit von hervorragenden Leuten mit knechtischen Rechenarbeiten zu verschwenden, weil bei Einsatz einer Maschine auch der Einfältigste die Ergebnisse sicher hinschreiben kann. -- Leibniz

wird eine Grenze zwischen Mensch und Maschine gezogen. 
Dem Erfindergeist (Freiheit, Spontaneität und Vernunft) als das spezifisch Menschliche wird das Mechanische der technisch-natürlichen Kausalität gegenübergestellt.

Die erste massenproduzierte Rechenmaschine war die sog. [Arithmomètre](https://de.wikipedia.org/wiki/Arithmometer), eine Konstruktion eines französischen Erfinders.
Er war Hauptaktionär einer Versicherungsgesellschaft und die notwendigen Berechnungen von Versicherungsfällen bewogen ihn, sich mit dem Bau einer Rechenmaschine zu beschäftigen.
1820 ließ er das erste Modell patentieren.
Es wurde 18 000 mal verkauft.

1842 entwarf die britische Mathematikerin Ada Lovelace (1815-1852) einen Algorithmus, mit welchem Bernoulli-Zahlen mit einer Rechenmaschine (Analytical Engine) berechnet werden konnten.
Die Maschine wurde zu ihrer Lebzeit nie gebaut.
Ada Lovelace gilt heute als die erste Programmiererin und wurde mit dem Namen der Programmiersprache ``Ada`` gewürdigt.

Es sei an dieser Stelle erwähnt, dass Frauen der Zugang zu Bildung und einer Hochschulausbildung aus verschiedenen Gründen bis ins 20. Jahrhundert verwehrt wurde und sie auf männliche Hilfe angewiesen waren.
Eine große Ausnahme stellt die griechische spätantike Mathematikerin, Astronomin und Philosophin Hypatia (ca. 355-415) dar, welche aus politisch-religösen Gründen in Alexandria ermordet wurde. 

```{figure} ../../figs/history/ada-lovelace.jpeg
---
height: 150px
name: ada-lovelace
---
Erste bekannte Programmiererin Ada Lovelace.
```

Im 19. Jahrhundert konzipierte der Vater des Computers und Ingenieur, Charles Baddage (1791-1871), den ersten mechanischen Computer.
Baddage war seiner Zeit weit voraus.
Programme und Daten seiner Maschine sollten per Lochkarten eingelesen werden.
Die Maschine sollte ihre Ergebnisse per Ausdruck ausgeben.
Baddage's mechanischer Computer war bereits [Turing-vollständig](def-turing-complete) und konnte daher theoretisch all das berechnen, was heutige Computer berechnen können.
Da es ihm an finanziellen Mitteln fehlte, sollte es erst seinem Sohn im Jahr 1888 gelingen, eine vereinfachte Variante der Maschine herzustellen.
Zu jener Zeit war die Entwicklung analoger Computer bereits rückläufig.


Konrad Zuse (1910-1995) stellte 1939 einen der ersten auf Relais basierten elektromechanischen Computer her.
Als die Zuverlässigkeit der Relais sichergestellt war, entwickelte Zuse den Z3, welcher mit einer Taktfrequenz von 5-10 Hz Gleitkommazahlen verarbeiten konnte.
Anders als Baddage's machanischer Computer war der Z3 jedoch nicht *[Turing-vollständig](def-turing-complete)*.

Zwischen 1942 und 1944, während des tobenden zweiten Weltkriegs, wurde die Überlegenheit der Maschinen gegenüber dem menschlichen Computer deutlich.
Um die Kommunikation der deutschen Wehrmacht zu entschlüsseln wurden große Anstrengungen unternommen.
Zu dieser Zeit war die Tätigkeit des Programmierens fast ausschließlich in der Hand von Frauen.
Sie wurde als Bürotätigkeit angesehen.
Die Bezahlung der Frauen fiel deutlich geringer aus und so konnten Kosten gespart werden.
Frauen wurden sehr häufig auch als menschliche Computer eingestellt, ihre Erfolge gingen in der Geschichte allzu oft unter.

```{figure} ../../figs/history/turing-bomb.jpeg
---
height: 150px
name: turing-bomb
---
Die sog. Turing-Bombe, welche für die Entschlüsselung der Enigma verwendet wurde, [Quelle](https://commons.wikimedia.org/wiki/File:Wartime_picture_of_a_Bletchley_Park_Bombe.jpg).
```

Zur Zeit des Weltkriegs gelang es den Codeknacker\*innen um Alan Turing (1912-1954) die Verschlüsselung der Enigma zu schlagen.
Etwas später wurde auch der Code der Lorenz SZ 40/42 durch Max Newman (1897-1984) und seiner Gruppe geknackt.
Beide Gruppen konnten diesen Erfolg nur durch die Rechenleistung ihrer Maschinen erzielen.
Daraus ging nicht nur ein wichtiger strategischer Vorteil hervor, sondern auch der erste elektrisch-digitale programmierbare Computer.
Die USA zogen mit einer sehr ähnlichen Konstruktion, der ENIAC, nach.
Beide Maschinen waren *[Turing-vollständig](def-turing-complete)*.
Für den Erfolg der ENIAC wurden Kathleen McNulty Mauchly Antonelli, Jean Bartik, Frances Elizabeth Holberton, Marlyn Meltzer, Frances Spence und Ruth Teitelbaum über 50 Jahre nach ihren männlichen Kollegen ausgezeichnet.

```{figure} ../../figs/history/eniac-programmiererinnen.png
---
height: 150px
name: eniac-programmiererinnen
---
ENIAC-Programmiererinnen Marlyn Wescoff und Ruth Lichterman, [Quelle](https://commons.wikimedia.org/wiki/File:Reprogramming_ENIAC.png).
```

Im Jahr 1945 begann Turing mit seiner Arbeit an der Entwicklung eines elektronisch-programmierbaren Computers mit Speicher.
Zur gleichen Zeit notierte der charismatische John von Neumann (1903-1957) auf einem 101-seitigen Dokument einen ähnlichen Entwurf.
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
