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

(sec-induction)=
# Vollständige Induktion

Bei einer *Induktion* schließen wir von speziellen Sachverhalten (häufig empirischen Beobachtungen) auf einen generellen Sachverhalt.
Wenn ich, zum Beispiel, Katzen untersuche und immer nur schwarze Katzen zu Gesicht bekomme, dann wäre ein induktiver Schluss, dass alle Katzen schwarz sind.
Diese Art des Schließens wurde und wird immer wieder attackiert, da die Induktion keine abolute Gewissheit zulässt.
Dennoch ist sie nützlich, so dachte Newton *induktiv* als er seine Gesetze der Mechanik aufgestellt hat.
Aus der Beobachtung mehrerer Sachverhalte, z.B. dass der Apfel vom Baum fällt, schloss er auf ein allgemeines physikalisches Gesetz.
Doch hatte er keine Gewissheit und wie wir mittlerweile Wissen konnte Einstein die Gesetze von Newton widerlegen.
Newton lag also falsch und dennoch reicht sein falsches aber nützliches Modell aus um zum Mond zu fliegen.

Auch Einsteins Modell kann sich in der Zukunft als falsch herausstellen.
Das Scheitern einer Theorie wird heutzutage immer erwartet, denn in den Naturwissenschaften verwendet man gewöhnlich den sog. *Falsifikationismus* von Karl Popper.
Dabei gehen Wissenschaftler davon aus, dass eine Theorie niemals wahr ist.
Stattdessen wird sie solange anerkannt bis sie widerlegt wurde.
Zudem muss sie widerlegbar sein, um überhaupt als Theorie gelten zu können.

Das Gegenstück zur Induktion ist die *Deduktion*.
Traditionell schließen wir dabei von einem allgemeinen Sachverhalt auf einen spezielleren Sachverhalt.
Zum Beispiel:

1. Alle Menschen sind sterblich und
2. Sokrates ist ein Mensch.
3. Daraus folgt, dass Sokrates sterblich ist.

Durch (1 u. 2) schließen wir *deduktiv* auf (3).
In der moderne Logik spricht man davon, dass eine Schlussfolgerung **zwingend** gültig ist.
Diese Art des Schließens ist unbedenklich.
Allerdings kommt man mit ihr oft nicht weit, wenn neue Theorien über die Welt erschlossen werden sollen, da wir in diesem Fall auf empirische Beobachtungen angewiesen sind.

Die *vollständige Induktion* behebt die Probleme der herkömmlichen Induktion, indem sie alle möglichen Spezialfälle einbezieht, selbst wenn es sich um unendlich viele handelt.
Anstelle nach einer bestimmten Anzahl von betrachteten schwarzen Katzen aufzuhören, sehen ich mir **alle** Katzen, selbst wenn es unendlich viele sind, an!
Die herkömmliche Induktion wird sozusagen vervollständigt.
Leider ist es in der Praxis unmöglich alle Katzen anzusehen.
Möglicherweise werden neue Katzen geboren und selbst wenn derzeit alle Katzen ein schwarzes Fell haben, wird möglicherweise morgen schon eine weiße Katze geboren.

## Der Dominoeffekt

Es gibt allerdings ein Beispiel aus der Praxis, was der vollständigen Induktion sehr Nahe kommt: Der Fall einer Reihe von Dominosteinen.
Angenommen Sie sollen beweisen, dass alle Dominosteine umfallen, sobald sie den ersten Stein umwerfen.
Sie möchten den Vorgang aber nicht dadurch zeigen, indem sie ihn tatsächlich ausführen.
Ihre 1000 Dominosteine wieder aufzustellen ist einfach zu aufwendig.
Um uns zu überzeugen verfahren Sie stattdessen wie folgt: Sie nehmen sich zwei Dominosteine und stellen diese hintereinander angeordnet auf.
Sie werfen den ersten Stein um, sodass dieser den zweiten zu Fall bringt.
Daraufhin stellen Sie folgenden "Beweis" auf:

1. **Induktionsannahme:** Der erste Dominostein fällt um 
2. **Induktionsschritt:** Wenn ein Dominostein umfällt, so fällt auch sein Nachfolger um.
3. **Induktionsschluss:** Gilt (1) und (2) folgt daraus, dass alle Dominosteine umfallen.

Wenn wir definieren, dass $A(n)$ bedeutet, dass der $n$-te Dominostein umfällt, dann können wir den eben beschriebenen Schluss wie folgt formulieren:

1. **Induktionsannahme:** $A(1)$
2. **Induktionsschritt:** $\forall n \in \mathbb{N}: A(n) \Rightarrow A(n+1)$
3. **Induktionsschluss:** $[A(1) \land (\forall n \in \mathbb{N}: A(n) \Rightarrow A(n+1))] \Rightarrow (\forall n \in \mathbb{N}: A(n))$

oder kurt

$$[A(1) \land (A(n) \Rightarrow A(n+1))] \Rightarrow A(n).$$

Den Induktionsschritt können Sie allerdings nur annehmen, wenn wirklich immer wenn ein Dominostein umfällt auch sein Nachfolger umfällt.
In der Praxis ist diese Gewissheit nicht gegeben.
Sie könnten argumentieren, dass alle Steine exakt gleich angeordnet sind und dass sie den ersten Stein genau so umstoßen als wäre er von einem anderen Stein umgestoßen worden und dass mehrere umfallende Steine in Zeitlupe betrachtet haben und alle Fallen auf die scheinbar exakt gleich Art um.
All das macht den Schluss allerdings noch immer nicht gewiss, da Sie sich in einer physikalischen Welt bewegen in der wir nicht alles bis aufs kleinste Elektron berücksichtigen können.

Glücklicherweise sind mathematische Objekte zeitlos und abstrakt.
Für mathematische Dominosteine können wir den Beweis, wie er oben beschrieben wurde, führen.
Unsere mathematischen Dominosteine sind dabei die *natürlichen Zahlen*, denn wir benötigen die Eigenschaft des Abzählens oder Nummerierens---wir müssen jedem Objekt (z.B. unserem imaginären Dominostein) eine Zahl zuweisen können und wir müssen den Nachfolger eines Objekts benennen können.
Da jede abzählbare Menge sich durch natürliche Zahlen repräsentieren lässt, wird die vollständige Induktion über die natürlichen Zahlen geführt.

Die *vollständige Induktion* ist also eine mathematische Beweistechnik im Zusammenhang mit den natürlichen Zahlen.
Darüber hinaus ist sie eine *Denkart* die insbesondere bei der Entwicklung von Datenstrukturen und Algorithmen eine große Rolle spielt, denn jede Wiederholung von bestimmten Befehlsabfolgen, beispielsweise druch eine Schleife, kann man *abzählen*. 
Deshalb können wir mit der vollständigen Induktion oftmals die Korrektheit und Laufzeit unserer Programme darlegen.
In der vollständige Induktion selbst ist die [(rekursiven) Wiederholung](sec-recursion) eingebaut.

## Gaußsche Summenformel

Starten wir mit der Mutter aller Beispiele: Der Addition aller natürlichen Zahlen die kleiner gleich $n$ sind.
Man erzählt sich, dass der kleine Gauß eines Tages in der Schule die Aufgabe erhielt alle natürlichen Zahlen von $1$ bis $n$ zu addieren.
Gesucht ist also:

$$1 + 2 + 3 + 4 + \ldots + n.$$

Wir können diese Summe in ``Python`` sehr einfach berechnen:

```{code-cell} python3
n = 100
sum([i for i in range(n+1)])
```

Der kleine Gauß hatte jedoch keinen Computer zur Hand und wollte sich wahrscheinlich die lästige Rechnerei vereinfachen.
Er kam auf folgenden Gedanken:
Sagen wir $n = 100$.
Dann müssen wir die folgende Summe berechnen:

$$1 + 2 + 3 + 4 + \ldots + 100.$$

Ordnen wir diese Summe aber nach dem kleveren Schema von Gauß an:

$$[1 + 100] + [2 + 99] + [3 + 98] + [4 + 97] \ldots + [50 + 51]$$

wird klar, dass diese Summe gleich

$$[1 + 100] \cdot 50$$

ergibt.
Versuchen wir es nun mit der allgemeinen Summe, also

$$1 + 2 + 3 + 4 + \ldots + n$$

dann können wir diese wie folgt anordnen


$$[1 + n] + [2 + (n-1)] + [3 + (n-2)] + \ldots + [n/2 + (n-n/2+1)] = \frac{n \cdot (n+1)}{2}.$$

Das erscheint nach längerer Betrachtung einleuchtend.
Es scheint, als gelte

$$1 + 2 + 3 + 4 + \ldots + n = \sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}.$$

Aber wir wollen dies nun auch beweisen, sodass es absolut einwandfrei und unangreifbar der Wahrheit entspricht.
Die meisten wären durch den soeben gezeigten Zusammenahang überzeugt.
Doch bietet die vollständige Induktion ein gewisses Schema, durch das wir auch andere Zusammenhänge beweisen können.

(sec-induction-proof)=
## Induktionsbeweis

Beim Induktionsbeweis wollen wir eine Aussage $A(n)$ für alle $n \geq n_0$ beweisen.
Dabei sind alle $n$ und $n_0$ natürliche Zahlen und $n_0$ ist ein (einzelner) fester Wert, üblicherweise 0 oder 1.
Wir nutzten den Dominoeffekt.

1. **Induktionsanfang:** Wir zeigen, dass $A(n_0)$ gilt.
2. **Induktionsschritt:** Wir zeigen für ein **beliebiges** $n \geq n_0$ dass wenn $A(n)$ gilt, $A(n+1)$ folgt.

```{admonition} Induktionsschritt
:name: attention-induction
:class: attention

Wir zeigen **nicht** dass $A(n+1)$ gilt, sondern dass

$$A(n) \Rightarrow A(n+1)$$

gilt.

```

Lassen Sie uns folgendes Theorem beweisen.
Sie können es gerne erst einmal selbst versuchen.

````{admonition} Gaußsche Summenformel
:name: theorem-gauss-sum
:class: theorem

Sei $n$ eine natürliche Zahl so gilt:

$$\sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}.$$

````

```{admonition} Gaußsche Summenformel
:name: proof-gauss-sum
:class: proof dropdown

**(1) Induktionsanfang:** $n_0 = 1$ und es gilt in der Tat 

$$\sum\limits_{k=1}^1 k = 1 = \frac{1 \cdot (1+1)}{2} = \frac{2}{2}.$$

Damit gilt $A(n_0)$.

**(2) Induktionsschritt:** Angenommen es gilt $A(n)$ also

$$\sum\limits_{k=1}^n k = \frac{n \cdot (n+1)}{2}.$$ 

Die Summe der Zahlen $1$ bis $n+1$ lässt sich deshalb schreiben als:

$$\sum\limits_{k=1}^{n+1} k = n+1 + \sum\limits_{k=1}^{n} k \stackrel{\text{I.A.}}{=} n+1 + \frac{n \cdot (n+1)}{2}.$$

Beim letzten Schritt verwenden wir den Induktionsannahme (I.A.) aus dem Induktionsanfang, in anderen Worten die Tatsache dass $A(n)$ gilt, jedoch nur für $n < n+1$!
Nun können wir die Formel etwas umstellen:

$$n+1 + \frac{n \cdot (n+1)}{2} = \frac{2n+2 + n \cdot (n+1)}{2} = \frac{2n+2 + n^2 + n}{2}.$$

Klammern wir $n+1$ aus, erhalten wir:

$$\frac{2n+2 + n \cdot (n+1)}{2} = \frac{(n+1) \cdot 2 + n \cdot (n+1)}{2} = \frac{(n+1) \cdot (n+2)}{2}.$$

D. h. es gilt $A(n+1)$ also

$$\sum\limits_{k=1}^{n+1} = \frac{(n+1) \cdot (n+2)}{2}$$

unter der Annahme von $A(n)$.
Aus **(1)** und **(2)** folgt die Aussage.
```

## Induktive Denkweise

Anstatt eine Aussage zu beweisen kann die Induktion auch dabei helfen Algorithmen zu entwickeln.
Wenn Sie ein Problem für $n$ Datenpunkte / Elemente lösen wollen hilft es möglicherweise, wenn Sie stattdessen das Problem für $n_0$ Elemente zu lösen versuchen.
Wenn Sie zusätzlich wissen wie sie von $n$ nach $n+1$ gelangen, also das Problem für $n+1$ lösen unter der Annahme, dass sie das Problem für $n$ bereits gelöst haben, dann haben Sie eine Lösung für alle $n$, also alle Fälle, entwickelt.
Zusammengenommen reicht das aus um das Problem für beliebig viele Elemente zu lösen!

Ein Algorithmus der nach diesem Prinzip entwickelt wurde ist der [Mergesort Algorithmus](https://de.wikipedia.org/wiki/Mergesort) oder die Lösung für die [Türme von Hanoi](sec-hanoi).
Betrachten wir eine andere konkrete Programmieraufgabe: Die Generierung aller *Permutationen* eines Tupels.

```{exercise} Permutationen
:label: induction-permutation-exercise

Sei ein $n$-Tupel $(a_1, a_2, \ldots, a_n)$ aus verschiedenen natürlichen Zahlen gegeben.
Schreiben Sie ein Programm was eine Liste aller Permutationen des Tupels erzeugt.
Eine Permutation ist ein Tupel mit den gleichen Elementen in einer anderen Reihenfolge.

```

Diese Aufgabe können wir *induktiv* bzw. *rekursiv* lösen.

**(1) Induktionsanfang:** 
Für $n_0=1$ hat das Tupel nur ein Element und somit enthält unsere Lösung genau ein Tupel.
Es gibt genau eine Permutation.

**(2) Induktionsschritt:** 
Was machen wir für ein Tupel welches $n+1$ verschiedene Elemente enthält jedoch annehmen, wir haben das Problem für $n$ bereits gelöst?
Nun, für jede Permutation des $n$-Tupels erzeugen wir $n+1$ Permutationen des $n+1$-Tupels indem wir das hinzugekommene $n+1$-te Elemente zwischen jede zwei Elemente (und an den Anfang und das Ende eines Tupels) stecken.

Haben wir zum Beispiel das Tupel $(1,2)$ ergibt das die Permutationen $(1,2), (2,1)$.
Wollen wir nun die Permutationen von $(1,2,3)$ erzeugen ergibt dies: $(3,1,2), (1,3,2), (1,2,3)$ und zusätzlich $(3, 2, 1), (2, 3, 1), (2, 1, 3)$.

```{code-cell} python3

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
```

Ist das die beste, effizienteste bzw. einzige Lösung?
Sicher nicht!
Darum geht es vorerst auch nicht.

Das schöne an *Induktionsbeweisen* ist, dass Sie konstruktiv sind, d. h., der Beweis offenbart uns einen Algorithmus, welcher zur Lösung führt!

```{exercise} Teilbarkeit
:label: induction-division-exercise

Zeigen Sie durch vollständige Induktion, dass für jede natürliche Zahl $n$, die Zahl $n^2 + n$ gerade ist, d.h. durch 2 teilbar ist.
```

```{solution} induction-division-exercise
:label: induction-division-solution
:class: dropdown

**(1) Induktionsanfang:** $n_0 = 1$ und es gilt offensichtlich

$$2 \ | \ (1^2 + 1) \iff 2 \ | \ 2.$$

Damit gilt $A(n_0)$.

**(2) Induktionsschritt:** Angenommen es gilt $A(n)$ also

$$2 \ | \ (n^2 + n).$$

Wir berechnen nun $(n+1)^2 + (n+1)$ und versuchen $n^2 + n$ herauszuklammern:

$$(n+1)^2 + (n+1) = (n^2 + 2n + 1) + (n+1) = (n^2 + n) + (2n + 2)$$

wobei wir wegen der Induktionsannahme annehmen können, dass

$$2 \ | \ (n^2 + n).$$

Der andere Teil der Summe, also $(2n + 2) = 2 \cdot (n+1)$ ist eine gerade Zahl und damit ebenfalls durch 2 teilbar.
Da somit auch die Summe der beiden Terme durch 2 teilbar ist, folgt

$$2 \ | \ [(n+1)^2 + (n+1)].$$

Aus **(1)** und **(2)** folgt die Aussage.
```
