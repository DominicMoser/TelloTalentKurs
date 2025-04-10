from djitellopy import Tello

myDrone = Tello()
myDrone.connect()

myDrone.takeoff()

# Setzen der Distanz ab welcher die Drohne landen soll.
landing_threashold = 8

# Endlosschleife
while True:
    # Wenn die Distanz kleiner als landing_threashold ist, soll die Schleife beendet werden.
    if myDrone.get_distance_tof() < landing_threashold:
        break

myDrone.land()