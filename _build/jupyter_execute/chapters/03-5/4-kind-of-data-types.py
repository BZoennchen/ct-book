#!/usr/bin/env python
# coding: utf-8

# (sec-kind-of-data-types)=
# # Arten von Datentypen
# 
# Der *Datentyp* einer Variablen gibt an, wie die [Bits](def-bit) und [Bytes](def-byte) [interpretiert](sec-interpretation) werden.
# Die Bits und Bytes des Speicherbereichs, auf welchen die Variable *zeigt*, machen den *Wert* der Variablen aus.
# Im folgenden definieren und initialisieren wir Variablen mit unterschiedlichen Datentypen: 
# 
# + [Ganze Zahl](sec-int) ``int``, 
# + [Fließkommazahl](sec-float) ``float``, 
# + [Zeichenkette](sec-string) ``str``, 
# + [Wahrheitswert](sec-bool) ``bool``, 
# + eine [Liste](sec-list) ``list``, welche ganze Zahlen ``int`` enthält und
# + ein [Tupel](sec-tuple) ``tuple``, welche Zeichenketten ``str`` enthält.

# In[1]:


number = 111
floating_number = 1.3
characters = 'Hello'
boolean = True
mylist = [1,2,3,4]
mytuple = ('A', 'B', 'C')


# Beim Datentyp ``list`` und ``tuple`` fällt auf, dass diese Werte eines anderen Datentyps enthalten, hier ``int`` und ``str``.
# Solche Datentypen nennen wir [zusammengesetzt Datentypen](sec-datastructures)) wohingegen wir Datentypen, welche wir nicht zerlegen können als [atomare Datentypen](def-atomare-data-types) bezeichnen.
# Diese *atomaren Datentypen* können zudem auch [atomare Datentypen](def-primitive-datatypes) sein.
# 
# Zudem gibt es Datentypen, welche von der jeweiligen Programmiersprache definiert sind und solche die Sie selbst definieren.
# Erstere nennen wir *built-in Datentypen* und letztere werden durch *Klassen* realisiert.
# Wir werden auf [Klassen](sec-class-and-object) erst am Ende des Kurses eingehen.
# 
# Zusammenfassend gibt es fünf Arten von Datentypen:
# 
# 1. Primitive Datentypen,
# 2. atomare Datentypen
# 3. zusammengesetzte Datentypen,
# 4. built-in Datentypen und
# 5. eigens definierte Datentypen.
# 
# Dabei ist ein Datentyp entweder atomar oder zusammengesetzt und zugleich entweder built-in oder eigens definiert.
# Primitive Datentypen sind spezielle atomare Datentypen.
# Oftmals sind built-in Datentypen zugleich primitive Datentypen (siehe z.B. ``Java``, ``C/C++``).
# Eigens definierte Datentypen können niemals primitiv sein.
# 
# ## Primitive Datentypen
# 
# ```{admonition} Primitive Datentypen
# :name: def-primitive-datatypes
# :class: definition
# 
# *Primitive Datentypen* sind jene Datentypen aus denen alle anderen Datentypen einer Sprache hervorgehen.
# Sie sind nicht weiter reduzierbar.
# ```
# 
# Unsere Definitionen von [atomaren](def-atomare-data-types) und [primitiven](def-primitive-datatypes) Datentypen ähneln sich sehr.
# 
# >Worin besteht der Unterschied zwischen einem primitiven und einem atomaren Datentyp?
# 
# Nehmen wir zum Beispiel den ``Python`` Datentyp ``int``.
# Der Wert vom Typ ``int`` besteht nicht nur ais dem reinen Wert der ganzen Zahl sondern enthält zusätzlich noch einen Zähler, welcher angibt wie viele Variablen auf den Wert verweisen.
# Das heißt wir können ``int`` weiter in den Zähler und den eigentlichen Wert zerlegen.
# Allerdings macht es keinen Sinn diese beiden Teile zu zersplittern und separat weiter zu verarbeiten -- sie gehören zusammen, da sie nur gemeinsam verarbeitbar sind!
# Zeichenketten sind weder primitiv noch atomar, denn eine Zeichenkette lässt sich in ihre einzelnen Zeichen zersplittern und die Weiterverarbeitung der einzelner Zeichen macht durchaus Sinn.
# 
# Übertragen wir das auf die 'echte' Welt, so könnte man bei einem Brief von einem Wert eines [zusammengesetzten Datentyps](def-data-structures) sprechen.
# Dieser enthält einen Briefkopf, ein Datum einen Absender, Empfänger und den Text.
# Das Datum ist wiederum ein *zusammengesetzten Datentyp* bestehend aus Tag, Monat und Jahr.
# Der Tag ist schließlich ein *primitiver* oder (in ``Python``) ein *atomarer* Datentyp (eine Zahl zwischen 0 und 31).
# 
# ```{exercise} Der Datentyp Zeichenkette
# :label: datatype-str-exercise
# Ist ``set``, d.h. eine Menge, ein atomarer oder zusammengesetzter Datentyp?
# Begründen Sie Ihre Antwort.
# ```
# 
# ```{solution} datatype-str-exercise
# :label: datatype-str-solution
# :class: dropdown
# 
# ``set`` ist ein zusammengesetzter Datentyp dessen Wert eine variable Anzahl an Werten verschiedener Datentypen enthalten kann.
# ```
# 
# (sec-built-in-data-types)=
# ## Built-in Datentypen
# 
# *Built-in* Datentypen sind jene Datentypen, welche die Programmiersprache (ohne weitere Bibliotheken) mitliefert.
# Zur Vollständigkeit listen wir hier alle *built-in Datentypen* von ``Python`` auf.
# Einige davon werden Sie jedoch in diesem Kurs nicht verwenden.
# Die wichtigsten *built-in Datentypen* sind hervorgehobenen:
# 
# 1. **Das Nichts** ``None``
# 2. Zahlen (Numbers)
#    + **Ganze Zahlen** ``int``
#    + **Fließkommazahl (rationale Zahlen)** ``float``
#    + Komplexe Zahlen ``complex``
# 3. Sequenzen (Sequences)
#     1. Unveränderlich
#        + **Zeichenketten** ``str``
#        + **Tupels** ``tuple``
#        + Bytes ``bytes``
#     2. Veränderlich
#        + **Listen** ``list``
#        + Byte Arrays ``bytearray``
# 4. Mengen (Set types)
#    + **(normale) Mengen** ``set``
#    + (gefrorene Mengen) ``frozenset``
# 5. Abbildungen (Mappings)
#    + **Wörterbuch** ``dict``
# 6. Aufrufbare Typen (Callable)
#    + **Funktionen**
#    + Methoden
#    + Klassen
# 7. Module
# 
# Diese Datentypen stehen Ihnen zur Verfügung sobald Sie ``Python`` auf Ihrem System oder Ihrer Umgebung installiert haben.
# 
# Anders als in vielen anderen Sprachen müssen Sie den (built-in) Datentyp einer Variablen in ``Python`` nicht explizit angeben.
# ``Python`` schließt von der Schreibweise des Wertes automatisch auf den richtigen Datentyp.
# 
# Eine Folge von Ziffern mit einem optional vorangestellten Minuszeichen werden als ganze Zahl ``int`` interpretiert.
# Befindet sich in der Folge ein Punkt ``.`` so wird der Wert als Fließkommazahl interpretiert.
# Sie können den Datentyp einer Variablen ``x`` oder eines Wertes mit ``type(x)`` abfragen:

# In[2]:


type(-3123)


# In[3]:


type(1.313)


# In[4]:


name = 'Anna'
type(name)


# In[5]:


mylist = [1, 2, 3, 4, 'A']
print(f'List Type: {type(mylist)}')
print(f'Element 0 Type: {type(mylist[0])}')
print(f'Element 4 Type: {type(mylist[4])}')


# ## Zusammengesetzte Datentypen
# 
# Zusammengesetzte Datentypen definieren wir durch andere Datentypen, welche bereits definiert wurden.
# Die Basis der zusammengesetzten Datentypen sind deshalb entweder *built-in Datentypen* der Sprache oder eigens definierte zusammengesetzte Datentypen.
# 
# Angenommen Sie wollen den Datentyp ``Person`` definieren welcher sich dadurch auszeichnet, dass er sich aus zwei Zeichenketten ``str`` nämlich dem Vor- und Nachnamen zusammensetzt.
# Durch [Klassen](sec-class-and-object) können Sie einen solchen Datentyp definieren.
# Wie wir dies machen, werden wir auf einen späteren Zeitpunkt verschieben.
# 
# Listen ``list``, Tupel ``tuple``, Mengen ``set`` und Wörterbücher ``dict`` sind *zusammengesetzter built-in Datentypen* und zugleich enthalten die Werte (Objekte) dieser Datentypen eine
# variable Anzahl an Elementen unterschiedlicher Datentypen.
# Eine gute Analogie zu diesen sog, [Sammlung / Kollektion (engl. Collections)](def-collection) sind physikalische Ordner, Schließfächer, Listen auf Papier geschrieben, Rücksäcke, Körbe, Tüten und andere physikalischen Objekte die wir im Alltag verwenden um andere physikalische Objekte zu ordnen, strukturieren oder schlicht zu halten.
# Auch der Arbeitsspeicher ist in diesem Sinne eine sowohl physikalische wie auch virtuelle Kollektion an Bits.
# 
# ```{admonition} Sammlung (Collection)
# :name: def-collection
# :class: definition
# 
# Als *Sammlung* bezeichnen wir alle Datentypen ([Tupel](sec-tuple), [Dictionary](def-python-dictionary), [Listen](sec-list), [Mengen](sec-set) usw.), die eine **variable Anzahl** an anderen Elementen (normalerweise mehrere) beinhalten.
# 
# ```
# 
# Mit **variabler Anzahl** ist gemeint, dass es Sammlung gibt, welche 5 Elemente enthalten und Sammlung gibt die 1000 Elementen enthalten.
# Es kann dennoch sein, dass eine Sammlung die 10 Elemente enthält nicht verändert werden kann, d.h. sie wird auf immer dieser 10 Elemente enthalten.

# In[6]:


mylist = [1, 2, 'A', 3, 1.23, [1, 2, 3]]
mylist


# In[7]:


mytuple = (mylist, 'D')
mytuple


# In[8]:


mydict = {'firstname' : 'Paulina', 'lastname' : 'Schmidt', 'age' : 23 }
mydict


# In[9]:


month = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
month


# Eine Zeichenkette ``str`` ist ebenfalls eine Kollektion, jedoch sind deren Elemente alle vom gleichen Typ -- dem Zeichen.
