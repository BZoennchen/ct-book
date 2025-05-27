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

> You can't think about thinking without thinking about thinking about something. — Seymour Papert

Es mag zunächst vermessen klingen, dass Sie in diesem Kurs das "richtige" Denken lernen sollen.
Beherrschen Sie das nicht bereits? Wären Sie sonst überhaupt im Studium?

*Computational Thinking* ist eine spezifische Form des Denkens.  
Sie ist anderen Denkformen weder überlegen noch unterlegen.  
Vergleichen wir das *Computational Thinking* mit dem *Systems Thinking* so fällt auf, dass Computational Thinking das Ganze auf Teile reduziert, während System Thinking das Ganze in den Blick nimmt.
Auch ist es in vielen Lebensbereichen hilfreich, wenn Bedeutungen offenbleiben.  
Literarische Meisterwerke zum Beispiel leben von ihrer Interpretationsvielfalt.  
Auch unsere natürliche Sprache ist oft mehrdeutig – gerade das ermöglicht Flexibilität und Perspektivenvielfalt.

Beim *Computational Thinking* ist das anders:  
Wir bewegen uns in einer Welt **formaler Sprachen**, in der Mehrdeutigkeiten ausgeschlossen sein müssen.

## Schnelles und langsames Denken

In seinem Buch *Schnelles Denken, langsames Denken* {cite:p}`kahneman:2011` beschreibt Nobelpreisträger Daniel Kahneman, wie Menschen Entscheidungen treffen.  
Zwei Denksysteme bestimmen unser Verhalten:
1. Das **schnelle Denken**: intuitiv, automatisch, mühelos  
2. Das **langsame Denken**: bewusst, analytisch, anstrengend

Betrachten Sie folgende Aufgabe:

```{exercise} Blinzeln des Alphabets
:label: fast-and-slow-thinking-exercise
Ein Schläger und ein Ball kosten zusammen 1,10 €.  
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
display_quiz(quiz, border_radius=2, lang='de')
```

Die häufige Antwort ist: **10 Cent**. Doch das ist falsch.
Die korrekte Lösung mithilfe des langsamen Denkens lautet:


$$b + s = 1.10 \text{ und } s = b + 1.0$$

Einsetzen und umstellen ergibt:

$$b = s - 1 \land b = 1.10 - s \Rightarrow s-1 = 1.10-s \Rightarrow 2s = 2.10 \Rightarrow s = 1.05$$

und demnach gilt $b = s - 1= 1.05-1 = 0.05$ also **5 Cent**.

Intuition führt uns oft in die Irre – genau deshalb brauchen wir das bewusste, reflektierende Denken.
Das *schnelle Denken* funktioniert hervorragend bei Routineaufgaben:
Autofahren, einen Ball fangen, Tischtennis spielen.
Doch viele dieser Fähigkeiten begannen mit *langsamem Denken*, mühsamem Üben, Fehlern, Reflexion - wir können uns teilweise nur nicht mehr daran erinnern.

Mit genug Übung wandern Denkmuster vom langsamen ins schnelle Denken.
Wer Programmieren beherrscht, erkennt Code-Strukturen und Muster intuitiv – und kann sein langsames Denken auf die eigentliche Problemlösung konzentrieren.
Aber: Intuition ist fehleranfällig.
Deshalb ist *Metakognition* entscheidend – also das Nachdenken über das eigene Denken.

Viele kognitive Verzerrungen entstehen aus dem schnellen Denken.
Ein Beispiel:

```{exercise} Blinzeln des Alphabets
:label: confirmation-bias-exercise
Sie überholen den dritten. Welchen Platz haben Sie dann?
```

Die spontane Antwort lautet oft: **Zweiter Platz** – doch korrekt ist: **dritter Platz**.
Sie haben den Dritten überholt, nehmen also seinen Platz ein.

Wir können solche Denkfehler nicht vermeiden – aber wir können lernen, sie zu erkennen.
Dazu müssen wir immer wieder bewusst innehalten und unser *langsames Denken* aktivieren.

## Durch Fehler lernen

Kreativ-logisches Denken ist keine binäre Fähigkeit – man hat sie nicht einfach, man entwickelt sie.
Wie im Sport: Bewegungsmuster entstehen durch ständiges Training.
Auch im „Denksport“ lernen wir durch Wiederholung, Muster zu erkennen:

+ Schachspieler*innen sehen Stellungsmuster und ziehen daraus strategische Schlüsse.
+ Mathematische Ausdrücke werden mit der Zeit wie eine Sprache verstanden.
+ Programmcode erschließt sich immer schneller – je mehr Code Sie analysieren.

Das bedeutet: **Tägliches Üben** ist der Schlüssel.

Denken ist ein dynamischer Prozess.
Unsere heutigen Gedanken formen die Gedanken von morgen.
In der Biologie spricht man von Autopoiesis {cite}maturana:1987 – der Fähigkeit eines Systems, sich selbst zu erschaffen und zu erhalten.
Auch unser Denken hat diese Rückkopplung: Denken über das Denken.

Klare Gedanken und präzise Ausdrucksweise sind nicht nur nützlich – sie haben einen Eigenwert.
Sie fördern kritisches Denken, schärfen das Urteilsvermögen und verbessern die Kommunikationsfähigkeit.

Wir behaupten: Durch [Computational Thinking](sec-what-is-ct) betreten Sie eine Welt, in der Sie das Ruder übernehmen.
Eine Welt, in der es klare Strukturen gibt – aber zugleich kreatives Schaffen ermöglicht wird.

Sie werden sehen: Es gibt viel zu entdecken.