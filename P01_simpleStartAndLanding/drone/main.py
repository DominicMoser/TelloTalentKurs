# Importieren der Tello Klasse aus der djitellopy Bibliothek
from djitellopy import Tello

# Erstellen eines Objektes der Klasse Tello. Dieses Objekt ist unsere Drohne und besitzt alle für uns notwendigen 
# Methoden um diese zu steuern.
myDrone = Tello()

# Verbindung mit der Drohne herstellen. Dazu muss der Computer im WLan netzwerk der Drohne sein. Sollte hierbei
# ein Fehler auftreten, kann es helfen myDrone.connect(False) zu benutzen. Dies hat mit einer Falsch konfigurierten
# Firewall zu tun und muss vor P07_rcController korrigiert werden. Dazu mehr in install.md unter Firewall Konfigurieren.
myDrone.connect()

# Senden des start Befehl an die Drohne. Der Code geht erst weiter wenn der Befehl fertig abgeschlossen ist,
# was ein paar Sekunden dauern kann.
myDrone.takeoff()

# Senden des lande Befehls.
myDrone.land()