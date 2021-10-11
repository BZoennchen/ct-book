# O-Notation

TODO

Sie benötigt höchstens so viele Schritte $\mathcal{O}(\log(n))$ aber auch mindestens so viele Schritte $\Omega(\log(n))$.
Nutzen wir hingegen die *lineare Suche*, ob mit oder ohne Häufigkeit, benötigen wir höchstens $\mathcal{O}(n)$ Schritte aber (nur) mindestens $\Omega(1)$ Schritte.
$\mathcal{O}(f(n)), \Omega(f(n))$ sind sogenannte Komplexitätsklassen.
Ein Algorithmus dessen Aufwand durch eine Funktion beschrieben wird. die sich in der Klasse $\mathcal{O}(f(n))$ befindet hat, salopp gesagt, keinen höheren Aufwand als $f(n)$ wobei $n$ die Problemgröße ist (in unserem Fall die größe der Menge).