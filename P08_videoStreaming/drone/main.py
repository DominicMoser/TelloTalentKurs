from pynput.keyboard import Listener
from djitellopy import Tello
from time import sleep
from threading import Thread
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
    # Match case mit dem Wert von key.char.
    # Sollte key.char nicht existieren (z.b bei gedrückter shift taste), wird ein Error enstehen.
    # Der Umgang mit diesem Error wird im nächsten Projekt gelöst.
    match key.char:
        # Die Geschwindigkeit in x richtung (vorne/hinten) soll auf speed_value gesetzt werden wenn wir auf w drücken.
        case "w":
            speed["x"] = 50
        # Die Geschwindigkeit in x richtung (vorne/hinten) soll auf negativ speed_value gesetzt werden wenn wir auf a drücken.
        case "a":
            speed["y"] = -50
        case "s":
            speed["x"] = -50
        case "d":
            speed["y"] = 50
        case "r":
            speed["z"] = -50
        case "f":
            speed["z"] = 50
        case "q":
            speed["r"] = -50
        case "e":
            speed["r"] = 50
        # Starten der Drohne wenn t gedrückt wird.
        case "t":
            myDrone.takeoff()
        # Landen der Drohne wenn l gedrückt wird.
        case "l":
            myDrone.land()
            # Einschalten der Motoren, damit die Drohne nicht überhitzt.
            myDrone.turn_motor_on()

# Definieren der Funktion set_speed_to_zero(key). Diese wird im Hintergrund von pynput ausgeführt wenn eine Taste losgelassen wird.
# In dieser Funktion setzen wir die Geschwindigkeit innerhalb des speed Dictionarys wieder zurück auf 0.
def set_speed_to_zero(key):
    match key.char:
        case "w" | "s":
            speed["x"] = 0
        case "a" | "d":
            speed["y"] = 0
        case "r" | "f":
            speed["z"] = 0
        case "q" | "e":
            speed["r"] = 0


# Erstellen eines ActionListeners und registrieren der Funktion set_speed als funktion welche beim Drücken von Tasten ausgeführt wird
# und der Funktion set_speed_to_zero welche beim loslassen von Tasten ausgeführt wird.
listener = Listener(on_press=set_speed, on_release=set_speed_to_zero)
listener.start()

# Endlosschleife
while True:
    # Senden der geschwindigkeiten an die Drohne.
    myDrone.send_rc_control(speed["y"], speed["x"], speed["z"] ,speed["r"])

