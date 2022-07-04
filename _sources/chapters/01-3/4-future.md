# Ausblick

Das [Computational Thinking](sec-what-is-ct) hat sich über die Jahrhunderte weiterentwickelt, doch blieben die wesentlichen Grundkonzepte: Dekomposition, Abstraktion, Mustererkennung und Algorithmen erhalten.
Das wird sich auch in absehbarer Zukunft nicht verändern.

Was sich verändert, sind technische Entwicklungen und neue Algorithmen -- d.h. Hard- und Software.
Auf der Softwareseite sind insbesondere Algorithmen aus dem Bereich des *maschinellen Lernens* zu nennen.
Hier feierten wir große Erfolge aber es wird auch deutlich, dass wir durch die immensen Rechenanforderungen und den damit verbundenen und stetig steigenden Energieverbrauch in der nahen Zukunft ein weiteres ökologisches Problem ansteuern.
Ob das *maschinelle Lernen* uns bei der Energiewende wie auch bei der Eindämmung des Klimawandels behilflich sein kann oder sich als hinderlich erweisen wird, ist eine noch offene Forschungsfrage.

Ein Bereich welcher sich unter anderem dem Energieproblem widmet, ist der des *Neuromorphic Computings*.
Anstatt mühsam *neuronale Netze* auf einer [von Neumann Architektur](sec-von-neumann) zu simulieren ist es Ziel, neuronale Netze direkt in Hardware zu gießen.
Das menschliche Gehirn ist zu ganz erstaunlichen Berechnungen fähig und verbraucht dabei gerade einmal 20 Watt.
Computer basierend auf der von Neumann Architektur und operieren wesentlich anders. 
Unter anderem benötigen sie durch die strikte Trennung zwischen Speicher und Recheneinheit sehr viel mehr Energie, um Daten zur Recheneinheit und wieder zurück zu befördern.
Auch sind sie nicht im Stande persistent (ohne Stromzufuhr) ihren schnellen Speicher und die Arbeitsweise ihrer Recheneinheiten zu verändern, d.h., zu lernen.
Ein in Hardware gegossenes neuronalen Netz klingt deshalb nach einer vielversprechenden Idee um effizient und stromsparend dedizierte Berechnungen durchführen zu können.

Ein weiteres Schlagwort, was insbesondere durch die Medienlandschaft kreist, ist das sog. *Quantum Computing*.
Die Entwicklung um die Quantencomputer begann bereits 1980.
Anstatt der klassischen Bits, basieren Quantencomputer auf sog. *Qubits*.
Diese Qubits befinden sich, anders als klassische Bits nicht in einem von zwei Zuständen (0 oder 1), sondern in mehreren Zuständen zugleich.
Misst man den Zustand des Qubits, zerfällt es mit einer bestimmten Wahrscheinlichkeit in den einen oder anderen Zustand.
Diese Wahrscheinlichkeiten können durch Logikgatter manipuliert werden.
Zusätzlich können Qubits verschränkt werden.
Sehr vereinfacht ausgedrückt bedeutet dies, dass deren Werte beim Messen alle bestimmt werden und voneinander abhängen. 
Die Änderung der Qibits kann sich somit in *Überlichtgeschwindigkeit* ausbreiten.
Deshalb kann man $2^{10}$ Zustände **gleichzeitig** mit nur $10$ Qubits speichern.
Die Entwicklung von Quantenalgorithmen gestaltet sich allerdings als schwierig, da man die Wahrscheinlichkeiten der verschränkten Qubits verändern muss.
Auch braucht man häufig mehrere Durchläufe, da das richtige Ergebnis nur zu einer hohen Wahrscheinlichkeit ausgegeben wird.
Zudem müssen Qubits vor minimalen Erschütterungen geschützt und auf Temperaturen nahe am absoluten Nullpunkt herabgekühlt werden -- das Handy mit einem Quantencomputerchip bleibt deshalb vorerst ein Traum.

Im Oktober 2019, behaupteten Google AI Quantum und die NASA, dass sie ein Problem auf einem Quantencomputer gelöst hätten, und zwar $3 \cdot 10^{6}$ schneller als auf jedem verfügbaren klassischen existierenden Supercomputer auf dieser Welt.
Das Resultat ist Gegenstand laufender Diskussionen.
Weitere Spieler in der Quantencomputerwelt zogen seither nach.
Derzeit sind die zu lösenden Probleme noch speziell auf Quantencomputer angepasst, z.B., die Simulation von Quanteneffekten oder die Generierung von Zufallszahlen.

Die Hoffnung ist groß.
Quantencomputer sollen uns in ein neues Zeitalter befördern, doch fehlt heute noch jedwede Bestätigung, dass Quantencomputer in der Breite Anwendung finden.
Der US-amerikanische Physiker Richard Feynman begann mit der Idee der Quantencomputer, da Simulationen von Quanteneffekten auf klassischen Computern schnell zu einem zu hohen Rechenaufwand führten.
Vielleicht liegt hierin die beste Anwendungen der Technologie -- die Simulation des Kleinen.
Es gibt zwar schon funktionierende Quantencomputer, allerdings braucht es für interessante Anwendungen noch deutlich mehr Qubits und hier liegt wohl die Herausforderung begraben.
So kritisiert der russische Physiker Mikhail Dyakonov, dass die Komplexität der Kontrolle der Qubits mit ihrer Anzahl ins unermessliche steige:

>So the number of continuous parameters describing the state of such a useful quantum computer at any given moment must be... about $10^{300}$... Could we ever learn to control the more than $10^{300}$ continuously variable parameters defining the quantum state of such a system? My answer is simple. No, never. --  Mikhail Dyakonov

Zugleich wird dieser von seinen Kolleg\*innen kritisiert.
Er mache falsche oder fehlgeleitete Aussagen.
In einem Artikel *The Case Against ‘The Case Against Quantum Computing’* reagiert Ben Criger (damals Postdoc der *TU Delft*) mit aufklärerischen Mitteln und erklärt zugleich weshalb die Kritik soviel Anklang findet:

>We lament the lack of well-founded criticism, but how often, and how loudly, do we lament the abundance of unfounded optimism? Are these two things not equally dangerous to the progress of science? We’re the people best able to criticise quantum computing, is it then our responsibility to do so? -- Ben Criger

Die haltlose, da fehlerhafte Kritik, findet ihren Anklang da sie auf haltlosen Optimismus prallt.
Ob Quantencomputer auf spezielle aber interessante Probleme angewendet werden können oder ob sie darüber hinaus auch für generelle Zwecke ihre Anwendung finden, bleibt abzuwarten.
Wir dürfen hoffen, mehr aber **noch** nicht.