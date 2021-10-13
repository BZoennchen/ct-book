# Antike

Die Geschichte der Computer und Algorithmen beginnt 2700 bis 2400 Jahre vor Christus.
Zu dieser Zeit konstruierten vermutlich die Sumerer das älteste bekannte Rechenhilfsmittel, den Abakus.
Er unterstützte sie bei der Addition, Subtraktion, Multikation und Division ganzer Zahlen.
Ziel war es Rechenfehler bei einfachen Berechnungen zu verhindern.
Über zweitausend Jahre später erschufen die antiken Griechen eine Art mechanisch analogen Computer -- eine ganz erstaunliche Leistung, die für die kommenden tausend Jahre einzigartig bleiben sollte.
Dieser antike Computer war dazu gedacht, bestimmte Positionen der Himmelskörper zu bestimmen.

```{figure} ../../figs/greeks.png
---
height: 150px
name: greeks
---
Denker*innen Ihrer Zeit: Euklid, Eratosthenes, Hypatia.
```

Sumerer, Ägypter, Babylonier, Chinesen, Griechen und andere antike Völker entwickelten Rechenhilfsmittel um insbesondere die Bewegung der Himmelskörper besser zu bestimmen und zu verstehen.
In Alexandria bildete sich das Zentrum der damaligen Wissenschaft.
Es wurden große Anstrengungen unternommen um das Wissen der damals bekannten Welt zu sammeln und zu erweitern.
Bücher von Reisenden wurden händisch kopiert.
Schiffe, die im Hafen ankerten, wurden nach neuen Mitschriften durchsucht.
In der Agora wurde rege über die Laufbahn der Himmelskörper, geometrische Körper und besondere Zahlen diskutiert.

```{figure} ../../figs/earth-curvature.png
---
height: 150px
name: fig-earth-curvature
---
Eratosthenes und die Erdkrümmung.
```

Eratosthenes (276 v. Chr. - 194 v. Chr.) war einer der herausragenden Denker dieser Zeit und zugleich Leiter der Bibliothek in Alexandria.
Eines Tages machte er eine herausragende Entdeckung:
Er beobachtet, dass zur gleichen Zeit zwei Obelisken in verschiedenen Orten unterschiedlich lange Schatten auf die Erde warfen.
Erstaunlicherweise schloss er daraus auf die Krümmung der Erde.
Und da die Griechen von der Perfektion des Kreises überzeugt waren, folgerte Eratosthenes, dass die Erde eine Kugel sei.
Er war sogar in der Lage die Erdkrümmung relativ genau zu berechnen und dadurch auf den Umfang der Erde zu schließen.
Um seine Berechnungen durchführen zu können bediente er sich vermutlich eines menschlichen Computers, der ihm die Strecke zwischen Alexandria und Syren (800 km) ablief und berechnete.

import numpy as np

def sieve_of_eratosthenes(N):
    N = 100
    prime_sieve = [True for i in range(N)]
    prime_sieve[0] = False
    prime_sieve[1] = False
    for i in range(2, int(np.sqrt(N))):
        if prime_sieve[i]:
            for j in range(i**2, N, i):
                prime_sieve[j] = False
    
    primes = []
    for i in range(N):
        if prime_sieve[i]:
            primes.append(i)
    return primes
        
sieve_of_eratosthenes(100)

Wir finden also bereits zu dieser Zeit erste Beispiele für eine computergestützte Forschung.
Für lästige und primitive Berechnungen begann man Computer zu beauftragen.
Der Begriff *Computer* sollte lange Zeit auf eine Person anstatt eine Maschine hindeuten.
So wurden bis Ende des zweiten Weltkrieg menschliche Computer, oft Frauen, mit Berechnungen beauftragt.

Auch begann man zu dieser Zeit die ersten Algorithmen zu entwickeln.
Nach Eratosthenes ist einer der ersten Algorithmen benannt, der *Sieb des Eratosthenes*.
Es ist eine clevere Technik um Primzahlen zu berechnen.

```{figure} ../../figs/the-elements.jpg
---
height: 150px
name: fig-euklid-elements
---
Ein Fragment der Werke *Die Elemente*.
```

Doch noch vor Eratosthenes, notierte Euklid von Alexandria (ca 450 v. Chr. - Mitte 350 v. Chr.) in seinem Werk *Die Elemente*, einen Algorithmus für die Berechnung des größten gemeinsamen Teilers ``gcd(a,b)`` zweier natürlicher Zahlen ``a, b``.
Über zweitausend Jahre später finden wir jene Algorithmen in einer anderen Form wieder.

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

gcd(36, 24)

>[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day. -- Donald Knuth, The Art of Computer Programming, Vol 2.

Zwischen der Logik und der theoretischen Informatik gibt es einen sehr starken Zusammenhang.
Berechnungen eines Rechners basieren auf logischen Operationen und das theoretische Prinzip des universellen digitalen Computers, wie auch wichtige Grenzen dessen was berechenbar ist, entstand aus den Arbeiten vieler Logiker.
Den Anfang machten auch hier die Griechen.
Ihnen haben wir ein System des logischen Schließens, die sog. Syllogismen des Aristoteles, zu verdanken.
Neben den Syllogismen beschäftigte sich Aristoteles bereits mit dem *Satz vom Widerspruch* und dem *Satz vom ausgeschlossenen Dritten* sowie der Beweistechnik des *indirekten Beweises* -- allesamt fundamentale mathematische Techniken und Fragestellungen.
Zur Zeit des römischen Reichs formulierten die Stoiker das erste aussagelogische Kalkül und auch im Mittelalter sollten sich kleinere Fortschritte im Bereich der Logik ergeben.
Jedoch sollte erst im 19. Jahrhundert durch Mathematiker wie George Boole, Gottlob Frege und Bertrand Russell weitreichende Fortschritte möglich gemacht werden.

```{figure} ../../figs/logicians.png
---
height: 150px
name: logicians
---
Einflussreiche Logiker ihrer Zeit: Georg Boole, Gottlob Frege und Bertrand Russell.
```

In China wurde zwischen 200 vor und 100 nach Christus das Mathematikbuch *Jiu Zhang Suanshu* (*Neun Bücher arithmetischer Technik*) verfasst.
In ihm findet sich einer der noch heute bekanntesten Algorithmen zum Lösen linearer Gleichungssystem: das sog. *Gaußsche Eliminationsverfahren*.
Es wurde in Europa 1759 vom italienischen Mathematiker Lagrange publiziert und wohl unabhängig davon vom deutschen Mathematiker Gauß im Jahr 1811 entwickelt.
Schon die Babylonier wussten wie sich Gleichungen mit zwei Unbekannten lösen lassen, jedoch waren ihre zu lösenden Probleme durch konkrete oft geometrische Fragestellungen motiviert.
Das Besondere am *Gaußsche Eliminationsverfahren* ist seine Abstraktion, die zu einer allgemeinen Lösungstheorie für lineare Gleichungssysteme führte.

Wie bereits erwähnt, dauerte es tausend Jahre bis an den Fortschritt der antiken Griechen wieder angeknüpft wurde.
Wir wissen natürlich nicht welches, möglicherweise entscheidendes Wissen durch die Zerstörung und Plünderung der Bibliothek von Alexandria verloren gegangen ist.