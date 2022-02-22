#!/usr/bin/env python
# coding: utf-8

# (sec-functions-basics)=
# # Grundlagen
# 
# Ok, lassen Sie ganz frisch starten, von der Definition einer Funktion bis hin zu ihrer Benutzung!
# 
# ## Definition
# 
# In ``Python`` definieren wir eine Funktion mit dem Signalwort ``def`` (für Definition).
# Es folgt der Funktionsname und in runden Klammern, getrennt durch Komma, die Parameter der Funktion.
# Nach dem ``:`` beginnt der Funktionskörper, welcher eingerückt sein muss!
# 
# ```python
# def name_der_funktion(parameter1, parameter2, ...):
#     '''
#     An dieser Stelle steht der sog. "docstring".
#     Dieser wird ausgegeben wenn help() zur Funktion aufgerufen wird.
#     Er dient der Dokumentation und soll klären WAS Ihre Funktion macht.
#     '''
#     # Code
#     # Code
#     return output # (optional)
# ```
# 
# ``Python`` erlaubt uns vor den Code des Funktionskörpers eine Zeichenkette zu schreiben.
# Diese dient lediglich der Dokumentation.
# Rufen wir zum Beispiel ``help(name_der_funktion)`` auf, erscheint genau jener Text.
# Nach diesem ``docstring`` folgt unser Befehlsbündel.
# 
# Eine Funktion kann kein oder mehrere ``return``-Ausdrücke beinhalten.
# Allerdings liefert eine ``Python``-Funktion immer etwas zurück.
# Sollte die Funktion keinen ``return``-Ausdruck beinhalten oder das Programm in einen Zweig laufen, welcher ohne ein ``return`` endet, so gibt die Funktion ``None`` zurück.
# 
# Der Name für ``name_der_funktion`` darf frei vergeben werden.
# Jedoch achtet man in der Programmierung stets auf **sprechende** Funktions- und Parameternamen.
# Vergleichen Sie:

# In[1]:


def dddd(something, l):
    """
    computes the subtraction of something and l.
    """
    return something - l
dddd(5, 6)


# und

# In[2]:


def subtract(x, y):
    """
    returns x - y
    """
    return x - y
subtract(5, 6)


# Die erste Benennung erschwert das Lesen und Verstehen der Funktion.
# Für die zweite Version müssen wir lediglich auf den Namen ``subtract`` und den kurzen ``docstring`` blicken um zu verstehen was die Funktion tut.
# 
# Den ``docstring`` könnten wir uns auch schenken, doch bedenken Sie dass andere Entwickler\*innen, welche Ihren Code benutzten, oft nicht in den Code blicken sondern sich lediglich den ``docstring`` ausgeben lassen.
# 
# ```{admonition} Docstrings und Kommentare
# :class: attention
# :name: attention-missleading-doc
# 
# Nichts ist irreführender als fehlerhafte, widersprüchliche oder schlicht falsche Kommentare!
# ```
# 
# ## Rückgabewerte
# 
# In ``Python`` ist es sehr einfach mehrere Rückgabewerte zu definieren:

# In[3]:


def modulo(n, k):
    """
    returns div, rest such that n = k * div + rest, 
    where n, k, div, rest are whole numbers.
    """
    div = n // k
    rest = n % k
    return div, rest

modulo(10, 7)


# Doch genau genommen hat eine ``Python``-Funktion genau einen Rückgabewert.
# Im obigen Beispiel handelt es sich um **ein** Tupel ``tuple``, wodurch der Eindruck entsteht, wir würden mehrere Werte zurückgeben.
# Durch das packing und unpacking (siehe Abschnitt [Tupel](sec-tuple)) 'simuliert' ``Python`` mehrere Rückgabewerte.

# In[4]:


div, rest = modulo(10, 7)
print(div)
print(rest)


# Verwenden wir kein ``return`` so gibt die Funktion (sofern sie keinen Fehler oder eine Endlosschleife verursacht) ``None`` zurück.

# In[5]:


def print42():
    print('42')
    
print(print42())


# entspricht

# In[6]:


def print42():
    print('42')
    return None
    
print(print42())


# ## Standardargumente für Parameter
# 
# Wir können Parametern auch einen sog. Standardargumente (Standardwerte) verpassen.
# Das Standardargument wird genau dann verwendet, wenn der Wert des Parameters beim Aufruf der Funktion nicht definiert wurde.
# 
# Erinnern Sie sich noch an die Funktion ``range()``?
# Diese konnten wir mit einem, zwei, oder drei Argumenten aufrufen.
# Das gelang, weil auch ``range()`` Standardwerte für zwei der drei Parameter festlegt.
# 
# Lassen Sie uns eine Funktion ``lrange(start, stop, step)`` definieren, welche eine Liste bestehend aus dem entsprechenden Zahlenbereich ``range(start, stop, step)`` zurückliefert:

# In[7]:


def lrange(start, stop, step):
    numbers = list(range(start, stop, step))
    return numbers

lrange(0, 10, 2)


# Die Funktion ``lrange()`` verhält sich wie ``range()``, jedoch gibt Sie eine Liste zurück.
# Ohne Standardargumente können wir die Funktion jedoch nicht mit nur einem Argument aufrufen.

# In[8]:


lrange(10)


# Definieren wir Standardargumente, müssen wir uns überlegen welche Werte sinnvoll sind.
# Was soll also passieren wenn wir beim Funktionsaufruf bestimmte Parameter weglassen?
# 
# Standardargumente setzten wir durch eine Zuweisung im Funktionskopf.
# Dabei müssen alle Parameter mit Standardargumenten **hinten stehen!** 
# Folgender Code wird ebenfalls zu einem Fehler führen:

# In[9]:


def lrange(start=0, stop, step=1):
    numbers = list(range(start, stop, step))
    return numbers

lrange(0, 10, 2)


# Wir müssen die Reihenfolge der Parameter verändern (und diese Änderung auch beim Aufruf der Funktion berücksichtigen):

# In[10]:


def lrange(stop, start=0, step=1):
    numbers = list(range(start, stop, step))
    return numbers

print(lrange(10, 0, 2))
print(lrange(10))


# Wir können auch **einzelne** Standardargumente beim Funktionsaufruf verändern. 
# Zum Beispiel wollen wir vielleicht eine Liste mit ``lrange()`` erzeugen, für die ``stop=10``, ``start=0`` und ``step=2`` gilt. 
# Da wir ``start`` weiterhin auf dem Standardwert ``0`` belassen, müssen wir es nicht angeben.

# In[11]:


lrange(10, step=2)


# Um den Code besser lesen zu können macht es hin und wieder Sinn, diese Schreibweise auch dann zu verwenden, wenn Sie eigentlich gar nicht notwendig wäre.

# In[12]:


lrange(stop=10, start=0, step=2)


# Verwenden wir diese Schreibweise, können wir auch die Reihenfolge der Parameter missachten:

# In[13]:


lrange(start=0, stop=10, step=2)


# Lassen Sie sich nicht verwirren wenn wir einem Parameter eine Variable zuweisen, die denselben Namen trägt:

# In[14]:


start = 0
lrange(start=start, stop=10, step=2)


# Diese beiden Variablen mit dem Namen ``start`` sind nicht dieselben Variablen.
# Das linke ``start`` ist der Parameter welches die Funktion schlussendlich verwendet und das rechte ``start`` ist das Argument, welches wir zuvor definiert haben.
# Wir setzten beim Aufruf die Adresse des linken ``start`` auf die Adresse des rechten ``start``.
