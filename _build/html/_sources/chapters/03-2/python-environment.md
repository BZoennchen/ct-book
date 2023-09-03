(sec-python-ecosystem)=
# Das Python Ökosystem

Als ``Python``-Ökosystem bezeichnen wir den Zusammenschluss aus dem was die Softwareentwicklung mit ``Python`` ermöglicht.
Dazu zählen wir unter anderem

+ bestehenden Quellcode (Module, Pakte), 
+ Entwicklungsumgebungen und Werkzeuge, 
+ Paketverwaltungsprogramme wie ``pip`` und ``conda``, 
+ Dokumentationen,
+ andere Technologien, die mit ``Python`` gut integrierbar sind
+ und vorallem die Gemeinschaft bzw. Unterstützer:innen

```{admonition} Lernziel
:class: learngoals

Wie nutze ich das ``Python``-Ökosystem?
Wie bringe ich ``Python`` "zum Laufen"?
Wie nutze ich Pakte und Module (fremden Code) und die Jupyter Notebooks?

Dieses Kapitel soll Sie in der Praxis "in Gang" setzen, sodass Sie mit dem ``Python``-Programmieren loslegen können.
Der Inhalt ist daher sehr ``Python`` spezifisch und hat nur wenig mit dem eigentlichen [Computational Thinking](sec-what-is-ct) zu tun.
```

Sie werden feststellen, dass das ``Python``-Ökosystem reich, erwachsen und breit aufgestellt ist.
Es wird täglich erweitert und verbessert.
Blicken wir nur einmal auf einen Auszug bestimmter Pakete, welche wir nach deren Anwendungsbereich sortiert haben:

+ Maschinelles Lernen: [Scikit-learn](https://scikit-learn.org/stable/#), [TensorFlow](https://www.tensorflow.org/), [Theano](https://theano-pymc.readthedocs.io/en/latest/), [Caffe](https://caffe.berkeleyvision.org/), [PyTorch](https://pytorch.org/) ...
+ Computerlinguistik: [Natural Language Toolkit (NLTK)](https://www.nltk.org/), [Gensim](https://radimrehurek.com/gensim/), ...
+ Webentwicklung: [Django](https://www.djangoproject.com/), [Pyramid](https://www.pylonsproject.org/), [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Tornado](https://www.tornadoweb.org/en/stable/), ...
+ Graphische Benutzeroberflächen: [PyQt5](https://www.riverbankcomputing.com/software/pyqt/), [Tkinter](https://docs.python.org/3/library/tkinter.html), [Kivy](https://kivy.org/#home), ...
+ Wissenschaftliches Rechnen: [NumPy](https://numpy.org/), [SciPy](https://scipy.org/), [StatsModels](https://www.statsmodels.org/stable/index.html), [Pandas](https://pandas.pydata.org/), ...
+ Datenvisualisierung: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), ...
+ DevOps: [Ansible](https://www.ansible.com/), [SaltStack](https://docs.saltproject.io/en/getstarted/system/python.html) 
+ Internet der Dinge (IoT): [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/), PyBoard mit [MicroPython](https://store.micropython.org/), [MQTT](https://mqtt.org/) mit [paho](https://www.eclipse.org/paho/), ...
+ Generative Kunst: [Pillow](https://pillow.readthedocs.io/en/stable/), [samila](https://github.com/sepandhaghighi/samila), Python Modus für [Processing](https://py.processing.org/), ...
+ Notebooks und deren Ökosystem: [Jupyter](https://jupyter.org/)
+ Spieleentwicklung (begrenzt geeignet): [PyGame](https://www.pygame.org/news), [Pyglet](http://pyglet.org/), [PyOgre](https://wiki.ogre3d.org/PyOgre), ...
+ Softwareentwicklung: [Buildbot](https://buildbot.net/), [Trac](https://trac.edgewall.org/), ...
+ ...

Die eine, objektiv beste Programmiersprache existiert nicht.
Die Bewertung einer Sprache ist immer ein subjektives Maß und sollte immer auch das Ökosystem einer Sprache beinhalten.
Und ja: Die Popularität einer Sprache ist ebenfalls ein wichtiger Faktor.
Was nutzt uns die perfekte Programmiersprache, wenn sie niemand sonst benutzt?

Durch die gestiegenen Ansprüche an Software ist deren Komplexität gestiegen.
Wollen Sie heute eine Webseite erstellen, die den Ansprüchen der heutigen Standards entspricht, werden Sie nicht damit beginnen reines ``Python``, ``HTML``, ``CSS`` und ``JavaScript`` zu schreiben.
In der Praxis werden Sie sich mit Frameworks wie [Django](https://www.djangoproject.com/), [jQuerry](https://jquery.com/), [Bootstrap](https://getbootstrap.com/), [Vue](https://vuejs.org/) und mehr beschäftigen.
Diese Frameworks haben bereits viele wesentliche und sich immer wiederholende Probleme der Webentwicklung für Sie gelöst.

Auf [stackshare.io](https://stackshare.io/) können Sie nachlesen, welche Technologien hinter vielen bekannten Webanwendungen wie 

+ [Instagram](https://stackshare.io/instagram/instagram): ``Python``, ``JavaScript``, ``Java``, ``ObjectiveC``, [Django](https://www.djangoproject.com/), [React](https://reactjs.org/), ...
+ [WhatsApp](https://stackshare.io/whatsapp/whatsapp): ``Erlang``, ``PHP``, ...
+ [GitHub](https://stackshare.io/github/github): ``Ruby``, ``Markdown``, ``C``, [Git](https://git-scm.com/), [MySQL](https://www.mysql.com/), ...
+ [Google](https://stackshare.io/google/google): ``Python``, ``Java``, ``Go``, ``C++``, ``Dart``, [AngularJS](https://angularjs.org/), [Kubernetes](https://kubernetes.io/), ...
+ ...

stecken.

Selbstverständlich ändern sich die Ökosysteme ständig.
Zu meiner kurzen Zeit als Webentwickler, um das Jahr 2006, war der sog. LAMP-Stack (Linux, Apache, MySQL, PHP/Perl) einer der gängisten Bündelungen an Technologie, die zur serverseitigen Webentwicklung genutzt wurde.
Das hat sich mittlerweile geändert.

Ein anderes Beispiel ist die Entwicklung neuer Algorithmen aus dem Bereich des maschinellen Lernens.
Sie werden im Normalfall das Rad in der Praxis nicht neu erfinden.
Sie werden stattdessen analysieren welche Module (z.B. [Scikit-learn](https://scikit-learn.org/stable/#), [TensorFlow](https://www.tensorflow.org/)) Ihren Ansprüchen genügen und diese nutzen bzw. erweitern.

Als Entwickler\*innen müssen wir in der Praxis unser reiches Ökosystem kennenlernen und effektiv nutzen.
Dazu gehört insbesondere auch der bedachte Verzicht aufgeblähter Frameworks, die für unseren Anwendungsfall bzw. unser Ziel ungeeignet sind.
Aus Sicht der Anwender\*innen spielt es am Ende keine Rolle, welche tollen Technologien hinter Ihrer Anwendung stecken.
Wichtig ist stattdessen, ob Ihre Anwendung das zu lösende Problem löst und ob die Anwender\*innen eine gute Erfahrung mit Ihrer Anwendung machen, seien es Kunden einer Webanwendung oder Entwickler\*innen, die Ihr Modul verwenden wollen.