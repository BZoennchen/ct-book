#!/usr/bin/env python
# coding: utf-8

# (sec-languages-abstraction)=
# # Abstraktion des Computers
# 
# Im Kapitel [Der digitale Computer](sec-information-processing) haben wir uns angesehen wie 
# 
# 1. ein digitaler Computer die Informationsverarbeitung realisiert, 
# 2. wie auf dem Computer Information [repräsentiert](sec-representation) und digitalisiert wird und 
# 3. wie dieser durch Logikgatter (realisiert durch elektronische Bauteile) Information [manipulieren](sec-manipulation).
# 
# Wir haben gezeigt, dass die einfache Addition von zwei natürlichen Zahlen durch eine Vielzahl an Interaktionen der einzelnen Bauteile des Computers umgesetzt wird.
# Der Computer muss erst *booten*.
# Dann muss das Programm in den Speicher geladen werden.
# Dieses muss ausgeführt werden.
# Das Programm veranlasst die [Kontrolleinheit](def-cpu), die zu addierenden Zahlen in Register zu laden.
# Die [arithmetische Einheit](def-cpu) berechnet daraufhin das Ergebnis, was wiederum in den [Hauptspeicher](def-main-memory) zurückgeschrieben werden muss.
# Welch ein Aufwand!
# Müssen wir uns um all das kümmern?
# 
# Ja und nein lautet unsere Antwort.
# 
# ```{admonition} Abstraktion der Spezifika
# :name: remark-abstraction-of-the-concrete
# :class: remark
# 
# Programmiersprachen abstrahieren die Spezifika des digitalen Computers.
# 
# ```
# 
# Die Hardware wird durch Programmiersprachen so weit abstrahiert, dass wir uns um Register, Kontrolleinheit, arithmetische Einheit und oft nicht einmal mehr um den Hauptspeicher kümmern müssen.
# Je nach Wahl der Programmiersprache unterscheidet sich dieses *Abstraktionsniveau*.
# 
# In [Berechenbarkeit](sec-computability) haben wir Ihnen gezeigt, dass Computer, als auch Programmiersprachen, [Turing-vollständig](def-turing-complete) sind.
# Der Computer ist eine [universelle Turingmaschine](sec-utm) und simuliert die [Turingmaschinen](info-universal-turing-machine) (Programme), die in seinem Speicher liegen.
# Der Computer spricht [binär](sec-binary-system), d.h., jeder Teil des Befehls zum addieren von zwei Zahlen
# 
# $$\text{ADD } \text{Reg}_1 \text{ Reg}_2 \text{ Reg}_3$$
# 
# wird in einen Binärcode übersetzt, d.h., durch eine Folge von $0$, und $1$ repräsentiert.
# Zum Beispiel könnte es sein, dass $\text{ADD }$ durch $1001$ codiert wird.
# Uns Menschen fällt es extrem schwer ein Programm in Form einer langen Sequenz von $0$ und $1$ zu lesen.
# Deshalb gibt es Programme ([Interpreter](def-interpreter) und [Compiler](def-compiler)), die einen abstrakten Programmcode, geschrieben in Sprache $L_1$, in *maschinennäheren* Code der Sprache $L_2$ überführen.
# 
# In sogenannten *Hochsprachen* kümmern Sie sich nicht mehr um Register.
# Ein Befehl wie
# 
# ```python
# z = x + y
# ```
# 
# wird schrittweise von der Hochsprache in immer maschinennähere Sprachen übersetzt.
# Zunächst möglicherweise in ``Assembler``, eine Sprache welche auf Registerebene arbeitet und dann ein zweitesmal in binären Maschinencode.
# 
# 
# ```{exercise} Kompilieren und Interpretieren
# :label: languages-abstraction-exercise
# Angenommen es gäbe eine Sprache ``SimplePython`` die äquivalent zu ``Python`` ist aber keine Multiplikation und auch keine Schleifen/Iteration kennt.
# 
# Schreiben Sie eine ``Python``-Funktion ``spython_compile_mul(a,b)``, welche ein ``SimplePython``-Programm mithilfe von ``print`` ausgibt.
# Dieses Programm soll ``c = a * b`` berechnen!
# Nehmen Sie ``a`` und ``b`` als Werte und nicht als Variablen an.
# 
# ```
# 
# ````{solution} languages-abstraction-exercise
# :label: languages-abstraction-solution
# :class: dropdown
# 
# ```python
# def python_compile_mul(a,b):
#     print("c = 0")
#     for _ in range(a):
#         print(f"c = c + {b}")
# 
# python_compile_mul(3, 4)
# ```
# 
# ````
# 
# Sprachen wie ``Java``, ``Python`` und ``C#`` bieten ein sehr hohes Abstraktionsniveau wohingegen ``C++`` maschinennäher ist.
# Doch selbst wenn das Abstraktionsniveau weniger hoch ist, können wir uns als Programmierer\*innen selbst auf ein höheres Niveau hieven.
# Nehmen wir zum Beispiel einmal an, unsere Sprache könnte keine Zahlen multiplizieren.
# Das einzige was wir zur Verfügung haben ist die Addition ``+`` und die Möglichkeit Anweisungen ``n``-mal zu wiederholen ``for i in range(n)``.
# Mit diesen Mitteln können wir uns die Multiplikation selbst bauen:

# In[1]:


def mul(a, b):
    result = 0
    for _ in range(a):
        result = result + b
    return result


# Wenn wir dann in unserem Code die Multiplikation ausführen wollen, z.B., durch

# In[2]:


mul(4,5)


# wird stattdessen unsere Funktion ``mul`` mit den Argumenten ``a = 4, b = 5`` *aufgerufen*.
# Anders ausgedrückt der Code ``mul(a, b)`` wird ersetzt durch

# In[3]:


result = 0
for _ in range(4):
    result = result + 5
result


# und zusätzlich wird aus ``mul(4, 5)`` der Wert, den die Funktion zurückgibt (``return result``).
# Wir sagen auch ``mul(4, 5)`` wird zum Wert ``20`` evaluiert/ausgewertet.
# Wir **abstrahieren** die Berechnung und gleichzeitig wird das **Muster** ``mul(a, b)`` durch den Code der Funktion ersetzt.
# 
# Das gleiche passiert bei der (maschinennahen) Addition zweier Zahlen.
# Wann welcher Wert in welches Register geschrieben wird, ist durch eine Funktion bereits festgelegt.
# Diese wird aufgerufen wenn wir

# In[4]:


x = 4 + 9
x


# berechnen.
# Der ``Python``-Code wird in immer maschinennäheren Code umgewandelt bis wir am Ende wieder beim Addieren von Werten in Registern herauskommen.
# Somit kontrollieren wir den Computer nicht direkt, sondern befehligen ein Program welches unsere Anweisungen in maschinennahe Anweisungen umwandelt!
# Erstellen wir zum Beispiel eine Liste

# In[5]:


numbers = [1, 2, 3, 4, 5]
numbers


# werden auf maschinennaher Ebene die Zahlen nebeneinander in den Hauptspeicher geschrieben.
# 
# Programme, geschrieben in verschiedenen Programmiersprachen, steuern den Computer und abstrahieren damit die reale physikalische Welt der elektrischen Schaltungen und Transistoren.
# Sie hieven uns in eine abstrakte Welt der Algorithmen und Datenstrukturen.
# Wir treten aus der Welt der Register und Speicheradressen hinaus in eine Welt der Variablen, Listen, Tupel, Schleifen, Bedingungen, Objekte und alles was wiederum von diesen Konstrukten abstrahiert werden kann.
# 
# Als *Computational Thinker\*innen* konzipieren Sie Algorithmen durch Nachdenken, Skizzen und Mitschriften.
# Können Sie Ihr Problem durch einen [Algorithmus](def-algorithm) lösen, so existiert eine [Turingmaschinen](info-universal-turing-machine) die Ihr Problem löst.
# Da alle gängigen Programmiersprachen [Turing-vollständig](def-turing-complete) sind, können Sie jeden [Algorithmus](def-algorithm) in einer solchen Sprache formulieren!
# Diese Gewissheit befreit Sie von
# 
# 1. der physischen Welt der Computer aber auch
# 2. von der konkreten Programmiersprache
# 
# ```{admonition} Nutzen der Programmiersprachen
# :name: remark-languages-usefulness-complete
# :class: remark
# 
# Da alle gängigen Programmiersprachen Turing-vollständig sind, können Sie jeden Algorithmus in einer solchen Sprache formulieren!
# Programmiersprachen sind das Bindeglied zwischen Mensch und Maschine.
# 
# ```
