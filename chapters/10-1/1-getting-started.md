# Python zum Laufen bringen

Wollen Sie ``Python`` auf Ihrer nutzten müssen Sie die ``Python``-Arbeitsumgebung auf Ihrem Rechner erst einrichten.
Wir bieten Ihnen in diesem Abschnitt hierzu eine kurze Anleitung.

Es gibt unterschiedliche Möglichkeiten ``Python`` und neue Module (engl. module) oft auch Pakete (engl. packages) genannt zu installieren.
Vorzugsweise verwendet man:

+ [reines Python](https://www.python.org/downloads/)
+ [Anaconda](https://www.anaconda.com/products/individual)
+ [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Der von uns empfohlene Weg ist der über die Verwaltungssoftware Miniconda.

## Plain Python

Mit 'reines' Python meinen wir ``Python`` ohne zusätzliche Verwaltungssoftware wie etwa Anaconda oder Miniconda.
Sie laden sich [hier](https://www.python.org/downloads/) das entsprechende Installationsprogramm für Ihr Betriebssystem herunter und folgen den Anweisungen.
Achten Sie darauf, dass Sie **Add Python 3.7 to PATH** ankreuzen, sodass ``Python`` auch von Ihrem System bzw. von Ihrer Konsole gefunden wird!
Sie können diesen Pfad (engl. Path) auch noch nachträglich hinzufügen, jedoch braucht das weitere Schritte.
Nach abgeschlossener Installation, testen Sie ob ``Python`` und ``pip`` von Ihrem System gefunden wird, indem Sie auf der Konsole folgendes testen:

```
python --version
```

```{figure} ../../figs/python-tutorial/environment/python-version.png
---
width: 600px
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


## Anaconda

Lassen Sie uns eine der meist benutzten Hilfswerkzeuge ansehen: [Anaconda](https://www.anaconda.com/products/individual).
Mit Anaconda oder [Miniconda](https://docs.conda.io/en/latest/miniconda.html) können Sie Ihre ``Python``-Umgebung bequem verwalten.
Miniconda ist eine abgespeckte Variante von Anaconda und enthält weniger vordefinierte Module.
Je nach Betriebssystem (Windows, Mac OS X oder Linux) müssen Sie einen bestimmten Installationsassistenten herunterladen.
Die Installation erfolgt über eine graphische Benutzeroberfläche.

Im folgenden werden wir Miniconda auf einem Mac OS X installieren.
Die Installationen ähneln sich jedoch auf allen Betriebssystemen.

### Schritt 1: Herunterlande und starten des Miniconda Installationsassistenten

Sie gehen auf [Miniconda](https://docs.conda.io/en/latest/miniconda.html) und suchen unter Ihrem Betriebssystem die gewünschte (im normalfall neueste) ``Python``-Version.
In unserem Fall ist das Mac OS X und Version 3.9.

```{figure} ../../figs/python-tutorial/environment/miniconda-download.png
---
width: 600px
name: fig-miniconda-download
---
```

Sie klicken sich durch die Installationsanweisungen. 
Sie können dabei den Installationsort ändern.

```{figure} ../../figs/python-tutorial/environment/miniconda-installation-gui.png
---
width: 600px
name: fig-miniconda-installation-gui
---
```

Ändern Sie den Installationsort nicht so befindet sich Miniconda in Ihrem Benutzerverzeichnis unter miniconda3.

```{figure} ../../figs/python-tutorial/environment/miniconda-location.png
---
width: 600px
name: fig-miniconda-location
---
```

Nachdem die Installation beendet ist, können Sie mit folgenden Befehlen

```
which python
which pip
which conda
```

```{figure} ../../figs/python-tutorial/environment/miniconda-which.png.png
---
width: 600px
name: fig-miniconda-location
---
```

prüfen welche Pakte auf Ihrem System installiert sind.

Um ein Modul in Ihre Miniconda-Umgebung zu installieren, verwenden Sie das [pip](), welches bereits in Miniconda enthalten ist.
Durch den Aufruf

```
pip install [modulename]
```

wird die aktuelle Version des Moduls mit dem Namen ``modulename`` installiert.







## pip

Bevor wir die Installation durchführen wollen wir noch über das wichtige Verwaltungswerkzeug ``pip`` sprechen.
``pip`` ist ein Paketmanager für ``Python``, d.h. es ist ein Werkzeug (ein Programm) was es uns ermöglicht ``Python``-Module und deren Abhängigkeiten zu installieren und zu verwalten,
welche nicht bereits Teil der [Python Standard Bibliothek](https://docs.python.org/3/library/) sind.
Die Python Standard Bibliothek wird mit jeder ``Python``-Installation mitgeliefert.

Da das Verwalten von Paketen so wichtig geworden ist, wird ``pip`` seit der ``Python``-Version 3.4 bzw. 2.7.9 durch die ``Python``-Installationssoftware mit installiert.
Derartige Paketverwalter sind auch für andere Sprachen, wie etwa ``Java`` ([Maven](http://maven.apache.org/)) oder ``JavaScript`` ([npm](https://www.npmjs.com/)).
Sobald wir ``Python`` installiert haben wird Ihnen ``pip`` zur Verfügung stehen.
Dies können wir mit auf der Konsole mit

```
pip --version
```


```{figure} ../../figs/python-tutorial/environment/pip-version.png
---
width: 600px
name: fig-pip-version
---
```

testen.
Falls nach dies nach der Installation von ``Python`` nicht funktioniert empfehlen wir die [pip Installationsanleitung](https://pip.pypa.io/en/stable/installation/).