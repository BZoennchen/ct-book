(sec-purity)=
# Reinheit

Bevor wir nochmals die Implementierung und Nutzung einer ``Python``-Funktion besprechen, möchten wir Ihnen den Unterschied zwischen einer mathematischen Funktion und einer ``Python``-Funktion verdeutlichen -- Funktion ist eben nicht gleich Funktion!

## Reine Funktionen

Den Begriff 'Funktion' kennen wir aus der Mathematik, z.B. ist 

$$f(x) = 2 \cdot x + 3$$

eine [mathematische Funktion](sec-math-function).
Sind wir pedantisch oder geht der Definitions- und Wertebereich nicht aus dem Kontext hervor, so geben wir bei einer Funktionsdefinition üblicherweise diese beiden Mengen an, z.B.

$$f : \mathbb{R} \rightarrow \mathbb{R}$$

Diese mathematische Funktion $f$ können wir als ``Python``-Funktion realisieren:

def f(x):
    return 2*x + 3

f(5)

Dennoch unterscheiden sich die beiden Funktionen.
Die mathematische Funktion ist das abstrakte Etwas und die ``Python``-Funktion eine Realisierung.
Wir bringen das Abstrakte in die echte Welt.

Funktionen, welche Funktionen im mathematischen Sinne sind, bezeichnet man als [reine Funktionen](def-pure-function) (engl. *pure Functions*).

```{admonition} Reine Funktionen
:class: attention
:name: attention-pure-functions

*Unreine Funktionen* zu definieren sollte einen wichtigen Grund haben, andernfalls sind *reine Funktionen* zu bevorzugen! 
```

## Unreine Funktionen

Allerdings ist nicht jede ``Python``-Funktion auf eine mathematische Funktion zurückzuführen.
Eine mathematische Funktion **kennt keinen Zustand**, also keine Dinge die sich ändern können.
Sie erhält einen oder mehrere Argumente und gibt ein Ergebnis zurück -- das ist alles.

In ``Python`` und nahezu allen anderen Programmiersprachen gibt es jedoch Dinge die sich ändern können, nämlich zusammengesetzte Datentypen bzw. *Datenstrukturen*.
Und niemand verbietet uns diese *Datenstrukturen* innerhalb einer Funktion zu verändern.

Zum Beispiel löscht folgende ``Python``-Funktion das letzte Element aus einer Liste.
Sie hat keinen ``return``-Ausdruck und gibt deshalb ``None`` zurück.
Allerdings verändert sie die übergebene Liste ``mylist``!

def remove_last(mylist):
    del mylist[-1]
    
mylist = [1,2,3]
remove_last(mylist)
mylist

Dies bezeichnen wir als einen sog. *Seiteneffekt*, welcher oft erwünscht aber auch oft unerwünscht ist.

Wir können durch eine kleine Änderung aus der Funktion eine Funktion im mathematischen Sinne machen.
Dafür dürfen wir keinen **Zustand** verändern, d.h. die übergebenen Argumente (die Eingabe) dürfen nicht verändert werden.

def remove_last(mylist):
    copy = mylist.copy()
    del copy[-1]
    return copy
   
mylist = [1,2,3]
returned_list = remove_last(mylist)
print(f'mylist: {mylist}')
print(f'returned_list: {returned_list}')

## Ist rein auch immer besser?

Das Wort *rein* ist wertend, was uns, um ehrlich zu sein, nicht sonderlich gefällt.
Zwar sollten wir, wenn es geht und keine Nachteile entstehen, *reine Funktionen* bevorzugen, doch basiert die [imperative Programmierung]() auf Seiteneffekten und damit auf der *'Unreinheit'*.
Diese ist nicht per se schlecht.
Oftmals ist sie notwendig und wichtig.

Nehmen wir eine Funktion, welche ein paar wenige Elemente einer Liste verändert.
Diese kann nur *rein* sein, wenn wir eine Kopie der Liste anlegen.
Was ist aber wenn diese Funktion oft auf der gleichen Liste aufgeführt werden soll?
Der verschwendete Speicherplatz und die verschwendete Rechenzeit machen eine Implementierung als *reine Funktion* wenig sinnvoll.

Dennoch, reine Funktionen machen Ihren Code für Sie und andere leserlicher.
Oftmals reicht es lediglich genau jene Funktion zu betrachten um herauszufinden was geschieht.
Funktionen die hingegen einen Zustand ändern, sind oft schwer zu verstehen.
Wir müssen oftmals den Zustand selbst betrachten und das kann eine ganze Kaskade von Analysen erfordern.

Als Randnotiz sei gesagt, dass es in der funktionalen Programmierung nur *reine Funktionen* gibt.
Um den Laufzeiteinbußen und dem erhöhten Speicherverbrauch entgegenzuwirken, wird das Kopieren von *Datenstrukturen* jedoch clevere gelöst.
Schlüssel ist die *Unveränderlichkeit* **aller** *Datentypen*.