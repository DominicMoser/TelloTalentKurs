# Guide
## Installation 
### Windows install

1. Python
    Über microsoft store: Python 3.13
2. Visual Studio Code
    Über Microsoft store
3. Python plugin
    über visual studio extensions
4. Djitellopy
    In Terminal: `pip install djitellopy`
5. PlatformIo Extension

### Drohen vorbereiten
1. Die [Tello App](https://www.dji.com/de/downloads/djiapp/tello) installieren.
2. Die Drohne einschalten.
3. Das Smartphone mit dem wlan der Drohne verbinden.
4. Die App öffnen um die Drohen zu aktivieren.

### Firewall Konfigurieren
1. Öffnen der Windows Firewall einstellungen.
2. Auf advanced setting (erweiterte einstellungen) klicken.
3. Administrator password eingeben.
4. Auf Eingehende Regeln klicken.
5. Auf Neue Regel klicken.
6. Als Regeltyp `Port` auswählen und auf Weiter klicken.
7. TCP Port auswählen und bei `Bestimmte lokale Ports:` `8890` eingeben und auf Weiter klicken.
8. `Verbindung zulassen` auswählen und auf Weiter klicken.
9. Alle Profile ausgewählt lassen und auf Weiter klicken.
10. Einen Namen wählen. Im besten fall etwas mit `Tello` am Anfang und auf Fertig stellen klicken.
11. Schritt 5-10 wiederholen mit `UDP` und `11111` als Port.
12. Schritt 5-10 wiederholen mit `UDP` und `8889` als Port.


## Projekt strukture
-Workspace Folder
 |- install.md
 |- README.md
 |- Project1 Folder: P01_NAME
 |  |- Tutorials
 |  |- task.md
 |  |- Python Folder
 |  |  +- Python Code
 |  +- C++ Folder
 |     +- C++ Code (PlatformIO)
 |
 |- Project2 Folder: P02_NAME
    |- Tutorials
    |- task.md
    |- Python Folder
    |  +- Python Code
    +- C++ Folder
       +- C++ Code