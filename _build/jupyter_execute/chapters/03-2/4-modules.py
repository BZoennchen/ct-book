#!/usr/bin/env python
# coding: utf-8

# # Module
# 
# ``Python`` ist unter anderem so erfolgreich, da es für immense viele Bereiche und Probleme eingesetzt wird und durch einer großen Gemeinschaft gepflegt wird.
# In dieser Gemeinschaft wird Programmiercode für eine Vielzahl an Problemen entwickelt, weiterentwickelt und **frei**, **kostenlos** wie auch **offen** angeboten!
# Stoßen Sie auf ein Problem, welches Sie lösen möchten ist die Wahrscheinlichkeit groß, dass andere Programmierer\*innen dafür bereits eine Lösung entwickelt haben.
# 
# Fremder wie auch Ihr eigener Code wird irgendwann eine Anzahl an Zeilen beinhalten, welche Sie nicht mehr in einem Notebook oder einer Datei halten möchten.
# Sie möchten Ihren Code strukturiert auf mehrere Dateien verteilen und diesen Code wiederverwenden.
# Was Sie benötigen sind sogenannte Module.
# 
# >Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; -- [offizielle Dokumentation](https://docs.python.org/3/tutorial/modules.html#tut-modules)
# 
# Module verhindern zudem sogenannte Namenskonflikte.
# Angenommen Sie schreiben ein Modul, welches andere Programmierer\*innen benutzten wollen.
# Sie definieren Funktionen in Ihrem Modul, doch woher wissen Sie, dass die anderen Programmierer\*innen nicht die gleichen Namen für ihre Funktionen verwenden.
# Würden wir zum Beispiel eine Methode ``func1()`` definieren und diese den anderen zur Verfügung stellen und diese würden Sie vor folgenden Code Einbinden/Importieren:
# 
# ```python
# # import our func1() 
# def func1():
#     return 42
# ```
# 
# So würde unsere Funktion von deren ``func1()`` überschrieben werden, wie folgender Code zeigt:

# In[1]:


# our imaginative func1()
def func1():
    return 0

print(func1())

def func1():
    return 42

print(func1())


# Module lösen dieses Problem, sofern es keine zwei Module mit dem gleichen Namen gibt.
# Der obige Code könnte dann wie folgt aussehen:
# 
# ```python
# def func1():
#     return 42
# 
# func1()
# ourmodulename.func1()
# ```
# 
# ## Ein eigenes Modul
# 
# Lassen Sie uns eine Datei ``squaresum.py`` im aktuellen Verzeichnis erstellen und folgenden Code einfügen:
# 
# ```python
# def square_sum(n):
#     result = 0
#     for i in range(n):
#         result += (i+1)**2
#     return result
# ```
# 
# Diese Funktion ``square_sum(n)`` gibt die Summe alle Quadratzahlen von 1 bis ``n`` zurück.
# Lassen Sie uns nun Kommandozeileninterpreter im gleichen Verzeichnis ausführen:
# 
# ```sh
# python
# ```
# 
# Wie können wir nun unsere Funktion, welche in der Datei ``square_sum.py`` steht?
# Wir importieren ``squaresum``, denn der Name unseres eben geschriebenen Moduls ist standardmäßig gleich seinem Dateinamen ohne die Endung ``.py``.
# 
# ```python
# >>> import squaresum
# >>> squaresum.square_sum(100)
# 338350
# ```
# 
# Diese Befehle erzeugen folgende Ausgabe
# 
# ```{figure} ../../figs/python-tutorial/environment/square-sum.png
# ---
# width: 800px
# name: fig-square-sum
# ---
# ```
# 
# Ein Modul ist demnach nichts weiter als eine Datei, welche ``Python``-Definitionen und Ausdrücke enthält.
# Den Namen des Moduls erhalten wir auch durch
# 
# ```python
# >>> squaresum.__name__
# 'squaresum'
# ```
# 
# Wir können sowohl den Namen mit dem wir auf das Modul zugreifen als auch dessen Funktionen umbenennen.
# 
# ```python
# >>> import squaresum as ss
# >>> ss.square_sum(100)
# 338350
# ```
# 
# oder 
# 
# ```python
# >>> import squaresum as ss
# >>> square_sum = ss.square_sum
# >>> square_sum(100)
# 338350
# ```
# 
# ## Wie findet Python die Module?
# 
# Befindet sich das Modul nicht in unserem aktuellen Verzeichnis funktioniert der obige Code nicht, da der ``Python``-Interpreter das Modul ``squaresum`` nicht findet.
# Schreiben wir 
# 
# ```python
# import squaresum
# ```
# 
# sucht der Interpreter nach dem Modul ``squaresum`` an verschiedenen Orten.
# 
# 1. Ist das Modul ein *built-in* Modul welches zur [Python Standard Bibliothek](https://docs.python.org/3/library/) gehört?
# 2. Findet sich die Datei mit dem Namen ``squaresum.py`` in einem der Verzeichnisse die in der Variable ``sys.path`` angegeben ist?
# 
# ``sys.path`` enthält auch immer das Verzeichnis indem das Skript welches den ``import squaresum`` Ausdruck enthält.
# Die Liste enthält auch alle Verzeichnisse die sich in **PYTHONPATH** (ähnlich wie **PATH**) befinden.
# Und zu guter Letzt beinhaltet es alle Verzeichnisse die von der ``Python``-Installation selbst oft abhängen, z.B. die von Anaconda oder Miniconda.
# 
# Aber keine Sorge, Sie müssen sich um das alles nicht kümmern, dafür gibt es die Modulverwaltungswerkzeuge ``conda`` bzw. ``pip``.
# Installieren Sie Module oder Pakete über diese Werkzeuge auf korrekte Art und Weise, so findet der Interpreter diese.
# 
# Möchten Sie Ihr eigenes Modul für andere zur Verfügung stellen können Sie es auf einer Webseite in das Ökosystem einfügen.
# Wie das geht würde an dieser Stelle zu weit führen.
# 
# ## Pakete
# 
# Ein Paket bildet eine hierarchisch strukturierte Ansammlung an Modulen.
# Zum Beispiel ist [roboworld](https://github.com/BZoennchen/robo-world) ein Paket mit den Teilmodulen (engl. submodules) 
# 
# + ``agent``, 
# + ``world``,
# + ...
# 
# Um nur ein Teilmodul eines Pakets einzubinden um es nutzbar zu machen verwenden wir die ``.`` Dot-Notation:
# 
# ```python
# import roboworld.world
# ```
# 
# oder 
# 
# ```python
# from roboworld import world
# ```
# 
# Wie wir Module und Pakete installieren haben wir in [Python installieren](sec-python-installation) angerissen und das soll an dieser Stelle auch ersteinmal ausreichen.
# Soweit zu den Grundlagen in sehr wenigen Worten.
# Weiterführende Informationen können Sie der exzellenten [Dokumentation](https://docs.python.org/3/tutorial/modules.html#tut-modules) entnehmen.
