# Programmieren

Programmieren ist eine Tätigkeit bei der wir unsere Ideen und Konzepte, d.h. das was wir beim [Computational Thinking](sec-what-is-ct) mental zustande bekommen haben, in Text überzuführen.
Ob das Programmieren nun wirklich mit dem Schreiben des Codes beginnt oder wir den ganzen Prozess der Softwareentwicklung als das Programmieren betrachten sei dahingestellt.
Auch ist klar, dass geschriebener Code wie auch die Betrachtung von Code neue Ideen hervorrufen wird und zu neuen Lösungen führen wird.

Als gute Programmierer\*innen müssen wir 

+ unseren Kontext kennen.
+ logisch und mathematisch Denken können.
+ uns exakt ausdrücken können und uns auch unmissverständlich mit anderen austauschen können.
+ unsere Entwicklungswerkzeuge beherrschen können.
  
Wir benötigen ein Grundverständnis davon wie ein [Computer funktioniert](sec-information-processing) und wie wir uns in der abstrakten Welt der [Kontrollstrukturen](sec-control-structures) und [Datenstrukturen](sec-data-structures) ausdrücken können.

## Begrifflichkeiten

Die Begriffe *Algorithmus*, *Pseudocode*, *Programmcode* und *Programm* ähneln sich sehr und wir haben noch keine strickte Differenzierung durchgenommen.
Im Abschnitt [Algorithmen](sec-algorithms) ist klar definiert, was genau ein Algorithmus ist.

```{admonition} Pseudocode
:name: def-pseudocode
:class: definition

*Pseudocode* ist eine einfache, weniger strikte Beschreibung eines Algorithmus in einer der natürlichen Sprache ähnlicheren Art.
```

Mit *Pseudocode* können wir einen Algorithmus in einer Sprache beschreiben, die keine bestimmte Programmiersprache zur Basis hat.

```{admonition} Programm
:name: def-program
:class: definition

Ein *Programm* ist eine Folge von Instruktionen, die ein konkreter Computer (über die Umwege eines [Übersetzers](def-compiler) oder [Interpreters](def-interpreter)) ausführen kann.
```

Ein *Algorithmus* ist eine wohldefinierte Sequenz von Anweisungen, welche eine Lösung für ein bestimmtes Problem berechnen.
Er kann in der Form von *Pseudocode* niedergeschrieben werden, sofern die Beschreibung alle Eigenschaften für einen Algorithmus erfüllt.
Er kann aber auch in einer ganz anderen Form niedergeschrieben werden, z.B., einem Flussdiagramm.

*Pseudocode* orientiert sich an der Syntax von Programmiersprachen, wird aber sprachenübergreifend verwendet.

Ein *Programm* ist im Gegensatz dazu in einer Programmiersprache wie ``Python`` geschrieben und kann auf einer Maschine ausgeführt werden.
*Programmiercode* auch genannt *Quellcode*, *Source Code* oder kurz *Code*, ist das Resultat der *Programmierung* und teil eines *Programms*.
Das heißt zur Ausführung des *Quellcodes* fehlt möglicherweise ein Teil des gesamten Codes.

*Pseudocode*, *Quellcode* *Programme* und *Algorithmen* sind Manifestation des [Computational Thinkings](sec-what-is-ct) in Form von endlichem Text.

Ein *Algorithmus* kann auch in einer Programmiersprache niedergeschrieben werden.
Dies werden wir in diesem Kurs bevorzugen und den Umweg über *Pseudocode* weitestgehend vermeiden.

```{admonition} Von anderen Entwickler\*innen lernen
:class: remark
Um neue Denkmuster anderer Denker\*innen zu erlernen oder sich von ihnen inspirieren zu lassen, lohnt es sich den Programmiercode anderer Entwickler\*innen zu analysieren.
```

## Kenne deinen Kontext

Das Entwerfen eines Algorithmus und das Programmieren gehen fließend ineinander über.
Oftmals, gerade bei einfachen Problemen, entwerfen Sie ihren Algorithmus indem Sie ihre Gedanken in Programmiercode umwandeln.
Bei komplexeren Problemen ist es jedoch oft ratsam zu Stift und Papier zu greifen und Ihr [Computational Thinking](sec-what-is-ct) durch Skizzen und Mitschriften zu unterstützen.

Nehmen wir unser Beispiel des [Kartensortierens](sec-sorting).
Hierbei kann es Sinn machen erst darüber nachzudenken wie das Sortieren auf einer abstrakten Ebene durchgeführt werden soll.
Sie möchten vielleicht zuerst darüber nachdenken, welche Karte Sie auf der Hand wo hinbewegen, bevor Sie sich darüber Gedanken machen wie Sie Ihren Algorithmus in ``Python`` realisieren.
Natürlich kann es auch sinnvoll sein Ihre Idee zu realisieren und dann zu testen, denn möglicherweise sind Sie sich nicht sicher ob Ihr Algorithmus korrekt definiert ist.
Oft werden Sie zwischen Code und Stift und Papier wechseln.

Ein wesentliche Teil des Computational Thinkings findet vor dem Programmieren statt.
Das Programmieren ist dann eine Frage der Realisierung/Modellierung.
Ist Ihr Algorithmus den Sie programmieren möchten gut durchdacht und kennen Sie Ihren *Kontext* gut genug, dann ist die Programmierung oft keine allzu große Herausforderung mehr.

## Ein kreativer Akt

Der Entwurf eines Algorithmus und dessen Programmierung sind äußerst kreative Aufgaben.
Programmieren ist eine Kunstform die durch logisch-basierte Kreativität angetrieben wird.
Wenn wir vom Programmieren sprechen, meinen wir oft beides:

1. Das Entwerfen eines Algorithmus und
2. dessen Realisierung (*Implementierung*) durch eine Programmiersprache.

Für mich persönlich bietet die Welt der Programmierung enorme Freiheiten.
Sie bietet die Möglichkeit sich seine eigene Welt zu erschaffen und seine Ideen Realität werden zu lassen.
Offensichtlich wird dies, wenn wir uns die Arbeiten von Spieleentwickler\*innen ansehen.
Wie neidisch müssen Architekten werden, wenn Sie sehen wie Entwickler\*innen bei der Kreation virtueller Welten ihrer Phantasie freien Lauf lassen können.

Weniger offensichtlich wird es bei Arbeiten die kein visuelles oder auditives Resultat hervorbringen.
Denken wir nochmals zurück an das [Kartensortieren](sec-sorting).
Wir haben einen Algorithmus entworfen und realisiert mit dem sich vergleichbare (modellierte) Objekte aller Art sortieren lassen.
Wann immer Sie in ihrer virtuellen Welt einen solchen Algorithmus benötigen, steht er Ihnen nun zur Verfügung.
Sie wissen **was** er macht und **wie** er funktioniert.
Sie können den Algorithmus sogar in der echten Welt zum Sortieren anwenden.

Das Problem Dinge zu sortieren gehört nun zu Ihrem Baukasten, zu Ihrer teils virtuellen aber auch realen Welt.
Und diesen Baukasten können Sie stetig erweitern, ob alleine oder in einer Gruppe.
Sie können Baukästen von anderen Entwickler\*innen verwenden und darauf aufbauend neue phantastische Konstrukte kreieren.

Jedesmal wenn wir programmieren, begeben wir uns auf eine Reise.
Es warten vielen Abzweigungen auf uns.
Wir wandern hin zu einer ungewissen, noch nie zuvor kreierten Lösung.
Diese Reise ist ein Stück weit eine Selbstentdeckung und ein Ausdruck unseres Intellekts.
Sie merken es an meiner Wortwahl; ich finde das ganz und gar faszinierend! 

>Computer programming is an art, because it applies accumulated knowledge to the world, because it requires skill and ingenuity, and especially because it produces objects of beauty. -- Donald Knuth