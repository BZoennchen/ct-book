#!/usr/bin/env python
# coding: utf-8

# (sec-why-data-types)=
# # Existenzberechtigung
# 
# Ziehen wir nochmals den Vergleich zwischen Datentypen und *Dateiformate*.
# 
# Weshalb enden PDF-Dokumente mit ``.pdf`` und Bilder mit, z.B., ``.png``?
# Ändern wir die Dateiendung oder lassen Sie weg, so ändert sich der Inhalt der Datei nicht.
# Allerdings kann Ihr Programm zum Lesen von PDFs, ausschließlich PDFs lesen.
# Die Dateiendung ist ein Versprechen, dass es sich bei dieser Datei auch wirklich um eine PDF handelt.
# Zudem leitet Ihr Betriebssystem das Öffnen der Datei an ein Programm weiter, welches das entsprechende Dateiformat verarbeiten kann.
# Da das Betriebssystem nicht alle Dateiformate kennen kann (jeden Tag entstehen neue Formate) achtet es auf die Dateiendung.
# Wir als Benutzer können dem Betriebssystem mitteilen, welche Datei es mit welchem Programm öffnen soll.
# 
# Datentypen existieren aus einem ähnlichen Grund.
# Sie sind ein verpflichtendes Versprechen, wie der Speicherbereich (die Bits und Byte), der den Wert ausmacht, aussieht und wie er interpretiert werden muss.
# Funktionen und Operationen verlassen sich auf dieses Versprechen.
# 
# Informationen können auch wir Menschen nur dann verarbeiten wenn wir uns auf eine [Interpretation](sec-interpretation) einigen, bzw. diese bekannt ist und auch eingehalten wird.
# Genauso verhält es sich mit Programmen und Maschinen.
# 
# Zum Beispiel erwartet die Addition ``+`` zwei Zahlen.
# Dabei kann es sich bei jeder der beiden Zahlen entweder um eine ganze Zahl ``int`` oder um eine Fließkommazahl handeln.

# In[1]:


3 + 9       # int + int
3 + 8.6     # int + float
-3.6 + 3.4  # float + float
3.1 + 9     # float + int


# Der Datentyp des Ergebnisses der Addition hängt von den Datentypen der beiden Summanden ab.

# In[2]:


print(type(3 + 9))      # int + int -> int
print(type(3 + 8.6))    # int + float -> float
print(type(-3.6 + 3.4)) # float + float -> float
print(type(3.1 + 9))    # float + int -> float


# Zudem wird nicht jeder Datentyp von der Addition unterstützt:

# In[3]:


3 + 'a' # int + str -> Fehler!


# Der Fehler der durch diesen Code erzeugt wird besagt: ``unsupported operand type(s) for +: 'int' and 'str'``, d.h., diese Kombination aus Datentypen (``int`` und ``str``) wird nicht unterstützt.
# Was passiert wenn wir zwei Zeichenketten 'addieren'?

# In[4]:


'a' + 'b' # str + str -> str!


# Überraschenderweise führt dies nicht zu einem Fehler.
# Wir sprechen hierbei nicht mehr von einer Addition, stattdessen handelt es sich um die sog. *Konkatenation* (Verkettung) von Zeichenketten.
# In anderen Worten: Es entscheiden die Datentypen darüber, welche Operation der ``+``-Operator definiert bzw. welche Operation ausgeführt wird!
# 
# In der [objektorientierten Programmierung](sec-oop) erzielt man dies indem Datentypen nicht nur einen Wert sondern auch Operationen, die auf dem Datentyp ausgeführt werden, definieren.
# Zum Beispiel bietet der Datentyp ``str`` die *Methode* ``count``:

# In[5]:


'peter'.count('e')


# Betrachten wir ein weiteres Beispiel:

# In[6]:


max([1,2,3,4,5])


# und

# In[7]:


max('a','b')


# Wir rufen beide Male die *built-in Funktion* ``max`` auf.
# Einmal ist das Argument eine Liste ``list`` und einmal rufen wir ``max`` mit zwei Argumenten, zwei Zeichenketten ``str`` auf.
# Das Ergebnis ist einmal das größte Element der Liste und einmal das lexikographisch größere Element der beiden Argumente.
# Der Datentyp des Rückgabewerte ist einmal eine ganze Zahl ``int`` und einmal eine Zeichenkette ``str``.
# 
# Wird folgender Code funktionieren?

# In[8]:


max(3,'b')


# Wir können das an dieser Stelle nicht wissen.
# Es kommt darauf an **WIE** die Funktion ``max`` implementiert wurde und **WAS** sie genau macht.
# Macht aus Ihrer Sicht ein solcher Aufruf Sinn?
# 
# Führen wir den Code aus, so kommt es zu einem weiteren Fehler: ``'>' not supported between instances of 'str' and 'int'``.
# Was soll das nun bedeuten?
# Wer hat denn was von größer ``>`` gesagt?
# Nun, scheinbar verwendet die Funktion ``max`` den Größer-[Vergleichsoperator](sec-python-operator-compare) und dieser kann mit der Kombination ``str`` und ``int`` nicht umgehen.
# Wir erhalten den gleichen Fehler mit

# In[9]:


3 > 'b'


# Es ist im Allgemeinen unklar wie wir eine Zahl mit einem Buchstaben vergleichen sollen.
# Wir können selbstverständlich einen solchen Vergleich selbst definieren.
# Wir greifen hier etwas vor:

# In[10]:


def get_key(value):
    if type(value) == str:
        return ord(value[0])
    else:
        return value

max(3, 'b', key=get_key)


# Was passiert hier?
# Wir definieren eine eigene Funktion ``get_key``.
# Diese transformiert den Wert, welchen wir vergleichen wollen, in einen anderen Wert.
# Ist der Wert eine Zeichenkette, so transformieren wir diese in eine ganze Zahl (ihren ASCII-Code).
# Andernfalls geben wir den Wert zurück (keine Transformation).
# 
# Wir sagen der Funktion ``max`` Sie solle doch bitte vor jedem Vergleich die zu vergleichenden Werte durch unsere Funktion ``get_key`` transformieren.
# Dies Funktionalität bietet uns ``max``.
# Somit sieht der Vergleich wie folgt aus

# In[11]:


get_key(3) > get_key('b')


# also

# In[12]:


3 > ord('b')


# Dabei ergibt ``ord('b')`` den Wert ``98``.
# Der Rückgabewert ist eine Zeichenkette ``str``.
# Rufen wir allerdings folgenden Code auf

# In[13]:


def get_key(value):
    if type(value) == str:
        return ord(value[0])
    else:
        return value

max(100, 'b', key=get_key)


# so ist der Rückgabewert eine ganze Zahl ``int``.
# Auch das ist in vielen anderen Sprachen anders.
# In ``Java``, ``C/C++`` ist der Rückgabewert einer Funktion immer vom gleichen Datentyp, denn diese Sprachen sind *statisch getypt* wohingegen ``Python`` oder auch ``JavaScript`` *dynamisch getypt* sind.
