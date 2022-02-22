#!/usr/bin/env python
# coding: utf-8

# (sec-induction)=
# # Vollständige Induktion
# 
# Die *vollständige Induktion* ist eine mathematische Beweistechnik aber viel mehr ist sie auch eine *Denkart* die insbesondere bei der Entwicklung von Datenstrukturen und Algorithmen eine große Rolle spielt.
# Mithilfe der vollständigen Induktion können wir oftmals die Korrektheit und Laufzeit unserer Programme darlegen.
# Auch ist die vollständige Induktion eine Art der [(rekursiven) Wiederholung](sec-recursion).
# 
# ## Gaußsche Summenformel
# 
# Starten wir mit dem Mutter aller Beispiele: Der Addition aller natürlichen Zahlen die kleiner gleich $n$ sind.
# Man erzählt sich, dass der kleine Gauß eines Tages in der Schule die Aufgabe erhielt alle natürlichen Zahlen von $1$ bis $n$ zu addieren.
# Gesucht ist also:
# 
# $$1 + 2 + 3 + 4 + \ldots + n.$$
# 
# Wir können diese Summe in ``Python`` sehr einfach berechnen:

# In[1]:


n = 100
sum([i for i in range(n+1)])


# Der kleine Gauß hatte jedoch keinen Computer zur Hand und wollte sich die lästige Rechnerei vereinfachen.
# Sagen wir $n = 100$.
# Dann wird aus der Summe:
# 
# $$1 + 2 + 3 + 4 + \ldots + 100.$$
# 
# Ordnen wir diese Summe aber nach dem Schema von Gauß an:
# 
# $$[1 + 100] + [2 + 99] + [3 + 98] + [4 + 97] \ldots + [50 + 51]$$
# 
# wird klar, dass diese Summe gleich
# 
# $$[1 + 100] \cdot 50$$
# 
# ergibt.
# Versuchen wir es nun mit der allgemeinen Summe, also
# 
# $$1 + 2 + 3 + 4 + \ldots + n$$
# 
# dann können wir diese wie folgt anordnen
# 
# 
# $$[1 + n] + [2 + (n-1)] + [3 + (n-2)] + \ldots + [n/2 + (n-n/2+1)] = \frac{n \cdot (n+1)}{2}.$$
# 
# Das erscheint nach längerer Betrachtung einleuchtend.
# Es scheint als gelte
# 
# $$1 + 2 + 3 + 4 + \ldots + n = \sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}$$
# 
# aber wir wollen dies nun auch beweisen, sodass es absolut einwandfrei und unangreifbar der Wahrheit entspricht.
# 
# ## Der Dominoeffekt
# 
# Der Trick bei der *vollständigen Induktion* könnten wir als den Dominoeffekt bezeichnen.
# Wenn wir wissen dass
# 
# 1. der erste Dominostein umfällt und
# 2. sofern der $n$-te Dominostein umfällt auch der $n+1$-te Stein umfällt
# 
# dann folgt daraus, dass alle Steine umfallen!
# Wir zeigen zwei lokale Sachverhalte und können dadurch auf einen globalen Sachverhalt schließen.
# 
# (sec-induction-proof)=
# ## Induktionsbeweis
# 
# Beim Induktionsbeweis wollen wir eine Aussage $A(n)$ für alle $n \geq n_0$ beweisen.
# Dabei sind $n$ und $n_0$ natürliche Zahlen und $n_0$ ist ein fester Wert, üblicherweise 0 oder 1.
# Wir nutzten den Dominoeffekt.
# 
# 1. **Induktionsanfang:** Wir zeigen, dass $A(n_0)$ gilt.
# 2. **Induktionsschritt:** Wir zeigen für ein beliebiges $n \geq n_0$ dass wenn $A(n)$ gilt, $A(n+1)$ folgt.
# 
# ```{admonition} Induktionsschritt
# :name: attention-induction
# :class: attention
# 
# Wir zeigen **nicht** dass $A(n+1)$ gilt, sondern dass
# 
# $$A(n) \Rightarrow A(n+1)$$
# 
# gilt.
# 
# ```
# 
# ````{admonition} Gaußsche Summenformel
# :name: theorem-gauss-sum
# :class: theorem
# 
# Sei $n$ eine natürliche Zahl so gilt:
# 
# $$\sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}.$$
# 
# ````
# 
# ```{admonition} Gaußsche Summenformel
# :name: proof-gauss-sum
# :class: proof
# 
# **(1) Induktionsanfang:** $n_0 = 1$ und es gilt in der Tat 
# 
# $$\sum\limits_{k=1}^1 k = 1 = \frac{1 \cdot (1+1)}{2} = \frac{2}{2}.$$
# 
# Damit gilt $A(n_0)$.
# 
# **(2) Induktionsschritt:** Angenommen es gilt $A(n)$ also
# 
# $$\sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}.$$ 
# 
# Die Summe der Zahlen $1$ bis $n+1$ lässt sich schreiben als:
# 
# $$\sum\limits_{k=1}^{n+1} k = n+1 + \sum\limits_{k=1}^{n} k = n+1 + \frac{n \cdot (n+1)}{2}.$$
# 
# Bei diesem Schritt verwenden wir die Annahme, dass $A(n)$ gilt!
# Nun können wir die Formel etwas umstellen:
# 
# $$n+1 + \frac{n \cdot (n+1)}{2} = \frac{2n+2 + n \cdot (n+1)}{2} = \frac{2n+2 + n^2 + n}{2}.$$
# 
# Klammern wir $n+1$ aus, erhalten wir:
# 
# $$\frac{2n+2 + n \cdot (n+1)}{2} = \frac{(n+1) \cdot 2 + n \cdot (n+1)}{2} = \frac{(n+1) \cdot (n+2)}{2}.$$
# 
# D.h. es gilt $A(n+1)$ also
# 
# $$\sum\limits_{k=1}^{n+1} = \frac{(n+1) \cdot (n+2)}{2}$$
# 
# unter der Annahme von $A(n)$.
# 
# Aus **(1)** und **(2)** folgt die Aussage.
# ```
# 
# ## Induktive Denkweise
# 
# Anstatt eine Aussage zu beweisen kann die Induktion auch dabei helfen Algorithmen zu entwickeln.
# Wenn Sie ein Problem für $n$ Datenpunkte / Elemente lösen wollen hilft es möglicherweise, wenn Sie stattdessen das Problem für $n_0$ Elemente zu lösen.
# Und zusätzlich das Problem für $n+1$ Elemente lösen jedoch **unter der Annahme** Sie hätten es bereits für $n$ Elemente gelöst.
# Zusammengenommen reicht das aus um das Problem für beliebig viele Elemente zu lösen!
# 
# Ein Algorithmus der nach diesem Prinzip entwickelt wurde ist der [Mergesort Algorithmus](https://de.wikipedia.org/wiki/Mergesort) oder die Lösung für die [Türme von Hanoi](sec-hanoi).
# 
# ```{exercise} Permutationen
# :label: induction-permutation-exercise
# 
# Sei ein $n$-Tupel $(a_1, a_2, \ldots, a_n)$ aus verschiedenen natürlichen Zahlen gegeben.
# Schreiben Sie ein Programm was eine Liste aller Permutationen des Tupels erzeugt.
# Eine Permutation ist ein Tupel mit den gleichen Elementen in einer anderen Reihenfolge.
# 
# ```
# 
# Diese Aufgabe können wir *induktiv* bzw. *rekursiv* lösen.
# 
# **(1) Induktionsanfang:** 
# Für $n_0=1$ enthält unsere Lösung genau ein Tupel.
# Es gibt genau eine Permutation.
# 
# **(2) Induktionsschritt:** 
# Was machen wir für ein ein $n+1$-Tupel unter der Annahme wir haben das Problem für $n$ gelöst?
# Nun, für jede Permutation des $n$-Tupels erzeugen wir $n+1$ Permutationen des $n+1$-Tupels indem das hinzugekommene $n+1$-te Elemente zwischen jede zwei Zahlen (und an den Anfang und das Ende eines Tupels) stecke.
# 
# Haben wir zum Beispiel das Tupel $(1,2)$ ergibt das die Permutationen $(1,2), (2,1)$.
# Wollen wir nun die Permutationen von $(1,2,3)$ erzeugen ergibt dies: $(3,1,2), (1,3,2), (1,2,3)$ und $(3, 2, 1), (2, 3, 1), (2, 1, 3)$.

# In[2]:


numbers = [1,2,3]

def permutations(numbers):
    if len(numbers) == 1:
        return [numbers] # A(n0)
    else:
        result = []
        last = numbers[-1]
        perms = permutations(numbers[:-1]) # A(n)

        # A(n+1) assuming A(n)
        for perm in perms:
            for i in range(len(perm)+1):
                perm_copy = perm.copy()
                perm_copy.insert(i, last)
                result.append(perm_copy)
        return result

permutations(numbers)


# Ist das die beste, effizienteste bzw. einzige Lösung?
# Sicher nicht!
# Darum geht es vorerst auch nicht.
# 
# Das schöne an *Induktionsbeweisen* ist, dass Sie konstruktiv sind, d.h., der Beweis offenbart uns einen Algorithmus, welcher zur Lösung führt!
