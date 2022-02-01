# Sprachevolution

Hat sich eine Sprache einmal etabliert, muss sie fortwährend aktiv weiterentwickelt werden.
Um erfolgreich zu bleiben, müssen neue zeitgemäße Konzepte in die Sprache eingepflegt werden und veraltete Konzepte langsam hinausfallen.

Ein Paradebeispiel ist die Programmiersprache ``Java``.
``Jave``-Entwickler\*innen sahen einige Nachteile der Sprache z.B. dass oft recht viel Text für recht wenig Logik zu schreiben ist (fehlende **Kompaktheit**).
Mit Java 8 führte man deshalb ``Lambdas`` (annonyme Funktionen) in die Syntax ein und aus

```java
Runnable runnable = new Runnable(){
       @Override
       public void run(){
         System.out.println("Hello world !");
       }
     };
```

wurde

```java
Runnable runnable = () -> System.out.println("Hello world two!");
```

Java 9 brachte dann das sogenannte ``Type-Inference`` (die automatische Typ-Erkennung).
Dadurch wird der Datentyp einer Variable aus dem Kontext bestimmt und die Programmierer\*innen müssen diesen nicht explizit angeben.
Aus

```java
String name = "Julia";
int age = 23;
```

wurde

```java
var name = "Julia";
var age = 23;
```

Mit Java 14 kamen dann die ``records`` in die Sprache und aus

```java
final class Point {
    public final int x;
    public final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

wurde 

```java
record Point(int x, int y) { }
```

All diese Konzepte sind aus anderen Sprachen (vor allem funktionalen Sprachen) motiviert.
Sie erweitern die [Syntax](def-syntax), d.h., die alte Schreibweise ist immer noch gültig und die Sprache wurde, bezogen auf die angeführten Beispiele, nicht um Funktionalität erweitert, sondern um neue syntaktische Mittel.
Durch die kürzere Schreibweise müssen Programmierer\*innen wissen was dahinter steckt ([Semantik](def-semantik)).
Es werden also bewerte und sich wiederholende **Muster** vereinfacht.

Neue Hardwareanforderungen übertragen sich auch auf Programmiersprachen.
Wie Sie vielleicht beobachtet haben, hat sich die Taktrate der Prozessoren in den letzten Jahren nicht mehr verbessert.
Wir sind an eine Grenze gestoßen.
Deshalb gibt es statt schnellerer Prozessoren mehr Prozessoren.

Um dies zu nutzen müssen wir mit Parallelität umgehen, doch ist die Entwicklung paralleler Algorithmen schwierig.
Auch hier wird versucht immer wiederkehrende **Muster** direkt in die Sprache zu übertragen.
Da für die *Nebenläufigkeit* [Seiteneffekte](def-side-effect) besonders problematisch sind, lernen imperative Sprachen auch hier von den funktionalen Sprachen.

In Java 8 führte man sogenannte ``Streams`` ein, um zum Beispiel eine Liste von Zahlen ohne großen Programmieraufwand parallel addieren zu können:

```java
// List of Integers
var numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// parallel summation (0 is the neutral element)
var sum = numbers.parallelStream().reduce(0, Integer::sum);

// print the result, i.e., 55.
System.out.println(sum);
```

Bei der Ausführung dieses Codes werden automatisch mehrere Prozessoren, je nachdem wie viele Prozessoren Ihr Computer besitzt, verwendet.
Wie das genau umgesetzt wird, ist verborgen und soll uns an dieser Stelle auch nicht weiter beschäftigen.
