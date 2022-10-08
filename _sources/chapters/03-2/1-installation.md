(sec-python-installation)=
# Installation

Wollen Sie ``Python`` auf Ihrem Rechner/System nutzen müssen Sie die ``Python``-Arbeitsumgebung auf Ihrem Rechner/System erst einrichten.
Wir bieten Ihnen in diesem Abschnitt eine kurze Anleitung.

Es gibt unterschiedliche Möglichkeiten ``Python`` und neue Module (engl. module) oder Pakete (engl. packages) zu installieren.
Vorzugsweise verwendet man:

+ [(Reines) Python](https://www.python.org/downloads/)
+ [Anaconda](https://www.anaconda.com/products/individual)
+ [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (empfohlen)

Der von uns empfohlene Weg nutzt die Verwaltungssoftware **Miniconda**.
Diese Software bietet Ihnen alles was Sie benötigen.
Installieren Sie lediglich (reines) ``Python``, so müssen Sie für weitere nützliche Dienste möglicherweise weitere Programme installieren.

## Unterschied zwischen conda und pip

``pip`` ist ein *Paketverwaltungsprogramm* für ``Python``-Pakete aus dem *Python Package Index* (PyPI).
PyPI ist ein Paketpool, welcher über 100 000 Pakete umfasst.
Entwickler\*innen können Pakete in den Pool hochladen und diese anderen Entwickler\*innen und Anwender\*innen zur Verfügung stellen.
So haben wir, zum Beispiel, unser ``roboworld``-Paket in PyPI eingepflegt (siehe [roboworld](https://pypi.org/project/roboworld/)).

``conda`` ist ebenfalls ein *Paketverwaltungsprogramm*, welches vor ``pip`` entwickelt wurde und seine Pakete durch das *Anaconda Repository* und der *Anaconda Cloud* bereitstellt.
Es wird vorallem für die Programmiersprachen ``Python`` und ``R`` verwendet und löst Paketabhängigkeiten, welche insbesondere im Bereich *Data Science*, eine große Herausforderunge waren.

Im Unterschied zu ``conda`` installiert ``pip`` Ihnen alle benötigten Paketabhängigkeiten, egal ob es *Konflikte* zu bereits installierten Paketen gibt oder nicht.
Dies kann zu Problemen führen.
Nehmen wir an Sie haben ein Paket ``A`` welches ein anderes Paket ``B`` in der Version ``1.1.0`` benötigt.
Und nehmen wir an Sie installieren ein Paket ``C``, welches ebenfalls das Paket ``B`` benötigt, jedoch in der neuesten Version ``1.1.1``.
``pip`` installiert ``B`` in der Version ``1.1.1``, was jedoch dazu führen kann, dass Ihr Code, der auf Paket ``A`` aufbaut, nicht mehr funktioniert oder ein anderes Ergebnis liefert.
Wurde die Version ``1.1.0`` für unseren Code spezifiziert, würde ``conda`` entweder automatisch herausfinden wie beide Abhängigkeiten eingehalten werden oder melden, dass die Installation nicht möglich ist.

Für diesen Kurs macht es keinen großen Unterschied ob Sie ``pip`` oder ``conda`` verwenden.
Es ist auch möglich, und manchmal auch notwendig, beide Paketmanager parallel zu nutzen.
So verwenden wir ``pip``, falls wir Pakete benötigen, die sich nicht im *Anaconda Repository* befinden. 

## Anaconda / Miniconda (empfohlen)

Lassen Sie uns eine der meist benutzten Hilfswerkzeuge ansehen: [Anaconda](https://www.anaconda.com/products/individual).
Mit Anaconda oder [Miniconda](https://docs.conda.io/en/latest/miniconda.html) können Sie Ihre ``Python``-Umgebung bequem verwalten.
Miniconda ist eine abgespeckte Variante von Anaconda und enthält weniger vordefinierte Pakete.
Je nach Betriebssystem (Windows, Mac OS oder Linux) müssen Sie einen bestimmten Installationsassistenten herunterladen.
Die Installation erfolgt über eine graphische Benutzeroberfläche.

Im Folgenden werden wir Miniconda auf einem Mac OS installieren.
Die Installationen ähneln sich jedoch auf allen Betriebssystemen.

***Schritt 1: Herunterladen***<br>
Sie gehen auf [Miniconda](https://docs.conda.io/en/latest/miniconda.html) und suchen unter Ihrem Betriebssystem die gewünschte (im Normalfall neueste) ``Python``-Version.
In unserem Fall ist das Mac OS und Version 3.9.

```{figure} ../../figs/python-tutorial/environment/miniconda-download.png
---
width: 600px
name: fig-miniconda-download
---
```

***Schritt 2: Installieren***<br>
Sie starten den Miniconda-Installationsassistenten, welchen Sie soeben heruntergeladen haben.
Sie klicken sich durch die Installationsanweisungen. 
Sie können dabei den Installationsort ändern.

```{figure} ../../figs/python-tutorial/environment/miniconda-installation-gui.png
---
width: 600px
name: fig-miniconda-installation-gui
---
```

Ändern Sie den Installationsort nicht, so befindet sich Miniconda in Ihrem Benutzerverzeichnis unter ``opt/miniconda3``, d.h. der absolute Pfad wäre ``/Users/[username]/opt/miniconda3``.

```{figure} ../../figs/python-tutorial/environment/miniconda-location.png
---
width: 600px
name: fig-miniconda-location
---
```

***Schritt 3: Testen***<br>
Nachdem die Installation beendet ist, können Sie mit folgenden Befehlen

```sh
which python
which pip
which conda
pip list
```

```{figure} ../../figs/python-tutorial/environment/miniconda-which.png
---
width: 600px
name: fig-miniconda-which
---
```

prüfen, wo sich Ihr ``Python``, ``pip`` und ``conda`` befinden und welche Pakte auf Ihrem System installiert sind.
Diese Liste ist kurz, da Sie bisher nur das nötigste installiert haben.
Um z.B. **Jupyter-Notebooks** auszuführen benötigen Sie das Paket ``jupyter`` bzw. ``jupyterlab``, welches Sie zuvor mit dem Paketmanager ``conda`` oder ``pip`` installieren müssen.

### Paketverwaltung mit conda

Mit dem Programm ``conda`` können Anaconda bzw. Miniconda ansprechen.
Im Vergleich zu ``pip`` sind die Befehle nahezu identisch!

#### conda installiert?

Um zu prüfen ob ``conda`` auf Ihrem System gefunden wird können Sie folgenden Befehl auf der Konsole ausführen:

```
conda --version
```

```{figure} ../../figs/python-tutorial/environment/conda-version.png
---
width: 600px
name: fig-conda-version
---
```

Sollte der Befehl nicht gefunden werden haben Sie Anaconda bzw. Miniconda noch nicht installiert.

#### Pakete Installieren

Durch den Aufruf

```
conda install [paketename]
```

wird die aktuelle Version des Pakets mit dem Namen ``paketename`` in den entsprechenden Installationsordner Ihrer Anaconda bzw. Miniconda-Standardumgebung installiert.

````{admonition} Pakte mit conda installieren
:class: attention
:name: attention-conda-pip-install

Sollte das zu installierende Paket sich nicht im ``conda`` repository befinden und somit nicht über ``conda`` installierbar sein, können Sie es oft dennoch über

```
pip install [paketename]
```

installieren. Versuchen Sie jedoch ``conda`` vor ``pip``.

````

Versuchen wir einmal die Jupyter-Lab-Umgebung zum Ausführen der Jupyter-Notebooks zu starten.

```sh
jupyter lab
```

Wir erhalten eine Fehlermeldung bzw. der Befehl ist unserem System nicht bekannt.

Das war zu erwarten, da das Paket ``jupyterlab`` noch nicht installiert wurde.
Lassen Sie uns das nachholen:

```sh
conda install jupyterlab
```

Bevor Sie die Installation akzeptieren, wird Ihnen angezeigt welche Pakte (inkl. Abhängigkeiten) installiert werden.

```{figure} ../../figs/python-tutorial/environment/jupyter-install-conda.png
---
width: 600px
name: fig-jupyter-install-conda
---
```

Und Sie werden gefragt ob Sie fortfahren wollen.
Mit ``y`` akzeptieren Sie den Vorgang und die Installation wird durchgeführt.

```{figure} ../../figs/python-tutorial/environment/jupyter-install-conda-accept.png
---
width: 600px
name: fig-jupyter-install-conda-accept
---
```

Nun könnten wir die Jupyter-Umgebung mit 

```sh
jupyter notebook
```

starten.
Es würde folgendes Fenster im Browser Ihres Systems erscheinen.

```{figure} ../../figs/python-tutorial/environment/jupyter-start.png
---
width: 800px
name: fig-jupyter-start-2
---
Alte Jupyter-Umgebung.
```

Wir bevorzugen die alternative Jupyter-Lab-Umgebung, welche Sie mit 

```sh
jupyter lab
```

starten können.

```{figure} ../../figs/python-tutorial/environment/jupyter-lab-start.png
---
width: 800px
name: fig-jupyter-lab-start
---
Neue Jupyter-Lab-Umgebung.
```

## Plain Python

### Installation

Mit "reinem" Python meinen wir ``Python`` ohne zusätzliche Verwaltungssoftware wie etwa Anaconda oder Miniconda.

***Schritt 1: Herunterladen***<br>
Sie laden sich [hier](https://www.python.org/downloads/) das entsprechende Installationsprogramm für Ihr Betriebssystem herunter.

***Schritt 2: Installieren***<br>
Sie führen das Installationsprogramm aus und folgen den Anweisungen. Achten Sie darauf, dass Sie **Add Python 3.7 to PATH** ankreuzen, sodass ``Python`` auch von Ihrem System bzw. von Ihrer Konsole gefunden wird! Sie können diesen Pfad (engl. Path) auch noch nachträglich hinzufügen, jedoch braucht das weitere Schritte.

***Schritt 3: Testen***<br>
Nach abgeschlossener Installation, testen Sie ob ``Python`` und ``pip`` von Ihrem System gefunden werden indem Sie auf der Konsole folgende Befehle aufrufen:

```
python --version
```

```{figure} ../../figs/python-tutorial/environment/python-version.png
---
width: 350px
name: fig-python-version
---
```

```
pip --version
```


```{figure} ../../figs/python-tutorial/environment/pip-version.png
---
width: 600px
name: fig-pip-version
---
```

### Paketverwaltung mit pip

``pip`` ist ein Paketmanager für ``Python``, d.h. es ist ein Werkzeug (ein Programm) was es uns ermöglicht ``Python``-Pakete und deren Abhängigkeiten zu installieren und zu verwalten,
welche nicht bereits Teil der [Python Standard Bibliothek](https://docs.python.org/3/library/) sind.
Die Python Standard Bibliothek wird mit jeder ``Python``-Installation mitgeliefert.

Da das Verwalten von Paketen so wichtig geworden ist, wird ``pip`` seit der ``Python``-Version 3.4 bzw. 2.7.9 durch die ``Python``-Installationssoftware mit installiert.
Derartige Paketverwalter gibt es auch für andere Sprachen, wie etwa ``Java`` ([Maven](http://maven.apache.org/)) oder ``JavaScript`` ([npm](https://www.npmjs.com/)).
Sobald wir ``Python`` installiert haben wird Ihnen ``pip`` zur Verfügung stehen.

#### pip installiert?

Um zu prüfen ob ``pip`` auf Ihrem System gefunden wird können Sie folgenden Befehl auf der Konsole ausführen:

```
pip --version
```

```{figure} ../../figs/python-tutorial/environment/pip-version.png
---
width: 600px
name: fig-pip-version-2
---
```

Sollte der Befehl nicht gefunden werden haben Sie entweder ``Python`` nicht richtig installiert oder ``Python`` bzw. ``pip`` ist nicht in Ihrer *Umgebungsvariable* **PATH** enthalten. 
Falls nach der Installation von ``Python`` der Aufruf nicht funktioniert, hilft Ihnen möglicherweise die [pip Installationsanleitung](https://pip.pypa.io/en/stable/installation/).

#### Pakete Installieren

Durch den Aufruf

```
pip install [paketename] --user
```

wird die aktuelle Version des Pakets mit dem Namen ``paketename`` für Sie als Benutzer (in Ihr Benutzerverzeichnis) installiert.
Ohne ``--user`` wird das Paket für alle Benutzer installiert und kann nur durch Adminrechte (root-Rechte) genutzt werden.

Versuchen wir einmal die Jupyter-Lab-Umgebung zum Ausführen der Jupyter-Notebooks zu starten.

```sh
jupyter lab
```

Wir erhalten eine Fehlermeldung bzw. wird der Befehl nicht erkannt.

Das war zu erwarten, da das Paket ``jupyter`` noch nicht installiert wurde.
Lassen Sie uns das nachholen.

```sh
pip install jupyterlab --user
```

```{figure} ../../figs/python-tutorial/environment/jupyter-installation.png
---
width: 600px
name: fig-jupyter-installation
---
```

In unserem Fall erschien eine Warnung, die besagt dass das Verzeichnis, das die Ausführbaren Dateien der Pakete enthält, nicht im **PATH** enthalten ist.
Dies holen wir mit 

```sh
export PATH="/Users/bzoennchen/.local/bin:$PATH"
```

nach.
Dieser Befehl verändert die Umgebungsvariable **PATH** und fügt dieser einen weiteren Pfad ``/Users/bzoennchen/.local/bin`` zum Durchsuchen an.
Dieser Pfad wird auf Ihrem System anders aussehen!
Nun können wir die Jupyter-Umgebung mit 

```sh
jupyter lab
```

starten und es erscheint ein neues Fenster im Browser Ihres Systems.

```{figure} ../../figs/python-tutorial/environment/jupyter-lab-start.png
---
width: 800px
name: fig-jupyter-lab-start-3
---
```