# Symbole, Schrift und Zahlen

Ohne *Zeichen* gibt es keine Algorithmen.
Ein (abstraktes) Zeichen steht für etwas anderes und stellt oftmals eine Gleichheit von ungleichen Dingen oder Prozessen her.
Zum Beispiel repräsentiert die Folge von Zeichen 'Stuhl' viele verschiedene Dinge auf denen man gewöhnlich sitzen kann.
Eine solche Folge von Zeichen bezeichnen wir als *Wort*.
Das Wort 'Stuhl' verweist auf einen *Begriff*, der von der jeweils gesprochenen Sprache unabhängig ist.
So verweisen die Wörter 'Stuhl' und 'chair' auf den gleichen Begriff unserer mentalen Vorstellung.
Wir gehen im Kapitel [Was ist Information?](sec-information) genauer auf diesen Zusammenhang ein.
Wichtig an dieser Stelle ist, dass wir Symbole in Form von Zeichen benötigen um Algorithmen kulturell weiterzugeben.
Dabei mag die Bedeutung der Zeichen oder Wörter frei bestimmt worden sein.

Die Entwicklung der Schrift begann mit dem sog. *Logogrammen*---eine Art Schriftzeichensystem, welches die Bedeutung der einzelnen Sprachausdrücke durch grafische Zeichen bestimmt.
Logogramme können dabei 

1. Bildsymbole: Bilder die dem ähneln was sie bezeichnen oder 
2. Begriffszeichen: Bilder die Ideen repräsentieren und als Bedeutungsträger dienen, oder 
3. Lautzeichen (Spechsilben) sein.
   
Das besondere ist, dass ein Logogramm einen Begriff darstellt und, im Gegensatz zu Bilderschriften, in der Regel aus mehreren logographischen Zeichen besteht.
Auf Grundlage der Phonetisierung, d.h. der Entwicklung einer *Lautschrift*, entwickelte sich im nächsten Schritt häufig eine Art *Silbenschrift*---Zeichen werden vertont.
Die *Lautschrift* kann zur Grundlage für die Entwicklung eines *Alphabets* eines Schreibsystems werden.
Allerdings muss dies nicht so sein.
Beispielsweise besteht das chinesische Schreibsystem aus Logogrammen.
Der Übergang von *Silbenschrift* zum *alphabetischen Schreibsystem* geschah lediglich für Sprachen, die wegen ihrer Struktur, in ihre Basiskomponente zerlegt werden konnten.

Das erste uns bekannte voll entwickelte Schreibsystem wurde 3000 Jahre v. Chr. in Mesopotanien und Ägypten entwickelt.
Diese Schreibsysteme basierten ursprünglich auf bildhaften Repräsentationen, welche später weiterentwickelt wurden, um einen höheren Grad an Abstraktion zu ermöglichen.
Die umständlichen Hieroglyphen wurden standardisiert und zur hieratische Schrift (3200 v. Chr. bis 394 n. Chr) hin vereinfacht.
Durch weitere Abstraktionen wurde die demotische Schrift abgeleitet (650 v. Chr. bis 450 n. Chr.).

Durch diese Entwicklung wurde ein essenzieller Schritt der Abstraktion hin zum Computational Thinking geschaffen.
Die Menschen konnten dadurch Objekte durch ein Zeichen oder eine Zeichenfolge [repräsentieren](sec-representation).
Dadurch wurde es möglich abstrakte Operationen auf Objekten durchzuführen ohne diese dabei zu verwenden!
Die Operationen müssen nicht länger auf den Objekten selbst durchgeführt werden.

Eine solche Operationen ist das Zählen von Objekten.
Ein Zeichen, die wir Zahl nennen, repräsentiert dabei die Erscheinung von einem oder mehreren Objekten.
Ein Zahlensystem legt fest, wie eine Zahl dargestellt wird, insbesondere wenn ihr Wert nicht unmittelbar überschaubar ist wie bei der Anzahl von Punkten auf einem Spielwürfel.
In der Geschichte der Entwicklung von Zahlensystemen gab es mehr oder weniger nützliche Systeme.
Solche durch die man mit Regeln der Symbolmanipulation berechnungen realisierten konnte und welche für die das nicht möglich war.

Es ist ungeklärt zu welcher Zeit genau die Menschen mit dem Zählen begannen.
Es wird vermutet, dass 35 000 Jahre v. Chr. die ersten Gravierungen auf Knochenstücken darauf hindeuten, dass die Menschen begonnen haben durch Markierungen bewusst zu zählen bzw. dieses Zählen schriftlich festzuhalten.

Für ein gutes Zahlensystem bedarf es weiterer Abstraktion, sodass Zahlensymbole auf einer Basis beruhen.
Es wurden häufig Systeme gefunden die auf einer Basis von 5, 10 oder 20 basieren, was darauf zurückzuführen ist, dass wir 5 Finger an einer und ingesamt 10 Finger an beiden Händen bzw. Zehen haben.
Heute hat sich das Dezimalsystem weitestgehend durchgesetzt allerdings gibt es in manchen Sprachen noch Überbleibsel von anderer Basen.
Beispielsweise finden wir in der französischen und dänischen Sprache Reste eines Systems mit der Basis von 20.

Beim Vergleich der historisch entwickelten Zahlensysteme können wir zwei Gemeinsamkeiten der Systematisierung feststellen:
Entweder werden Zahlensymbole für unterschiedliche Werte kummulativ zu einer Einheit zusammengefügt (*Additionssystem*) oder der Wert der Symbole wird durch Positionierung bestimmt (*Stellenwertsystem*).
Ein einfaches Beispiel für ein Additionssystem ist die Ihnen wohl bekannte Strichliste.
Dabei handelt es sich um ein Unärsystem, da es lediglich eine Ziffer gibt.
Diese eine Ziffer wird wiederholt notiert und der Wert ergibt sich als Summe aller notierten Ziffern.
Ein weiteres bekanntes Beispiel ist das römische Zahlensystem.
Das Addieren fällt in diesen Systemen leicht, allerdings sind andere Berechnungen oft unsystematisch.

Das erste uns bekannte in sich abgeschlossene Zahlensystem ist das der Sumerer, welches ca. 3000 v. Chr. entstand.
Es handelt sich jedoch um ein *Additionssystem*, was im weiteren Verlauf in der babylonischen Mathematik ab ca. 2000 v. Chr. zum *Stellenwertsystem* transformiert wurde.
Dieses gründet sich auf einer Basis von 60, daher der name *Sexagesimalsystem* oder *Sechziger-System*.
Es wird heute noch verwendet, um Winkel und geografische Längen und Breiten anzugeben.
In der babylonischen Verwendung gibt es lediglich zwei Zeichen.
Eines für die eins und eines für die zehn.
Bis 60 wird mit diesen beiden Zahlen additiv gezählt.
D.h. die 59 ergibt sich aus fünf mal dem Zeichen für die zehn und neun mal das Zeichen für die eins.
62 benötigt hingegen nur drei positionierte Zeichen.
Eine eins an der forderen Stelle, die für die 60 steht, und zwei einsen an der hinteren Stelle, die die 2 repräsentiert.

Eine weitere interessante Zahlennotation erfand die südamerikanische Bevölkerung des Inkareichs.
Diese Notation ist unter dem Namen *Khipu* oder *Quipu* bekannt.
Der Name Khipu (spanisch: Quipu, quechua: Khipu) bedeutet Knoten und steht sowohl für den einzelnen Knoten, als auch für das gesamte Gebilde aus Knotenschnüren.
Mit dieser *Knotenschrift* lassen sich komplexe Informationen kodieren.
Die Inkas stellten damit mehrstellige Zahlen im Dezimalsystem dar.
Nach heutiger Erkenntnis gab es zwei verschiedene Schriftsysteme: eines zur Erfassung von Mengen von Lagerbeständen, Menschen, Tieren, Pflanzen und Ländereien, und eines für Nachrichtenverkehr, wie Briefwechseln.

```{figure} ../../figs/history/quipu.png
---
height: 150px
name: fig-quipu
---
Beispiel eines Khipu.
```

Das ägyptische Zahlensystem entstand im alten Imperium um ca. 2700-2200 v. Chr.
Dieses hieroglyphische Zahlensystem ist ein dezimales *Additionssystem*.
Eine aufgeschriebene Zahl beginnt von rechts nach links mit dem kleinsten Symbol und die Symbole werden nach links hin immer größer.
Es scheint fast so als würde die Position der Symbole eine Rolle spielen, jedoch ist der Wert der repräsentierten Zahl gleich der Summe aller Werte der einzelnen Symbole.
Somit spielt die Position eigentlich gar keine Rolle.

Das Zahlensystem welches wir heute verwenden, das sog. hindu-arabische oder indo-arabische System, ist ein *Stellenwertsystem*.
Es ist das bekannteste und am weitverbreitetste Zahlensystem.
Es wurde ca. 100-400 n. Chr. in Indien entwickelt.
Vermutlich geht es ursprünglich auf die chinesischen Zahlenzeichen (1200 v. Chr.) zurück.
Das chinesische System ist eine Mischung aus Additions- und Stellenwertsystem und basiert ebenfalls auf Dezimalzahlen.
Häufig sprechen wir vom arabischen oder persischen Zahlensystem, da es in Europa von arabischen Kaufleuten herangetragen wurde.
Die Basiselemente dieses Stellenwertsystems sind bekanntlich neun unterschiedliche Zeichen 1, 2, 3, 4, 5, 6, 7, 8 und 9.
Und was ist mit der Zahl 0?

Die Geschichte der Zahl Null ist faszinierend und umspannt verschiedene Kulturen und Zeitalter.
Der Konzept der Null hat seinen Ursprung in verschiedenen alten Zivilisationen, einschließlich der Babylonier und der Maya, aber die Form der Null, wie wir sie heute kennen, hat ihren Ursprung in Indien.
Wahrscheinlich war es die Expansion von Alexamder dem Großen, welche das babylonische System nach Indien brachte.
Zu jener Zeit verwendeten die Inder ein Zahlensystem, welches dem des griechischen Systems glich.
Daraufhin wurde das babylonische System in Indien weiterentwickelt.
Als einer der größen Errungenschaften brachten die indische Mathematiker die Zahl 0 in das System ein.
Um 820 n. Chr. überlieferten die Inder durch al-Khwarizmi das System---welches nun mit der 0 ausgestattet war---in die islamische Kultur.
Vielleicht war diese kulturelle und zeitliche Reise für die Entwicklung der 0 notwendig, da die indische Philosophie einen anderen Bezug zum Nichts hatte und noch immer hat.
Die westliche Philosophie, welche stark von den Pythagoreern geprägt war, hatte große Probleme das Konzept des Nichts anzuerkennen.
Der scholastische Mönch Gerbert von Aurillac machte sich um 950 n. Chr. mit dem arabischen Zahlensystem vertraut und versuchte das Konzept der Zahl 0 einzuführen.
Dabei Stoß er allerdings auf großen Widerstand, da nach der Lehre von Pythagoras es eine Gleichheit zwischen Zahlen und Formen gibt.
Welche Form würde der Null gleichen?
Ein Würfel mit der Seitenlänge 0 verliert seine Form.
Die Null einer Form gleichzusetzen schien unmöglich und deshalb schien die Null selbst unsinnig.
Für das Denken von Pythagoras und seinen Anhänger:innen stellte die Zahl 0 eine Gefahr dar---sie könnte jenes Denken erschüttern und als unzureichend entlarven.
Schlussendlich scheiterte Gerberts mit seinem Versuch.

Schlussendlich war das Konzept der Null aber nicht aufzuhalten.
Das Wissen um die Null und das arabische Zahlensystem breitete sich durch arabische Handelsrouten und Wissenszentren wie die Bibliothek von Cordoba in Spanien aus. 
Im Hochmittelalter wurden diese arabischen Texte ins Lateinische übersetzt, was den europäischen Mathematikern und Wissenschaftlern Zugang zu diesem Wissen ermöglichte.
In Italien sollte sich die Zahl aus praktischen Gründen durchsetzen.
Leonardo von Pisa (1170 - 1240 n. Chr.), welcher heute auch unter dem Namen Fibonacci bekannt ist, war der Sohn eines Händlers der regen Konktakt zu anderen Händlern aus den arabischen Gebieten hatte.
Leonardo erkannte die praktischen Vorteile des arabischen Zahlensystems und so wurde er zum Verfechter des neuen Systems.
Ein Schlüsselmoment in der Geschichte der Null in Europa war Leonardo's Veröffentlichung von *Liber Abaci* im Jahr 1202.
Fibonacci stellte das dezimale Zahlensystem vor und erklärte dessen Vorteile gegenüber dem römischen Zahlensystem, das keine Null hatte. 
Die Verwendung der Null in Rechenoperationen, in der Buchhaltung und schließlich in der Wissenschaft setzte sich im Laufe der nächsten Jahrhunderte allmählich durch.

Es ist erstaunlich wie lange es gedauert hat bis sich dieses fruchtbare Konzept gegen alte Vorstellungen durchsetzen konnte zumal die Schule von Pythagoras schon viel früher kritisiert wurden.
Ein Beispiel sind die Atomisten, die an einen leeren Raum zwischen den Atomen glaubten oder der griechische Philosoph Zenon von Elea, der durch das Paradoxon [von Achilles und der Schildkröte](https://de.wikipedia.org/wiki/Achilles_und_die_Schildkr%C3%B6te) ein Problem aufstellte, welches durch einen gegen 0 immer kleiner werdenden Abstand lösbar aufgelöst werden kann.
Doch die Philosophie des Aristoteles (384-322 v. Chr.), welcher die Sichtweise der Pythagoreer übernahm, sollte etwa 2000 Jahre das abendländische Denken bestimmen.
Die Null war eben nicht nur in der Mathematik von Bedeutung. 
Sie hatte philosophische und theologische Implikationen.
Deshalb gab es im christlichen Europa anfangs einige Widerstände gegen die Null, da sie als ein Symbol für das Nichts angesehen wurde, das im Gegensatz zum christlichen Schöpfungsglauben stand.
Schlussendlich waren die praktischen Vorteile der Null und des dezimalen Systems so groß, dass sie sich schließlich durchsetzten konnten.

Wir können festhalten, dass die Entwicklung der Symbole, Sprachen und Zahlensysteme eine weltliche Geschichte ist.
Der Austausch zwischen verschiedenen Kulturen war und ist von entscheidender Bedeutung.
Ein anderer Blick auf ein bestehendes Konzept führte zu Neuerungen, die den Erfinder:innen oder Entdecker:innen des Konzepts nicht möglich gewesen ist.