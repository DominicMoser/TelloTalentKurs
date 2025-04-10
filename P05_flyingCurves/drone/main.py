from djitellopy import Tello

myDrone = Tello()
myDrone.connect()

# Beispiel einer möglichen Kurve. Für ein besseres 3 Dimensionales Verständniss,
# können die Kurven über geogebra gezeichnet werden
# Fliege von der aktuellen Positon zu der Position 100, 0, 0 über die Position 50, 50, 0 
# mit einer Geschwindigkeit von 30.
# Hierbei fliegt die Drohne nur eine 2 Dimensionale Kurve.
myDrone.curve_xyz_speed(50,50,0, 100,0,0, 30)

myDrone.takeoff()

myDrone.land()