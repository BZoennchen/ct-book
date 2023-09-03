(sec-information-natural-sciences)=
# Naturwissenschaften

Beginnen wir mit der naturwissenschaftlichen Perspektive.
Wir konzentieren uns auf die Informatik und Physik.
In beiden Disziplinen wird Information über die sog. *Entropie* definiert, welche gewöhnlich mit dem Grad der Unordnung, Zufälligkeit oder Unsicherheit assoziiert wird.

> Information is the resolution of uncertainty. -- Claude E. Shannon

Sie kommen gerade Abends in der Winterzeit nach Hause und machen sich einen schönen warmen Tee.
Ihre Hände sind kalt und Sie halten die warme Teetasse in den Händen.
Wir können Ihre Hände und die Tasse als physikalisch abgeschlossenes System annehmen.
Nun ist für uns absolut verständlich, dass sich Ihre Hände erwärmen.
Das hat jedoch nichts mit der Energieerhaltung des Systems zu tun.
Es wäre nach dem Energieerhaltungssatz durchaus möglich, dass Ihre Hände wärme der Tasse zuführen, obwohl die Tasse deutlich wärmer ist.
Es wäre theoretisch sogar möglich, dass ein Ei, was Ihnen auf dem Boden zersprungen ist, wieder zu Ihnen zurückspringt.

Beide eben beschriebenen Prozesse nennen Physiker *irreversibel*.
Damit ist gemeint, dass solche Prozesse durch kleine Änderungen in der Umgebung nicht rückgängig gemacht werden können.
Wir würden vermutlich an unserem Verstand zweifeln, sollte so etwas passieren.
Warum dies nicht geschieht und weshalb sich Ihre Hände erwärmen, liegt an der *Entropie* bzw. an der *Entropieänderung*.

```{admonition} Irreversible Prozesse
:class: remark
:name: remark-irreversible-process

Findet in einem abgeschlossenen System ein *irreversibler Prozess* statt (einer der sich nicht umkehren lässt), so nimmt die *Entropie* dieses Systems immer zu. Sie nimmt niemals ab!
```

Blicken wir auf ein weiteres Beispiel.
Nehmen wir an, wir haben zwei gleiche isolierte Behälter die durch einen Kanal verbunden sind.
Das eine Behältnis enthält ein Gas.
Das andere ist im Vakuum.
Die Behältnisse sind durch eine Verriegelung voneinander abgeschlossen.
Nun öffnen wir die Verriegelung.
Was wird geschehen?
Intuitiv werden Sie richtigerweise annehmen, dass das Gas sich in beiden Behältnissen gleich verteilt.
Wir können uns das Gas als eine Menge vieler gleicher winziger Teilchen vorstellen, welche sich in beiden Behältnissen gleich verteilen.
Auch in diesem Fall nimmt die Entropie zu, denn der Vorgang ist irreversibel.

```{figure} ../../figs/information/gas-entropie.png
---
width: 600px
name: fig-gas-entropie
---
Links die der Zustand vor dem öffnen der Verriegelung, rechts der Zustand nachdem sich das Gas ausgebreitet hat. Die Entropie des Systems nimmt zu.
```

Was beschreibt nun die Entropie genau?
Nun in dem eben beschriebenen Beispiel betrachten wir das System einmal vor und einmal nach dem lösen der Verriegelung.
Die gleiche Anzahl an Teilchen ist einmal auf weniger und einmal auf mehr Raum verteilt.
Für den Zustand des Systems gibt es deshalb einmal weniger und einmal mehr Möglichkeiten der Verteilung der Teilchen.
Die Anzahl dieser Möglichkeiten ist die *Entropie*.

Lassen wir einmal die Physik kurz außer acht und denken mathematisch an einen Zufallsprozess (z.B. einen Münzwurf).
Wir haben eine Menge an Zuständen, die das System annehmen kann.
Im Fall unsere Teetasse wäre dies beispielsweise eine noch mehr abgekühlte Hand oder eine wärmere Hand.
Jeder (Makro-)Zustand hat eine bestimmte Anzahl an unterschiedlichen Teilchenanordnungen bzw. Energieverteilungen (Mikrozuständen).
Besitzt jeder Mikrozustand die gleiche Wahrscheinlichkeit, so steigt die Wahrscheinlichkeit eines Makrozustands mit der Anzahl seiner möglichen Mikrozustände.
Und da das Ei, welches Ihnen entgegen springt, derart wenige Mikrozustände hat, tritt dieser Zustand niemals ein.

```{admonition} Entropie (Physik)
:class: definition
:name: def-entropy-physics
Die Entropie beschreibt die Anzahl der Teilchenanordnungen (Mikrozustände), die zu einem gegebenen (Makro)-Zustand des Systems führen.
```

Theoretisch ist es also möglich, dass sich warme Objekte weiter erwärmen.
Da solche Objekte allerdings aus derart vielen Teilchen bestehen, die alle eine bestimmte Energiekonfiguration besitzen, ist es statistisch gesehen derart *unwahrscheinlich*, sodass dies in der Realität niemals passiert.
Es gibt keine unsichtbare Kraft die ein solches System zur hohen Entropie drückt.

Nun gut, wir wissen was Entropie ist.
Wie aber definieren Physiker die *Information*?
Ist die Entropie groß, so bedarf es viel Information, um auf die korrekte (mikroskopische) Teilchenanordnung zu schließen.
Es besteht eine hohe *Unsicherheit* in welchem mikroskopischen Zustand sich das System befindet.
Information, die diese Unsicherheit auflöst, hat demnach einen hohen *Informationsgehalt*.

```{admonition} Information (Physik)
:class: definition
:name: def-information-physics
Die *Information* ist jenes etwas, durch das ein Beobachter auf die exakte mikroskopische Teilchenanordnungen eines Systems schließen kann.
```

Da bei irreversiblen Prozessen die Entropie *mit der Zeit* stets zunimmt, bezeichnen Physiker die Entropieänderung auch als den *Pfeil der Zeit*.