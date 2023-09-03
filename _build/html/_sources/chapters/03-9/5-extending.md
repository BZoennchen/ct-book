# CPython erweitern

CPython lässt sich selbstverständlich durch ``Python``-Code erweitern.
Nichts anderes haben wir bisher in diesem Kurs getan.

Dadurch dass der Interpreter in ``C`` geschrieben ist, können wir CPython auch durch ``C`` bzw. ``C++``-Code erweitern.
In [Extending Python with C or C++](https://docs.python.org/3/extending/extending.html) wird dieser Vorgang beschrieben.
Wir können auch den Interpreter selbst erweitern und unseren eigenen erweiterten CPython-Interpreter bauen.

Die Programmiersprache [Cython](https://cython.org/), mit gleichnamingen [Übersetzer](def-compiler), wurde entwickelt um ``Python``-ähnlichen Code (``Python`` + expliziete Typinformation) in möglicht performanten ``C``-Code zu übersetzen.
Der durch den ``Cython``-Compiler erzeugte ``C``-Code lässt sich durch alle gängigen ``C``-Compiler übersetzen.
Das Compilant kann dann relativ einfach als Modul in das ``Python``-Ökosystem integriert werden.