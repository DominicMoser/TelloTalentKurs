from djitellopy import Tello

myDrone = Tello()

myDrone.connect()
myDrone.takeoff()

# Schleife mit 3 Durchgängen.
for i in range(3):
    # Ausgabe des aktuellen Durchgangs.
    print("Durchgang: " + str(i))
    # Linkssalto ausfühern
    myDrone.flip_left()
    myDrone.move_back(20)
    # Rückwärtssalto ausfühern
    myDrone.flip_back()
    myDrone.move_left(20)
    # Rechtssalto ausfühern
    myDrone.flip_right()
    myDrone.move_right(20)
    # Vorwärts ausfühern
    myDrone.flip_forward()
    myDrone.move_forward(20)

myDrone.land()