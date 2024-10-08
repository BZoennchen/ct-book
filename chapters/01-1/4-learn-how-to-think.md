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

# Denken lernen?

>I think everybody should learn how to program a computer, because it teaches you how to think. So I view computer science as a liberal art. It should be something everybode learns. -- Steve Jobs

Es mag für Sie ein wenig vermessen klingen, dass Sie in diesem Kurs das "richtige" Denken lernen sollen.
Sollten Sie das nicht bereits beherrschen?
Wären Sie andernfalls überhaupt im Studium gelandet?

Computational Thinking ist eine Form des Denkens, die anderen Formen weder überlegen noch unterlegen ist.
In vielen Bereichen des Lebens ist es von Vorteil wenn die Bedeutung einer Arbeit unklar bleibt.
Literarische Meisterwerke sind beispielweise oftmals genau deshalb so meisterlich, da sie eine Vielzahl an Interpretationen zulassen.
Oder denken Sie an unsere naturliche Sprache, die ungenau und oft mehrdeutig ist aber dadurch eine Flexibilität aufweist, die viele Perspektiven und Interpretationen zulässt.

Wie wir sehen werden verhält es sich beim Computational Thinking anders.
Wir wagen in die Welt der formalen Sprachen, welche keine Missverständnisse und Mehrdeutigkeiten zulassen.

## Schnelles und langsames Denken

In seinem Buch *Schnelles Denken, Langsames Denken* {cite:p}`kahneman:2011` beschreibt der Nobelpreisträger und einflussreiche Wissenschaftler unserer Zeit Daniel Kahneman sehr eindringlich, wie wir Menschen Entscheidungen treffen.
Er betont dabei, dass Zögern ein überlebensnotwendiger Reflex ist und beschreibt was in unserem Gehirn vor sich geht, wenn wir andere Menschen oder Dinge beurteilen. 
Vereinfacht ausgedrückt wird das menschliche Denken durch zwei kognitive Systeme bestimmt:
Durch das *(1) schnelle Denken* und durch das *(2) langsame Denken*.
Blicken Sie auf folgende Aufgabe:

```{exercise} Blinzeln des Alphabets
:label: fast-and-slow-thinking-exercise
Ein Schläger und ein Ball kosten zusammen 1.10 Euro.
Der Schläger kostet einen Euro mehr als der Ball.
Wie viel kostet der Ball?
```

```{code-cell} python3
---
tags: 
    - remove-input
---
quiz=[{
    "question": "Nennen Sie Ihre Antwort:",
    "type": "numeric",
    "precision": 2,
    "answers": [
        {
            "type": "value",
            "value": 0.05,
            "correct": True,
            "feedback": "Richtig."
        }
    ]
}]

from jupyterquiz import display_quiz
display_quiz(quiz, border_radius=2)
```


Intuitiv, d.h., durch das *schnelle Denken* beantworten die meisten Menschen diese Frage mit: Der Ball kostet 10 Cent.
Diese Antwort ist jedoch falsch!
Nehmen wir uns einen Augenblick Zeit und aktivieren unser *langsames Denken*.
Sagen wir der Preis des Balls sei $b$ und der Preis des Schlägers $s$.
Dann erkennen wir, dass 

$$b + s = 1.10 \text{ und } s = b + 1.0$$

gilt.
Wir lösen beide Gleichungen nach $b$ auf und erhalten:

$$b = s - 1 \land b = 1.10 - s \Rightarrow s-1 = 1.10-s \Rightarrow 2s = 2.10 \Rightarrow s = 1.05$$

und demnach gilt $b = s - 1= 1.05-1 = 0.05$ also 5 Cent.
Das falsche Ergebnis entstammt dem *schnellen* und das richtige dem *langsamen Denken*!

Wenn Sie etwas intuitiv, quasi aus dem Bauch heraus und mühelos abschätzten oder unbewusst einfach tun, dann ist das *schnelle Denken* aktiv.
Nehmen wir das Autofahren.
Wenn Sie geübt darin sind, werden Sie ohne darüber nachzudenken "einfach fahren".
Sie werden allein durch den Ton den das Auto macht und wie die Straße schimmert wissen was zu tun ist.
Wenn Sie einen Ball fangen wollen, dann werden Sie keine komplizierte Berechnung durchführen, sondern eine fast schon automatische Abschätzung vornehmen.
Tischtennisspieler\*innen können den Ball, der sich in einer unglaublichen Geschwindigkeit über den Tisch bewegt, scheinbar mühelos verfolgen und treffen.
Wie ist das möglich?

In all diesen Beispielen haben wir in früherer Zeit mit dem *langsamen Denken* begonnen.
In der Fahrschule mussten wir noch über den genauen Ablauf beim Autofahren nachdenken.
Tischtennisspieler\*innen benötigen tausende von Stunden Training, um derartige Leistungen zu erzielen.
Durch das *langsame Denken* schaffen wir es Stück für Stück, entsprechende Fähigkeit ins *schnelle Denken* zu transformieren.
Das allerdings kostet Zeit und Anstrengung, besonders zu Beginn.
Können wir irgendwann das *schnelle Denken* nutzen vergessen wir häufig wie schwer es zu Beginn gewesen ist und wundern uns über Anfänger\*innen, welche sich noch in der Phase des *langsamen Denkens* befinden.
Oftmals fällt es uns als Expert\*innen schwer zu erklären was wir genau machen, also warum wir z.B. beim Autofahren eine bestimmte Entscheidung treffen.
Wir sehen die Lösung oder was zu tun ist einfach vor uns.

Als geübte und erfolgreiche Programmierer\*innen können wir auf viele Techniken, Konzepte, die Form und Bedeutung von Anweisungen, die Struktur des Programmiercodes, oder auch Codemuster im Modus des *schnellen Denkens* zugreifen.
So können wir unser gesamtes *langsames Denken* auf das eigentlich zu lösende Problem loslassen.

Jedoch geht es nicht nur darum, dass *schnelle Denken* zu nutzen, sondern es zu kontrollieren und es uns bewusst zu machen.
Man spricht dabei von der sog. *Metakognition*.
Viele kognitive Verzerrungen (Bias) sind auf das *schnelle Denken* zurückzuführen.
Zum Beispiel neigen wir aufgrund des sog. Bestätigungseffekt (engl. confirmation bias) dazu Informationen auszuwählen und aufzunehmen, die unserer vorher gebildeten Meinung entsprechen.
Wir deuten Informationen, sodass sie die eigenen Erwartungen bestätigen.

```{exercise} Blinzeln des Alphabets
:label: confirmation-bias-exercise
Sie überholen den dritten. Welchen Platz haben Sie dann?
```

Vorschnell ist die Antwort: Den zweiten Platz!
Dies suggeriert der Überholvorgang.
Wir können unsere Verzerrungen, die durch das *schnelle Denken* entstehen, nicht verhindern.
Doch können wir immer wieder innehalten und unser *langsames Denken* aktivieren und nachprüfen ob unsere Intuition korrekt ist.

## Durch Fehler lernen

Kreativ-logisches Denken ist, wie so vieles im Leben, keine binäre Fähigkeit, die entweder vorhanden ist oder nicht.
Ein gewisses Talent ist hilfreich aber um richtig gut darin zu werden braucht es Übung---die Denkmuskel müssen gefüttert werden.
Vergleichbar mit den abgespeicherten Bewegungsabläufen im Leistungssport, welche Sie problemlos automatisch abrufen können, erlernen wir im Denksport Muster, welche Sie problemlos erkennen.
Schachspieler blicken auf einen Spielstand analysieren Muster (Positionen von mehreren Figuren als Ganzes), durch die sie auf neue Spielzüge schließen.
Das Lesen von mathematischen Ausdrücken wird Ihnen immer leichter Fallen je mehr Ausdrücke Sie lesen.
Das liegt nicht nur daran, dass Sie besser in Mathe werden, sondern dass Sie die Symbole wie Ihre Muttersprache schneller und besser als Muster erkennen.
Programmcode werden Sie immer schneller und besser verstehen, je mehr Programmcode Sie zu verstehen versuchen.
Um diese Erfolge zu feiern bedarf es der täglichen Übung des Programmierens und der Konfrontation mit immer komplexeren Problemen.

Denken ist zudem ein lebenslanger Prozess mit einem Rückkopplungseffekt.
Unsere Gedanken der Vergangenheit formen unsere Gedanken der Zukunft.
In der Biologie spricht man dabei von Autopoesie {cite}`maturana:1987`, d.h. von der Selbsterschaffung und Selbsterhaltung eines Systems, in diesem Fall unseres Geistes.
Es ist deshalb ratsam sich hin und wieder Gedanken über seine Gedanken zu machen.
Diese rekursive Eigenschaft der Selbstbeobachtung ist uns Menschen zum Glück möglich, wir können uns sogar dabei beobachten wie wir uns beobachten und so weiter und so fort.

Klare Gedanken zu fassen und sich präzise auszudrücken ist nicht nur nützlich, sondern birgt auch einen intrinsischen Wert.
Es schult Ihre Fähigkeit Sachverhalte schnell aufzunehmen, schärft Ihren Verstand und wirkt sich nach unserer Ansicht auch auf das kritische Denken aus.
Zum Beispiel fällt es Ihnen möglicherweise bei einem Gespräch leichter feststellen, ob eine Argumentation logische Fehler enthält.

Außerdem wage ich zu behaupten, dass Sie durch [Computational Thinking](sec-what-is-ct) in eine Welt eintauchen können in der Sie das Ruder übernehmen.
Es ist eine sehr reine Welt die, anders als unsere oft verschwommene Realität, noch klare Wahrheiten und Strukturen bietet und zugleich eine Spielwiese für kreatives Schaffen darstellt.
Sie werden im Laufe des Kurses feststellen, dass es viele neue interessante Konzepte und Objekte zu entdecken gibt.