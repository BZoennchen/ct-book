---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(sec-data-structures)=
# Datenstrukturen

Programmiersprachen und deren Standardbibliotheken bieten viele vordefinierte Datentypen und Datenstrukturen.
In diesem Abschnitt wollen wir über die fundamentalsten Datenstrukturen sprechen.
Wir werden Ihnen dabei auch eine Implementierung präsentieren, die Sie sich ansehen können sobald Sie genug Erfahrung mit ``Python`` gesammelt haben.
Für eine weiterführende und zugleich angewandte Diskussion verweisen wir auf im **PYTHON** Teil auf das Kapitel [Datentypen (Grundlagen)](sec-python-data-types) und [Datentypen (Fortsetzung)](sec-data-types-advanced).

(sec-pointer)=
## Zeiger

Da sich alle Daten (Programm und dessen Eingabe/Ausgabe) im [Arbeitsspeicher](def-main-memory) befinden, müssen wir begreifen welche Funktionalität diese *konkrete* Datenstruktur bietet.
Alle weiteren *abstrakten* Datenstrukturen bauen auf den Möglichkeiten auf, welche uns der Arbeitsspeicher bietet.

Über die Geschichte hat sich der Arbeitsspeicher in Geschwindigkeit und Größe und bezüglich anderer Eigenschaften weiterentwickelt.
Was uns jedoch interessiert sind die wenigen grundlegenden Eigenschaften, welche sich im Wesentlichen nicht verändert haben:

Addressierbarkeit
: Der Arbeitsspeicher ist im Wesentlichen eine lange **adressierbare** endliche Liste von Bits

Effizienz
: Die Adressierung eines Listeneintrags für eine gegebene Adresse ist sehr effizient

Die Eigenschaft der *effizienten Adressierung* spiegelt sich in allen Programmiersprachen mehr oder weniger pregnannt wieder.

```{figure} ../../figs/art-of-programming/ram.png
---
width: 400px
name: fig-ram-banks
---
Der Arbeitsspeicher ist eine sehr lange Liste bestehend aus [Bits](def-bit).
Die Adresse (links) ist im Wesentlichen die Nummer / der Index eines bestimmten Speicherplatzes (rechts).
Alle Werte sind im Binärsystem dargestellt. An Adresse 00000111 befindet sich eine Adresse.
```

Gewöhnlich adressiert die CPU keine einzelnen Bits, sondern ein ganzes [Byte](def-byte).
{numref}`Abbildung {number} <fig-ram-banks>` zeigt ein Beispiel eines Arbeitsspeichers der uns erlaubt jeweils ein Byte zu adressieren, zugleich werden Adressen, in diesem Beispiel, durch ein Byte dargestellt.

```{exercise} Adressraum
:label: address-space-exercise
Wie viel Byte können im Beispiel von {numref}`Abbildung {number} <fig-ram-banks>` maximal adressiert werden?
```

```{solution} address-space-exercise
:label: address-space-solution
:class: dropdown
Der Adressraum geht von $0000\,0000_2$ bis $1111\,1111_2$.
Das heißt von $0_{10}$ bis $1\,0000\,0000_2 - 1_2 = 2^8-1 = 256-1 = 255$.
Da jede Adresse ein Byte adressiert, können wir somit lediglich $256$ Byte adressieren.
```

```{exercise} 32-Bit-Adressraum
:label: address-space-32-bit-exercise
Weshalb war es vor Jahren nicht möglich mehr als ca. 4 GiB Arbeitsspeicher im Rechner zu verwenden?

**Hinweis:** Es ereignete sich ein Wechsel von einer 32-Bit auf eine 64-Bit Adressierung.
```

```{solution} address-space-32-bit-exercise
:label: address-space-32-bit-solution
:class: dropdown
Mit $32$ bildet sich ein *Adressraum* von $2^{32}$ Adressen.
Wenn die CPU jedes einzelne Byte adressieren können soll, so ergibt sich ein Maximum an 

$$2^{32} \cdot 1 = 2^{10} \cdot 2^{10} \cdot 2^{10} \cdot 2^2$$

Byte und das sind $2^{10} \cdot 2^{10} \cdot 2^2$ KiB, $2^{10} \cdot 2^2$ MiB bzw. $4$ GiB.

```

Im Arbeitsspeicher befinden sich alle Werte (Zahlen, Text, Bilder, Videos) und Adressen in Binärdarstellung.
Eine Adresse im Speicher bezeichnet man häufig auch als *Zeiger/Pointer* oder *Referenz*.
Ein *Zeiger* kann auf einen weiteren *Zeiger* *zeigen/verweisen/referenzieren*.

In {numref}`Abbildung {number} <fig-ram-banks>` zeigt der *Zeiger* an Adresse 3 auf den Speicherbereich bei Adresse 7.
Dies ist wiederum eine Adresse die auf den Speicherbereich 1 zeigt und dort liegt der Wert 0.
Selbstverständlich bedarf es der richtigen [Interpretation](sec-interpretation) der jeweiligen Speicherbereiche, denn es könnte sich beim Wert bei Adresse 3 auch um den Dezimalwert 7 oder irgendetwas anderes als einen *Zeiger* handeln.

Für *Zeiger* gibt es keine perfekte Analogie aus der Realwelt, jedenfalls ist uns keine eingefallen.
Folgendes kommt an den Sachverhalt nahe heran: Nehmen sie eine große geordnete Anreihung von Bankschließfächer als Arbeitsspeicher.
Jedes Schließfach hat eine eindeutige Nummer (Speicheradresse).
In jedem Schließfach kann sich etwas befinden, unter anderem auch ein Zettel mit einer Schließfachnummer (Zeiger).

Das Problem an dieser Analogie ist jedoch, dass, wenn wir den Zettel in Händen halten, wir erst zum entsprechenden Schließfach gehen müssen.
Dabei laufen wir an vielen anderen Schließfächern vorbei.
Das kostet Zeit.
Wenn wir allerdings einen Zeiger haben, so können wir auf den Wert unglaublich schnell zugreifen.
Es kostet der CPU zwar auch etwas Zeit um den Zeiger *aufzulösen* aber muss sie nicht über alle dazwischenliegenden Speicherbereiche "hinweglaufen", d.h. iterieren.

Ein Zeiger ähnelt einer Schnur, dessen erstes Ende wir in Händen halten und dessen anderes Ende am Objekt im Schließfach befestigt ist.
Bei Aktivierung des Zeigers werden wir direkt ins Schließfach teleportiert!

## Einfach verkette Liste

Bleiben wir bei der Analogie der Schließfächer und Schnüre.
Sie möchten ihre Lieblingsgerichte in alphabetischer Reihenfolge abspeichern.
Dazu verwenden Sie die Schließfächer und Schnüre.
Sie halten eine Schnur in den Händen, die auf das Schließfach mit Ihrem absoluten Lieblingsgericht zeigt.
Das darauffolgende Schließfach verweist auf ihr zweitliebstes Gericht usw.
Die bilden eine sog. *verkette Liste* (engl. *Linked List*).

```{figure} ../../figs/art-of-programming/linked-list-ram.png
---
width: 800px
name: fig-linked-list-ram
---
Gerichte 1 bis 5 in einer *verketteten Liste*. 
Jede Kachel repräsentiert ein Schließfach bzw. einen adressierbaren Speicherbereich.
```

Befinden Sie sich an einem Schließfach der Liste, so können Sie recht einfach ein neues Element an dieser Stelle einfügen.
Eine *verkettete Liste* besteht aus sogenannten *Knoten* (Schließfach + Schnur zum nächsten Schließfach), welche durch *Zeiger* verbunden sind.
Sie ist eine *dynamischen* Datenstruktur, d.h. Sie kann zur Laufzeit vergrößert und verkleinert werden.

```{admonition} Dynamische Datenstrukturen
:name: def-dynamic-ds
:class: definition
*Dynamische Datenstrukturen* können zur Laufzeit des Programms anwachsenden und schrumpfen, d.h. ihr Speicherverbrauch kann sich verändern. Möglich wird dies durch die Verwendung von *[Zeigern](sec-pointer)*.
```

Haben wir direkten Zugriff auf einen Knoten so können wir in die *verkettete Liste* ein neues Element was direkt nachfolgt effizient einfügen ohne dabei die anderen Elemente der Liste zu verschieben -- ein wesentlicher Vorteil dieser Datenstruktur.
Jeder Knoten besteht aus zwei Teilen:

Daten
: Der Wert des Knotens (oder auch ein Zeiger auf den Wert des Knotens). Das ist der Inhalt des Schließfachs.

Zeiger
: Verweist auf den nächsten Knoten. Das ist die Schnur, die zum nächsten Schließfach führt.

```{figure} ../../figs/art-of-programming/linked-list-node.png
---
width: 200px
name: fig-linked-list-node
---
Knoten einer *verketteten Liste*.
```

```{code-cell} python3
class Node:
    def __init__(self, value, successor=None):
        self.value = value
        self.successor = successor
        
    def __repr__(self):
        return repr(self.value)
```

Den Anfangsknoten der Liste bezeichnet man als *Kopf/Head*.

```{figure} ../../figs/art-of-programming/linked-list.png
---
width: 800px
name: fig-linked-list
---
Einer *verkettete Liste* aus Zahlen.
```

Um Elemente am *Ende* (engl. *Tail*) einzufügen, kann es sinnvoll sein sich zusätzlich den letzten Knote der Liste zu merken.

## Der Stapel

### Eigenschaften

Der *Stapel* (engl. *Stack*) oder auch *Stapelspeicher/Keller* ist einer der einfachsten [dynamischen Datenstrukturen](def-dynamic-ds), welche dem *Last-In-First-Out (LIFO)* Prinzip folgt.
LIFO bedeutet soviel wie: *zuletzt hinein - zuerst heraus*.
Das was zuletzt hinein gekommen ist, wird auch als erstes herausgenommen.
Das beudeutet, dass wir eingefügte Elemente nur in umgekehrter Reihenfolge aus dem Stapel herausnehmen können.
Gleichbedeutend ist der Begriff *Last Come, First Serve*, d.h. wer zuletzt kommt wird zuerst bedient.

**Wie** der Stapel intern funktioniert ist nicht genau definiert, jedoch ist garantiert, dass die Datenstruktur die folgenden Operationen anbietet.

| Operation                    | Laufzeit                           | Beschreibung                                                            |
| ---------------------------- | ---------------------------------- | ----------------------------------------------------------------------- |
| ``size``                     |  $\mathcal{O}(1)$                  | Liefert Anzahl der Elemente                                             |
| ``push(element)``            |  $\mathcal{O}(1)$                  | Legt das Element ``element`` auf den Stapel                             |
| ``peek()``                   |  $\mathcal{O}(1)$                  | Liefert das Element zurück, welches ganz oben auf dem Stapel liegt      |
| ``pop()``                    |  $\mathcal{O}(1)$                  | Liefert das oberste Element des Stapels zurück und löscht es von diesem |

All diese Operationen müssen eine gute Laufzeit haben. 
Man sagt auch, ihre (Zeit-)Komplexität ist konstant, d.h. $\mathcal{O}(1)$.

Stellen Sie sich einen Stapel aus Büchern vor.
Das Buch was Sie zuletzt auf den Bücherstapel gelegt haben liegt zugriffsbereit ganz oben.
Um auf die anderen Bücher zuzugreifen ohne den Stapel komplett zu zerstören, müssen Sie sich von oben nach unten durcharbeiten und alle Bücher bis zu dem gewünschten Buch vom Stapel nehmen.

Wann könnte diese Datenstruktur sinvoll einsetzbar sein?
Stellen Sie sich vor Sie laufen durch eine fremde Stadt.
Sie orientieren sich anhand von Straßennamen.
Um wieder zurück zu finden laufen Sie diese markanten Stellen in umgekehrter Reihenfolge ab.
Sie können mit einem Stapel auch die Reihenfolge einer Serie von Elementen verändern.
Das Ein- und Austreten aus einem Bus können wir durch einen Stapel modellieren.

### Realisierung

Für die genaue Realisierung eines Stapels gibt es viele Möglichkeiten.
Eine davon stellt die Realisierung der *einfach verketteten Liste* mit einem *Head* dar:

```{code-cell} python3       
class Stack:
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __repr__(self):
        text = '=>'
        node = self._head
        for i in range(self.size):
            if i != 0:
                text += '  '
            text += node.__repr__()
            node = node.successor
            if i < self.size-1:
                text += '\n'
        text += ''
        return text
        
    @property
    def size(self):
        return self._size
    
    def peek(self):
        return self._head.value
    
    def pop(self):
        result = self._head
        self._head = self._head.successor
        result.successor = None
        self._size -= 1
        return result.value
            
    def push(self, value):
        if self._head:
            node = Node(value, self._head)            
            self._head = node
        else:
            self._head = Node(value)
            
        self._size += 1
```

```{code-cell} python3
# Last In
stack = Stack()
print(f'{stack}\n')
stack.push('A')
print(f'{stack}\n')
stack.push('B')
print(f'{stack}\n')
stack.push('C')
print(stack)
```

```{code-cell} python3
# First Out
while stack.size > 0:
    stack.pop()
    print(f'{stack}\n')
```

Wollen wir testen ob ein geklammerter Ausdruck z.B. ``'((3+2)+6)'`` richtig geklammert ist, können wir einen *Stapel* einsetzten, denn ist die erste Klammer eine offene, muss die letzte eine geschlossene sein.
Die folgende Funktion ``parse`` bedient sich eines *Stapels*.
Sie testet ob die Klammerung korrekt ist.

```{code-cell} python3
def parse(expression):
    stack = Stack()
    for c in expression:
        if c == '(':
            stack.push('(')
        elif c == ')':
            if stack.size == 0 or stack.peek() != '(':
                return False
            else:
                stack.pop()
    if stack.size > 0:
        return False
    return True

print(parse('(3+5)*2'))
print(parse('((3+5)*2'))
print(parse('(3+5)*2)'))
print(parse('()()()()((((()))))'))
print(parse('()()()()((((())))'))
```

## Die Warteschlange

### Eigenschaften

Die *Warteschlange* (engl. *Queue*) ist eine [dynamischen Datenstrukturen](def-dynamic-ds) und folgt dem sog. *First-In-First-Out (FIFO)* Prinzip.
FIFO bedeutet soviel wie: *zuerst hinein - zu erst hinaus*.
Das was zuerst hinein gekommen ist, wird auch als erstes herausgenommen.
Das beudeutet, dass wir eingefügte Elemente nur in der gleichen Reihenfolge aus der Queue herausnehmen können.
Gleichbedeutend ist der Begriff *First Come, First Serve*, d.h. wer zuerst kommt mahlt zu erst.

**Wie** die Warteschlange intern funktioniert ist nicht genau definiert, jedoch ist garantiert, dass die Datenstruktur die folgenden Operationen anbietet.

| Operation                    | Laufzeit                           | Beschreibung                                                                   |
| ---------------------------- | ---------------------------------- | ------------------------------------------------------------------------------ |
| ``size``                     |  $\mathcal{O}(1)$                  | Liefert Anzahl der Elemente                                                    |
| ``enqueue(element)``         |  $\mathcal{O}(1)$                  | Fügt das Element ``element`` hinten an                                         |
| ``dequeue()``                |  $\mathcal{O}(1)$                  | Liefert Element an forderster Stelle und löscht dieses aus der Struktur        |

All diese Operationen müssen eine gute Laufzeit haben. 
Man sagt auch, ihre (Zeit-)Komplexität ist konstant, d.h. $\mathcal{O}(1)$.
Der $i$-ten ``dequeue`` Aufruf liefert genau das Element, welches beim $i$-ten ``enqueue`` Aufruf von eingefügt wurde.

Der Name rührt daher, dass die Datenstruktur wie eine Warteschlange an der Kasse funktioniert.
Der Kunden die sich zuerst in die Schlange einreihen, werden auch zuerst bedient und können die Schlange auch zuerst wieder verlassen.
Wegen dieser Eigenschaft werden *Queues* oft als *Puffer* eingesetzt.
Zum Beispiel werden die Netzwerkpakete die Ihr Router versendet erst in einer Queue gehalten und dann gesendet.

### Realisierung

Erneut gibt es unterschiedliche Möglichkeiten diese Datenstruktur zu realisieren.
Glücklicherweise können wir abermals auf die *einfach verketteten Liste* zurückgreifen.
Allerdings ist es notwendig sowohl auf den Kopf (*Head*) als auch auf das Ende (*Tail*) der Liste effizient zugreifen zu können.
Deshalb merken wir uns und verwalten zusätzlich das Ende der Liste, d.h. den (*Tail*).

```{code-cell} python3
class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __repr__(self):
        text = '['
        node = self._head
        for i in range(self.size):
            text += node.__repr__()
            node = node.successor
            if i < self.size-1:
                text += ', '
        text += ']'
        return text
        
    @property
    def size(self):
        return self._size
    
    def dequeue(self):
        result = self._head
        self._head = self._head.successor
        result.successor = None
        self._size -= 1
        return result.value
            
    def enqueue(self, value):
        node = Node(value)   
        if self._tail:         
            self._tail.successor = node
            self._tail = node
        else:
            self._tail = node
            self._head = self._tail
            
        self._size += 1
```

Lassen uns die Warteschlange fülle

```{code-cell} python3
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue
```

 und wieder leeren.

```{code-cell} python3
for _ in range(queue.size):
    print(queue.dequeue())
```

## Doppelt verkettete Liste

Die *doppelt verkettete Liste* (engl. *Dequeue*) ist einer Erweiterung der *(einfach) verketteten Liste* und zugleich eine Kombination aus Warteschlange und Stack.
Sie besteht aus Knoten, die nicht nur einen Zeiger auf den nächsten sondern auch auf den vorherigen Knoten enthalten.
Das macht die Liste flexibler.
Es lassen sich effizient vorne und hinten Elemente einfügen und löschen, doch ist der Verwaltungsaufwand größer.

```{code-cell} python3
class NodeD:
    def __init__(self, value, predecessor=None, successor=None):
        self.value = value
        self.successor  = successor
        self.predecessor = predecessor
        
    def __repr__(self):
        return repr(self.value)
    
    def append(self, node):
        successor = self.successor
        
        self.successor = node
        node.predecessor = self
        
        node.successor = successor
        if successor:
            successor.predecessor = node
        
    def prepend(self, node):
        predecessor = self.predecessor
        
        self.predecessor = node
        node.successor = self
    
        node.predecessor = predecessor    
        if predecessor:
            predecessor.successor = node
```


Um einen neuen Knoten hinter einem gegebenen Knoten anzuhängen ``append`` müssen wir lediglich die *Zeiger* richtig "verbiegen".
Auch diese Operation ist, bezogen auf die Laufzeit, sehr günstig.
Wollen wir testen ob die Liste einen bestimmten Wert enthält ``contains``, so müssen wir diese von Kopf bis Fuß durchsuchen.
Diese Operation ist teuer!

Der Folgende Code zeigt die Realisierung eines Knotens durch eine ``Python``-Klasse.

Die Klasse ``DoubleLinkedList`` zeigt eine sehr simple Realisierung einer *doppelt verketteten Liste*:

| Operation                    | Laufzeit                           | Beschreibung                                                   |
| ---------------------------- | ---------------------------------- | -------------------------------------------------------------- |
| ``size``                     |  $\mathcal{O}(1)$                  | Liefert Anzahl der Elemente                                    |
| ``prepend(element)``         |  $\mathcal{O}(1)$                  | Fügt das Element ``element`` vorne an (es wird zum Head)       |
| ``append(element)``          |  $\mathcal{O}(1)$                  | Fügt das Element ``element`` hinten an (es wird zum Tail)      |
| ``first()``                  |  $\mathcal{O}(1)$                  | Liefert erstes Element (Head) ohne es zu löschen               |
| ``last()``                   |  $\mathcal{O}(1)$                  | Liefert letzte Element (Tail) ohne es zu löschen               |
| ``remove_first()``           |  $\mathcal{O}(1)$                  | Liefert erstes Element (Head) und löscht es aus der Liste      |
| ``remove_last()``            |  $\mathcal{O}(1)$                  | Liefert letzte Element (Tail) und löscht es aus der Liste      |
| ``contains(element)``        |  $\mathcal{O}(n)$                  | ``True`` genau dann wenn ``element`` in der Liste ist.         |
| ``__getitem__(i)``           |  $\mathcal{O}(n)$                  | Liefert Element an der ``i``-ten Stelle in der Liste           |
| ``__setitem__(i, value)``    |  $\mathcal{O}(n)$                  | Ersetzt ``i``-tes Element in der Liste mit ``value``           |
| ``__delitem__(i)``           |  $\mathcal{O}(n)$                  | Ersetzt ``i``-tes Element in der Liste mit ``value``           |

```{code-cell} python3
class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __repr__(self):
        text = '['
        node = self._head
        for i in range(self._size):
            text += node.__repr__()
            node = node.successor
            if i < self._size-1:
                text += ', '
        text += ']'
        return text
        
    @property
    def size(self):
        return self._size
    
    def first(self):
        return self._head.value
    
    def last(self):
        return self._tail.value
    
    def remove_last(self):
        tail = self._tail
        self._tail = self._tail.predecessor
        tail.predecessor = None
        
        if self._tail:
            self._tail.successor = None
        self._size -= 1
        return tail.value
        
    def remove_first(self):
        head = self._head
        self._head = self._head.successor
        head.successor = None
        
        if self._head:
            self._head.predecessor = None
        self._size -= 1
        return head.value
            
    def append(self, vale):
        node = NodeD(value)
        if self._head:
            self._tail.append(node)
            self._tail = node
        else:
            self._head = node
            self._tail = self._head
        self.size += 1
        
    def prepend(self, value):
        node = NodeD(value)
        if self._head:
            self._head.prepend(node)
            self._head = node
        else:
            self._head = node
            self._tail = self._head
        self._size += 1
        
    def contains(self, value):
        node = self._head
        for _ in range(self.size):
            if node.value == value:
                return True
            node = node.successor
        return False
    
    def __get_node(self, key):
        if key < 0:
            key = key+self.size
        
        if self.size//2 > key:        # forwards
            r = range(key)
            node = self._head
            for _ in range(key):
                node = node.successor
        else:                         # backwards
            node = self._tail
            r = range(self.size-1, -1, -1)
            for _ in range(key):
                node = node.predecessor
        return node
    
    def __delitem__(self, key):
        # del lst[key]
        if key == 0:
            self.remove_first()
        elif key == self.size-1 or key == -1:
            self.remove_last()
        else:
            node = self.__get_node(key)
            predecessor = node.successor
            successor = node.successor
            predecessor.successor = succesor
            successor.predecessor = predecessor
            
            node.successor = None
            node.predecessor = None
            self._size -= 1
    
    def __getitem__(self, key):
        # self[key]
        return self.__get_node(key).value
            

    def __setitem__(self, key, value):
        # self[key] = value
        node = self.__get_node(key)
        node.value = value
```

```{code-cell} python3
lst = DoubleLinkedList()
lst.prepend(13)
lst.prepend(31)
lst.prepend(44)
lst.prepend(54)

lst
```

```{code-cell} python3
lst.last()
```

```{code-cell} python3
lst.first()
```

```{code-cell} python3
print(lst.contains(13))
print(lst[3])
del lst[3]
print(lst.contains(13))
lst
```


```{code-cell} python3
while lst.size > 0:
    print(lst.remove_last())

lst
```





## Dequeue

TODO

## Arrays

TODO

## Hashmaps

TODO

## Bäume

TODO
