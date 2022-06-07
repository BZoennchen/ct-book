#!/usr/bin/env python
# coding: utf-8

# (sec-python)=
# # Python
# 
# In **PYTHON** widmen wir uns der Sprache ``Python`` für einen ganzen Teil des Buches.
# Dort besprechen wir die Einzelheiten der Programmierung mit ``Python`` und wie wir mit der Sprache [Algorithmen](def-algorithm) entwickeln und niederschreiben können.
# In diesem Abschnitt versuchen wir hingegen die Sprache mit anderen Sprachen zu vergleichen.
# 
# ## Laufzeitvergleiche
# 
# Ein Vergleich von Programmiersprachen geht über die eignentliche Sprache hinaus.
# Wir analysieren nicht nur die Grammatik einer Sprache oder was mit dieser ausgedrückt werden kann, sondern auch wie verbreitet die Sprache ist oder wie leicht es fällt Programme mit ihr zu schreiben.
# 
# Insbesondere interessiert uns die Laufzeit der Programme die wir in einer Sprache verfassen.
# Dabei werden Begrifflichkeiten oft durcheinander geworfen.
# Oft hört man, zum Beispiel,
# 
# >``C`` ist eine effiziente Sprache.
# 
# Doch genau genommen macht diese Aussage keinen Sinn.
# Wie wir im Abschnitt [Interpretation](sec-interpretation) besprochen haben, wird Programmcode [übersetzt](def-compiler) oder [interpretiert](def-interpreter).
# Oftmals gibt es verschiedene [Interpreter](def-interpreter) oder [Übersetzer](def-compiler) für ein und dieselbe Sprache.
# Wie effizient ein Programm läuft hängt von der konkreten Maschine und den Maschinenbefehlen in die das Programm übersetzt oder interpretiert wird ab.
# Verwenden wir zwei unterschiedliche Übersetzer für den gleichen Code und lassen den übersetzten Code auf der gleichen Maschine laufen, kann die Laufzeit sehr unterschiedlich sein.
# Dennoch werden Sie oft lesen, dass die Sprache ``Python`` eine langsame Sprache sei!
# Präzise ausgedrückt müsste man jedoch sagen dass:
# 
# >Die ``Python``-Implementierungen (Interpreter/Übersetzer) üblicherweise zu einer langsamen Ausführung von ``Python``-Programmen führen.
# 
# ## Python gegen den Rest der Welt
# 
# Wie ``Java``, ``C++``, ``C#``, ``Scala`` und viele mehr, zählt ``Python`` zu den Universalsprachen (General Purpose Languages) und ist damit [Turing-vollständig](info-universal-turing-machine). 
# Das heißt ``Python`` ist in sehr vielen Bereichen anwendbar und ist im Stande all die Probleme zu lösen, die im Allgemeinen als lösbar angesehen werden.
# Der Name ``Python`` stammt von der Comedy-Gruppe Monty Python, was möglicherweise darauf hindeuten soll, dass die Sprache Spaß verbreiten soll.
# 
# Was unterscheidet aber ``Python`` von den anderen oben genannten Sprachen? 
# ``Python`` ist heute eine der weitverbreitetsten Sprachen und sie scheint sich weiter und weiter auszubreiten.
# Einer der Hauptgründe hierfür ist der einfache Zugang.
# ``Python`` ist einfach zu lesen und zu erlernen.
# Als [interpretierte](def-interpreter) Sprache mit guter Werkzeugunterstützung kann jeder in wenigen Klicks einfach loslegen.
# Sie installieren ``Python`` (auf vielen Systemen ist es vorinstalliert), öffnen Ihre Konsole, tippen ``python`` und los geht's.
# 
# Auch lässt sich in nur wenigen Zeilen ein kleines ``Python``-Skript schreiben und ausführen.
# Erstellen wir eine neue Datei ``sum-squares.py`` und fügen folgenden ``Python``-Code ein.
# 
# ```python
# import sys
# n = int(sys.argv[1])
# squares = sum([(i+1)**2 for i in range(n)])
# print(squares)
# ```
# 
# Führen wir dann das Programm durch den Konsolenbefehl
# 
# ```
# python sum-squares.py 5
# ```
# 
# aus, erhalten wir als Ausgabe die Summe der Quadratzahlen von 1 bis 5.
# So schnell geht's!
# 
# ``Python`` wurde bereits 1990 entwickelt und ist damit älter als z.B. ``Java``.
# Sie ist jedoch erst in den letzten Jahren so richtig in Fahrt gekommen.
# Der Zugang war vor nicht allzu langer Zeit keineswegs derart einfach, was den anfänglichen Erfolg behindert hat.
# Doch ist es unter Umständen auch ein Vorteil, wenn eine Sprache langsam aber stetig an Verbreitung gewinnt.
# So bleibt den Entwicklern Zeit über neue Verbesserungen intensiv nachzudenken und sodass diese nicht unbedacht aufgenommen werden.
# 
# Der Erfolg lässt sich auch auf die Unterstützung durch große IT-Unternehmen wie Google und Facebook aber auch der Universitäten zurückführen.
# Diese Unterstützung trieb die Entwicklung vieler Pakete, insbesondere im wissenschaftlichen Umfeld an.
# Paketen wie ``Numpy``, ``SciPy``, ``Pandas`` und ``Matplotlib`` ist es zu verdanken, dass ``Python`` im wissenschaftlichen Bereich derart verbreitet ist.
# Im Unterschied zu ``MATLAB`` und ``Mathematica``, gegen die sich ``Python`` im wissenschaftlichen Umfeld behaupten musste, ist ``Python`` frei zugänglich, was schlussendlich zu einer höheren Codequalität wie auch einer schnelleren Weiterentwicklung geführt hat.
# 
# Wissenschaftler\*innen sind keine Programmierexpert\*innen, legen besonders viel Wert auf die Reproduzierbarkeit und haben oft auch noch hohe Ansprüche an die Geschwindigkeit des ausgeführten Codes.
# Sie entwickeln keine großen Geschäftsanwendungen aber durchaus effiziente Algorithmen.
# Im wissenschaftlichen Bereich der Modellierung und Simulation programmierte man beispielsweise hauptsächlich in ``C/C++`` und ``Fortran`` -- zwei nicht gerade einfache Spachen.
# Die Möglichkeit sehr schnell gut leserliche Skripte zu schreiben, die auch noch performant laufen (dazu gleich mehr), brachte ``Python`` in der Wissenschaft schnell voran.
# Und da heute die Methoden des wissenschaftlichen Rechnens, *Big Data Analysis* und des *Machine Learnings* auch in der Wirtschaft immer wichtiger werden, überträgt sich dieser Erfolg auf die Wirtschaft.
# 
# Mit den ``Jupyter``-Notebooks haben Wissenschaftler\*innen eine Möglichkeit erhalten, ihre Ergebnisse samt Code anderen in aufbereiteter Weise zur Verfügung zu stellen.
# Das beschleunigt den wissenschaftlichen Austausch und verbessert die Transparenz.
# Auch dieses Konzept gab es bereits durch ``Mathematica``, doch ist diese Sprache viel schwerer zu lesen und deren Lizenzen sind teuer.
# 
# Gute Skripte zu schreiben ist zudem nicht nur für Wissenschaftler\*innen sondern auch für Systemadministrator\*innen und DevOps wichtig.
# Deshalb trat auch in diesem Bereich ``Python`` einen Siegeszug an.
# 
# Da ``Python`` einen so schnellen und einfachen Zugang bietet, begannen mehr und mehr Anfänger die Sprache zu nutzen.
# Das brachte eine große Menge neue potenzieller Entwickler\*innen auf den Arbeitsmarkt.
# Um dieses Potenzial nutzen zu können wurden die Bibliotheken um weitere Pakete für die Webentwicklung (``Django``, ``Flask``), graphische Benutzeroberflächen (``PyQt5``, ``Tkinter``, ``Kivy``) und mehr ergänzt.
# Das **Ökosystem** passte sich diesem Potenzial an, ganz nach dem Motto:
# 
# >Wollen die Entwickler\*innen nicht zum passenden Ökosystem kommen, muss das Ökosystem zu ihnen kommen.
# 
# Dieses Ökosystem ist heute ``Pythons`` größte Stärke.
# Sie bekommen einen unglaublichen Schatz geschenkt!
# Das können Sie sich gar nicht vorstellen.
# Was Sie nicht kostenfrei und offen bekommen sind die riesigen Rechnerressourcen die in großen Rechenzentren schlummern.
# 
# Wir hatten Eingangs erwähnt, dass man sich oft zwischen Performance und Lesbarkeit bzw. Entwicklungszeit entscheiden muss.
# ``Python`` trifft hier einen ganz bestimmten "Sweetspot": die Sprache ist maschinenenfern, sehr leserlich, man bekommt schnell viel zustande und dennoch ist sie leistungsstark, sofern wir das Ökosystem gut nutzen.
# Pakte verlagern aufwendige Berechnungen in ``C/C++`` oder gar ``Fortran``-Programme.
# Diese Sprachen sind maschinennah und [kompilierbar](def-compiler) und damit leistungsstark.
# So heißt es auf der offiziellen ``SciPy``-Seite:
# 
# >SciPy wraps highly-optimized implementations written in low-level languages like Fortran, C, and C++. Enjoy the flexibility of Python with the speed of compiled code.
# 
# Wie dies funktioniert, soll uns an dieser Stelle noch nicht kümmern.
# Durch das Zusammenspiel zwischen hocheffizientem kompiliertem Code und leicht leserlichen interpretierten Code bekommen wir beides: Die Leistung der maschinennahen Spachen und Abstraktion und Lesbarkeit durch ``Python``!
# 
# ``Python`` hat aber auch seine Tücken.
# Als [dynamisch getypte](sec-type-systems) sehr flexible und [interpretierte](def-interpreter) Sprache kann es schwer sein Garantien für den geschriebenen Code sicherzustellen.
# Software oder auch Entwickler\*innen, die Quellcode analysieren und auf Korrektheit prüfen, können es schwer haben.

# In[1]:


def sum_squares(n):
    return sum([(i+1)**2 for i in range(n)])


# Blicken wir nur auf die Argumente der Funktion ``sum_squares``, so wissen wir nicht ob die Funktion eine [Ganzzahl](sec-int), eine [Fließkommazahl](sec-float) oder eine [Zeichenkette](sec-string), oder irgendetwas anderes erwartet.
# Um anderen Entwickler\*innen die Fehlersuche zu erleichtern, sollten wir deshalb mit Kommentaren kennzeichnen um welchen [Datentyp](sec-python-data-types) es sich bei ``n`` handelt.
# Rufen wir die Methode mit einer Zeichenkette auf, z.B., ``sum_square('a')`` wird uns niemand daran hindern und wir bemerken unseren Fehler erst, wenn das Programm abstürzt.
# 
# Eine recht neue Möglichkeit ist es den Typ direkt im Code anzugeben, es bleibt aber reine Dokumentation und hat keine Wirkung auf die Ausführung:

# In[2]:


def sum_squares(n: int) -> int:
    return sum([(i+1)**2 for i in range(n)])


# Für [statisch getypten](sec-type-systems) Sprachen wie ``Java``, ``C++`` oder ``Haskell`` (siehe oben), wäre der Datentyp durch die Definition der Funktion festgelegt.
# Hier würde bereits vor dem Start des Programms (während des [Übersetzens](def-compiler)) ein Fehler entstehen, falls wir ``sum_square('a')`` ausführen.
# Gerade bei sicherheitsrelevanter Software wie der Flugzeugsteuerung, Finanzsystemen oder großen Businessanwendungen kann eine dynamische Typisierung zum Problem werden.
# 
# ## Kritik
# 
# Die dynamische Typisierung gepaart mit der Interpretierung der Sprache bringt sicherheitsrelevante Nachteile.
# Syntaktische Fehler führen erst bei der Ausführung zu Fehlern und können unter Umstände zu Bugs führen, die lange unentdeckt bleiben.
# 
# Ein zweiter Aspekt, den man gut oder schlecht finden kann ist, dass es ``Python`` den Entwickler\*innen erschwert ihren Code als geistiges Eigentum zu schützen. 
# 
# Ein weiterer Nachteil der Sprache ist, dass ``Python``-Programme, sofern sie keine externen kompilierten Code verwenden, eine langsame Laufzeit aufweisen.
# Angenommen wir haben ein Problem welches wir effizient lösen wollen.
# Finden wir keinen vorkompilierten Code im ``Python``-[Ökosystem](sec-python-ecosystem), so müssen wir möglicherweise selbst diesen Code entwickeln und das Ökosystem selbst erweitern.
# Natürlich können wir das Problem auch mit reinem ``Python``-Code lösen, doch wird dieser Code, im Vergleich zu kompilierten Sprachen, langsamer laufen.
# Entwickler:innen, die hocheffiziente Python-Pakete entwickeln, benötigen häufig gute Kenntnisse in der Entwicklung mit ``C/C++``.
# 
# Als letzter Punkt ist das sogenannte *GIL (Global Interpreter Lock)-Problem* von [CPython](https://docs.python.org/3.11/) zu nennen.
# CPython ist die vorherrschende Implementierung von Python.
# Der *GIL* behindert die effiziente Nutzung von Multiprozessor-Systemen da durch ihn keine echte parallele Ausführung mehrere sog. Threads möglch ist.
# Um die Parallelität der Multiprozessoren nutzen zu können, müssen Entwickler\*innen anstatt (leichtgewichter) Threads mehrere (schwergewichtige) Prozesse verwenden.
# In jedem Prozess läuft dann ein eigener CPython-[Interpreter](def-interpreter).
# Pakete/Module wie ``numpy`` nutzten vorkompilierten Code, welcher wiederum durchaus auf Threads basieren kann.
# 
# ## Schlusswort
# 
# Heute ist ``Python`` eine der populärsten Sprachen mit dem Potenzial immer weiter an Fahrt aufzunehmen.
# Sie hat eine sehr leserliche [Syntax](def-syntax), ein herausragendes [Ökosystem](sec-python-ecosystem), ist in sehr vielen Anwendungsbereichen anzutreffen (Tendenz steigend) und bietet bei richtiger Verwendung auch eine gute Laufzeit.
# Die größte Stärke von ``Python`` ist jedoch dessen Gemeinschaft.
# Neben den angeführten Pluspunkten, entwickelt sich eine solche Gemeinschaft nur dann, wenn es den Entwickler\*innen auch Spaß macht die Sprache zu verwenden.
# 
# Deshalb ist ``Python`` eine ausgezeichnete Wahl, wenn Sie eine neue Programmiersprache erlernen wollen.
# Wir empfehlen dennoch, im Laufe Ihres Studiums, zusätzlich mindestens eine [statisch getypte](sec-type-systems) [kompilierte](def-compiler) Sprache zu erlernen, da diese weitere wichtige wesentliche Konzepte des digitalen Computers und damit des [Computational Thinkings](sec-what-is-ct) offenlegen.
