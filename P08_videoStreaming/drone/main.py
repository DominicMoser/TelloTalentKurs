from pynput.keyboard import Listener
from djitellopy import Tello
# Importieren der Methode sleep der time Bibliothek.
from time import sleep
# Importieren der Thread Klasse aus der threading library.
from threading import Thread
# Importieren der cv2 library (OpenCv2)
import cv2

myDrone = Tello()
myDrone.connect()

# Erstellen eines Dictionary mit x,y,z und r als keys. Initialisiert mit 0.
speed = {"x":0, "y":0, "z":0, "r":0}
speed_value = 50

# Definieren der Funktion set_speed(key). Diese wird im Hintergrund von pynput ausgeführt wenn eine Taste gedrückt wird.
# Der Parameter key gibt uns Informationen über die gedrückte Taste. Der Sinn dieser Funktion ist es den passenden Wert
# innerhalb des speed Dictionarys auf speed_value zu setzen.
# Es wird nicht direkt die Geschwindikeit der Drohne gesetzt, da es sonst Probleme gibt, bei welchen wir immer nur eine Achse auf einen Wert setzen.
def set_speed(key):
    # Wenn innerhalb dieses Blocks ein Error entsteht, wird der Block "execpt:" ausgeführt.
    try:
        # Match case mit dem Wert von key.char.
        match key.char:
            # Die Geschwindigkeit in x richtung (vorne/hinten) soll auf speed_value gesetzt werden wenn wir auf w drücken.
            case "w":
                speed["x"] = speed_value
            # Die Geschwindigkeit in x richtung (vorne/hinten) soll auf negativ speed_value gesetzt werden wenn wir auf a drücken.
            case "a":
                speed["y"] = -speed_value
            case "s":
                speed["x"] = -speed_value
            case "d":
                speed["y"] = speed_value
            case "r":
                speed["z"] = -speed_value
            case "f":
                speed["z"] = speed_value
            case "q":
                speed["r"] = -speed_value
            case "e":
                speed["r"] = speed_value
            # Starten der Drohne wenn t gedrückt wird.
            case "t":
                myDrone.takeoff()
            # Landen der Drohne wenn l gedrückt wird.
            case "l":
                myDrone.land()
                # Einschalten der Motoren, damit die Drohne nicht überhitzt.
                myDrone.turn_motor_on()
    # Führe folgendes aus wenn ein Error ensteht.
    except:
        # Mache nichts.
        pass

# Definieren der Funktion set_speed_to_zero(key). Diese wird im Hintergrund von pynput ausgeführt wenn eine Taste losgelassen wird.
# In dieser Funktion setzen wir die Geschwindigkeit innerhalb des speed Dictionarys wieder zurück auf 0.
def set_speed_to_zero(key):
    try:
        match key.char:
            case "w" | "s":
                speed["x"] = 0
            case "a" | "d":
                speed["y"] = 0
            case "r" | "f":
                speed["z"] = 0
            case "q" | "e":
                speed["r"] = 0
    except:
        pass

# Statt am Ende des Codes steht des senden nun in einer eigenen Funktion, damit sie in einem eigenen Thread ausgeführt werden kann.
def send_loop():
    # Endlosschleife
    while True:
        # Senden der geschwindigkeiten an die Drohne.
        myDrone.send_rc_control(speed["y"], speed["x"], speed["z"] ,speed["r"])
        # Sehr kurze Pause, damit andere Threads zeit haben aktionen auszuführen. Dies ist nicht unbedingt nötig,
        # kann aber bei lags im Video output helfen.
        sleep(0.001)

# Funktion welche für dass Videostreaming verantwortlich ist. Läuft in einem eigenen Thread.
def stream_loop():
    # Schalten das Streaming von Videosignalen der Drohne an.
    myDrone.streamon()
    # Mit Hilfe von myDrone.get_frame_read() bekommen wir ein Objekt, in welchem immer das aktuelle Bild der Drohne gespeichert ist.
    frameObject = myDrone.get_frame_read()
    # Endlosschleife
    while True:
        # Das aktuelle Bild(frame) der Drohne wird aus frameObject.frame in frame geschrieben.
        frame = frameObject.frame
        # Ändern der Größe des angezeigten Bildes auf 320 auf 240 Pixel. (Es kann auch ein anderer Wert verwendet werden.)
        frame = cv2.resize(frame,(320,240))
        # Als Bonus: Zeichnen des Akkuladestands der Drohne auf dem Bild.
        frame = draw_battery(myDrone.get_battery(), frame)
        # Anzeigen des Bildes.
        cv2.imshow("Dronestream", frame)
        # Cv2 soll das nächste bild direkt anzeigen sobald imshow ein weiteres mal aufgerufen wird.
        cv2.waitKey(1)

# Funktion zum zeichnen des aktuellen Akkuleves. 
def draw_battery(battery_level, frame):
    # Erstellen von Color als eine leere Liste
    color = ()
    # Je nach Akkustand, soll die Battery in einer anderen Farbe dargestellt werden.
    if battery_level > 80:
        # Grün
        color = (0,255,0)
    elif battery_level > 40:
        # Gelb
        color = (0,255,255)
    else:
        # Rot
        color = (0,0,255)
    # Zeichen eines schwarzen Rechtecks als Outline der Akkuanzeige
    frame = cv2.rectangle(frame, (8, 8), (32,112), color=(0,0,0), thickness=2)
    # Zeichen des Aukkustandes.
    frame = cv2.rectangle(frame, (10, 110), (30,110-battery_level),  color=color, thickness=-1)
    # Rückgabe des frames mit gezeichnetem Akkustand.
    return frame

# Erstellen eines ActionListeners und registrieren der Funktion set_speed als funktion welche beim Drücken von Tasten ausgeführt wird
# und der Funktion set_speed_to_zero welche beim loslassen von Tasten ausgeführt wird.
listener = Listener(on_press=set_speed, on_release=set_speed_to_zero)
listener.start()

# Erstellen eines Threads, welcher send_loop ausführt.
sendThread = Thread(target=send_loop)
# Starten des Threads.
sendThread.start()

# Erstellen eines Threads, welcher stream_loop ausführt.
streamingThread = Thread(target=stream_loop)
# Starten des Threads.
streamingThread.start()

# Warten bis sendThread endet. Da jedoch send_loop eine Endlosschleife beinhaltet, wird dies nie der Fall sein.
# Damit wird verhindert, dass das Programm unbeabsichtigt beendet wird.
sendThread.join()