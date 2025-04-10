from djitellopy import Tello
myDrone = Tello()
myDrone.connect()

myDrone.takeoff()

# Aktivieren der Erkennung von MissionPads.
myDrone.enable_mission_pads()
# Nur die untere Kamera verwenden, da es langsamer ist beide zu verwenden.
myDrone.set_mission_pad_detection_direction(0) 

# Etwas höher fliegen, damit ein größere Bereich erkannt wird.
myDrone.go_xyz_speed(0,0,50,10)

# Endlosschleife
while True:
    # Führe diesen Block nur aus wenn ein MissionPad erkannt wurde.
    if myDrone.get_mission_pad_id() != -1:
        # Schreibe die Id des erkannten MissionPads in die Konsole.
        print("found: " + str(myDrone.get_mission_pad_id()))
        
        # Fliege die Drohne über das MissionPad.
        myDrone.go_xyz_speed_mid(0,0,50, 10, myDrone.get_mission_pad_id())
        # Verringere die Höhe über dem MissionPad auf 20cm.
        myDrone.go_xyz_speed_mid(0,0,20, 10, myDrone.get_mission_pad_id())
        
        # Beende die Endlosschleife, damit die Drohne landen kann.
        break;

# Lande die Drohne.
myDrone.land()