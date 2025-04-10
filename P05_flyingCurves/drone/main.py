from djitellopy import Tello

myDrone = Tello()
myDrone.connect()

myDrone.takeoff()

myDrone.land()